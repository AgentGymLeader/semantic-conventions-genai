> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.

## Waiting on approvers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova | ✅ | ❌ | 8d |
| [semconv for a2a protocol (#195)](https://github.com/open-telemetry/semantic-conventions-genai/pull/195) | eternalcuriouslearner |  | ✅ | ✅ | 6d |
| [Generalize the `gen_ai.provider.name` description (#212)](https://github.com/open-telemetry/semantic-conventions-genai/pull/212) ✅✅ | trask |  | ✅ | ✅ | 10h |
| [Clarify that billed token counts should be reported for Cohere usage (#211)](https://github.com/open-telemetry/semantic-conventions-genai/pull/211) ✅✅ | trask |  | ✅ | ✅ | 9h |
| [Normalize requirement-level condition notes to capitalized sentences (#245)](https://github.com/open-telemetry/semantic-conventions-genai/pull/245) | trask |  | ✅ | ✅ | 9h |
| [Add gen_ai.agent.invocation.id attribute for invoke_agent spans (#250)](https://github.com/open-telemetry/semantic-conventions-genai/pull/250) | singankit |  | ✅ | ✅ | 3h |

## Waiting on authors

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: make input-messages BlobPart content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid |  | ✅ | ✅ | 24d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede |  | ✅ | ❌ | 17d |
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) ✅ | app/renovate |  | ❌ | ✅ | 16d |
| [gen-ai: add evaluation operation name and gen_ai.evaluate.internal span (#185)](https://github.com/open-telemetry/semantic-conventions-genai/pull/185) | hippoley |  | ❌ | ✅ | 14d |
| [Add experimental GenAI context selection event (#190)](https://github.com/open-telemetry/semantic-conventions-genai/pull/190) | caioribeiroclw-pixel |  | ❌ | ❌ | 13d |
| [Update dependency google-adk to v2 (#173)](https://github.com/open-telemetry/semantic-conventions-genai/pull/173) | app/renovate |  | ❌ | ✅ | 8d |
| [Add prompt versioning and variable support to GenAI attributes (#179)](https://github.com/open-telemetry/semantic-conventions-genai/pull/179) | steverao | lmolkova | ✅ | ❌ | 8d |
| [Add gen_ai.agent.invocation.duration and gen_ai.tool.execution.duration metrics (#201)](https://github.com/open-telemetry/semantic-conventions-genai/pull/201) | pvlsirotkin |  | ✅ | ❌ | 7d |
| [gen-ai: add gen_ai.response.id to deepeval evaluation result event (#184)](https://github.com/open-telemetry/semantic-conventions-genai/pull/184) ✅ | hippoley |  | ✅ | ✅ | 7d |
| [Add workflow node convention (#188)](https://github.com/open-telemetry/semantic-conventions-genai/pull/188) | RKest |  | ✅ | ❌ | 5d |
| [Add modality, cache, and phase breakdowns for token usage (#197)](https://github.com/open-telemetry/semantic-conventions-genai/pull/197) | trask | lmolkova | ✅ | ❌ | 5d |
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid |  | ✅ | ✅ | 3d |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) ✅ | eternalcuriouslearner | lmolkova, JWinermaSplunk | ✅ | ❌ | 3d |
| [Replace Jupiter notebook with models with python file and add CI check that json schemas are up-to-date (#226)](https://github.com/open-telemetry/semantic-conventions-genai/pull/226) ✅✅ | lmolkova |  | ✅ | ✅ | 2d |
| [Limit gen_ai.agent.id to stable / static identifiers (#242)](https://github.com/open-telemetry/semantic-conventions-genai/pull/242) | lmolkova |  | ✅ | ❌ | 20h |
| [Add gen_ai.agent.finish_reason attribute for agent loop termination (#238)](https://github.com/open-telemetry/semantic-conventions-genai/pull/238) | Nik-Reddy |  | ✅ | ❌ | 12h |
| [Add gen_ai.agent.request.size and gen_ai.agent.response.size metrics (#202)](https://github.com/open-telemetry/semantic-conventions-genai/pull/202) | pvlsirotkin |  | ✅ | ✅ | 11h |
| [Add gen_ai.workflow.steps metric (#203)](https://github.com/open-telemetry/semantic-conventions-genai/pull/203) | pvlsirotkin |  | ✅ | ✅ | 10h |
| [Clarify scope of `gen_ai.client.operation.duration` metric (#215)](https://github.com/open-telemetry/semantic-conventions-genai/pull/215) | trask |  | ✅ | ❌ | 3h |
| [Add Reviewers column to PR dashboard (#251)](https://github.com/open-telemetry/semantic-conventions-genai/pull/251) | trask |  | ✅ | ✅ | 18m |
| [Add gen_ai.invoke_agent.server span (SERVER kind) (#252)](https://github.com/open-telemetry/semantic-conventions-genai/pull/252) | singankit |  | ✅ | ✅ | 14m |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 13d |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | 6d |

<details>
<summary>Diagnostics</summary>

```text
PR #252
llm: PRRT_kwDOSUeMrM6HO1Cy -> author (Reviewer requested new reference scenario coverage and regenerated outputs for the new `gen_ai.invoke_agent.server` span, so the PR author needs to make the change.)

PR #251
llm: PRRT_kwDOSUeMrM6HOzFr -> author (A reviewer asked to reformat the long assignment; the author needs to make the code change or respond.)
llm: PRRT_kwDOSUeMrM6HOzGB -> author (A reviewer asked for a formatting change and there’s no author reply yet, so the author needs to update the PR.)
llm: PRRT_kwDOSUeMrM6HOzGK -> author (A reviewer pointed out a maintainability issue and requested an explicit \u2060 escape, so the PR author needs to update the code or respond.)
llm: PRRT_kwDOSUeMrM6HOzGR -> author (A reviewer pointed out an issue and suggested using an explicit `\u2060` escape, so the author needs to address or जवाब to the comment.)
llm: PRRT_kwDOSUeMrM6HOzGd -> author (The reviewer pointed out a renderer/UI mismatch and requested a fix; the author needs to update the PR.)

PR #242
llm: PRRT_kwDOSUeMrM6G8yXJ -> reviewer (The last comment is from the author saying they couldn't find the `id` property, so the reviewer/maintainer needs to clarify or adjust the request.)
llm: PRRT_kwDOSUeMrM6G8ys_ -> reviewer (The latest comment is from the author pushing back on the instrumentation suggestion, so the reviewer/maintainer needs to respond or resolve the thread.)
llm: PRRT_kwDOSUeMrM6G8zAI -> reviewer (The only comment is from the PR author and it reads like an explanation, not a completed resolution or self-deferral, so the reviewer still needs to respond.)
llm: PRRT_kwDOSUeMrM6G9Yjt -> author (The reviewer asked for comment/docstring updates to match the changed plan-span behavior, so the PR author needs to make that follow-up change.)

PR #238
llm: PRRT_kwDOSUeMrM6GrEAT -> reviewer (The author has replied with a rationale and declined the suggested edit, so the ball is back with the reviewer to accept the explanation or continue the discussion.)
llm: PRRT_kwDOSUeMrM6HEq0i -> author (Reviewer flagged the wording as too strict and suggested a change; the author needs to update or respond.)
llm: PRRT_kwDOSUeMrM6HEq4S -> author (A reviewer asked for an additional scenario to cover non-completed finish reasons, so the author needs to update the PR.)
llm: pr-conversation -> author (The latest comment is a reviewer’s review note with suggestions, so the author needs to respond or address them.)

PR #226
llm: PRRT_kwDOSUeMrM6GgW8E -> author (A reviewer raised a suggestion and explicitly left it open for the author to confirm or resolve; the ball is with the author.)
llm: PRRT_kwDOSUeMrM6GgYDR -> author (A reviewer asked for a lockfile to be generated for the script, so the author needs to act or respond.)
llm: PRRT_kwDOSUeMrM6GgbzS -> author (A reviewer asked whether the check could be made generic for the `generate-all` make target, so the author needs to respond or update the PR.)

PR #215
llm: PRRT_kwDOSUeMrM6Fl7mu -> author (The latest reviewer comment only notes that an issue was created; it doesn’t close the discussion or acknowledge a prior author reply, so the ball is still with the author to respond or follow up.)

PR #212
llm: pr-conversation -> reviewer (The author replied with a question asking the reviewer to clarify the proposed pointer, so the ball is back with the reviewer.)

PR #211
llm: PRRT_kwDOSUeMrM6HDyxU -> reviewer (The author asked a follow-up question (“Is this true for Cohere?”), so the ball is back with the reviewer to answer.)

PR #203
llm: PRRT_kwDOSUeMrM6HGQJ7 -> author (Reviewer asked whether an unbounded freeform metric value is appropriate and suggested moving it to spans, so the author needs to respond or adjust the design.)
llm: PRRT_kwDOSUeMrM6HGTO5 -> author (A reviewer asked for stronger wording in the docs, so the PR author needs to update the text or respond.)
llm: PRRT_kwDOSUeMrM6HGVHV -> author (Reviewer asked for an explicit change to add histogram buckets, so the author needs to update the PR or जवाब back.)
llm: PRRT_kwDOSUeMrM6HGVko -> author (A reviewer suggested adding the `attributes.gen_ai.error` reference, so the author needs to update the PR or जवाब back.)
llm: PRRT_kwDOSUeMrM6HGYBs -> author (The reviewer asked for clarification about the meaning of "attributed to" and how tool calls are handled, so the author needs to პასუხ/clarify.)
llm: PRRT_kwDOSUeMrM6HGaQ9 -> author (A reviewer asked a clarification question about the metric definition, so the PR author needs to जवाब/clarify.)

PR #202
llm: PRRT_kwDOSUeMrM6FJWY9 -> reviewer (The author has replied and left the wording as-is, explicitly asking maintainers to weigh in on any style preference, so the next action is on the reviewer/maintainer side.)
llm: PRRT_kwDOSUeMrM6FJWZf -> reviewer (The author replied but did not resolve the concern, effectively handing it back for reviewer/maintainer judgment on whether the phrasing should be standardized.)
llm: PRRT_kwDOSUeMrM6HFBNY -> author (A reviewer pointed out that `gen_ai.agent.invocation.duration` is not a known metric and suggested an alternative, so the PR author needs to respond or revise the docs.)
llm: PRRT_kwDOSUeMrM6HFBTV -> author (A reviewer asked whether to add missing refs, so the author needs to जवाब/respond or update the PR.)
llm: PRRT_kwDOSUeMrM6HFIOO -> author (The latest reviewer comment հարցs whether the condition is needed, so the PR author needs to जवाब/adjust the code.)
llm: PRRT_kwDOSUeMrM6HFKa9 -> author (The latest reviewer comment asks for clarification on byte-length calculation, so the PR author needs to जवाब/respond and update the docs.)

PR #201
llm: PRRT_kwDOSUeMrM6FYxtF -> author (The reviewer raised a documentation gap, and the author replied that they will add the explanatory sentence; the ball is still with the author to make that change.)
llm: PRRT_kwDOSUeMrM6FY1gg -> reviewer (The author replied with a proposed compromise and asked whether `recommended` or `required` is preferred, so the reviewer needs to answer or decide the level.)
llm: PRRT_kwDOSUeMrM6FY5Vy -> reviewer (The author replied that they added the suggested field, so the reviewer now needs to re-check or acknowledge the change.)
llm: PRRT_kwDOSUeMrM6FY3VY -> reviewer (The author asked for clarification on the approach and offered to do the work; the ball is back with the reviewer to confirm whether metric validation should be wired up in this PR.)
llm: pr-conversation -> author (Reviewer left CHANGES_REQUESTED with specific fixes needed and no follow-up from the author yet.)

PR #197
llm: PRRT_kwDOSUeMrM6E-Ear -> reviewer (The author responded to the reviewer’s question and proposed a concrete metric name, so the ball is back with the reviewer to accept or object.)
llm: PRRT_kwDOSUeMrM6FkB2H -> author (The latest comment is from the reviewer and answers the author’s question with specifics, so the ball is back with the author to decide whether to add `gen_ai.token.modality` or leave the omission intentional.)
llm: PRRT_kwDOSUeMrM6F1og7 -> none (The last reviewer comment defers the follow-up to later and does not ask for any immediate action, so the thread is effectively closed for now.)
llm: PRRT_kwDOSUeMrM6F1nUT -> author (A reviewer/approver asked whether to define phases as `unknown` etc., and the thread is unresolved, so the PR author needs to respond or update the proposal.)
llm: pr-conversation -> external (The thread is deferred to an ad-hoc call tomorrow, so resolution depends on an external meeting rather than a repo-side reply or change.)

PR #190
llm: PRRT_kwDOSUeMrM6EO3Gw -> author (The reviewer asked to align the changelog wording with the registry’s `development` stability, so the author needs to respond and likely update the PR.)
llm: pr-conversation -> author (A reviewer asked the PR author to fill out the template and sign the CLA, so the author needs to act next.)

PR #188
llm: PRRT_kwDOSUeMrM6EP5P6 -> reviewer (The reviewer asked where the behavior would come from; the author replied with concrete implementation and example evidence, so the ball is back with the reviewer to assess or respond.)
llm: PRRT_kwDOSUeMrM6EP9-D -> reviewer (The author replied with the requested investigation and scenario updates, so the ball is back with the reviewer to review or respond.)
llm: PRRT_kwDOSUeMrM6F5pCw -> author (A reviewer asked a question and passed the ball to the PR author to confirm or respond.)

PR #185
llm: PRRT_kwDOSUeMrM6DuuPn -> author (The reviewer raised a substantive naming inconsistency and asked for alignment, so the PR author needs to respond or make a change.)
llm: PRRT_kwDOSUeMrM6E_Amb -> author (A reviewer requested a concrete change (“we need a verb here”), so the PR author needs to update the line and reply.)
llm: PRRT_kwDOSUeMrM6E_COY -> author (The reviewer asked for clarification and a prototype, and there is no author reply yet, so the author needs to respond.)
llm: PRRT_kwDOSUeMrM6HOBHP -> author (The reviewer raised a substantive concern that the attribute does not seem relevant, so the PR author needs to जवाब/adjust the change.)
llm: PRRT_kwDOSUeMrM6HOBik -> author (The reviewer says the same feedback applies here, so the author needs to update this attribute and respond.)
llm: pr-conversation -> author (A reviewer asked for clarification and no author reply is present yet, so the author needs to respond.)

PR #184
llm: pr-conversation -> author (A reviewer issued a changes-requested review noting changes were lost in a force-push, so the author needs to update the PR and respond.)

PR #179
llm: pr-conversation -> author (A reviewer asked the PR author to add a closing keyword and fill out the PR template, so the author needs to act next.)

PR #173
llm: pr-conversation -> author (The latest reviewer comment reports a CI snapshot mismatch and explicitly asks for investigation/update before the PR can land, so the author needs to act next.)

PR #164
llm: PRRT_kwDOSUeMrM6C-3Kb -> author (Reviewer asked for justification and suggested changing the metric definition; the author needs to respond or adjust the PR.)
llm: pr-conversation -> author (The last comment is from a reviewer/approver asking the author to clarify the existing metric description, so the author needs to respond or update the PR.)

PR #162
llm: PRRT_kwDOSUeMrM6GRukM -> author (The reviewer asked a follow-up question about whether to reference it on the operation duration metric, so the author needs to პასუხ/respond or update the PR.)
llm: PRRT_kwDOSUeMrM6G1k52 -> author (A reviewer asked whether `finish_reason` should also be added, so the author needs to जवाब/implement or explain the choice.)
llm: PRRT_kwDOSUeMrM6G2GhO -> author (A reviewer asked whether the shared `MessagePart` alias change is intended, so the PR author needs to जवाब/confirm or adjust the docs regeneration scope.)

PR #144
llm: PRRT_kwDOSUeMrM6BMiXX -> author (The reviewer raised a concrete issue and asked for a code or documentation adjustment, so the PR author needs to respond and act.)

PR #143
llm: PRRT_kwDOSUeMrM6F1Aqk -> none (The latest reviewer comment is an acknowledgement explaining the suggestion’s usefulness, with no explicit request for the author to act or respond.)
llm: PRRT_kwDOSUeMrM6F0-FD -> author (Reviewer asked for reference scenarios for FilePart and UriPart, so the PR author needs to implement that follow-up.)

PR #112
llm: pr-conversation -> author (Reviewer requested changes: the PR depends on google-adk relaxing its google-genai constraint and then bumping google-adk, so the author needs to update the PR or wait on that dependency.)

PR #98
llm: PRRT_kwDOSUeMrM6E9NFw -> reviewer (The author responded to the reviewer’s suggestion with a substantive explanation, so the ball is back with the reviewer to acknowledge or continue the review.)
llm: pr-conversation -> reviewer (The author asked the reviewer to take another pass, so the next action is for the reviewer to review again.)

```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

