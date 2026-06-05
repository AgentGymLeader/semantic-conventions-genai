> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.

## Waiting on approvers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova | ✅ | ✅ | 8d |
| [semconv for a2a protocol (#195)](https://github.com/open-telemetry/semantic-conventions-genai/pull/195) | eternalcuriouslearner |  | ✅ | ✅ | 6d |
| [Generalize the `gen_ai.provider.name` description (#212)](https://github.com/open-telemetry/semantic-conventions-genai/pull/212) ✅✅ | trask |  | ✅ | ✅ | 16h |
| [Clarify that billed token counts should be reported for Cohere usage (#211)](https://github.com/open-telemetry/semantic-conventions-genai/pull/211) ✅✅ | trask |  | ✅ | ✅ | 15h |
| [Normalize requirement-level condition notes to capitalized sentences (#245)](https://github.com/open-telemetry/semantic-conventions-genai/pull/245) ✅ | trask |  | ✅ | ✅ | 15h |
| [Add gen_ai.agent.invocation.id attribute for invoke_agent spans (#250)](https://github.com/open-telemetry/semantic-conventions-genai/pull/250) | singankit |  | ❌ | ✅ | 47m |

## Waiting on authors

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: make input-messages BlobPart content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid |  | ✅ | ✅ | 24d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede |  | ✅ | ❌ | 17d |
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) ✅ | app/renovate |  | ❌ | ✅ | 16d |
| [gen-ai: add evaluation operation name and gen_ai.evaluate.internal span (#185)](https://github.com/open-telemetry/semantic-conventions-genai/pull/185) | hippoley |  | ❌ | ✅ | 14d |
| [Add experimental GenAI context selection event (#190)](https://github.com/open-telemetry/semantic-conventions-genai/pull/190) | caioribeiroclw-pixel |  | ❌ | ❌ | 13d |
| [Update dependency google-adk to v2 (#173)](https://github.com/open-telemetry/semantic-conventions-genai/pull/173) | app/renovate |  | ❌ | ✅ | 8d |
| [Add gen_ai.agent.invocation.duration and gen_ai.tool.execution.duration metrics (#201)](https://github.com/open-telemetry/semantic-conventions-genai/pull/201) | pvlsirotkin |  | ✅ | ❌ | 7d |
| [gen-ai: add gen_ai.response.id to deepeval evaluation result event (#184)](https://github.com/open-telemetry/semantic-conventions-genai/pull/184) ✅ | hippoley |  | ✅ | ✅ | 7d |
| [Add workflow node convention (#188)](https://github.com/open-telemetry/semantic-conventions-genai/pull/188) | RKest |  | ✅ | ❌ | 5d |
| [Add modality, cache, and phase breakdowns for token usage (#197)](https://github.com/open-telemetry/semantic-conventions-genai/pull/197) | trask | lmolkova | ✅ | ❌ | 5d |
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid |  | ✅ | ✅ | 3d |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) ✅ | eternalcuriouslearner | lmolkova, JWinermaSplunk | ✅ | ❌ | 3d |
| [Replace Jupiter notebook with models with python file and add CI check that json schemas are up-to-date (#226)](https://github.com/open-telemetry/semantic-conventions-genai/pull/226) ✅✅ | lmolkova |  | ✅ | ✅ | 2d |
| [Limit gen_ai.agent.id to stable / static identifiers (#242)](https://github.com/open-telemetry/semantic-conventions-genai/pull/242) | lmolkova |  | ✅ | ❌ | 1d |
| [Add gen_ai.agent.finish_reason attribute for agent loop termination (#238)](https://github.com/open-telemetry/semantic-conventions-genai/pull/238) | Nik-Reddy |  | ✅ | ❌ | 18h |
| [Add gen_ai.agent.request.size and gen_ai.agent.response.size metrics (#202)](https://github.com/open-telemetry/semantic-conventions-genai/pull/202) | pvlsirotkin |  | ✅ | ✅ | 17h |
| [Add gen_ai.workflow.steps metric (#203)](https://github.com/open-telemetry/semantic-conventions-genai/pull/203) | pvlsirotkin |  | ✅ | ✅ | 16h |
| [Clarify scope of `gen_ai.client.operation.duration` metric (#215)](https://github.com/open-telemetry/semantic-conventions-genai/pull/215) | trask |  | ✅ | ❌ | 9h |
| [Add gen_ai.invoke_agent.server span (SERVER kind) (#252)](https://github.com/open-telemetry/semantic-conventions-genai/pull/252) | singankit |  | ✅ | ✅ | 6h |
| [Add Reviewers column to PR dashboard (#251)](https://github.com/open-telemetry/semantic-conventions-genai/pull/251) ✅ | trask |  | ✅ | ✅ | 4h |
| [Add prompt versioning and variable support to GenAI attributes (#179)](https://github.com/open-telemetry/semantic-conventions-genai/pull/179) | steverao | lmolkova | ✅ | ❌ | 2h |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 13d |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | 6d |

<details>
<summary>Diagnostics</summary>

```text
```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

