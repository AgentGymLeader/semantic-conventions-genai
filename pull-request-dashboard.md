> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.

## Waiting on maintainers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Add GenAI memory operation conventions (#140)](https://github.com/open-telemetry/semantic-conventions-genai/pull/140) ✅ | nagkumar91 | trask | ⏳ | ✅ | 1h |

## Waiting on approvers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova | ✅ | ✅ | 14h |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) | eternalcuriouslearner |  | ✅ | ✅ | 12h |
| [Update reference implementation dependencies (non-major) (#172)](https://github.com/open-telemetry/semantic-conventions-genai/pull/172) | app/renovate |  | ✅ | ✅ | 7h |

## Waiting on authors

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid |  | ✅ | ❌ | 7d |
| [gen-ai: make multimodal content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid |  | ✅ | ❌ | 7d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede |  | ✅ | ❌ | 18h |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | trask | ✅ | ✅ | 6h |
| [chore: add moonshot_ai, minimax, z_ai to well-known values (#99)](https://github.com/open-telemetry/semantic-conventions-genai/pull/99) | ariesdevil |  | ✅ | ✅ | 23m |

## Waiting on external

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) ✅ | app/renovate |  | ❌ | ✅ | 20m |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 1d |

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

PR #96
llm: PRRT_kwDOSUeMrM6Ck7X- -> author (The latest comment is from a reviewer asking that modality be considered, so the ball is back with the PR author to respond or adjust the PR.)

```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

