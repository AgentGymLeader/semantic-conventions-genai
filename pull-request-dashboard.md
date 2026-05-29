> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.

## Waiting on maintainers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Clarify that billed token counts should be reported for Cohere usage (#211)](https://github.com/open-telemetry/semantic-conventions-genai/pull/211) ✅ | trask |  | ✅ | ✅ | 18h |
| [Generalize the `gen_ai.provider.name` description (#212)](https://github.com/open-telemetry/semantic-conventions-genai/pull/212) ✅ | trask |  | ✅ | ✅ | 14h |
| [Relax `gen_ai.provider.name` on `gen_ai.client.operation.duration` to Conditionally Required (#214)](https://github.com/open-telemetry/semantic-conventions-genai/pull/214) ✅ | trask |  | ✅ | ✅ | 13h |
| [Clarify GenAI span duration (#216)](https://github.com/open-telemetry/semantic-conventions-genai/pull/216) ✅ | trask |  | ✅ | ✅ | 12h |

## Waiting on approvers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: add gen_ai.response.id to deepeval evaluation result event (#184)](https://github.com/open-telemetry/semantic-conventions-genai/pull/184) | hippoley |  | ✅ | ✅ | 3d |
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova | ✅ | ✅ | 1d |
| [Add modality, cache, and phase breakdowns for token usage (#197)](https://github.com/open-telemetry/semantic-conventions-genai/pull/197) | trask |  | ✅ | ✅ | 16h |
| [Clarify GenAI conversation ID fallbacks (#219)](https://github.com/open-telemetry/semantic-conventions-genai/pull/219) | trask |  | ✅ | ✅ | 54m |

## Waiting on authors

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid |  | ✅ | ❌ | 17d |
| [gen-ai: make multimodal content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid |  | ✅ | ❌ | 17d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede |  | ✅ | ❌ | 10d |
| [gen-ai: add evaluation operation name and gen_ai.evaluate.internal span (#185)](https://github.com/open-telemetry/semantic-conventions-genai/pull/185) | hippoley |  | ❌ | ✅ | 8d |
| [Add experimental GenAI context selection event (#190)](https://github.com/open-telemetry/semantic-conventions-genai/pull/190) | caioribeiroclw-pixel |  | ❌ | ✅ | 6d |
| [Add prompt versioning and variable support to GenAI attributes (#179)](https://github.com/open-telemetry/semantic-conventions-genai/pull/179) | steverao | lmolkova | ✅ | ✅ | 6d |
| [semconv for a2a protocol (#195)](https://github.com/open-telemetry/semantic-conventions-genai/pull/195) | eternalcuriouslearner |  | ✅ | ✅ | 2d |
| [Add workflow node convention (#188)](https://github.com/open-telemetry/semantic-conventions-genai/pull/188) | RKest |  | ✅ | ❌ | 2d |
| [Update dependency google-adk to v2 (#173)](https://github.com/open-telemetry/semantic-conventions-genai/pull/173) | app/renovate |  | ❌ | ✅ | 2d |
| [Add gen_ai.agent.request.size and gen_ai.agent.response.size metrics (#202)](https://github.com/open-telemetry/semantic-conventions-genai/pull/202) | pvlsirotkin |  | ✅ | ✅ | 2d |
| [Add gen_ai.workflow.steps metric (#203)](https://github.com/open-telemetry/semantic-conventions-genai/pull/203) | pvlsirotkin |  | ✅ | ✅ | 2d |
| [Add gen_ai.agent.invocation.duration and gen_ai.tool.execution.duration metrics (#201)](https://github.com/open-telemetry/semantic-conventions-genai/pull/201) | pvlsirotkin |  | ✅ | ✅ | 1d |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) | eternalcuriouslearner | lmolkova, JWinermaSplunk | ✅ | ✅ | 1d |
| [Clarify scope of `gen_ai.client.operation.duration` metric (#215)](https://github.com/open-telemetry/semantic-conventions-genai/pull/215) | trask |  | ✅ | ✅ | 11h |

## Waiting on external

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) ✅ | app/renovate |  | ❌ | ✅ | 10d |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 6d |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | 1h |
| [Change gen_ai.request.top_k from double to int (#218)](https://github.com/open-telemetry/semantic-conventions-genai/pull/218) | trask | 50m |
| [Change gen_ai.request.top_k type to int and split out retrieval top_k (#217)](https://github.com/open-telemetry/semantic-conventions-genai/pull/217) | trask | 2m |

<details>
<summary>Diagnostics</summary>

```text
PR #215
llm: PRRT_kwDOSUeMrM6Fl7mu -> author (The latest comment is from a reviewer/approver and asks open design questions about metric naming and grouping, so the PR author needs to respond or propose a direction.)

PR #203
llm: PRRT_kwDOSUeMrM6FJXxu -> author (The reviewer requested a wording standardization in the metric, so the author needs to update the file and respond.)

PR #202
llm: PRRT_kwDOSUeMrM6FJWXQ -> author (Reviewer flagged a schema inconsistency and explicitly asked to add missing `id` fields or regenerate the snapshot, so the author needs to act.)
llm: PRRT_kwDOSUeMrM6FJWYO -> author (The reviewer pointed out a missing `id` field and requested a fix or regeneration of the snapshot, so the PR author needs to act.)
llm: PRRT_kwDOSUeMrM6FJWY9 -> author (Reviewer requested a wording consistency change in `model/gen-ai/metrics.yaml`; the author needs to update the text or respond.)
llm: PRRT_kwDOSUeMrM6FJWZf -> author (Reviewer asked to standardize the user-facing phrasing in `model/gen-ai/metrics.yaml`; the author needs to update the text or जवाब back.)

PR #201
llm: PRRT_kwDOSUeMrM6FYxtF -> author (The latest comment is a reviewer question/suggestion asking for an explanation to be added, so the PR author needs to respond or update the docs.)
llm: PRRT_kwDOSUeMrM6FY1gg -> author (A reviewer asked whether `gen_ai.agent.name` should be required and raised a substantive concern; the author needs to respond or adjust the metric definition.)
llm: PRRT_kwDOSUeMrM6FY3VY -> author (Reviewer asked to add a reference scenario in this PR; the author needs to respond by implementing it or addressing the request.)
llm: PRRT_kwDOSUeMrM6FY5Vy -> author (The latest comment is from a reviewer asking whether `gen_ai.tool.type` should also be added, so the author needs to जवाब/implement or push back.)

PR #197
llm: PRRT_kwDOSUeMrM6E-Ear -> reviewer (The author responded with a preferred option and linked a commit; the ball is back with the reviewer to acknowledge or review the added change.)
llm: PRRT_kwDOSUeMrM6FkB2H -> reviewer (The author asked for clarification and details on the reviewer’s claim, so the reviewer needs to जवाब/clarify next.)

PR #195
llm: PRRT_kwDOSUeMrM6E9S_1 -> author (A reviewer pointed out hardcoded `MOCK_A2A_URL` and requested deriving it from `MOCK_LLM_URL`; the author needs to update the scenario or respond.)
llm: PRRT_kwDOSUeMrM6E9TAi -> author (A reviewer asked to inline A2A span attributes at each instrumentation site, so the PR author needs to update the scenario or respond.)
llm: PRRT_kwDOSUeMrM6E9TA7 -> author (A reviewer asked for a code change and no author reply has been given, so the next action is on the PR author.)
llm: PRRT_kwDOSUeMrM6E9TBK -> author (Reviewer says the span should wrap the real A2A SDK call and suggests specific code changes, so the PR author needs to update the scenario.)
llm: PRRT_kwDOSUeMrM6E9TBd -> author (Reviewer asked to remove `gen_ai.request.stream = False` for non-streaming calls and only set it when streaming is enabled; the author needs to update the code.)
llm: PRRT_kwDOSUeMrM6E9TBt -> author (A reviewer pointed out that the scenario is using a locally constructed events list instead of a real streaming SDK call, so the PR author needs to revise the implementation.)

PR #190
llm: PRRT_kwDOSUeMrM6EO3GU -> author (The reviewer flagged an inconsistency in `schema-snapshot/registry.yaml` and suggested regenerating or fixing the snapshot, so the author needs to update it and respond.)
llm: PRRT_kwDOSUeMrM6EO3Gw -> author (A reviewer raised a specific wording inconsistency in the changelog and asked to align it, so the author needs to respond or update the file.)

PR #188
llm: PRRT_kwDOSUeMrM6EG_rG -> reviewer (The author जवाबed with a refusal and rationale, so the ball is back with the reviewer/maintainer to accept the explanation or respond further.)
llm: PRRT_kwDOSUeMrM6EP5P6 -> reviewer (The reviewer asked where the data would come from in real instrumentation, and the author replied with a concrete ADK example and trace, so the ball is back with the reviewer to confirm or continue the review.)
llm: PRRT_kwDOSUeMrM6EP9-D -> reviewer (The author replied with added scenarios and terminology findings, so the ball is back with the reviewer to review that update or respond.)
llm: pr-conversation -> author (The author replied that this PR only partly resolves the issue and says they will handle the follow-up later, so the thread is still with the author.)

PR #185
llm: PRRT_kwDOSUeMrM6DuuPn -> author (Reviewer raised a naming inconsistency and suggested a spec alignment change; the author needs to respond or make the update.)
llm: PRRT_kwDOSUeMrM6E_Amb -> author (A reviewer requested a concrete fix (“we need a verb here”), so the PR author needs to update the line and respond.)
llm: PRRT_kwDOSUeMrM6E_COY -> author (A reviewer asked which instrumentation should generate the span and requested a prototype, so the author needs to respond or provide the example.)
llm: pr-conversation -> author (The reviewer added a clarification/suggestion about linking evaluation results via traceId/spanId, so the author needs to respond or adjust the implementation.)

PR #179
llm: PRRT_kwDOSUeMrM6EP0dp -> author (The reviewer asked to add reference instrumentation scenarios, so the PR author needs to act on that request.)
llm: PRRT_kwDOSUeMrM6EP1ZF -> author (A reviewer raised a specific missing-field concern, so the author needs to respond or update the change.)
llm: PRRT_kwDOSUeMrM6EP2En -> author (Reviewer requested a documentation clarification about MCP prompt arguments mapping to variables, so the author needs to update or जवाब.)
llm: pr-conversation -> author (A reviewer asked the PR author to update the title with Resolves #137 and complete the PR template, so the next action is on the author.)

PR #173
llm: pr-conversation -> author (A reviewer reported a CI snapshot mismatch and explicitly asked to investigate whether ADK 2.x renamed or dropped the tool-call span before the PR can land.)

PR #164
llm: PRRT_kwDOSUeMrM6C-3Kb -> author (The reviewer asked for justification and raised an alternative approach, so the PR author needs to პასუხ/respond and possibly revise the metric change.)
llm: pr-conversation -> author (The latest comment is from the reviewer/approver, asking the author to align the metric description with OTel's intent, so the author needs to respond or update the PR.)

PR #162
llm: PRRT_kwDOSUeMrM6Fd-ZR -> author (The reviewer flagged a mismatch and requested either a code/docs fix or a description/changelog update, so the PR author needs to act next.)
llm: PRRT_kwDOSUeMrM6E_DcG -> author (A reviewer left a substantive note with supporting links about Anthropic supporting both formats; this passes the thread to the author to respond or adjust the code.)
llm: PRRT_kwDOSUeMrM6E_T2Z -> author (The approver/reviewer asked a substantive design question and raised a proposed modeling change, so the author needs to respond or adjust the implementation.)

PR #144
llm: PRRT_kwDOSUeMrM6BMiXX -> author (Reviewer flagged a mismatch between the comment and the Pydantic model and asked for either a validator or a clarification, so the author needs to respond or make a change.)

PR #143
llm: PRRT_kwDOSUeMrM6BMbLE -> author (Reviewer asked the PR author to add or update a reference scenario for the new `byte_size` convention change, so the ball is with the author.)

PR #112
llm: pr-conversation -> external (The blocker is an upstream google-adk/google-genai version constraint and the needed fix depends on a future external release, not on repo discussion.)

PR #98
llm: PRRT_kwDOSUeMrM6E9NFw -> reviewer (The author answered the reviewer’s question and raised a remaining gap, so the ball is back with the reviewer to respond or confirm the direction.)

```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

