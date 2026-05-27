> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.

## Waiting on maintainers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: add gen_ai.response.id to deepeval evaluation result event (#184)](https://github.com/open-telemetry/semantic-conventions-genai/pull/184) ✅ | hippoley |  | ✅ | ✅ | 22h |

## Waiting on approvers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-adk to v2 (#173)](https://github.com/open-telemetry/semantic-conventions-genai/pull/173) | app/renovate |  | ❌ | ✅ | 7d |
| [Remove OTEL_SEMCONV_STABILITY_OPT_IN transition blurb (#198)](https://github.com/open-telemetry/semantic-conventions-genai/pull/198) | trask |  | ✅ | ✅ | 6h |
| [Use GraphQL to find the existing dashboard issue (#199)](https://github.com/open-telemetry/semantic-conventions-genai/pull/199) | trask |  | ✅ | ✅ | 5h |

## Waiting on authors

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid |  | ✅ | ❌ | 15d |
| [gen-ai: make multimodal content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid |  | ✅ | ❌ | 15d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede |  | ✅ | ❌ | 8d |
| [gen-ai: add evaluation operation name and gen_ai.evaluate.internal span (#185)](https://github.com/open-telemetry/semantic-conventions-genai/pull/185) | hippoley |  | ❌ | ✅ | 5d |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | trask | ✅ | ❌ | 5d |
| [Add experimental GenAI context selection event (#190)](https://github.com/open-telemetry/semantic-conventions-genai/pull/190) | caioribeiroclw-pixel |  | ❌ | ✅ | 4d |
| [Add prompt versioning and variable support to GenAI attributes (#179)](https://github.com/open-telemetry/semantic-conventions-genai/pull/179) | steverao |  | ✅ | ✅ | 4d |
| [Add workflow node convention (#188)](https://github.com/open-telemetry/semantic-conventions-genai/pull/188) | RKest |  | ✅ | ✅ | 21h |
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova | ✅ | ✅ | 1h |
| [semconv for a2a protocol (#195)](https://github.com/open-telemetry/semantic-conventions-genai/pull/195) | eternalcuriouslearner |  | ✅ | ✅ | 53m |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) | eternalcuriouslearner |  | ✅ | ✅ | <1m |

## Waiting on external

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) ✅ | app/renovate |  | ❌ | ✅ | 7d |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 4d |
| [Add modality, cache, and phase breakdowns for token usage (#197)](https://github.com/open-telemetry/semantic-conventions-genai/pull/197) | trask | 1m |

<details>
<summary>Diagnostics</summary>

```text
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
llm: PRRT_kwDOSUeMrM6EG_rG -> reviewer (The author replied with a rationale for not making the requested change, so the ball is back with the reviewer to accept the explanation or continue the discussion.)
llm: PRRT_kwDOSUeMrM6EP5P6 -> reviewer (The reviewer asked a question, and the author replied with a concrete source/example, so the ball is back with the reviewer to confirm or continue the review.)
llm: PRRT_kwDOSUeMrM6EP9-D -> reviewer (The author responded with the requested investigation and said they added scenarios; the reviewer now needs to check whether that satisfies the request.)
llm: pr-conversation -> author (A reviewer left substantive feedback and open questions, so the author needs to respond or make changes.)

PR #185
llm: PRRT_kwDOSUeMrM6DuuPn -> author (Reviewer raised a naming inconsistency and suggested a spec alignment change; the author needs to respond or make the update.)

PR #184
llm: pr-conversation -> none (The reviewer’s last comment is a brief acknowledgement (“thanks”) with no follow-up requested, so the thread appears closed.)

PR #179
llm: PRRT_kwDOSUeMrM6EP0dp -> author (The reviewer asked to add reference instrumentation scenarios, so the PR author needs to act on that request.)
llm: PRRT_kwDOSUeMrM6EP1ZF -> author (A reviewer raised a specific missing-field concern, so the author needs to respond or update the change.)
llm: PRRT_kwDOSUeMrM6EP2En -> author (Reviewer requested a documentation clarification about MCP prompt arguments mapping to variables, so the author needs to update or जवाब.)

PR #164
llm: PRRT_kwDOSUeMrM6C-3Kb -> author (The reviewer asked for justification and raised an alternative approach, so the PR author needs to პასუხ/respond and possibly revise the metric change.)
llm: pr-conversation -> author (The latest comment is from the reviewer/approver, asking the author to align the metric description with OTel's intent, so the author needs to respond or update the PR.)

PR #162
llm: pr-conversation -> author (The latest approver comment asks the PR author to mark the thread as resolving the linked issue, so the next action is on the author.)

PR #144
llm: PRRT_kwDOSUeMrM6BMiXX -> author (Reviewer flagged a mismatch between the comment and the Pydantic model and asked for either a validator or a clarification, so the author needs to respond or make a change.)

PR #143
llm: PRRT_kwDOSUeMrM6BMbLE -> author (Reviewer asked the PR author to add or update a reference scenario for the new `byte_size` convention change, so the ball is with the author.)

PR #112
llm: pr-conversation -> external (The blocker is an upstream google-adk/google-genai version constraint and the needed fix depends on a future external release, not on repo discussion.)

PR #98
llm: PRRT_kwDOSUeMrM6E9NFw -> author (A reviewer asked whether the hierarchy should be changed and implied an attribute may no longer be needed, so the author needs to respond or make the requested adjustment.)

PR #96
llm: PRRT_kwDOSUeMrM6Ck7X- -> author (The latest comment is from the author and says they are still holding the modality patch until the design shape settles, so the author still has the next action.)
llm: pr-conversation -> reviewer (The latest comment is from the PR author and asks for a change (“Could you add `Closes #96`…”), so the reviewer/maintainer needs to act next.)

```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

