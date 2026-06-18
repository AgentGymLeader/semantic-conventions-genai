"""Reference implementation for Anthropic using opentelemetry-util-genai."""

import os

os.environ["OTEL_SEMCONV_STABILITY_OPT_IN"] = "gen_ai_latest_experimental"
os.environ["OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT"] = "SPAN_AND_EVENT"
os.environ["OTEL_INSTRUMENTATION_GENAI_EMIT_EVENT"] = "true"

from opentelemetry.instrumentation._semconv import _OpenTelemetrySemanticConventionStability

_OpenTelemetrySemanticConventionStability._initialize()

import base64  # noqa: E402
import json  # noqa: E402

import anthropic  # noqa: E402
from opentelemetry.util.genai.handler import get_telemetry_handler  # noqa: E402
from opentelemetry.util.genai.types import Blob, Error, InputMessage, OutputMessage, Text  # noqa: E402
from reference_shared import flush_and_shutdown, mock_server_host_port, setup_otel  # noqa: E402

MOCK_BASE_URL = os.environ["MOCK_LLM_URL"]


def run_chat(handler):
    """Scenario: basic chat completion with reasoning.level."""
    print("  [chat] basic chat completion (util-genai handler)")
    request_model = "claude-sonnet-4-20250514"
    request_max_tokens = 100
    request_reasoning_level = "medium"
    messages = [{"role": "user", "content": "Say hello."}]
    client = anthropic.Anthropic(base_url=MOCK_BASE_URL, api_key="mock-key")

    host, port = mock_server_host_port(MOCK_BASE_URL)
    # start_inference args: provider -> gen_ai.provider.name, request_model -> gen_ai.request.model,
    # server_address/server_port -> server.address/server.port
    inv = handler.start_inference(
        provider="anthropic",
        request_model=request_model,
        server_address=host,
        server_port=port,
    )
    inv.max_tokens = request_max_tokens  # -> gen_ai.request.max_tokens
    inv.attributes["gen_ai.request.reasoning.level"] = request_reasoning_level  # -> gen_ai.request.reasoning.level
    inv.input_messages = [InputMessage(role="user", parts=[Text(content="Say hello.")])]  # -> gen_ai.input.messages

    resp = client.messages.create(
        model=request_model,
        max_tokens=request_max_tokens,
        messages=messages,
        output_config={"effort": request_reasoning_level},
    )

    inv.response_model_name = resp.model  # -> gen_ai.response.model
    inv.response_id = resp.id  # -> gen_ai.response.id
    inv.finish_reasons = [resp.stop_reason]  # -> gen_ai.response.finish_reasons

    if resp.usage:
        cache_creation = getattr(resp.usage, "cache_creation_input_tokens", None) or 0
        cache_read = getattr(resp.usage, "cache_read_input_tokens", None) or 0
        inv.input_tokens = resp.usage.input_tokens + cache_creation + cache_read  # -> gen_ai.usage.input_tokens
        inv.output_tokens = resp.usage.output_tokens  # -> gen_ai.usage.output_tokens
        if cache_creation:
            inv.cache_creation_input_tokens = cache_creation  # -> gen_ai.usage.cache_creation.input_tokens
        if cache_read:
            inv.cache_read_input_tokens = cache_read  # -> gen_ai.usage.cache_read.input_tokens

    inv.output_messages = [  # -> gen_ai.output.messages
        OutputMessage(
            role="assistant",
            parts=[Text(content=block.text)],
            finish_reason=resp.stop_reason,
        )
        for block in resp.content
        if hasattr(block, "text")
    ]
    inv.stop()

    print(f"    -> {resp.content[0].text[:60]}")


def _has_compaction_block_in_input(messages):
    """Return True if any input message contains a compaction content block."""
    for message in messages:
        content = message.get("content") if isinstance(message, dict) else getattr(message, "content", None)
        if isinstance(content, list):
            for block in content:
                block_type = block.get("type") if isinstance(block, dict) else getattr(block, "type", None)
                if block_type == "compaction":
                    return True
    return False


def _has_compaction_block_in_response(response):
    """Return True if the response carries a compaction signal."""
    if getattr(response, "stop_reason", None) == "compaction":
        return True
    for block in getattr(response, "content", []) or []:
        if getattr(block, "type", None) == "compaction":
            return True
    return any(
        getattr(it, "type", None) == "compaction"
        for it in getattr(getattr(response, "usage", None), "iterations", []) or []
    )


def run_compaction(handler):
    """Scenario: server-side compaction via context_management beta.

    gen_ai.conversation.compacted is set via inv.attributes since
    InferenceInvocation does not have a first-class property for it yet.
    Compaction blocks in input/output messages are serialised manually
    via inv.attributes["gen_ai.input.messages"] because opentelemetry-util-genai
    v0.4b0 does not have a CompactionPart type.
    """
    print("  [chat_compaction] chat with server-side compaction (util-genai handler)")
    request_model = "claude-sonnet-4-20250514"
    request_max_tokens = 100
    messages = [
        {
            "role": "assistant",
            "content": [
                {
                    "type": "compaction",
                    "encrypted_content": "opaque encrypted compaction state from a prior turn",
                }
            ],
        },
        {"role": "user", "content": "Continue this long conversation."},
    ]
    client = anthropic.Anthropic(base_url=MOCK_BASE_URL, api_key="mock-key")

    host, port = mock_server_host_port(MOCK_BASE_URL)
    inv = handler.start_inference(
        provider="anthropic",
        request_model=request_model,
        server_address=host,
        server_port=port,
    )
    inv.max_tokens = request_max_tokens  # -> gen_ai.request.max_tokens

    # Compaction blocks have no util-genai type yet; set gen_ai.input.messages manually.
    inv.attributes["gen_ai.input.messages"] = json.dumps(  # -> gen_ai.input.messages
        [
            {
                "role": "assistant",
                "parts": [
                    {
                        "type": "compaction",
                        "content": "opaque encrypted compaction state from a prior turn",
                    }
                ],
            },
            {"role": "user", "parts": [{"type": "text", "content": "Continue this long conversation."}]},
        ]
    )

    resp = client.beta.messages.create(
        model=request_model,
        max_tokens=request_max_tokens,
        messages=messages,
        context_management={
            "edits": [
                {
                    "type": "compact_20260112",
                    "trigger": {"type": "input_tokens", "value": 200000},
                    "pause_after_compaction": True,
                }
            ]
        },
        betas=["context-management-2026-01-12"],
    )

    conversation_compacted = _has_compaction_block_in_input(messages) or _has_compaction_block_in_response(resp)
    inv.attributes["gen_ai.conversation.compacted"] = conversation_compacted  # -> gen_ai.conversation.compacted

    inv.response_model_name = resp.model  # -> gen_ai.response.model
    inv.response_id = resp.id  # -> gen_ai.response.id
    inv.finish_reasons = [resp.stop_reason]  # -> gen_ai.response.finish_reasons

    if resp.usage:
        inv.input_tokens = resp.usage.input_tokens  # -> gen_ai.usage.input_tokens
        inv.output_tokens = resp.usage.output_tokens  # -> gen_ai.usage.output_tokens

    output_parts = []
    for block in getattr(resp, "content", []) or []:
        block_type = getattr(block, "type", None)
        if block_type == "text" and getattr(block, "text", None):
            output_parts.append({"type": "text", "content": block.text})
        elif block_type == "compaction":
            part = {"type": "compaction"}
            compaction_content = getattr(block, "content", None)
            if compaction_content:
                part["content"] = compaction_content
            output_parts.append(part)
    if output_parts:
        inv.attributes["gen_ai.output.messages"] = json.dumps(  # -> gen_ai.output.messages
            [{"role": "assistant", "parts": output_parts, "finish_reason": resp.stop_reason}]
        )

    inv.stop()

    print(f"    -> compacted: {conversation_compacted}")


def run_chat_with_document_input(handler):
    """Scenario: chat with a PDF document block (document modality)."""
    print("  [chat_document] chat with PDF document block (util-genai handler)")
    request_model = "claude-sonnet-4-20250514"
    request_max_tokens = 100
    instruction = "Summarize the attached document in one sentence."
    pdf_bytes = b"%PDF-1.4\n%mock pdf for reference scenario\n%%EOF\n"
    pdf_b64 = base64.b64encode(pdf_bytes).decode("ascii")
    mime_type = "application/pdf"
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": instruction},
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": mime_type,
                        "data": pdf_b64,
                    },
                },
            ],
        }
    ]
    client = anthropic.Anthropic(base_url=MOCK_BASE_URL, api_key="mock-key")

    host, port = mock_server_host_port(MOCK_BASE_URL)
    # start_inference args: provider -> gen_ai.provider.name, request_model -> gen_ai.request.model,
    # server_address/server_port -> server.address/server.port
    inv = handler.start_inference(
        provider="anthropic",
        request_model=request_model,
        server_address=host,
        server_port=port,
    )
    inv.max_tokens = request_max_tokens  # -> gen_ai.request.max_tokens
    inv.input_messages = [  # -> gen_ai.input.messages
        InputMessage(
            role="user",
            parts=[
                Text(content=instruction),
                Blob(mime_type=mime_type, modality="document", content=pdf_bytes),
            ],
        )
    ]

    resp = client.messages.create(
        model=request_model,
        max_tokens=request_max_tokens,
        messages=messages,
    )

    inv.response_model_name = resp.model  # -> gen_ai.response.model
    inv.response_id = resp.id  # -> gen_ai.response.id
    inv.finish_reasons = [resp.stop_reason]  # -> gen_ai.response.finish_reasons

    if resp.usage:
        cache_creation = getattr(resp.usage, "cache_creation_input_tokens", None) or 0
        cache_read = getattr(resp.usage, "cache_read_input_tokens", None) or 0
        inv.input_tokens = resp.usage.input_tokens + cache_creation + cache_read  # -> gen_ai.usage.input_tokens
        inv.output_tokens = resp.usage.output_tokens  # -> gen_ai.usage.output_tokens
        if cache_creation:
            inv.cache_creation_input_tokens = cache_creation  # -> gen_ai.usage.cache_creation.input_tokens
        if cache_read:
            inv.cache_read_input_tokens = cache_read  # -> gen_ai.usage.cache_read.input_tokens

    inv.output_messages = [  # -> gen_ai.output.messages
        OutputMessage(
            role="assistant",
            parts=[Text(content=block.text)],
            finish_reason=resp.stop_reason,
        )
        for block in resp.content
        if hasattr(block, "text")
    ]
    inv.stop()

    print(f"    -> {resp.content[0].text[:60]}")


def run_chat_error(handler):
    """Scenario: error path."""
    print("  [chat_error] error path (util-genai handler)")
    request_model = "claude-sonnet-4-20250514"
    client = anthropic.Anthropic(base_url=MOCK_BASE_URL, api_key="mock-key")

    host, port = mock_server_host_port(MOCK_BASE_URL)
    inv = handler.start_inference(
        provider="anthropic",
        request_model=request_model,
        server_address=host,
        server_port=port,
    )
    inv.max_tokens = 1
    inv.input_messages = [InputMessage(role="user", parts=[Text(content="Trigger error")])]

    try:
        client.messages.create(
            model="",
            max_tokens=1,
            messages=[{"role": "user", "content": "Trigger error"}],
        )
    except Exception as exc:  # noqa: BLE001
        inv.fail(Error(type=type(exc), message=str(exc)))
        print(f"    -> caught expected error: {type(exc).__name__}")


def main():
    """Run all Anthropic reference scenarios."""
    print("=== Reference Implementation: Anthropic (util-genai) ===")

    tp, lp, mp = setup_otel()
    handler = get_telemetry_handler(
        tracer_provider=tp,
        meter_provider=mp,
        logger_provider=lp,
    )

    run_chat(handler)
    run_compaction(handler)
    run_chat_with_document_input(handler)
    run_chat_error(handler)

    flush_and_shutdown(tp, lp, mp)


if __name__ == "__main__":
    main()
