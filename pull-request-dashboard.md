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
| [Add gen_ai.request.reasoning.level attribute (#258)](https://github.com/open-telemetry/semantic-conventions-genai/pull/258) | katsuhisa91 | JWinermaSplunk<br>lmolkova | ✅ | ✅ | 16h |

## Waiting on authors

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: make input-messages BlobPart content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid | Copilot&nbsp;💬<br>lmolkova<br>trask | ✅ | ❌ | 28d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede | Cirilla-zmh&nbsp;💬<br>lmolkova&nbsp;💬 | ✅ | ❌ | 21d |
| [gen-ai: add evaluation operation name and gen_ai.evaluate.internal span (#185)](https://github.com/open-telemetry/semantic-conventions-genai/pull/185) | hippoley | Cirilla-zmh&nbsp;💬<br>Copilot&nbsp;💬<br>singankit&nbsp;💬 | ❌ | ✅ | 19d |
| [Add experimental GenAI context selection event (#190)](https://github.com/open-telemetry/semantic-conventions-genai/pull/190) | caioribeiroclw-pixel | Copilot&nbsp;💬<br>trask&nbsp;💬 | ❌ | ❌ | 17d |
| [gen-ai: add gen_ai.response.id to deepeval evaluation result event (#184)](https://github.com/open-telemetry/semantic-conventions-genai/pull/184) | hippoley | lmolkova&nbsp;✅<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ✅ | 12d |
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid | Cirilla-zmh<br>trask&nbsp;💬 | ✅ | ❌ | 10d |
| [Add modality, cache, and phase breakdowns for token usage (#197)](https://github.com/open-telemetry/semantic-conventions-genai/pull/197) | trask | alexmojaki&nbsp;💬<br>lmolkova&nbsp;💬<br>Nik-Reddy&nbsp;💬 | ✅ | ❌ | 9d |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) | eternalcuriouslearner | Copilot&nbsp;💬<br>JWinermaSplunk&nbsp;✅<br>lmolkova&nbsp;💬⁠✅<br>trask | ✅ | ❌ | 7d |
| [Add gen_ai.agent.request.size and gen_ai.agent.response.size metrics (#202)](https://github.com/open-telemetry/semantic-conventions-genai/pull/202) | pvlsirotkin | Copilot&nbsp;💬<br>lmolkova&nbsp;💬<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ✅ | 5d |
| [Add gen_ai.workflow.steps metric (#203)](https://github.com/open-telemetry/semantic-conventions-genai/pull/203) | pvlsirotkin | aabmass&nbsp;💬⁠✅<br>lmolkova&nbsp;💬<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ✅ | 5d |
| [Add gen_ai.invoke_agent.server span (SERVER kind) (#252)](https://github.com/open-telemetry/semantic-conventions-genai/pull/252) | singankit | Cirilla-zmh&nbsp;💬<br>Copilot&nbsp;💬 | ✅ | ✅ | 4d |
| [Add prompt versioning and variable support to GenAI attributes (#179)](https://github.com/open-telemetry/semantic-conventions-genai/pull/179) | steverao | lmolkova&nbsp;💬<br>trask | ✅ | ❌ | 4d |
| [Limit gen_ai.agent.id to stable / static identifiers (#242)](https://github.com/open-telemetry/semantic-conventions-genai/pull/242) | lmolkova | aabmass&nbsp;💬⁠✅<br>MikeGoldsmith&nbsp;💬⁠✅ | ✅ | ❌ | 1d |
| [Limit supported  part types  on `gen_ai.system_instructions` to text only (#257)](https://github.com/open-telemetry/semantic-conventions-genai/pull/257) | lmolkova | MikeGoldsmith&nbsp;💬⁠✅ | ✅ | ✅ | 1d |
| [Add workflow node convention (#188)](https://github.com/open-telemetry/semantic-conventions-genai/pull/188) | RKest | aabmass&nbsp;💬<br>lmolkova&nbsp;🔴<br>trask&nbsp;💬 | ✅ | ❌ | 22h |
| [Add gen_ai.agent.invocation.duration and gen_ai.tool.execution.duration metrics (#201)](https://github.com/open-telemetry/semantic-conventions-genai/pull/201) | pvlsirotkin | lmolkova&nbsp;💬<br>MikeGoldsmith&nbsp;🔴 | ✅ | ❌ | 20h |
| [gen-ai: add run guardrail span and security finding (#262)](https://github.com/open-telemetry/semantic-conventions-genai/pull/262) | nagkumar91 | aabmass<br>Copilot&nbsp;💬 | ✅ | ✅ | 3h |
| [semconv for a2a protocol (#195)](https://github.com/open-telemetry/semantic-conventions-genai/pull/195) | eternalcuriouslearner | aabmass&nbsp;💬<br>JWinermaSplunk&nbsp;💬<br>pwkowalski&nbsp;💬<br>trask&nbsp;💬 | ✅ | ✅ | 2h |
| [Add `gen_ai.agent.finish_reason` attribute for agent loop termination (#238)](https://github.com/open-telemetry/semantic-conventions-genai/pull/238) | Nik-Reddy | aabmass&nbsp;✅<br>Copilot&nbsp;💬<br>MikeGoldsmith&nbsp;✅<br>trask&nbsp;💬 | ✅ | ✅ | 1h |

## Waiting on external

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) | app/renovate | DylanRussell&nbsp;💬<br>lmolkova&nbsp;✅ | ❌ | ✅ | 21d |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 17d |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | 11d |
| [Add time_budget value for gen_ai.agent.finish_reason (#267)](https://github.com/open-telemetry/semantic-conventions-genai/pull/267) | Nik-Reddy | 12h |
| [Propose GenAI agent entity (#270)](https://github.com/open-telemetry/semantic-conventions-genai/pull/270) | aabmass | 39m |
| [Improve Slack PR notification links (#271)](https://github.com/open-telemetry/semantic-conventions-genai/pull/271) | trask | 9m |
| [Avoid reviewer badges from PR conversation (#272)](https://github.com/open-telemetry/semantic-conventions-genai/pull/272) | trask | 1m |

<details>
<summary>Diagnostics</summary>

```text
PR #262
llm: PRRT_kwDOSUeMrM6INU2v -> author (The reviewer requested a concrete code change to set the span kind to CLIENT, so the PR author needs to update the scenario.)
llm: PRRT_kwDOSUeMrM6INU32 -> author (A reviewer requested a wording change to the span briefs, and the author has not replied yet, so the ball is with the author to update the docs.)

PR #257
llm: pr-conversation -> author (The latest comment is from a reviewer and asks for scenario updates and a code simplification, so the PR author needs to respond or make the requested changes.)

PR #252
llm: PRRT_kwDOSUeMrM6HO1Cy -> author (The reviewer asked for additional reference scenario coverage and regeneration, so the PR author needs to make that change or respond.)
llm: PRRT_kwDOSUeMrM6IKVVh -> author (A reviewer left a suggestion on the changelog and there is no author follow-up yet, so the author needs to act.)

PR #250
llm: PRRT_kwDOSUeMrM6HQjux -> reviewer (The author replied with their thinking and an implementation detail, and asked for a judgment on whether the approach is reasonable, so the reviewer/maintainer needs to respond.)
llm: pr-conversation -> reviewer (The author replied with a rationale for keeping `invoke_agent.common`, but the reviewer’s earlier request about removing the scenario until Bedrock is wired up is still unresolved, so the ball is back with the reviewer.)

PR #242
llm: PRRT_kwDOSUeMrM6G8yXJ -> reviewer (The latest comment is from the author reporting they could not find the `id` property, so the thread is waiting on reviewer clarification or a response.)
llm: PRRT_kwDOSUeMrM6G8ys_ -> reviewer (The author replied with a rationale for not instrumenting it, so the reviewer/maintainer needs to acknowledge or decide whether to accept that pushback.)
llm: PRRT_kwDOSUeMrM6G8zAI -> reviewer (The latest comment is from the author and only explains a missing example, so the ball is with the reviewer to respond or decide whether that’s sufficient.)
llm: PRRT_kwDOSUeMrM6HfMuV -> reviewer (The author replied with a question asking whether the existing note is sufficient, so the reviewer needs to answer or confirm if more explicit wording is needed.)
llm: PRRT_kwDOSUeMrM6HzsI1 -> author (A reviewer raised a nit about the GCP identifier formatting, and there’s no author reply yet, so the author needs to address or respond.)

PR #238
llm: PRRT_kwDOSUeMrM6IPOxu -> author (Reviewer asked to add a reference scenario that emits `gen_ai.agent.finish_reason="guardrail"`; the PR author needs to make that change or respond.)
llm: pr-conversation -> reviewer (The author’s latest comment asks the SIG/reviewer for a decision on scope, so the next action is a reviewer response.)

PR #215
llm: PRRT_kwDOSUeMrM6Fl7mu -> none (The latest comment is a reviewer acknowledgement that the clarification is directionally aligned and does not ask for further action.)

PR #203
llm: PRRT_kwDOSUeMrM6HGTO5 -> author (The reviewer requested stronger wording, and there is no follow-up reply yet, so the PR author needs to update the docs or respond.)
llm: PRRT_kwDOSUeMrM6HGVHV -> author (A reviewer asked for an additional change (“Can we add the histogram buckets…”), so the PR author needs to respond or implement it.)
llm: PRRT_kwDOSUeMrM6HGVko -> author (A reviewer suggested adding the `attributes.gen_ai.error` reference, so the author needs to update the PR or जवाब to the suggestion.)
llm: PRRT_kwDOSUeMrM6HGYBs -> author (The reviewer asked for clarification about the meaning of "attributed to" and how tool calls are handled, so the PR author needs to जवाब/respond.)
llm: PRRT_kwDOSUeMrM6HGaQ9 -> author (A reviewer asked a clarification question and there is no author reply yet, so the author needs to respond.)
llm: PRRT_kwDOSUeMrM6HQMhq -> author (A reviewer asked whether the metric is still necessary and no author reply followed, so the author needs to respond or adjust the PR.)
llm: PRRT_kwDOSUeMrM6HQOdJ -> author (A reviewer asked whether the metric should be recorded per invoke_agent and raised a follow-up question; the author needs to जवाब/clarify and likely adjust the docs or proposal.)
llm: PRRT_kwDOSUeMrM6HQPlI -> author (A reviewer asked whether tool results or agent transfers should be counted as steps, and no one has जवाबed yet, so the author needs to respond or update the doc.)
llm: PRRT_kwDOSUeMrM6HGQJ7 -> author (The latest comment is a reviewer/approver raising a cardinality concern, so the PR author still needs to respond or adjust the proposal.)
llm: PRRT_kwDOSUeMrM6HfgKN -> author (A reviewer asked whether an additional link would be useful, so the author needs to जवाब/respond and decide whether to make the change.)
llm: PRRT_kwDOSUeMrM6HfhGd -> author (A reviewer asked whether this metric should be required, so the author needs to जवाब/confirm or update the PR.)
llm: PRRT_kwDOSUeMrM6HfjLl -> author (A reviewer raised a substantive suggestion about workflow counting, and there’s no author reply yet, so the author needs to respond or update the PR.)

PR #202
llm: PRRT_kwDOSUeMrM6FJWZf -> reviewer (The author replied and deferred to maintainers (“unless maintainers prefer otherwise”), so the ball is back with the reviewer/maintainer to decide whether to accept the phrasing or request a change.)
llm: PRRT_kwDOSUeMrM6HFBNY -> author (The reviewer asked whether the metric name is wrong and suggested alternatives, so the author needs to respond or update the docs.)
llm: PRRT_kwDOSUeMrM6HFBTV -> author (A reviewer asked whether to add missing metric/attribute refs, so the PR author needs to respond or make the change.)
llm: PRRT_kwDOSUeMrM6HFIOO -> author (The reviewer asked for a code change by questioning the condition, so the author needs to respond or update the PR.)
llm: PRRT_kwDOSUeMrM6HFKa9 -> author (Reviewer asked for clarification on how byte length should be calculated, and there is no author reply yet.)
llm: PRRT_kwDOSUeMrM6HQuab -> author (Reviewer asked whether the payload volume metric is intended for remote/a2a calls, so the PR author needs to जवाब/adjust the design or implementation.)
llm: PRRT_kwDOSUeMrM6HQuUW -> author (The last comment is a reviewer suggestion requesting a stricter definition of what counts, so the author needs to respond or update the PR.)
llm: PRRT_kwDOSUeMrM6HQwLc -> author (The last comment is from a reviewer and asks for the author to address the metric semantics/name suggestion.)
llm: PRRT_kwDOSUeMrM6FJWY9 -> none (The latest reviewer comment says they already normalized the text in another PR, so this thread is effectively closed with no follow-up needed here.)

PR #201
llm: PRRT_kwDOSUeMrM6FY1gg -> reviewer (The author replied with a proposed compromise and asked the reviewer to choose between `recommended` and `required`, so the next action is on the reviewer.)
llm: PRRT_kwDOSUeMrM6FY3VY -> reviewer (The author replied with an implementation/status update and asked for clarification on whether metric validation can be wired up another way, so the next action is on the reviewer to जवाब/confirm the approach.)
llm: PRRT_kwDOSUeMrM6H93N8 -> author (A reviewer asked a direct question and gave guidance on version reporting; the author needs to პასუხ/adjust the PR.)
llm: PRRT_kwDOSUeMrM6H95-W -> external (The reviewer is waiting on a naming decision from an upcoming GenAI call and said they will post back after that external discussion.)
llm: PRRT_kwDOSUeMrM6H96q1 -> author (A reviewer left a concrete suggestion on the metric description/note and there’s no author reply yet, so the PR author needs to respond or apply the change.)
llm: PRRT_kwDOSUeMrM6H9_Oc -> author (The latest comment is from a reviewer/approver proposing a metric-name alignment and explicitly suggesting the PR can start with `gen_ai.invoke_agent.duration`, so the author needs to decide/adjust the implementation.)
llm: PRRT_kwDOSUeMrM6H9_vs -> author (A reviewer left a nit with a concrete suggestion and the thread is unresolved, so the PR author needs to apply or जवाब/acknowledge it.)
llm: PRRT_kwDOSUeMrM6H-EfV -> author (A reviewer suggested aligning metric and span attributes; the author needs to respond or update the PR.)
llm: PRRT_kwDOSUeMrM6H-HJv -> author (A reviewer asked for a documentation change and hasn’t been answered yet, so the author needs to respond or update the PR.)
llm: PRRT_kwDOSUeMrM6H-Idj -> author (The reviewer asked for a change (“let's move it to the metric note in yaml”), so the PR author needs to update the PR or respond.)
llm: PRRT_kwDOSUeMrM6H-JSd -> author (Reviewer raised a nit about duplicated generated content, and the author has not replied or addressed it yet.)
llm: PRRT_kwDOSUeMrM6H-J5i -> author (A reviewer left a nit with a suggested deletion and no author response yet, so the PR author needs to act.)
llm: PRRT_kwDOSUeMrM6H-ZIz -> author (A reviewer asked for a change to the histogram boundaries, so the author needs to respond and likely update the PR.)

PR #197
llm: PRRT_kwDOSUeMrM6E-Ear -> reviewer (The reviewer asked whether to add an embeddings token metric, and the author replied with a preferred metric name and pointed to the change they made; the ball is back with the reviewer to confirm/close the thread.)
llm: PRRT_kwDOSUeMrM6FkB2H -> author (The reviewer’s last comment provided follow-up details and left the question open; the ball is back with the author to respond or decide whether to change the schema.)
llm: PRRT_kwDOSUeMrM6F1og7 -> author (The latest comment is from a reviewer and ends with a deferred suggestion about future work, so the ball is with the author to respond or follow up.)
llm: PRRT_kwDOSUeMrM6F1nUT -> author (The latest comment is from a reviewer/approver asking a design question about token phase handling, so the PR author needs to जवाब/decide and respond.)
llm: PRRT_kwDOSUeMrM6HcJqe -> author (A reviewer suggested a breaking rename approach and there’s no author reply yet, so the PR author needs to respond or update the change.)
llm: PRRT_kwDOSUeMrM6HcSsx -> author (A reviewer asked whether the spec should use a template or complex object instead of enumerating combinations, so the PR author needs to respond or adjust the design.)
llm: PRRT_kwDOSUeMrM6HckTh -> author (The latest comment is from a reviewer/approver and raises a substantive design concern/suggestion, so the PR author needs to respond or adjust the implementation.)
llm: PRRT_kwDOSUeMrM6HcoWo -> author (A reviewer asked whether span attributes and metrics should be in the same PR, so the author needs to जवाब/confirm the scope.)

PR #195
llm: pr-conversation -> author (The latest comment is from the author and says they still need to come back with a split-work plan, so the author has the next action.)

PR #190
llm: PRRT_kwDOSUeMrM6EO3Gw -> author (A reviewer raised a changelog wording mismatch and no one has replied yet, so the PR author needs to address or respond.)
llm: pr-conversation -> author (Reviewer requested the author to fill out the PR template and sign the CLA, so the author needs to act.)

PR #188
llm: PRRT_kwDOSUeMrM6EP5P6 -> reviewer (The author answered the reviewer’s question with concrete instrumentation sources and an example trace, so the ball is back with the reviewer to confirm or continue the review.)
llm: PRRT_kwDOSUeMrM6H9Vwj -> author (The reviewer asked whether other graphs can be reconstructed and raised a concern that needs a response or follow-up from the PR author.)
llm: PRRT_kwDOSUeMrM6F5pCw -> author (The latest comment is from a reviewer/approver, and it asks the author to respond to the naming discussion with the stated preference for "node".)
llm: PRRT_kwDOSUeMrM6H_ijb -> author (A reviewer raised a substantive concern and suggested removing the changes, so the author needs to respond or revise the PR.)
llm: PRRT_kwDOSUeMrM6H_pco -> author (A reviewer asked an open design question and linked to prior discussion, so the PR author needs to respond or clarify how edges are represented.)
llm: PRRT_kwDOSUeMrM6H_q9l -> author (The approver raised a change request about not reusing existing attributes, so the PR author needs to respond or update the PR.)

PR #185
llm: PRRT_kwDOSUeMrM6DuuPn -> author (The latest comment is a reviewer request to align the span naming/operation terminology, so the PR author needs to respond or make the change.)
llm: PRRT_kwDOSUeMrM6E_Amb -> author (A reviewer asked for a wording fix (“we need a verb here”), so the author needs to update the PR.)
llm: PRRT_kwDOSUeMrM6E_COY -> author (The reviewer asked for clarification and a prototype, so the PR author needs to जवाब/act next.)
llm: PRRT_kwDOSUeMrM6HOBHP -> author (A reviewer/approver raised a substantive concern and there is no author reply yet, so the PR author needs to address it.)
llm: PRRT_kwDOSUeMrM6HOBik -> author (The latest comment is a reviewer request to apply the same feedback to another attribute, so the PR author needs to update or जवाब back.)
llm: pr-conversation -> author (A reviewer asked for clarification and no author reply has been made, so the author needs to respond.)

PR #184
llm: pr-conversation -> author (A reviewer requested changes and there is no author follow-up, so the PR author needs to respond and update the branch.)

PR #179
llm: PRRT_kwDOSUeMrM6HQVdg -> author (A reviewer asked whether input messages should still be passed with the prompt, and there is no reply yet, so the author needs to respond or adjust the code.)
llm: PRRT_kwDOSUeMrM6HQXGO -> author (A reviewer asked a direct question about how instrumentation would know about prompt variables, so the PR author needs to जवाब/clarify.)
llm: PRRT_kwDOSUeMrM6HQbrq -> author (A reviewer asked for a documentation change and no author reply is present, so the PR author needs to update the file or respond.)

PR #173
llm: pr-conversation -> author (The reviewer identified a CI snapshot mismatch and explicitly said investigation is needed before landing, so the PR author needs to act on the scenario/update.)

PR #164
llm: PRRT_kwDOSUeMrM6C-3Kb -> author (A reviewer asked for clarification and questioned the need for a new metric, so the PR author needs to जवाब/respond or update the PR.)
llm: pr-conversation -> author (The latest comment is from a reviewer/approver and challenges the current proposal, so the author needs to respond or revise the PR.)

PR #162
llm: PRRT_kwDOSUeMrM6GRukM -> author (A reviewer asked whether the reference should also be added to the operation duration metric, so the author needs to जवाब/respond or make the change.)
llm: PRRT_kwDOSUeMrM6H5YA_ -> author (A reviewer requested a change to the condition note format, and there is no follow-up reply yet, so the author needs to update the PR.)

PR #144
llm: PRRT_kwDOSUeMrM6BMiXX -> author (The reviewer raised a concrete issue and requested either a validator or a wording change, so the author needs to respond or make the change.)
llm: PRRT_kwDOSUeMrM6HgmeM -> none (The only comment is a reviewer explanation with no request for follow-up, so no one needs to act on this thread.)

PR #143
llm: PRRT_kwDOSUeMrM6F1Aqk -> author (The latest comment is from a reviewer and is not a closing acknowledgement; it adds context about #144, so the author still needs to respond or act.)
llm: PRRT_kwDOSUeMrM6F0-FD -> author (The latest comment is a reviewer request to add reference scenarios for FilePart and UriPart, so the PR author needs to act.)

PR #112
llm: pr-conversation -> external (The reviewer says the change cannot work until google-adk relaxes its google-genai dependency and is bumped, so the thread is blocked on an upstream release outside this repository.)

```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

