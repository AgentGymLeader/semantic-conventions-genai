"""Reference implementation: agent governance decision join point with manual instrumentation.

Exercises: invoke_agent with a producer-emitted governance decision
(gen_ai.agent.decision.id / gen_ai.agent.decision.outcome /
gen_ai.agent.governance.ref) against a mock chat completions server, with
manual span instrumentation.

This scenario is a synthetic, manually instrumented stand-in for a
producer-side governance gate (for example a policy, approval, or
execution-context check) that runs before or around an agent invocation. It
does not integrate with, name, or imply any specific third-party governance
or policy product; the GovernanceGate class below is a minimal in-process
allow/block lookup used only to make the two scenarios below deterministic.
"""

import json
import os
from dataclasses import dataclass

from opentelemetry.trace import SpanKind
from reference_shared import flush_and_shutdown, mock_server_host_port, reference_tracer, setup_otel

MOCK_BASE_URL = os.environ["MOCK_LLM_URL"] + "/v1"
REQUEST_MODEL = "gpt-4o-mini"
AGENT_NAME = "governance_agent"
GOVERNANCE_REF = "ctx_7f3a9c"

_reference_tracer = reference_tracer()


@dataclass(frozen=True)
class GovernanceDecision:
    allow: bool
    decision_id: str
    outcome: str
    governance_ref: str


class GovernanceGate:
    def __init__(self, allowed_capabilities: set[str], decision_ids: dict[str, str], governance_ref: str):
        self._allowed_capabilities = allowed_capabilities
        self._decision_ids = decision_ids
        self._governance_ref = governance_ref

    def decide(self, capability: str) -> GovernanceDecision:
        allow = capability in self._allowed_capabilities
        return GovernanceDecision(
            allow=allow,
            decision_id=self._decision_ids[capability],
            outcome="allow" if allow else "block",
            governance_ref=self._governance_ref,
        )


def _input_messages(prompt: str) -> str:
    return json.dumps([{"role": "user", "parts": [{"type": "text", "content": prompt}]}])


def run_allowed_reference(client, gate: GovernanceGate) -> None:
    print("  [invoke_agent] allowed governance decision")
    prompt = "Check the weather in Seattle."
    decision = gate.decide("weather.lookup")
    messages = [{"role": "user", "content": prompt}]
    input_messages = _input_messages(prompt)

    host, port = mock_server_host_port(MOCK_BASE_URL)
    agent_attributes = {
        "gen_ai.operation.name": "invoke_agent",
        "gen_ai.provider.name": "openai",
        "gen_ai.request.model": REQUEST_MODEL,
        "gen_ai.agent.name": AGENT_NAME,
        "gen_ai.agent.decision.id": decision.decision_id,
        "gen_ai.agent.decision.outcome": decision.outcome,
        "gen_ai.agent.governance.ref": decision.governance_ref,
    }
    if host:
        agent_attributes["server.address"] = host
    if port is not None:
        agent_attributes["server.port"] = port

    with _reference_tracer.start_as_current_span(
        f"invoke_agent {AGENT_NAME}",
        kind=SpanKind.CLIENT,
        attributes=agent_attributes,
    ) as agent_span:
        agent_span.set_attribute("gen_ai.input.messages", input_messages)

        chat_attributes = {
            "gen_ai.operation.name": "chat",
            "gen_ai.provider.name": "openai",
            "gen_ai.request.model": REQUEST_MODEL,
        }
        if host:
            chat_attributes["server.address"] = host
        if port is not None:
            chat_attributes["server.port"] = port
        with _reference_tracer.start_as_current_span("chat gpt-4o-mini", attributes=chat_attributes) as chat_span:
            chat_span.set_attribute("gen_ai.input.messages", input_messages)
            resp = client.chat.completions.create(model=REQUEST_MODEL, messages=messages)
            finish_reasons = [choice.finish_reason for choice in resp.choices]
            output_messages = [
                {
                    "role": choice.message.role,
                    "parts": [{"type": "text", "content": choice.message.content}],
                    "finish_reason": choice.finish_reason,
                }
                for choice in resp.choices
                if choice.message.content
            ]

            chat_span.set_attribute("gen_ai.response.model", resp.model)
            chat_span.set_attribute("gen_ai.response.id", resp.id)
            chat_span.set_attribute("gen_ai.response.finish_reasons", finish_reasons)
            if resp.usage:
                chat_span.set_attribute("gen_ai.usage.input_tokens", resp.usage.prompt_tokens)
                chat_span.set_attribute("gen_ai.usage.output_tokens", resp.usage.completion_tokens)
            if output_messages:
                chat_span.set_attribute("gen_ai.output.messages", json.dumps(output_messages))

            agent_span.set_attribute("gen_ai.response.finish_reasons", finish_reasons)
            if resp.usage:
                agent_span.set_attribute("gen_ai.usage.input_tokens", resp.usage.prompt_tokens)
                agent_span.set_attribute("gen_ai.usage.output_tokens", resp.usage.completion_tokens)
            if output_messages:
                agent_span.set_attribute("gen_ai.output.messages", json.dumps(output_messages))

        tool_span_attributes = {
            "gen_ai.operation.name": "execute_tool",
            "gen_ai.tool.name": "get_weather",
            "gen_ai.tool.type": "function",
        }
        with _reference_tracer.start_as_current_span(
            "execute_tool get_weather", attributes=tool_span_attributes
        ) as tool_span:
            tool_span.set_attribute("gen_ai.tool.call.arguments", json.dumps({"location": "Seattle"}))
            tool_result = "Sunny in Seattle"
            tool_span.set_attribute("gen_ai.tool.call.result", tool_result)

        print(f"    -> {decision.outcome}: get_weather")


def run_allowed_internal_reference(client, gate: GovernanceGate) -> None:
    """Demonstrate the same decision join point on an in-process (internal) agent invocation."""
    print("  [invoke_agent internal] allowed governance decision")
    prompt = "Summarize today's weather checks."
    decision = gate.decide("weather.lookup")
    messages = [{"role": "user", "content": prompt}]
    input_messages = _input_messages(prompt)

    agent_attributes = {
        "gen_ai.operation.name": "invoke_agent",
        "gen_ai.provider.name": "openai",
        "gen_ai.request.model": REQUEST_MODEL,
        "gen_ai.agent.name": AGENT_NAME,
        "gen_ai.agent.decision.id": decision.decision_id,
        "gen_ai.agent.decision.outcome": decision.outcome,
        "gen_ai.agent.governance.ref": decision.governance_ref,
    }

    with _reference_tracer.start_as_current_span(
        f"invoke_agent {AGENT_NAME}",
        kind=SpanKind.INTERNAL,
        attributes=agent_attributes,
    ) as agent_span:
        agent_span.set_attribute("gen_ai.input.messages", input_messages)

        host, port = mock_server_host_port(MOCK_BASE_URL)
        chat_attributes = {
            "gen_ai.operation.name": "chat",
            "gen_ai.provider.name": "openai",
            "gen_ai.request.model": REQUEST_MODEL,
        }
        if host:
            chat_attributes["server.address"] = host
        if port is not None:
            chat_attributes["server.port"] = port
        with _reference_tracer.start_as_current_span("chat gpt-4o-mini", attributes=chat_attributes) as chat_span:
            chat_span.set_attribute("gen_ai.input.messages", input_messages)
            resp = client.chat.completions.create(model=REQUEST_MODEL, messages=messages)
            finish_reasons = [choice.finish_reason for choice in resp.choices]
            output_messages = [
                {
                    "role": choice.message.role,
                    "parts": [{"type": "text", "content": choice.message.content}],
                    "finish_reason": choice.finish_reason,
                }
                for choice in resp.choices
                if choice.message.content
            ]

            chat_span.set_attribute("gen_ai.response.model", resp.model)
            chat_span.set_attribute("gen_ai.response.id", resp.id)
            chat_span.set_attribute("gen_ai.response.finish_reasons", finish_reasons)
            if resp.usage:
                chat_span.set_attribute("gen_ai.usage.input_tokens", resp.usage.prompt_tokens)
                chat_span.set_attribute("gen_ai.usage.output_tokens", resp.usage.completion_tokens)
            if output_messages:
                chat_span.set_attribute("gen_ai.output.messages", json.dumps(output_messages))

            agent_span.set_attribute("gen_ai.response.finish_reasons", finish_reasons)
            if resp.usage:
                agent_span.set_attribute("gen_ai.usage.input_tokens", resp.usage.prompt_tokens)
                agent_span.set_attribute("gen_ai.usage.output_tokens", resp.usage.completion_tokens)
            if output_messages:
                agent_span.set_attribute("gen_ai.output.messages", json.dumps(output_messages))

        print(f"    -> {decision.outcome}: chat")


def run_denied_reference(gate: GovernanceGate) -> None:
    print("  [invoke_agent] blocked governance decision")
    prompt = "Refund the current invoice."
    decision = gate.decide("billing.refund")

    host, port = mock_server_host_port(MOCK_BASE_URL)
    agent_attributes = {
        "gen_ai.operation.name": "invoke_agent",
        "gen_ai.provider.name": "openai",
        "gen_ai.request.model": REQUEST_MODEL,
        "gen_ai.agent.name": AGENT_NAME,
        "gen_ai.agent.decision.id": decision.decision_id,
        "gen_ai.agent.decision.outcome": decision.outcome,
        "gen_ai.agent.governance.ref": decision.governance_ref,
    }
    if host:
        agent_attributes["server.address"] = host
    if port is not None:
        agent_attributes["server.port"] = port

    with _reference_tracer.start_as_current_span(
        f"invoke_agent {AGENT_NAME}",
        kind=SpanKind.CLIENT,
        attributes=agent_attributes,
    ) as agent_span:
        agent_span.set_attribute("gen_ai.input.messages", _input_messages(prompt))
        print(f"    -> {decision.outcome}: billing.refund")


def main() -> None:
    print("=== Reference Implementation: Agent Governance Reference Implementation ===")

    tp, lp, mp = setup_otel()

    import openai

    client = openai.OpenAI(base_url=MOCK_BASE_URL, api_key="mock-key")
    gate = GovernanceGate(
        allowed_capabilities={"weather.lookup"},
        decision_ids={
            "weather.lookup": "decision_01J8Z3K5G4QYX9V2XQ9K7YXTAM",
            "billing.refund": "decision_01J8Z3N2R8S6VT4MZ3YXK9B7QC",
        },
        governance_ref=GOVERNANCE_REF,
    )

    run_allowed_reference(client, gate)
    run_allowed_internal_reference(client, gate)
    run_denied_reference(gate)

    flush_and_shutdown(tp, lp, mp)


if __name__ == "__main__":
    main()
