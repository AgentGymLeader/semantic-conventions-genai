# Invoke Agent Client Span

> **[Semantic Convention](../../docs/gen-ai/gen-ai-agent-spans.md#invoke-agent-client-span)**

## Required

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.operation.name | [agent-governance], [aws-bedrock-agent], [azure-ai-foundry], [openai-assistants] |
| gen_ai.provider.name | [agent-governance], [aws-bedrock-agent], [azure-ai-foundry], [openai-assistants] |

## Conditionally Required

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.agent.description | [openai-assistants] |
| gen_ai.agent.id | [aws-bedrock-agent], [openai-assistants] |
| gen_ai.agent.name | [agent-governance], [azure-ai-foundry], [openai-assistants] |
| gen_ai.agent.version | [aws-bedrock-agent] |
| gen_ai.conversation.id | [aws-bedrock-agent], [openai-assistants] |
| gen_ai.data_source.id | (none) |
| gen_ai.output.type | [azure-ai-foundry] |
| gen_ai.request.choice.count | (none) |
| gen_ai.request.seed | (none) |
| server.port | [agent-governance], [aws-bedrock-agent], [azure-ai-foundry], [openai-assistants] |

## Recommended

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.request.frequency_penalty | (none) |
| gen_ai.request.max_tokens | [azure-ai-foundry], [openai-assistants] |
| gen_ai.request.model | [agent-governance], [azure-ai-foundry], [openai-assistants] |
| gen_ai.request.presence_penalty | (none) |
| gen_ai.request.stop_sequences | (none) |
| gen_ai.request.temperature | [azure-ai-foundry], [openai-assistants] |
| gen_ai.request.top_p | [azure-ai-foundry], [openai-assistants] |
| gen_ai.response.finish_reasons | [agent-governance] |
| gen_ai.usage.cache_creation.input_tokens | (none) |
| gen_ai.usage.cache_read.input_tokens | (none) |
| gen_ai.usage.input_tokens | [agent-governance], [azure-ai-foundry], [openai-assistants] |
| gen_ai.usage.output_tokens | [agent-governance], [azure-ai-foundry], [openai-assistants] |
| server.address | [agent-governance], [aws-bedrock-agent], [azure-ai-foundry], [openai-assistants] |

## Opt-In

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.input.messages | [agent-governance], [aws-bedrock-agent], [azure-ai-foundry], [openai-assistants] |
| gen_ai.output.messages | [agent-governance], [aws-bedrock-agent], [azure-ai-foundry], [openai-assistants] |
| gen_ai.system_instructions | [azure-ai-foundry], [openai-assistants] |
| gen_ai.tool.definitions | [agent-governance], [azure-ai-foundry], [openai-assistants] |

[agent-governance]: ../scenarios/agent-governance/scenario.py
[aws-bedrock-agent]: ../scenarios/aws-bedrock-agent/scenario.py
[azure-ai-foundry]: ../scenarios/azure-ai-foundry/scenario.py
[openai-assistants]: ../scenarios/openai-assistants/scenario.py
