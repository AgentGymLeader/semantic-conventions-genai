"""Reference implementation for Anthropic.

Exercises: chat completion
against a mock Anthropic server, with manual OTel spans.
"""

import json
import os
import time

from reference_shared import (
    flush_and_shutdown,
    mock_server_host_port,
    reference_event_logger,
    reference_meter,
    reference_tracer,
    setup_otel,
)

MOCK_BASE_URL = os.environ["MOCK_LLM_URL"]
TOKEN_BUCKET_BOUNDARIES = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864]

_reference_tracer = reference_tracer()
_reference_meter = reference_meter()
_token_usage_histogram = _reference_meter.create_histogram(
    "gen_ai.client.token.usage",
    unit="{token}",
    explicit_bucket_boundaries_advisory=TOKEN_BUCKET_BOUNDARIES,
)
_operation_duration_histogram = _reference_meter.create_histogram("gen_ai.client.operation.duration", unit="s")


def run_chat():
    """Scenario: basic chat via Anthropic with reference implementation."""
    import anthropic

    print("  [chat] basic chat completion (reference implementation)")
    request_model = "claude-sonnet-4-20250514"
    request_max_tokens = 100
    messages = [{"role": "user", "content": "Say hello."}]
    client = anthropic.Anthropic(base_url=MOCK_BASE_URL, api_key="mock-key")

    host, port = mock_server_host_port(MOCK_BASE_URL)
    span_attributes = {
        "gen_ai.operation.name": "chat",
        "gen_ai.provider.name": "anthropic",
        "gen_ai.request.model": request_model,
    }
    if host:
        span_attributes["server.address"] = host
    if port is not None:
        span_attributes["server.port"] = port
    with _reference_tracer.start_as_current_span("chat claude-sonnet-4-20250514", attributes=span_attributes) as span:
        span.set_attribute("gen_ai.request.max_tokens", request_max_tokens)
        span.set_attribute(
            "gen_ai.input.messages",
            json.dumps([{"role": m["role"], "parts": [{"type": "text", "content": m["content"]}]} for m in messages]),
        )
        start_time = time.perf_counter()
        resp = client.messages.create(
            model=request_model,
            max_tokens=request_max_tokens,
            messages=messages,
        )
        elapsed = time.perf_counter() - start_time
        metric_attributes = {
            "gen_ai.operation.name": "chat",
            "gen_ai.provider.name": "anthropic",
            "gen_ai.request.model": request_model,
        }
        response_model = getattr(resp, "model", None)
        if response_model:
            metric_attributes["gen_ai.response.model"] = response_model
        if host:
            metric_attributes["server.address"] = host
        if port is not None:
            metric_attributes["server.port"] = port
        if resp.usage:
            cache_creation = getattr(resp.usage, "cache_creation_input_tokens", None) or 0
            cache_read = getattr(resp.usage, "cache_read_input_tokens", None) or 0
            total_input = resp.usage.input_tokens + cache_creation + cache_read
            _token_usage_histogram.record(
                total_input,
                attributes={**metric_attributes, "gen_ai.token.type": "input"},
            )
            _token_usage_histogram.record(
                resp.usage.output_tokens,
                attributes={**metric_attributes, "gen_ai.token.type": "output"},
            )
        _operation_duration_histogram.record(elapsed, attributes=metric_attributes)
        span.set_attribute("gen_ai.response.model", resp.model)
        span.set_attribute("gen_ai.response.id", resp.id)
        span.set_attribute("gen_ai.response.finish_reasons", [resp.stop_reason])
        if resp.usage:
            cache_creation = getattr(resp.usage, "cache_creation_input_tokens", None) or 0
            cache_read = getattr(resp.usage, "cache_read_input_tokens", None) or 0
            total_input = resp.usage.input_tokens + cache_creation + cache_read
            span.set_attribute("gen_ai.usage.input_tokens", total_input)
            span.set_attribute("gen_ai.usage.output_tokens", resp.usage.output_tokens)
            if cache_creation:
                span.set_attribute("gen_ai.usage.cache_creation.input_tokens", cache_creation)
            if cache_read:
                span.set_attribute("gen_ai.usage.cache_read.input_tokens", cache_read)
        output_messages = json.dumps(
            [
                {
                    "role": "assistant",
                    "parts": [{"type": "text", "content": block.text}],
                    "finish_reason": resp.stop_reason,
                }
                for block in resp.content
                if hasattr(block, "text")
            ]
        )
        span.set_attribute("gen_ai.output.messages", output_messages)

        # Emit inference operation details event
        event_attrs = {
            "gen_ai.operation.name": "chat",
            "gen_ai.request.model": request_model,
            "gen_ai.response.id": resp.id,
            "gen_ai.response.model": resp.model,
            "gen_ai.response.finish_reasons": [resp.stop_reason],
            "gen_ai.input.messages": json.dumps(
                [{"role": m["role"], "parts": [{"type": "text", "content": m["content"]}]} for m in messages]
            ),
            "gen_ai.output.messages": output_messages,
        }
        if resp.usage:
            cache_creation = getattr(resp.usage, "cache_creation_input_tokens", None) or 0
            cache_read = getattr(resp.usage, "cache_read_input_tokens", None) or 0
            total_input = resp.usage.input_tokens + cache_creation + cache_read
            event_attrs["gen_ai.usage.input_tokens"] = total_input
            event_attrs["gen_ai.usage.output_tokens"] = resp.usage.output_tokens
            if cache_creation:
                event_attrs["gen_ai.usage.cache_creation.input_tokens"] = cache_creation
            if cache_read:
                event_attrs["gen_ai.usage.cache_read.input_tokens"] = cache_read
        if host:
            event_attrs["server.address"] = host
        if port is not None:
            event_attrs["server.port"] = port
        reference_event_logger().emit(
            event_name="gen_ai.client.inference.operation.details",
            body="Inference operation details",
            attributes=event_attrs,
        )

        print(f"    -> {resp.content[0].text[:60]}")


def run_chat_with_document_input():
    """Scenario: chat with a base64 document block (document modality).

    Exercises the `document` value of the `Modality` enum on a `BlobPart`
    in `gen_ai.input.messages`. Anthropic's Messages API has a first-class
    `document` content block that exposes the mime type and source bytes
    directly on the SDK call boundary -- so every emitted BlobPart field
    traces back to the SDK arg without any Files-API roundtrip:

      {"type": "document",
       "source": {"type": "base64", "media_type": "application/pdf", "data": "..."}}
    """
    import base64

    import anthropic

    print("  [chat_document] chat with PDF document block (reference implementation)")
    request_model = "claude-sonnet-4-20250514"
    request_max_tokens = 100
    instruction = "Summarize the attached document in one sentence."
    pdf_bytes = b"%PDF-1.4\n%mock pdf for reference scenario\n%%EOF\n"
    pdf_b64 = base64.b64encode(pdf_bytes).decode("ascii")
    mime_type = "application/pdf"

    # SDK boundary: native Anthropic document content block.
    user_content = [
        {"type": "text", "text": instruction},
        {
            "type": "document",
            "source": {"type": "base64", "media_type": mime_type, "data": pdf_b64},
        },
    ]
    messages = [{"role": "user", "content": user_content}]
    client = anthropic.Anthropic(base_url=MOCK_BASE_URL, api_key="mock-key")

    # Canonical OTel parts: TextPart + BlobPart(modality="document"). Each
    # BlobPart field is derivable from the document block above:
    #   - mime_type: `source.media_type`
    #   - content:   `source.data` (already base64)
    #   - modality:  classification of media_type "application/pdf"
    input_parts = [
        {"type": "text", "content": instruction},
        {
            "type": "blob",
            "modality": "document",
            "mime_type": mime_type,
            "content": pdf_b64,
        },
    ]
    input_messages = json.dumps([{"role": "user", "parts": input_parts}])

    host, port = mock_server_host_port(MOCK_BASE_URL)
    span_attributes_doc = {
        "gen_ai.operation.name": "chat",
        "gen_ai.provider.name": "anthropic",
        "gen_ai.request.model": request_model,
    }
    if host:
        span_attributes_doc["server.address"] = host
    if port is not None:
        span_attributes_doc["server.port"] = port
    with _reference_tracer.start_as_current_span(
        "chat claude-sonnet-4-20250514", attributes=span_attributes_doc
    ) as span:
        span.set_attribute("gen_ai.request.max_tokens", request_max_tokens)
        span.set_attribute("gen_ai.input.messages", input_messages)
        resp = client.messages.create(
            model=request_model,
            max_tokens=request_max_tokens,
            messages=messages,
        )
        span.set_attribute("gen_ai.response.model", resp.model)
        span.set_attribute("gen_ai.response.id", resp.id)
        span.set_attribute("gen_ai.response.finish_reasons", [resp.stop_reason])
        if resp.usage:
            cache_creation = getattr(resp.usage, "cache_creation_input_tokens", None) or 0
            cache_read = getattr(resp.usage, "cache_read_input_tokens", None) or 0
            total_input = resp.usage.input_tokens + cache_creation + cache_read
            span.set_attribute("gen_ai.usage.input_tokens", total_input)
            span.set_attribute("gen_ai.usage.output_tokens", resp.usage.output_tokens)
        output_messages = json.dumps(
            [
                {
                    "role": "assistant",
                    "parts": [{"type": "text", "content": block.text}],
                    "finish_reason": resp.stop_reason,
                }
                for block in resp.content
                if hasattr(block, "text")
            ]
        )
        span.set_attribute("gen_ai.output.messages", output_messages)
        print(f"    -> {resp.content[0].text[:60]}")


def run_chat_error():
    """Scenario: error path — records operation duration with error.type.

    Connects to an unreachable address so the Anthropic SDK raises
    APIConnectionError, exercising the error.type attribute on the
    gen_ai.client.operation.duration metric.
    """
    import anthropic

    print("  [chat_error] error path (reference implementation)")
    request_model = "claude-sonnet-4-20250514"
    # Point to a port that is not listening so the SDK raises APIConnectionError.
    bad_url = "http://127.0.0.1:1"
    client = anthropic.Anthropic(base_url=bad_url, api_key="mock-key")

    metric_attributes = {
        "gen_ai.operation.name": "chat",
        "gen_ai.provider.name": "anthropic",
        "gen_ai.request.model": request_model,
    }
    start_time = time.perf_counter()
    try:
        client.messages.create(
            model=request_model,
            max_tokens=100,
            messages=[{"role": "user", "content": "Say hello."}],
        )
    except anthropic.APIError as exc:
        elapsed = time.perf_counter() - start_time
        _operation_duration_histogram.record(
            elapsed,
            attributes={**metric_attributes, "error.type": type(exc).__qualname__},
        )
        print(f"    -> error recorded: {type(exc).__qualname__}")


def main():
    print("=== Reference Implementation: Anthropic Reference Implementation ===")

    tp, lp, mp = setup_otel()

    run_chat()
    run_chat_with_document_input()
    run_chat_error()

    flush_and_shutdown(tp, lp, mp)


if __name__ == "__main__":
    main()
