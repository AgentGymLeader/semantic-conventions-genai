> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.
>
> Reviewers column: ✅ approved · ✔️ approved (non-code-owner) · 💬 open thread · 🔴 changes requested.

## Waiting on reviewers

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-adk to v2 (#173)](https://github.com/open-telemetry/semantic-conventions-genai/pull/173) | app/renovate | MikeGoldsmith&nbsp;💬 | ❌ | ✅ | 17d |
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova<br>MikeGoldsmith&nbsp;🔴<br>trask&nbsp;💬 | ✅ | ❌ | 8d |
| [Clarify scope of `gen_ai.client.operation.duration` metric (#215)](https://github.com/open-telemetry/semantic-conventions-genai/pull/215) | trask | lmolkova | ✅ | ❌ | 7d |
| [semconv for a2a protocol (#195)](https://github.com/open-telemetry/semantic-conventions-genai/pull/195) | eternalcuriouslearner |  | ✅ | ✅ | 6d |
| [Add gen_ai.agent.invocation.id attribute for invoke_agent spans (#250)](https://github.com/open-telemetry/semantic-conventions-genai/pull/250) | singankit | lmolkova&nbsp;💬 | ✅ | ✅ | 11h |
| [Generalize the `gen_ai.provider.name` description (#212)](https://github.com/open-telemetry/semantic-conventions-genai/pull/212) | trask | lmolkova&nbsp;✅<br>MikeGoldsmith&nbsp;💬⁠✅ | ✅ | ✅ | 5m |

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
PR #252
llm: PRRT_kwDOSUeMrM6HO1Cy -> author (A reviewer asked for additional reference-scenario coverage and regeneration, so the PR author needs to act.)

PR #250
llm: PRRT_kwDOSUeMrM6HQjux -> reviewer (The latest comment is from the author asking whether reusing `gen_ai.response.id` is acceptable and providing more context, so the reviewer/maintainer needs to answer or decide.)

PR #242
llm: PRRT_kwDOSUeMrM6G8yXJ -> reviewer (The only comment is from the PR author reporting they could not find the `id` property, so the next response should come from a reviewer to clarify or adjust the requested change.)
llm: PRRT_kwDOSUeMrM6G8ys_ -> reviewer (The author responded with a rationale for not instrumenting it; the reviewer/maintainer now needs to accept that or continue the review.)
llm: PRRT_kwDOSUeMrM6G8zAI -> reviewer (The author’s last comment is a reply/explanation, so the ball is back with the reviewer to respond or resolve the concern.)
llm: PRRT_kwDOSUeMrM6G9Yjt -> author (The reviewer asked for comment/docstring updates to match the new behavior, so the PR author needs to make the requested change.)

PR #238
llm: PRRT_kwDOSUeMrM6GrEAT -> reviewer (The latest comment is from the author, and they explicitly chose not to make the requested wording change, so the ball is back with the reviewer/maintainer to accept, push back, or close the thread.)
llm: PRRT_kwDOSUeMrM6HEq4S -> reviewer (The reviewer requested an additional scenario, and the author replied that they added it; the ball is now with the reviewer to review/confirm the change.)
llm: pr-conversation -> author (A reviewer left CHANGES_REQUESTED with suggestions, so the author needs to respond or update the PR.)

PR #226
llm: PRRT_kwDOSUeMrM6GgW8E -> author (The reviewer suggested a possible alternative and explicitly left resolution to the author (“feel free to resolve if you've seen it”), so the author needs to respond or act.)
llm: PRRT_kwDOSUeMrM6GgYDR -> unclear (LLM timeout)
llm: PRRT_kwDOSUeMrM6GgbzS -> author (A reviewer asked whether the check could be made generic for the `generate-all` target, so the author needs to respond or update the workflow.)
error: 1 thread classification(s) failed

PR #215
llm: PRRT_kwDOSUeMrM6Fl7mu -> none (The last comment is just a status update that an issue was created from the offline discussion; it doesn’t ask either side to do anything further in this thread.)

PR #212
llm: pr-conversation -> reviewer (The author has replied and is waiting for the reviewer to clarify the hint’s usefulness or suggest better wording/place for it.)

PR #211
llm: PRRT_kwDOSUeMrM6HDyxU -> author (The latest reviewer comment says they’re unsure and leaves the fallback question unresolved, so the author needs to decide whether to add it or clarify the scenario.)

PR #203
llm: PRRT_kwDOSUeMrM6HGQJ7 -> author (A reviewer asked whether an unbounded freeform string should be on a metric and suggested spans instead; the author needs to პასუხ respond or revise.)
llm: PRRT_kwDOSUeMrM6HGTO5 -> author (Reviewer asked for stronger wording change; the author needs to update the docs or जवाब to the suggestion.)
llm: PRRT_kwDOSUeMrM6HGVHV -> author (A reviewer asked for a change and there is no author reply yet, so the PR author needs to act.)
llm: PRRT_kwDOSUeMrM6HGVko -> author (Reviewer requested an additional `attributes.gen_ai.error` reference and the author has not responded yet.)
llm: PRRT_kwDOSUeMrM6HGYBs -> author (The reviewer asked for clarification and no follow-up reply is present, so the PR author needs to answer.)
llm: PRRT_kwDOSUeMrM6HGaQ9 -> author (A reviewer asked whether partial/failed steps should count, and there is no follow-up yet from the author.)
llm: PRRT_kwDOSUeMrM6HQMhq -> author (The reviewer asked whether the metric is still necessary and no author response is present, so the PR author needs to जवाब/decide whether to keep or remove it.)
llm: PRRT_kwDOSUeMrM6HQOdJ -> author (The latest and only comment is a reviewer asking a clarification question, so the author needs to जवाब/respond.)
llm: PRRT_kwDOSUeMrM6HQPlI -> author (The reviewer asked a substantive question about metric semantics and is waiting on the PR author to जवाब/clarify.)

PR #202
llm: PRRT_kwDOSUeMrM6FJWZf -> reviewer (The author replied and deferred to maintainers on the phrasing choice, so the thread is back with the reviewer/maintainer side to decide whether to accept or request a change.)
llm: PRRT_kwDOSUeMrM6HFBNY -> author (Reviewer asked for a metric name correction or related-signal note, so the PR author needs to respond or update the docs.)
llm: PRRT_kwDOSUeMrM6HFBTV -> author (A reviewer asked whether to add two metric refs, so the PR author needs to जवाब/respond and likely update the file.)
llm: PRRT_kwDOSUeMrM6HFIOO -> author (The reviewer asked whether the condition is needed, so the author needs to respond or update the PR.)
llm: PRRT_kwDOSUeMrM6HFKa9 -> author (A reviewer asked for clarification on how byte length should be calculated, so the PR author needs to respond or update the docs.)
llm: PRRT_kwDOSUeMrM6HQuab -> author (Reviewer asked whether the payload volume metric belongs in a2a instead; the author needs to respond or adjust the PR.)
llm: PRRT_kwDOSUeMrM6HQuUW -> author (A reviewer raised a substantive suggestion about tightening the definition of what is counted, so the PR author needs to respond or update the change.)
llm: PRRT_kwDOSUeMrM6HQwLc -> author (Reviewer raised a substantive naming/semantics question and suggested a better metric name, so the PR author needs to respond or update the docs.)
llm: PRRT_kwDOSUeMrM6FJWY9 -> none (The reviewer says they normalized the phrasing already in another PR, so this thread is effectively addressed and needs no further follow-up.)

PR #201
llm: PRRT_kwDOSUeMrM6FYxtF -> author (The reviewer raised a clarification, and the author replied that they will add explanatory text, so the author still needs to make the follow-up change.)
llm: PRRT_kwDOSUeMrM6FY1gg -> reviewer (The author replied with a question and proposal, so the ball is back with the reviewer to decide between `recommended` and `required`.)
llm: PRRT_kwDOSUeMrM6FY5Vy -> reviewer (The author responded that they added the suggested attribute, so the reviewer/maintainer is next to confirm or resolve the thread.)
llm: PRRT_kwDOSUeMrM6FY3VY -> reviewer (The author replied with an implementation concern and asked for alignment on the approach, so the ball is back with the reviewer to clarify whether metrics support should be added or the PR should proceed another way.)
llm: pr-conversation -> author (Reviewer left CHANGES_REQUESTED and asked for fixes, so the PR author needs to respond/ अपडेट the PR.)

PR #197
llm: PRRT_kwDOSUeMrM6E-Ear -> reviewer (The author answered the suggestion by choosing `gen_ai.client.embeddings.tokens` and linking the change, so the ball is back with the reviewer to acknowledge or review that update.)
llm: PRRT_kwDOSUeMrM6FkB2H -> author (The reviewer’s last comment supplied the requested details and re-opened the decision back to the PR author to acknowledge or decide whether to change the schema.)
llm: PRRT_kwDOSUeMrM6F1og7 -> author (The latest comment is from a reviewer/approver and leaves the question open about whether to split input tokens; the author needs to respond or implement the follow-up.)
llm: PRRT_kwDOSUeMrM6F1nUT -> author (The last comment is from a reviewer asking whether the model should add an `unknown` phase, so the PR author needs to जवाब/decide and update the change.)
llm: pr-conversation -> external (The reviewer moved the discussion to an ad-hoc call, so resolution is blocked outside the repository rather than awaiting an in-thread response.)

PR #190
llm: PRRT_kwDOSUeMrM6EO3Gw -> author (The only comment is a reviewer request to align the changelog wording with the registry, so the PR author needs to update or जवाब back.)
llm: pr-conversation -> author (The reviewer asked the PR author to fill out the template and sign the CLA, so the next action is on the author.)

PR #188
llm: PRRT_kwDOSUeMrM6EP5P6 -> reviewer (The reviewer asked a question, and the author answered with a concrete source/example; the ball is back with the reviewer to acknowledge or continue the review.)
llm: PRRT_kwDOSUeMrM6EP9-D -> reviewer (The author replied with the requested investigation and updates, so the ball is back with the reviewer to assess or respond.)
llm: PRRT_kwDOSUeMrM6F5pCw -> author (A reviewer asked whether another PR proposes the same concept, so the ball is with the PR author to confirm, clarify, or adjust the change.)

PR #185
llm: PRRT_kwDOSUeMrM6DuuPn -> author (The reviewer raised a naming inconsistency and asked for alignment; no author reply is present, so the author needs to respond or implement a fix.)
llm: PRRT_kwDOSUeMrM6E_Amb -> author (A reviewer pointed out a specific wording issue and asked for a change, so the PR author needs to update the line or जवाब back.)
llm: PRRT_kwDOSUeMrM6E_COY -> author (The reviewer asked for clarification and a prototype, so the author needs to respond or update the PR.)
llm: PRRT_kwDOSUeMrM6HOBHP -> author (Reviewer said the attribute does not seem relevant and left the thread open, so the author needs to respond or adjust the change.)
llm: PRRT_kwDOSUeMrM6HOBik -> author (A reviewer said the same feedback applies to this attribute too, so the author needs to update the PR or respond.)
llm: pr-conversation -> author (A reviewer asked for clarification questions and has not received a reply, so the PR author needs to respond.)

PR #184
llm: pr-conversation -> author (The only comment is a reviewer request changes note saying changes were lost in a force-push, so the author needs to reapply/fix and respond.)

PR #179
llm: PRRT_kwDOSUeMrM6HQVdg -> author (A reviewer asked whether input messages are still passed along with the prompt, so the PR author needs to जवाब/clarify or adjust the implementation.)
llm: PRRT_kwDOSUeMrM6HQXGO -> author (The reviewer asked a substantive question about how instrumentation would capture prompt variables, so the author needs to जवाब/clarify or adjust the scenario.)
llm: PRRT_kwDOSUeMrM6HQbrq -> author (A reviewer requested a documentation change and the thread is unresolved, so the author needs to update the PR.)

PR #173
llm: pr-conversation -> author (The latest comment is from a reviewer/approver reporting a CI snapshot mismatch and asking for investigation or scenario updates before merge.)

PR #164
llm: PRRT_kwDOSUeMrM6C-3Kb -> author (Reviewer asked where the assumption comes from and whether a new metric is needed, so the author needs to जवाब/justify or revise the change.)
llm: pr-conversation -> author (The reviewer clarified the request and asked for the existing metric description to be aligned; the last substantive response is from the author, so the author needs to update or respond.)

PR #162
llm: PRRT_kwDOSUeMrM6GRukM -> author (A reviewer asked whether it should also be referenced on the operation duration metric, so the author needs to პასუხ/respond or update the PR.)

PR #144
llm: PRRT_kwDOSUeMrM6BMiXX -> author (A reviewer flagged a mismatch between the comment and the Pydantic model behavior, so the PR author needs to respond by fixing it or clarifying the constraint.)

PR #143
llm: PRRT_kwDOSUeMrM6F1Aqk -> none (The latest reviewer comment is a clear acknowledgment that closes the thread ('oh, I see...'), with no follow-up requested.)
llm: PRRT_kwDOSUeMrM6F0-FD -> author (The latest comment is a reviewer request to add reference scenarios for FilePart and UriPart, so the PR author needs to act.)

PR #112
llm: pr-conversation -> external (Blocked on an upstream google-adk release/dependency change outside this repository before the PR can proceed.)

PR #98
llm: PRRT_kwDOSUeMrM6E9NFw -> reviewer (The author’s last comment is a substantive reply to the reviewer’s suggestion and passes the discussion back for reviewer consideration; it is not a self-deferral about pending PR work.)
llm: pr-conversation -> reviewer (The author asked the reviewer to take another pass, so the next action is on the reviewer.)

```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

