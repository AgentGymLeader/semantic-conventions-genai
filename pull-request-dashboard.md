> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.
>
> Reviewers column: ✅ approved · ✔️ approved (non-code-owner) · 💬 open thread · 🔴 changes requested.

## Waiting on maintainers

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Generalize the `gen_ai.provider.name` description (#212)](https://github.com/open-telemetry/semantic-conventions-genai/pull/212) | trask | lmolkova&nbsp;✅<br>MikeGoldsmith&nbsp;✅ | ✅ | ✅ | 7m |

## Waiting on reviewers

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-adk to v2 (#173)](https://github.com/open-telemetry/semantic-conventions-genai/pull/173) | app/renovate | MikeGoldsmith&nbsp;💬 | ❌ | ✅ | 17d |
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova<br>MikeGoldsmith&nbsp;🔴<br>trask&nbsp;💬 | ✅ | ❌ | 8d |
| [Clarify scope of `gen_ai.client.operation.duration` metric (#215)](https://github.com/open-telemetry/semantic-conventions-genai/pull/215) | trask | lmolkova | ✅ | ❌ | 7d |
| [semconv for a2a protocol (#195)](https://github.com/open-telemetry/semantic-conventions-genai/pull/195) | eternalcuriouslearner |  | ✅ | ✅ | 6d |
| [Add gen_ai.agent.invocation.id attribute for invoke_agent spans (#250)](https://github.com/open-telemetry/semantic-conventions-genai/pull/250) | singankit | lmolkova&nbsp;💬 | ✅ | ✅ | 11h |

## Waiting on authors

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: make input-messages BlobPart content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid | Copilot&nbsp;💬<br>trask | ✅ | ✅ | 24d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede | lmolkova&nbsp;💬 | ✅ | ❌ | 17d |
| [gen-ai: add evaluation operation name and gen_ai.evaluate.internal span (#185)](https://github.com/open-telemetry/semantic-conventions-genai/pull/185) | hippoley | Cirilla-zmh&nbsp;💬<br>Copilot&nbsp;💬<br>singankit&nbsp;💬 | ❌ | ✅ | 15d |
| [Add experimental GenAI context selection event (#190)](https://github.com/open-telemetry/semantic-conventions-genai/pull/190) | caioribeiroclw-pixel | Copilot&nbsp;💬<br>trask&nbsp;💬 | ❌ | ❌ | 13d |
| [Add gen_ai.agent.invocation.duration and gen_ai.tool.execution.duration metrics (#201)](https://github.com/open-telemetry/semantic-conventions-genai/pull/201) | pvlsirotkin | MikeGoldsmith&nbsp;🔴 | ✅ | ❌ | 8d |
| [gen-ai: add gen_ai.response.id to deepeval evaluation result event (#184)](https://github.com/open-telemetry/semantic-conventions-genai/pull/184) | hippoley | lmolkova&nbsp;✅<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ✅ | 8d |
| [Add workflow node convention (#188)](https://github.com/open-telemetry/semantic-conventions-genai/pull/188) | RKest | lmolkova&nbsp;🔴<br>trask&nbsp;💬 | ✅ | ❌ | 5d |
| [Add modality, cache, and phase breakdowns for token usage (#197)](https://github.com/open-telemetry/semantic-conventions-genai/pull/197) | trask | alexmojaki&nbsp;💬<br>lmolkova&nbsp;💬<br>Nik-Reddy&nbsp;💬 | ✅ | ❌ | 5d |
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid | Cirilla-zmh<br>trask&nbsp;💬 | ✅ | ✅ | 4d |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) | eternalcuriouslearner | JWinermaSplunk<br>lmolkova&nbsp;💬⁠✅<br>trask | ✅ | ❌ | 3d |
| [Limit gen_ai.agent.id to stable / static identifiers (#242)](https://github.com/open-telemetry/semantic-conventions-genai/pull/242) | lmolkova | Copilot&nbsp;💬 | ✅ | ❌ | 1d |
| [Add gen_ai.agent.finish_reason attribute for agent loop termination (#238)](https://github.com/open-telemetry/semantic-conventions-genai/pull/238) | Nik-Reddy | Copilot&nbsp;💬<br>MikeGoldsmith&nbsp;🔴 | ✅ | ❌ | 1d |
| [Add gen_ai.agent.request.size and gen_ai.agent.response.size metrics (#202)](https://github.com/open-telemetry/semantic-conventions-genai/pull/202) | pvlsirotkin | Copilot&nbsp;💬<br>lmolkova&nbsp;💬<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ✅ | 1d |
| [Add gen_ai.workflow.steps metric (#203)](https://github.com/open-telemetry/semantic-conventions-genai/pull/203) | pvlsirotkin | lmolkova&nbsp;💬<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ✅ | 1d |
| [Add gen_ai.invoke_agent.server span (SERVER kind) (#252)](https://github.com/open-telemetry/semantic-conventions-genai/pull/252) | singankit | Copilot&nbsp;💬 | ✅ | ✅ | 17h |
| [Add prompt versioning and variable support to GenAI attributes (#179)](https://github.com/open-telemetry/semantic-conventions-genai/pull/179) | steverao | lmolkova&nbsp;💬<br>trask | ✅ | ❌ | 14h |
| [Clarify that billed token counts should be reported for Cohere usage (#211)](https://github.com/open-telemetry/semantic-conventions-genai/pull/211) | trask | lmolkova&nbsp;✅<br>MikeGoldsmith&nbsp;💬⁠✅ | ✅ | ❌ | 1h |

## Waiting on external

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) | app/renovate | DylanRussell&nbsp;💬<br>lmolkova&nbsp;✅ | ❌ | ✅ | 17d |

## Unknown

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Replace Jupiter notebook with models with python file and add CI check that json schemas are up-to-date (#226)](https://github.com/open-telemetry/semantic-conventions-genai/pull/226) | lmolkova |  | ✅ | ✅ | 3d |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 13d |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | 7d |

<details>
<summary>Diagnostics</summary>

```text
```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

