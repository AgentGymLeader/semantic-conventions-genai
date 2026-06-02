> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.

## Waiting on maintainers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Clarify that billed token counts should be reported for Cohere usage (#211)](https://github.com/open-telemetry/semantic-conventions-genai/pull/211) ✅ | trask |  | ✅ | ✅ | 4d |
| [Generalize the `gen_ai.provider.name` description (#212)](https://github.com/open-telemetry/semantic-conventions-genai/pull/212) ✅ | trask |  | ✅ | ✅ | 4d |
| [Relax `gen_ai.provider.name` on `gen_ai.client.operation.duration` to Conditionally Required (#214)](https://github.com/open-telemetry/semantic-conventions-genai/pull/214) ✅ | trask |  | ✅ | ✅ | 4d |
| [Clarify GenAI span duration (#216)](https://github.com/open-telemetry/semantic-conventions-genai/pull/216) ✅ | trask |  | ✅ | ✅ | 4d |
| [Clarify GenAI conversation ID fallbacks (#219)](https://github.com/open-telemetry/semantic-conventions-genai/pull/219) ✅ | trask |  | ✅ | ✅ | 4d |
| [Change `gen_ai.request.top_k` type to int and split out `gen_ai.retrieval.top_k` (#217)](https://github.com/open-telemetry/semantic-conventions-genai/pull/217) ✅ | trask |  | ✅ | ✅ | 3d |
| [Clarify MCP context propagation (#220)](https://github.com/open-telemetry/semantic-conventions-genai/pull/220) ✅ | trask |  | ✅ | ✅ | 18h |

## Waiting on approvers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova | ✅ | ✅ | 5d |
| [semconv for a2a protocol (#195)](https://github.com/open-telemetry/semantic-conventions-genai/pull/195) | eternalcuriouslearner |  | ✅ | ✅ | 3d |

## Waiting on authors

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: make input-messages BlobPart content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid |  | ✅ | ✅ | 21d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede |  | ✅ | ❌ | 14d |
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) ✅ | app/renovate |  | ❌ | ✅ | 14d |
| [gen-ai: add evaluation operation name and gen_ai.evaluate.internal span (#185)](https://github.com/open-telemetry/semantic-conventions-genai/pull/185) | hippoley |  | ❌ | ✅ | 12d |
| [Add experimental GenAI context selection event (#190)](https://github.com/open-telemetry/semantic-conventions-genai/pull/190) | caioribeiroclw-pixel |  | ❌ | ✅ | 10d |
| [Add prompt versioning and variable support to GenAI attributes (#179)](https://github.com/open-telemetry/semantic-conventions-genai/pull/179) | steverao | lmolkova | ✅ | ✅ | 10d |
| [Update dependency google-adk to v2 (#173)](https://github.com/open-telemetry/semantic-conventions-genai/pull/173) | app/renovate |  | ❌ | ✅ | 6d |
| [Add gen_ai.workflow.steps metric (#203)](https://github.com/open-telemetry/semantic-conventions-genai/pull/203) | pvlsirotkin |  | ✅ | ✅ | 6d |
| [Add gen_ai.agent.invocation.duration and gen_ai.tool.execution.duration metrics (#201)](https://github.com/open-telemetry/semantic-conventions-genai/pull/201) | pvlsirotkin |  | ✅ | ✅ | 5d |
| [gen-ai: add gen_ai.response.id to deepeval evaluation result event (#184)](https://github.com/open-telemetry/semantic-conventions-genai/pull/184) | hippoley |  | ✅ | ✅ | 5d |
| [Add gen_ai.agent.request.size and gen_ai.agent.response.size metrics (#202)](https://github.com/open-telemetry/semantic-conventions-genai/pull/202) | pvlsirotkin |  | ✅ | ✅ | 2d |
| [Add workflow node convention (#188)](https://github.com/open-telemetry/semantic-conventions-genai/pull/188) | RKest |  | ✅ | ❌ | 2d |
| [Add modality, cache, and phase breakdowns for token usage (#197)](https://github.com/open-telemetry/semantic-conventions-genai/pull/197) | trask | lmolkova | ✅ | ✅ | 2d |
| [Clarify scope of `gen_ai.client.operation.duration` metric (#215)](https://github.com/open-telemetry/semantic-conventions-genai/pull/215) | trask |  | ✅ | ✅ | 1d |
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid |  | ✅ | ✅ | 1d |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) ✅ | eternalcuriouslearner | lmolkova, JWinermaSplunk | ✅ | ✅ | 17h |
| [Replace Jupiter notebook with models with python file and add CI check that json schemas are up-to-date (#226)](https://github.com/open-telemetry/semantic-conventions-genai/pull/226) ✅ | lmolkova |  | ✅ | ✅ | 7m |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 10d |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | 4d |

<details>
<summary>Diagnostics</summary>

```text
```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

