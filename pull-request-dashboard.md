> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.

## Waiting on approvers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova | ? | ✅ | 2d |

## Waiting on authors

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid |  | ? | ❌ | 11d |
| [gen-ai: make multimodal content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid |  | ✅ | ❌ | 11d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede |  | ✅ | ❌ | 4d |
| [gen-ai: add evaluation operation name and gen_ai.evaluate.internal span (#185)](https://github.com/open-telemetry/semantic-conventions-genai/pull/185) | hippoley |  | ❌ | ✅ | 2d |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | trask | ✅ | ❌ | 2d |
| [Add experimental GenAI context selection event (#190)](https://github.com/open-telemetry/semantic-conventions-genai/pull/190) | caioribeiroclw-pixel |  | ❌ | ✅ | 20h |
| [Add workflow node convention (#188)](https://github.com/open-telemetry/semantic-conventions-genai/pull/188) | RKest |  | ? | ✅ | 17h |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) | eternalcuriouslearner |  | ❌ | ✅ | 13h |
| [chore: add moonshot_ai to well-known values (#99)](https://github.com/open-telemetry/semantic-conventions-genai/pull/99) | ariesdevil |  | ✅ | ✅ | 1h |

## Waiting on external

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) ✅ | app/renovate |  | ❌ | ✅ | 4d |

## Unknown

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: sync reference data.json files with scenario implementations (#186)](https://github.com/open-telemetry/semantic-conventions-genai/pull/186) | hippoley |  | ? | ? | ? |
| [gen-ai: add gen_ai.response.id to deepeval evaluation result event (#184)](https://github.com/open-telemetry/semantic-conventions-genai/pull/184) | hippoley |  | ? | ? | ? |
| [Add prompt versioning and variable support to GenAI attributes (#179)](https://github.com/open-telemetry/semantic-conventions-genai/pull/179) | steverao |  | ? | ? | ? |
| [Update dependency google-adk to v2 (#173)](https://github.com/open-telemetry/semantic-conventions-genai/pull/173) | app/renovate |  | ? | ? | ? |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 22h |

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
error: RuntimeError('gh api -H Accept: application/vnd.github+json --paginate --slurp /repos/open-telemetry/semantic-conventions-genai/issues/186/comments?per_page=100 failed: gh: Bad credentials (HTTP 401)')

PR #185
llm: PRRT_kwDOSUeMrM6DuuPn -> author (Reviewer raised a naming inconsistency and suggested a spec alignment change; the author needs to respond or make the update.)

PR #184
error: RuntimeError('gh api graphql -f query=\nquery($owner: String!, $name: String!, $number: Int!, $after: String) {\n    repository(owner: $owner, name: $name) {\n        pullRequest(number: $number) {\n            reviewThreads(first: 100, after: $after) {\n                pageInfo {\n                    hasNextPage\n                    endCursor\n                }\n                nodes {\n                    id\n                    isResolved\n                    isOutdated\n                    path\n                    line\n                    comments(first: 100) {\n                        pageInfo {\n                            hasNextPage\n                            endCursor\n                        }\n                        nodes {\n                            id\n                            body\n                            createdAt\n                            updatedAt\n                            author {\n                                login\n                            }\n                        }\n                    }\n                }\n            }\n        }\n    }\n}\n -F owner=open-telemetry -F name=semantic-conventions-genai -F number=184 failed: gh: Bad credentials (HTTP 401)')

PR #179
error: RuntimeError('gh api graphql -f query=\nquery($owner: String!, $name: String!, $number: Int!, $after: String) {\n    repository(owner: $owner, name: $name) {\n        pullRequest(number: $number) {\n            reviewThreads(first: 100, after: $after) {\n                pageInfo {\n                    hasNextPage\n                    endCursor\n                }\n                nodes {\n                    id\n                    isResolved\n                    isOutdated\n                    path\n                    line\n                    comments(first: 100) {\n                        pageInfo {\n                            hasNextPage\n                            endCursor\n                        }\n                        nodes {\n                            id\n                            body\n                            createdAt\n                            updatedAt\n                            author {\n                                login\n                            }\n                        }\n                    }\n                }\n            }\n        }\n    }\n}\n -F owner=open-telemetry -F name=semantic-conventions-genai -F number=179 failed: gh: Bad credentials (HTTP 401)')

PR #173
error: RuntimeError('gh api -H Accept: application/vnd.github+json --paginate --slurp /repos/open-telemetry/semantic-conventions-genai/pulls/173/reviews?per_page=100 failed: gh: Bad credentials (HTTP 401)')

PR #164
llm: PRRT_kwDOSUeMrM6C-3Kb -> author (The reviewer asked for justification and raised an alternative approach, so the PR author needs to პასუხ/respond and possibly revise the metric change.)
llm: pr-conversation -> author (The latest comment is from the reviewer/approver, asking the author to align the metric description with OTel's intent, so the author needs to respond or update the PR.)

PR #162
llm: PRRT_kwDOSUeMrM6ERPLE -> author (A reviewer asked whether the comment is outdated and whether the instrumentation already covers it; the author needs to respond or update the scenario.)
llm: PRRT_kwDOSUeMrM6ERPfp -> author (Reviewer asked whether the scenario is essentially hardcoded, so the author needs to जवाब/clarify or adjust the code.)

PR #144
llm: PRRT_kwDOSUeMrM6BMiXX -> author (Reviewer flagged a mismatch between the comment and the Pydantic model and asked for either a validator or a clarification, so the author needs to respond or make a change.)

PR #143
llm: PRRT_kwDOSUeMrM6BMbLE -> author (Reviewer asked the PR author to add or update a reference scenario for the new `byte_size` convention change, so the ball is with the author.)

PR #112
llm: pr-conversation -> external (The blocker is an upstream google-adk/google-genai version constraint and the needed fix depends on a future external release, not on repo discussion.)

PR #99
llm: PRRT_kwDOSUeMrM6EUYb4 -> author (Reviewer requested the author either add the missing reference scenario/data or adjust the PR checklist to match; a response or code change is needed from the PR author.)
llm: PRRT_kwDOSUeMrM6EUYbs -> author (The latest reviewer comment asks the PR author to update the PR description to cover the Copilot comments, so the author has the next action.)

PR #96
llm: PRRT_kwDOSUeMrM6Ck7X- -> author (The latest comment is from the author and says they are still holding the modality patch until the design shape settles, so the author still has the next action.)

```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

