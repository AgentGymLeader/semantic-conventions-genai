# Client Token Usage Metric

> **[Semantic Convention](../../docs/gen-ai/gen-ai-metrics.md#metric-gen_aiclienttokenusage)**

## Required

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.operation.name | [agent-framework], [anthropic], [google-adk] |
| gen_ai.provider.name | [agent-framework], [anthropic], [google-adk] |
| gen_ai.token.type | [agent-framework], [anthropic], [google-adk] |

## Conditionally Required

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.request.model | [agent-framework], [anthropic], [google-adk] |
| server.port | [anthropic] |

## Recommended

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.response.model | [agent-framework], [anthropic], [google-adk] |
| server.address | [agent-framework], [anthropic] |

[agent-framework]: ../scenarios/agent-framework/scenario.py
[anthropic]: ../scenarios/anthropic/scenario.py
[google-adk]: ../scenarios/google-adk/scenario.py
