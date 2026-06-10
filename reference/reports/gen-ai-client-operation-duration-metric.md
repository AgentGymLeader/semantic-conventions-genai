# Client Operation Duration Metric

> **[Semantic Convention](../../docs/gen-ai/gen-ai-metrics.md#metric-gen_aiclientoperationduration)**

## Required

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.operation.name | [anthropic] |

## Conditionally Required

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.provider.name | [anthropic] |
| gen_ai.request.model | [anthropic] |
| server.port | [anthropic] |

## Recommended

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.response.model | [anthropic] |
| server.address | [anthropic] |

[anthropic]: ../scenarios/anthropic/scenario.py
