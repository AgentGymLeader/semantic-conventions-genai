> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.
>
> Reviewers column: ✅ approved · ✔️ approved (non-code-owner) · 💬 open thread · 🔴 changes requested.

## Waiting on maintainers

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) | app/renovate | DylanRussell&nbsp;💬<br>lmolkova&nbsp;✅ | ❌ | ✅ | 29d |

## Waiting on reviewers

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-adk to v2 (#173)](https://github.com/open-telemetry/semantic-conventions-genai/pull/173) | app/renovate | MikeGoldsmith&nbsp;💬 | ❌ | ✅ | 18d |
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova<br>MikeGoldsmith&nbsp;🔴<br>trask&nbsp;💬 | ✅ | ❌ | 9d |
| [semconv for a2a protocol (#195)](https://github.com/open-telemetry/semantic-conventions-genai/pull/195) | eternalcuriouslearner | aabmass | ✅ | ✅ | 8d |
| [Limit gen_ai.agent.id to stable / static identifiers (#242)](https://github.com/open-telemetry/semantic-conventions-genai/pull/242) | lmolkova | aabmass&nbsp;💬⁠✅ | ✅ | ✅ | 2d |
| [Add gen_ai.agent.invocation.id attribute for invoke_agent spans (#250)](https://github.com/open-telemetry/semantic-conventions-genai/pull/250) | singankit | lmolkova&nbsp;💬 | ✅ | ❌ | 1d |
| [Clarify that billed token counts should be reported for Cohere usage (#211)](https://github.com/open-telemetry/semantic-conventions-genai/pull/211) | trask | lmolkova&nbsp;✅<br>MikeGoldsmith&nbsp;💬⁠✅ | ✅ | ✅ | 1d |
| [Limit supported  part types  on `gen_ai.system_instructions` to text only (#257)](https://github.com/open-telemetry/semantic-conventions-genai/pull/257) | lmolkova |  | ✅ | ✅ | 21h |
| [Add gen_ai.agent.finish_reason attribute for agent loop termination (#238)](https://github.com/open-telemetry/semantic-conventions-genai/pull/238) | Nik-Reddy | MikeGoldsmith&nbsp;🔴 | ✅ | ✅ | 14h |

## Waiting on authors

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: make input-messages BlobPart content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid | Copilot&nbsp;💬<br>lmolkova<br>trask | ✅ | ❌ | 26d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede | lmolkova&nbsp;💬 | ✅ | ❌ | 18d |
| [gen-ai: add evaluation operation name and gen_ai.evaluate.internal span (#185)](https://github.com/open-telemetry/semantic-conventions-genai/pull/185) | hippoley | Cirilla-zmh&nbsp;💬<br>Copilot&nbsp;💬<br>singankit&nbsp;💬 | ❌ | ✅ | 16d |
| [Add experimental GenAI context selection event (#190)](https://github.com/open-telemetry/semantic-conventions-genai/pull/190) | caioribeiroclw-pixel | Copilot&nbsp;💬<br>trask&nbsp;💬 | ❌ | ❌ | 15d |
| [Add gen_ai.agent.invocation.duration and gen_ai.tool.execution.duration metrics (#201)](https://github.com/open-telemetry/semantic-conventions-genai/pull/201) | pvlsirotkin | MikeGoldsmith&nbsp;🔴 | ✅ | ❌ | 9d |
| [gen-ai: add gen_ai.response.id to deepeval evaluation result event (#184)](https://github.com/open-telemetry/semantic-conventions-genai/pull/184) | hippoley | lmolkova&nbsp;✅<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ✅ | 9d |
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid | Cirilla-zmh<br>trask&nbsp;💬 | ✅ | ❌ | 7d |
| [Add workflow node convention (#188)](https://github.com/open-telemetry/semantic-conventions-genai/pull/188) | RKest | lmolkova&nbsp;🔴<br>trask&nbsp;💬 | ✅ | ❌ | 6d |
| [Add modality, cache, and phase breakdowns for token usage (#197)](https://github.com/open-telemetry/semantic-conventions-genai/pull/197) | trask | alexmojaki&nbsp;💬<br>lmolkova&nbsp;💬<br>Nik-Reddy&nbsp;💬 | ✅ | ❌ | 6d |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) | eternalcuriouslearner | JWinermaSplunk<br>lmolkova&nbsp;💬⁠✅<br>trask | ✅ | ❌ | 4d |
| [Add gen_ai.agent.request.size and gen_ai.agent.response.size metrics (#202)](https://github.com/open-telemetry/semantic-conventions-genai/pull/202) | pvlsirotkin | Copilot&nbsp;💬<br>lmolkova&nbsp;💬<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ✅ | 2d |
| [Add gen_ai.workflow.steps metric (#203)](https://github.com/open-telemetry/semantic-conventions-genai/pull/203) | pvlsirotkin | aabmass&nbsp;💬⁠✅<br>lmolkova&nbsp;💬<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ✅ | 2d |
| [Clarify scope of `gen_ai.client.operation.duration` metric (#215)](https://github.com/open-telemetry/semantic-conventions-genai/pull/215) | trask | lmolkova&nbsp;💬<br>Nik-Reddy&nbsp;💬 | ✅ | ❌ | 1d |
| [Add gen_ai.invoke_agent.server span (SERVER kind) (#252)](https://github.com/open-telemetry/semantic-conventions-genai/pull/252) | singankit | Copilot&nbsp;💬 | ✅ | ✅ | 1d |
| [Add prompt versioning and variable support to GenAI attributes (#179)](https://github.com/open-telemetry/semantic-conventions-genai/pull/179) | steverao | lmolkova&nbsp;💬<br>trask | ✅ | ❌ | 1d |
| [Add gen_ai.request.reasoning_effort attribute (#258)](https://github.com/open-telemetry/semantic-conventions-genai/pull/258) | katsuhisa91 | Copilot&nbsp;💬<br>lmolkova&nbsp;💬 | ✅ | ✅ | 2h |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 15d |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | 8d |

<details>
<summary>Diagnostics</summary>

```text
PR #258
llm: PRRT_kwDOSUeMrM6HjUT8 -> reviewer (The author replied with a rationale for keeping flow-style YAML, so the ball is back with the reviewer to accept it or continue the discussion.)
llm: PRRT_kwDOSUeMrM6HmC06 -> author (Reviewer left a suggested wording change on the registry entry, so the author needs to apply or respond to it.)
llm: PRRT_kwDOSUeMrM6HmEEf -> author (Reviewer requested concrete follow-up changes to the model and related spans/docs, so the PR author needs to act.)
llm: PRRT_kwDOSUeMrM6HmFo9 -> author (A reviewer raised a naming/design suggestion and explicitly said to consider future reasoning properties; the author needs to respond or adjust the PR.)
llm: PRRT_kwDOSUeMrM6HmF1r -> author (Reviewer requested adding the attribute to applicable instrumentations, and there is no author reply yet.)

PR #252
llm: PRRT_kwDOSUeMrM6HO1Cy -> author (Reviewer requested new reference scenario coverage and regenerated outputs for the new `gen_ai.invoke_agent.server` span, so the PR author needs to make the change.)

PR #250
llm: PRRT_kwDOSUeMrM6HQjux -> reviewer (The author’s latest comment is an open question asking whether using `gen_ai.response.id` is reasonable and inviting objection, so the reviewer needs to respond.)

PR #242
llm: PRRT_kwDOSUeMrM6G8yXJ -> reviewer (The author reported they couldn’t find the `id` property, so the reviewer/maintainer needs to जवाब clarify or respond to that point.)
llm: PRRT_kwDOSUeMrM6G8ys_ -> reviewer (The last comment is from the author pushing back on the instrumentation, so the reviewer/maintainer needs to respond or close the thread.)
llm: PRRT_kwDOSUeMrM6G8zAI -> reviewer (The only comment is from the author and is a substantive note, so the ball is with the reviewer/maintainer to respond or decide.)
llm: PRRT_kwDOSUeMrM6HfMuV -> reviewer (The author replied with a question asking whether the existing note is sufficient, so the ball is back with the reviewer to answer.)

PR #238
llm: pr-conversation -> reviewer (The author replied that both requested changes were addressed, so the ball is back with the reviewer to re-check and resolve the thread.)

PR #215
llm: PRRT_kwDOSUeMrM6Fl7mu -> author (The latest reviewer comment only notes that an issue was created; it doesn’t close the discussion or acknowledge a prior author reply, so the ball is still with the author to respond or follow up.)

PR #211
llm: PRRT_kwDOSUeMrM6HDyxU -> reviewer (The reviewer asked whether a fallback is needed; the author replied that Cohere always sends both, so the ball is back with the reviewer to acknowledge or continue review.)

PR #203
llm: PRRT_kwDOSUeMrM6HGTO5 -> author (A reviewer asked for stronger wording in the docs, so the PR author needs to update the text or respond.)
llm: PRRT_kwDOSUeMrM6HGVHV -> author (Reviewer asked for an explicit change to add histogram buckets, so the author needs to update the PR or जवाब back.)
llm: PRRT_kwDOSUeMrM6HGVko -> author (A reviewer suggested adding the `attributes.gen_ai.error` reference, so the author needs to update the PR or जवाब back.)
llm: PRRT_kwDOSUeMrM6HGYBs -> author (The reviewer asked for clarification about the meaning of "attributed to" and how tool calls are handled, so the author needs to პასუხ/clarify.)
llm: PRRT_kwDOSUeMrM6HGaQ9 -> author (A reviewer asked a clarification question about the metric definition, so the PR author needs to जवाब/clarify.)
llm: PRRT_kwDOSUeMrM6HQMhq -> author (The reviewer asked whether the metric is still necessary and requested justification; the author needs to जवाब/decide whether to keep or remove it.)
llm: PRRT_kwDOSUeMrM6HQOdJ -> author (A reviewer asked a substantive question about whether the metric should be recorded per invoke_agent, so the author needs to respond or clarify.)
llm: PRRT_kwDOSUeMrM6HQPlI -> author (A reviewer asked a substantive question about whether tool results or agent transfers should count as steps, so the author needs to जवाब/clarify and possibly adjust the docs.)
llm: PRRT_kwDOSUeMrM6HGQJ7 -> author (Reviewer raised a cardinality concern, and the latest reviewer reply only disagrees without closing the thread; the author still needs to respond or adjust the design.)
llm: PRRT_kwDOSUeMrM6HfgKN -> author (A reviewer asked whether adding a link would be useful, so the author needs to respond or make the change.)
llm: PRRT_kwDOSUeMrM6HfhGd -> author (A reviewer raised a concrete suggestion about making the metric required, so the author needs to respond or update the PR.)
llm: PRRT_kwDOSUeMrM6HfjLl -> author (Reviewer suggested an additional invariant change and the thread is unresolved, so the PR author needs to respond or update the PR.)

PR #202
llm: PRRT_kwDOSUeMrM6FJWZf -> reviewer (The author replied but did not resolve the concern, effectively handing it back for reviewer/maintainer judgment on whether the phrasing should be standardized.)
llm: PRRT_kwDOSUeMrM6HFBNY -> author (A reviewer pointed out that `gen_ai.agent.invocation.duration` is not a known metric and suggested an alternative, so the PR author needs to respond or revise the docs.)
llm: PRRT_kwDOSUeMrM6HFBTV -> author (A reviewer asked whether to add missing refs, so the author needs to जवाब/respond or update the PR.)
llm: PRRT_kwDOSUeMrM6HFIOO -> author (The latest reviewer comment հարցs whether the condition is needed, so the PR author needs to जवाब/adjust the code.)
llm: PRRT_kwDOSUeMrM6HFKa9 -> author (The latest reviewer comment asks for clarification on byte-length calculation, so the PR author needs to जवाब/respond and update the docs.)
llm: PRRT_kwDOSUeMrM6HQuab -> author (Reviewer asked whether the payload volume metric should apply to remote/A2A calls, so the author needs to जवाब/adjust the PR.)
llm: PRRT_kwDOSUeMrM6HQuUW -> author (A reviewer asked for a stricter definition of what counts, so the PR author needs to respond or update the docs.)
llm: PRRT_kwDOSUeMrM6HQwLc -> author (Reviewer asked a substantive question and proposed a metric rename, so the PR author needs to respond or update the design/docs.)
llm: PRRT_kwDOSUeMrM6FJWY9 -> none (The latest reviewer comment says the phrasing has already been normalized in another PR, which closes the issue here with no further action needed in this thread.)

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
llm: PRRT_kwDOSUeMrM6HcJqe -> author (Reviewer suggested a different namespacing approach for the breaking rename, so the author needs to respond or update the PR.)
llm: PRRT_kwDOSUeMrM6HcSsx -> author (Reviewer asked whether the spec should be generalized or modeled differently; the author needs to respond and likely adjust the PR.)
llm: PRRT_kwDOSUeMrM6HckTh -> author (The latest comment is a reviewer proposing a different metric design, so the author needs to respond or update the PR.)
llm: PRRT_kwDOSUeMrM6HcoWo -> author (A reviewer asked whether span attributes and metrics should be in the same PR, so the author needs to जवाब/clarify.)

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
llm: PRRT_kwDOSUeMrM6HQVdg -> author (The reviewer asked a substantive question about the implementation, and there is no author reply yet, so the author needs to respond.)
llm: PRRT_kwDOSUeMrM6HQXGO -> author (A reviewer asked a direct question about how instrumentation would know about prompt variables, and the author has not پاسخ yet.)
llm: PRRT_kwDOSUeMrM6HQbrq -> author (A reviewer requested a wording change and added a note to include; the author needs to update the PR.)

PR #173
llm: pr-conversation -> author (The latest reviewer comment reports a CI snapshot mismatch and explicitly asks for investigation/update before the PR can land, so the author needs to act next.)

PR #164
llm: PRRT_kwDOSUeMrM6C-3Kb -> author (Reviewer asked for justification and suggested changing the metric definition; the author needs to respond or adjust the PR.)
llm: pr-conversation -> author (The last comment is from a reviewer/approver asking the author to clarify the existing metric description, so the author needs to respond or update the PR.)

PR #162
llm: PRRT_kwDOSUeMrM6GRukM -> author (The reviewer asked a follow-up question about whether to reference it on the operation duration metric, so the author needs to პასუხ/respond or update the PR.)

PR #144
llm: PRRT_kwDOSUeMrM6BMiXX -> author (A reviewer flagged that the model/example currently does not enforce the stated constraint at runtime and asked for a code or documentation change, so the PR author needs to respond.)
llm: PRRT_kwDOSUeMrM6HgmeM -> none (The reviewer only explained that the file was converted in another PR and did not ask for any follow-up or action.)

PR #143
llm: PRRT_kwDOSUeMrM6F1Aqk -> author (The last comment is from the reviewer/approver, adding a substantive follow-up about #144, so the author needs to respond or act.)
llm: PRRT_kwDOSUeMrM6F0-FD -> author (The latest comment is a reviewer request to add reference scenarios for FilePart and UriPart, so the PR author needs to act.)

PR #112
llm: pr-conversation -> author (Reviewer requested changes: the PR depends on google-adk relaxing its google-genai constraint and then bumping google-adk, so the author needs to update the PR or wait on that dependency.)

PR #98
llm: PRRT_kwDOSUeMrM6E9NFw -> reviewer (The author replied to the nesting suggestion with a substantive explanation and did not indicate the PR is still waiting on their own follow-up, so the ball is back with the reviewer to respond.)
llm: pr-conversation -> reviewer (The author asked the reviewer to take another pass, so the ball is back with the reviewer.)

```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

