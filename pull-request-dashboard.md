> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.

## Waiting on approvers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-adk to v2 (#173)](https://github.com/open-telemetry/semantic-conventions-genai/pull/173) | app/renovate |  | ❌ | ✅ | 14h |
| [Disable PR preview for webhook (#176)](https://github.com/open-telemetry/semantic-conventions-genai/pull/176) | trask |  | ✅ | ✅ | 10h |
| [Refresh PR dashboard on check suite updates (#177)](https://github.com/open-telemetry/semantic-conventions-genai/pull/177) | trask |  | ✅ | ✅ | 9h |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) | eternalcuriouslearner |  | ✅ | ✅ | 6h |

## Waiting on authors

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid |  | ✅ | ❌ | 8d |
| [gen-ai: make multimodal content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid |  | ✅ | ❌ | 8d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede |  | ✅ | ❌ | 1d |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | trask | ✅ | ❌ | 21h |
| [chore: add moonshot_ai, minimax, z_ai to well-known values (#99)](https://github.com/open-telemetry/semantic-conventions-genai/pull/99) | ariesdevil |  | ✅ | ✅ | 15h |
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova | ✅ | ❌ | 12h |

## Waiting on external

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) ✅ | app/renovate |  | ❌ | ✅ | 15h |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 2d |

<details>
<summary>Diagnostics</summary>

```text
PR #164
llm: PRRT_kwDOSUeMrM6C-3Kb -> author (The reviewer asked for justification and raised an alternative approach, so the PR author needs to პასუხ/respond and possibly revise the metric change.)

PR #144
llm: PRRT_kwDOSUeMrM6BMiXX -> author (Reviewer flagged a mismatch between the comment and the Pydantic model and asked for either a validator or a clarification, so the author needs to respond or make a change.)

PR #143
llm: PRRT_kwDOSUeMrM6BMbLE -> author (Reviewer asked the PR author to add or update a reference scenario for the new `byte_size` convention change, so the ball is with the author.)

PR #112
llm: pr-conversation -> external (The blocker is an upstream google-adk/google-genai version constraint and the needed fix depends on a future external release, not on repo discussion.)

PR #99
llm: pr-conversation -> author (A reviewer asked whether any instrumentation uses these values, so the author needs to जवाब/confirm.)

PR #98
llm: PRRT_kwDOSUeMrM6DQ5Sd -> author (A reviewer pointed out a changelog link issue and requested a fix; the author needs to update the entry or respond.)
llm: PRRT_kwDOSUeMrM6DQ5Tg -> author (A reviewer asked to inline the attribute emissions at the instrumentation sites instead of using the helper, so the PR author needs to change the code and respond.)
llm: PRRT_kwDOSUeMrM6DQ5T0 -> author (The reviewer raised a concrete change request and there’s no author reply yet, so the PR author needs to update the scenario.)
llm: PRRT_kwDOSUeMrM6DQ5UG -> author (A reviewer pointed out a timing bug and requested a change; the author needs to respond or update the span handling.)

PR #96
llm: PRRT_kwDOSUeMrM6Ck7X- -> author (The latest comment is from a reviewer suggesting the SIG decision implies modality should be considered here, so the author needs to respond or act on that suggestion.)
llm: PRRT_kwDOSUeMrM6DToum -> author (A reviewer raised a concrete issue and asked for a change; the author needs to update the mapping table or respond.)
llm: PRRT_kwDOSUeMrM6DT__X -> author (The reviewer提出 a substantive redesign suggestion and asks the author to reconsider token usage modeling, so the author needs to respond or adjust the proposal.)

```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

