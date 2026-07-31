# Client Operation Duration Metric

> **[Semantic Convention](../../docs/gen-ai/gen-ai-metrics.md#metric-gen_aiclientoperationduration)**

## Required

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.operation.name | [agent-framework], [google-adk] |

## Conditionally Required

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.provider.name | [agent-framework], [google-adk] |
| gen_ai.request.model | [agent-framework], [google-adk] |
| server.port | (none) |

## Recommended

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.response.model | [agent-framework], [google-adk] |
| server.address | [agent-framework] |

[agent-framework]: ../scenarios/agent-framework/scenario.py
[google-adk]: ../scenarios/google-adk/scenario.py
