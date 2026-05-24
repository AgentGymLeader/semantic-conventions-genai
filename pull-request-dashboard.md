> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.

## Waiting on maintainers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Add Copilot review guidance to dashboard (#193)](https://github.com/open-telemetry/semantic-conventions-genai/pull/193) ✅ | trask |  | ✅ | ✅ | 21h |

## Waiting on approvers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-adk to v2 (#173)](https://github.com/open-telemetry/semantic-conventions-genai/pull/173) | app/renovate |  | ❌ | ✅ | 4d |
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova | ✅ | ✅ | 3d |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) | eternalcuriouslearner |  | ❌ | ✅ | 1d |
| [chore: add moonshot_ai to well-known values (#99)](https://github.com/open-telemetry/semantic-conventions-genai/pull/99) | ariesdevil |  | ✅ | ✅ | 5h |

## Waiting on authors

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid |  | ✅ | ❌ | 12d |
| [gen-ai: make multimodal content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid |  | ✅ | ❌ | 12d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede |  | ✅ | ❌ | 5d |
| [gen-ai: add gen_ai.response.id to deepeval evaluation result event (#184)](https://github.com/open-telemetry/semantic-conventions-genai/pull/184) ✅ | hippoley |  | ✅ | ✅ | 3d |
| [gen-ai: add evaluation operation name and gen_ai.evaluate.internal span (#185)](https://github.com/open-telemetry/semantic-conventions-genai/pull/185) | hippoley |  | ❌ | ✅ | 3d |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | trask | ✅ | ❌ | 3d |
| [Add experimental GenAI context selection event (#190)](https://github.com/open-telemetry/semantic-conventions-genai/pull/190) | caioribeiroclw-pixel |  | ❌ | ✅ | 1d |
| [Add prompt versioning and variable support to GenAI attributes (#179)](https://github.com/open-telemetry/semantic-conventions-genai/pull/179) | steverao |  | ✅ | ✅ | 1d |
| [Add workflow node convention (#188)](https://github.com/open-telemetry/semantic-conventions-genai/pull/188) | RKest |  | ✅ | ✅ | 1d |
| [gen-ai: sync reference data.json files with scenario implementations (#186)](https://github.com/open-telemetry/semantic-conventions-genai/pull/186) ✅ | hippoley |  | ✅ | ✅ | 1d |

## Waiting on external

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) ✅ | app/renovate |  | ❌ | ✅ | 5d |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 1d |

<details>
<summary>Diagnostics</summary>

```text
PR #190
llm: PRRT_kwDOSUeMrM6EO3GU -> author (A reviewer pointed out a snapshot inconsistency and suggested regenerating/fixing the output, so the PR author needs to respond or update the file.)
llm: PRRT_kwDOSUeMrM6EO3Gs -> author (Reviewer raised an open design concern and asked for clarification or a schema change; the author needs to respond or update the registry note.)
llm: PRRT_kwDOSUeMrM6EO3Gw -> author (A reviewer raised a specific wording inconsistency in the changelog and asked to align it, so the author needs to respond or update the file.)

PR #188
llm: PRRT_kwDOSUeMrM6EG_qb -> reviewer (The author addressed the review request by adding the requested `gen_ai.operation.name` wording and reported it as pushed, so the reviewer/maintainer has the next action to confirm or continue review.)
llm: PRRT_kwDOSUeMrM6EG_rG -> reviewer (The author replied with a rationale for not making the requested change, so the ball is back with the reviewer to accept the explanation or continue the discussion.)
llm: PRRT_kwDOSUeMrM6EP5P6 -> author (The latest comment is a reviewer question asking for clarification, so the PR author needs to जवाब/clarify where it would come from in real instrumentation.)
llm: PRRT_kwDOSUeMrM6EP8-Y -> author (The reviewer is asking the author to refine the definition of "node" and clarify when node spans should be captured, so the author needs to respond or update the spec.)
llm: PRRT_kwDOSUeMrM6EP9ao -> author (Reviewer asked for an added caveat to the spec, so the PR author needs to update or जवाब/respond.)
llm: PRRT_kwDOSUeMrM6EP9-D -> author (Reviewer asked the author to investigate affected instrumentations and update their scenarios, so the ball is with the author.)
llm: PRRT_kwDOSUeMrM6EP-c0 -> author (The reviewer asked to postpone adding the span event, which leaves the author needing to acknowledge and adjust the change.)
llm: PRRT_kwDOSUeMrM6EP_G4 -> author (A reviewer asked whether the placement under `gen_ai.retrieval.documents` was intentional and raised a possible schema update, so the author needs to जवाब/respond or make the change.)
llm: PRRT_kwDOSUeMrM6EP_N6 -> author (A reviewer said the item seems misplaced and pointed to another comment, so the author needs to respond or make the requested change.)
llm: PRRT_kwDOSUeMrM6EP_6S -> author (A reviewer objected to changing the attribute meaning, so the PR author needs to respond or adjust the change.)

PR #186
llm: PRRT_kwDOSUeMrM6EQAnF -> author (A reviewer asked to remove the comment, so the PR author needs to make that change or respond.)

PR #185
llm: PRRT_kwDOSUeMrM6DuuPn -> author (Reviewer raised a naming inconsistency and suggested a spec alignment change; the author needs to respond or make the update.)

PR #184
llm: PRRT_kwDOSUeMrM6Dun6Z -> author (A reviewer flagged formatting in the scenario comments and requested a change; the author needs to update the file or respond.)
llm: PRRT_kwDOSUeMrM6EK_PC -> author (A reviewer asked whether the comment is necessary, so the author needs to जवाब/adjust the code or explain the duplication.)
llm: PRRT_kwDOSUeMrM6ELPCJ -> author (Reviewer flagged a likely hardcoded value and asked the author to check the reference, so the author needs to respond or update the code.)

PR #179
llm: PRRT_kwDOSUeMrM6EP0dp -> author (The reviewer asked to add reference instrumentation scenarios, so the PR author needs to act on that request.)
llm: PRRT_kwDOSUeMrM6EP1ZF -> author (A reviewer raised a specific missing-field concern, so the author needs to respond or update the change.)
llm: PRRT_kwDOSUeMrM6EP2En -> author (Reviewer requested a documentation clarification about MCP prompt arguments mapping to variables, so the author needs to update or जवाब.)

PR #164
llm: PRRT_kwDOSUeMrM6C-3Kb -> author (The reviewer asked for justification and raised an alternative approach, so the PR author needs to პასუხ/respond and possibly revise the metric change.)
llm: pr-conversation -> author (The latest comment is from the reviewer/approver, asking the author to align the metric description with OTel's intent, so the author needs to respond or update the PR.)

PR #144
llm: PRRT_kwDOSUeMrM6BMiXX -> author (Reviewer flagged a mismatch between the comment and the Pydantic model and asked for either a validator or a clarification, so the author needs to respond or make a change.)

PR #143
llm: PRRT_kwDOSUeMrM6BMbLE -> author (Reviewer asked the PR author to add or update a reference scenario for the new `byte_size` convention change, so the ball is with the author.)

PR #112
llm: pr-conversation -> external (The blocker is an upstream google-adk/google-genai version constraint and the needed fix depends on a future external release, not on repo discussion.)

PR #99
llm: PRRT_kwDOSUeMrM6EUYbs -> reviewer (The author says they updated the PR and asked for another look, so the reviewer/maintainer needs to recheck the thread.)

PR #96
llm: PRRT_kwDOSUeMrM6Ck7X- -> author (The latest comment is from the author and says they are still holding the modality patch until the design shape settles, so the author still has the next action.)
llm: pr-conversation -> reviewer (The author is asking for confirmation on the partition shape and modality before reworking the PR, so the next move is for a reviewer/maintainer to answer.)

```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

