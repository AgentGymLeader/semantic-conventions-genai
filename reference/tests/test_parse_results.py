import json
import logging
from pathlib import Path

from semconv_genai.parse_results import parse_result_dir


def _no_spans(_span_name: str, _span_kind: str, _span_attrs: dict[str, object]) -> set[str]:
    return set()


def _parse_samples(tmp_path: Path, samples: list[dict[str, object]]):
    (tmp_path / "result.json").write_text(json.dumps({"samples": samples}), encoding="utf-8")
    result = parse_result_dir(tmp_path, "test-library", _no_spans)
    assert result is not None
    return result


def _metric_data_point(token_type: str) -> dict[str, object]:
    return {
        "attributes": [
            {"name": "gen_ai.operation.name", "value": "chat"},
            {"name": "gen_ai.provider.name", "value": "anthropic"},
            {"name": "gen_ai.request.model", "value": "claude-sonnet-4-20250514"},
            {"name": "gen_ai.token.type", "value": token_type},
        ]
    }


def test_metric_with_multiple_data_points_counts_once(tmp_path: Path):
    result = _parse_samples(
        tmp_path,
        [
            {
                "metric": {
                    "name": "gen_ai.client.token.usage",
                    "data_points": [
                        _metric_data_point("input"),
                        _metric_data_point("output"),
                    ],
                }
            }
        ],
    )

    assert result.detected.metrics["gen_ai.client.token.usage"] == 1


def test_non_dict_data_points_warns_and_skips(tmp_path: Path, caplog):
    caplog.set_level(logging.WARNING, logger="semconv_genai.parse_results")

    result = _parse_samples(
        tmp_path,
        [
            {
                "metric": {
                    "name": "gen_ai.client.token.usage",
                    "data_points": "not-a-data-point",
                }
            }
        ],
    )

    assert result.detected.metrics == {}
    assert "invalid data_points" in caplog.text
    assert "gen_ai.client.token.usage" in caplog.text


def test_unrecognized_metric_warns(tmp_path: Path, caplog):
    caplog.set_level(logging.WARNING, logger="semconv_genai.parse_results")

    _parse_samples(
        tmp_path,
        [
            {
                "metric": {
                    "name": "gen_ai.client.not_a_metric",
                    "data_points": [_metric_data_point("input")],
                }
            }
        ],
    )

    assert "unrecognized metric" in caplog.text
    assert "gen_ai.client.not_a_metric" in caplog.text
