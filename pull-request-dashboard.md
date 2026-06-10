> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.
>
> Reviewers column: ✅ approved · ✔️ approved (non-code-owner) · 💬 open thread · 🔴 changes requested.

## Waiting on reviewers

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-adk to v2 (#173)](https://github.com/open-telemetry/semantic-conventions-genai/pull/173) | app/renovate | MikeGoldsmith&nbsp;💬 | ❌ | ✅ | 21d |
| [Clarify scope of `gen_ai.client.operation.duration` metric (#215)](https://github.com/open-telemetry/semantic-conventions-genai/pull/215) | trask | lmolkova | ✅ | ❌ | 11d |
| [Add gen_ai.agent.invocation.id attribute for invoke_agent spans (#250)](https://github.com/open-telemetry/semantic-conventions-genai/pull/250) | singankit | lmolkova&nbsp;💬<br>MikeGoldsmith&nbsp;🔴 | ✅ | ✅ | 4d |
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova<br>MikeGoldsmith&nbsp;✅<br>trask | ✅ | ❌ | 1d |
| [Avoid reviewer badges from PR conversation (#272)](https://github.com/open-telemetry/semantic-conventions-genai/pull/272) | trask | lmolkova&nbsp;✅ | ✅ | ✅ | 5h |
| [Improve Slack PR notification links (#271)](https://github.com/open-telemetry/semantic-conventions-genai/pull/271) | trask | lmolkova&nbsp;✅ | ✅ | ✅ | 5h |
| [Add gen_ai.request.reasoning.level attribute (#258)](https://github.com/open-telemetry/semantic-conventions-genai/pull/258) | katsuhisa91 | JWinermaSplunk<br>lmolkova | ✅ | ✅ | 1h |

## Waiting on authors

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: make input-messages BlobPart content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid | Copilot&nbsp;💬<br>lmolkova<br>trask | ✅ | ❌ | 29d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede | Cirilla-zmh&nbsp;💬<br>lmolkova&nbsp;💬 | ✅ | ❌ | 22d |
| [gen-ai: add evaluation operation name and gen_ai.evaluate.internal span (#185)](https://github.com/open-telemetry/semantic-conventions-genai/pull/185) | hippoley | Cirilla-zmh&nbsp;💬<br>Copilot&nbsp;💬<br>singankit&nbsp;💬 | ❌ | ✅ | 19d |
| [Add experimental GenAI context selection event (#190)](https://github.com/open-telemetry/semantic-conventions-genai/pull/190) | caioribeiroclw-pixel | Copilot&nbsp;💬<br>trask&nbsp;💬 | ❌ | ❌ | 18d |
| [gen-ai: add gen_ai.response.id to deepeval evaluation result event (#184)](https://github.com/open-telemetry/semantic-conventions-genai/pull/184) | hippoley | lmolkova&nbsp;✅<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ✅ | 12d |
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid | Cirilla-zmh<br>trask&nbsp;💬 | ✅ | ❌ | 10d |
| [Add modality, cache, and phase breakdowns for token usage (#197)](https://github.com/open-telemetry/semantic-conventions-genai/pull/197) | trask | alexmojaki&nbsp;💬<br>lmolkova&nbsp;💬<br>Nik-Reddy&nbsp;💬 | ✅ | ❌ | 10d |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) | eternalcuriouslearner | Copilot&nbsp;💬<br>JWinermaSplunk&nbsp;✅<br>lmolkova&nbsp;💬⁠✅<br>trask | ✅ | ❌ | 8d |
| [Add gen_ai.agent.request.size and gen_ai.agent.response.size metrics (#202)](https://github.com/open-telemetry/semantic-conventions-genai/pull/202) | pvlsirotkin | Copilot&nbsp;💬<br>lmolkova&nbsp;💬<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ✅ | 5d |
| [Add gen_ai.workflow.steps metric (#203)](https://github.com/open-telemetry/semantic-conventions-genai/pull/203) | pvlsirotkin | aabmass&nbsp;💬⁠✅<br>lmolkova&nbsp;💬<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ✅ | 5d |
| [Add gen_ai.invoke_agent.server span (SERVER kind) (#252)](https://github.com/open-telemetry/semantic-conventions-genai/pull/252) | singankit | Cirilla-zmh&nbsp;💬<br>Copilot&nbsp;💬 | ✅ | ✅ | 4d |
| [Add prompt versioning and variable support to GenAI attributes (#179)](https://github.com/open-telemetry/semantic-conventions-genai/pull/179) | steverao | lmolkova&nbsp;💬<br>trask | ✅ | ❌ | 4d |
| [Limit supported  part types  on `gen_ai.system_instructions` to text only (#257)](https://github.com/open-telemetry/semantic-conventions-genai/pull/257) | lmolkova | MikeGoldsmith&nbsp;💬⁠✅ | ✅ | ✅ | 1d |
| [Add workflow node convention (#188)](https://github.com/open-telemetry/semantic-conventions-genai/pull/188) | RKest | aabmass&nbsp;💬<br>lmolkova&nbsp;🔴<br>trask&nbsp;💬 | ✅ | ❌ | 1d |
| [Add gen_ai.agent.invocation.duration and gen_ai.tool.execution.duration metrics (#201)](https://github.com/open-telemetry/semantic-conventions-genai/pull/201) | pvlsirotkin | lmolkova&nbsp;💬<br>MikeGoldsmith&nbsp;🔴 | ✅ | ❌ | 1d |
| [semconv for a2a protocol (#195)](https://github.com/open-telemetry/semantic-conventions-genai/pull/195) | eternalcuriouslearner | aabmass&nbsp;💬<br>JWinermaSplunk&nbsp;💬<br>pwkowalski&nbsp;💬<br>trask&nbsp;💬 | ✅ | ✅ | 8h |
| [Add `gen_ai.agent.finish_reason` attribute for agent loop termination (#238)](https://github.com/open-telemetry/semantic-conventions-genai/pull/238) | Nik-Reddy | aabmass&nbsp;✅<br>AgentGymLeader&nbsp;💬<br>Copilot&nbsp;💬<br>MikeGoldsmith&nbsp;✅<br>trask&nbsp;💬 | ✅ | ✅ | 6h |
| [gen-ai: add run guardrail span and security finding (#262)](https://github.com/open-telemetry/semantic-conventions-genai/pull/262) | nagkumar91 | aabmass<br>Copilot&nbsp;💬 | ✅ | ✅ | 3h |
| [Support entity rendering in Weaver v2 (#273)](https://github.com/open-telemetry/semantic-conventions-genai/pull/273) | aabmass | lmolkova&nbsp;💬 | ✅ | ✅ | 1h |
| [\[chore\] Small improvements to markdown templates (#274)](https://github.com/open-telemetry/semantic-conventions-genai/pull/274) | lmolkova | Copilot&nbsp;💬 | ✅ | ✅ | 21m |

## Waiting on external

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) | app/renovate | DylanRussell&nbsp;💬<br>lmolkova&nbsp;✅ | ❌ | ✅ | 21d |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 18d |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | 11d |
| [Add time_budget value for gen_ai.agent.finish_reason (#267)](https://github.com/open-telemetry/semantic-conventions-genai/pull/267) | Nik-Reddy | 17h |
| [Propose GenAI agent entity (#270)](https://github.com/open-telemetry/semantic-conventions-genai/pull/270) | aabmass | 31m |

<details>
<summary>Diagnostics</summary>

```text
```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

