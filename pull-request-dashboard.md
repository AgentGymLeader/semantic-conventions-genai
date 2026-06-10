> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.
>
> Reviewers column: ✅ approved · ✔️ approved (non-code-owner) · 💬 open thread · 🔴 changes requested.

## Waiting on reviewers

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-adk to v2 (#173)](https://github.com/open-telemetry/semantic-conventions-genai/pull/173) | app/renovate | MikeGoldsmith | ❌ | ✅ | 22d |
| [Clarify scope of `gen_ai.client.operation.duration` metric (#215)](https://github.com/open-telemetry/semantic-conventions-genai/pull/215) | trask | lmolkova | ✅ | ❌ | 12d |
| [Add gen_ai.agent.invocation.id attribute for invoke_agent spans (#250)](https://github.com/open-telemetry/semantic-conventions-genai/pull/250) | singankit | lmolkova&nbsp;💬<br>MikeGoldsmith&nbsp;🔴 | ✅ | ❌ | 5d |
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova<br>MikeGoldsmith&nbsp;✅<br>trask | ✅ | ❌ | 1d |
| [Add `gen_ai.request.reasoning.level` attribute (#258)](https://github.com/open-telemetry/semantic-conventions-genai/pull/258) | katsuhisa91 | JWinermaSplunk&nbsp;✅<br>lmolkova | ✅ | ❌ | 16h |
| [Add gen_ai.agent.request.size and gen_ai.agent.response.size metrics (#202)](https://github.com/open-telemetry/semantic-conventions-genai/pull/202) | pvlsirotkin | lmolkova<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ❌ | 2h |
| [Add gen_ai.workflow.steps metric (#203)](https://github.com/open-telemetry/semantic-conventions-genai/pull/203) | pvlsirotkin | aabmass&nbsp;✅<br>lmolkova<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ❌ | 1h |
| [Remove obsolete split model docs helper (#278)](https://github.com/open-telemetry/semantic-conventions-genai/pull/278) | trask | lmolkova&nbsp;✅ | ✅ | ✅ | 40m |
| [Filter Slack reviewer notifications (#279)](https://github.com/open-telemetry/semantic-conventions-genai/pull/279) | trask | lmolkova&nbsp;✅ | ✅ | ✅ | 39m |

## Waiting on authors

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: make input-messages BlobPart content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid | Copilot&nbsp;💬<br>lmolkova<br>trask | ✅ | ❌ | 29d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede | Cirilla-zmh<br>lmolkova&nbsp;💬 | ✅ | ❌ | 22d |
| [gen-ai: add evaluation operation name and gen_ai.evaluate.internal span (#185)](https://github.com/open-telemetry/semantic-conventions-genai/pull/185) | hippoley | Cirilla-zmh&nbsp;💬<br>Copilot&nbsp;💬<br>singankit&nbsp;💬 | ❌ | ✅ | 20d |
| [Add experimental GenAI context selection event (#190)](https://github.com/open-telemetry/semantic-conventions-genai/pull/190) | caioribeiroclw-pixel | Copilot&nbsp;💬<br>trask | ❌ | ❌ | 18d |
| [gen-ai: add gen_ai.response.id to deepeval evaluation result event (#184)](https://github.com/open-telemetry/semantic-conventions-genai/pull/184) | hippoley | lmolkova&nbsp;✅<br>MikeGoldsmith&nbsp;🔴<br>trask | ✅ | ✅ | 13d |
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid | Cirilla-zmh<br>trask&nbsp;💬 | ✅ | ❌ | 11d |
| [Add modality, cache, and phase breakdowns for token usage (#197)](https://github.com/open-telemetry/semantic-conventions-genai/pull/197) | trask | alexmojaki&nbsp;💬<br>lmolkova&nbsp;💬<br>Nik-Reddy&nbsp;💬 | ✅ | ❌ | 10d |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) | eternalcuriouslearner | Copilot&nbsp;💬<br>JWinermaSplunk&nbsp;✅<br>lmolkova&nbsp;💬⁠✅<br>trask | ✅ | ❌ | 8d |
| [Add gen_ai.invoke_agent.server span (SERVER kind) (#252)](https://github.com/open-telemetry/semantic-conventions-genai/pull/252) | singankit | Cirilla-zmh&nbsp;💬<br>Copilot&nbsp;💬 | ✅ | ❌ | 5d |
| [Add prompt versioning and variable support to GenAI attributes (#179)](https://github.com/open-telemetry/semantic-conventions-genai/pull/179) | steverao | lmolkova&nbsp;💬<br>trask | ✅ | ❌ | 5d |
| [Limit supported  part types  on `gen_ai.system_instructions` to text only (#257)](https://github.com/open-telemetry/semantic-conventions-genai/pull/257) | lmolkova | MikeGoldsmith&nbsp;✅ | ✅ | ❌ | 2d |
| [Add workflow node convention (#188)](https://github.com/open-telemetry/semantic-conventions-genai/pull/188) | RKest | aabmass&nbsp;💬<br>lmolkova&nbsp;🔴<br>trask&nbsp;💬 | ✅ | ❌ | 1d |
| [Add gen_ai.agent.invocation.duration and gen_ai.tool.execution.duration metrics (#201)](https://github.com/open-telemetry/semantic-conventions-genai/pull/201) | pvlsirotkin | lmolkova&nbsp;💬<br>MikeGoldsmith&nbsp;🔴 | ✅ | ❌ | 1d |
| [semconv for a2a protocol (#195)](https://github.com/open-telemetry/semantic-conventions-genai/pull/195) | eternalcuriouslearner | aabmass<br>JWinermaSplunk<br>trask | ✅ | ❌ | 1d |
| [Add `gen_ai.agent.finish_reason` attribute for agent loop termination (#238)](https://github.com/open-telemetry/semantic-conventions-genai/pull/238) | Nik-Reddy | aabmass&nbsp;✅<br>MikeGoldsmith&nbsp;✅<br>trask | ✅ | ❌ | 20h |
| [gen-ai: add run guardrail span and security finding (#262)](https://github.com/open-telemetry/semantic-conventions-genai/pull/262) | nagkumar91 | aabmass<br>Copilot&nbsp;💬 | ✅ | ❌ | 19h |
| [Propose GenAI agent entity (#270)](https://github.com/open-telemetry/semantic-conventions-genai/pull/270) | aabmass | Copilot&nbsp;💬<br>lmolkova&nbsp;💬 | ✅ | ❌ | 17h |

## Waiting on external

| PR | Author | Reviewers | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) | app/renovate | lmolkova&nbsp;✅ | ❌ | ✅ | 22d |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 18d |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | 12d |
| [Add time_budget value for gen_ai.agent.finish_reason (#267)](https://github.com/open-telemetry/semantic-conventions-genai/pull/267) | Nik-Reddy | 1d |

<details>
<summary>Diagnostics</summary>

```text
PR #270
llm: PRRT_kwDOSUeMrM6IUWvu -> reviewer (The author replied with a follow-up question about using `entity_associations`, so the ball is back with the reviewer to answer/confirm.)
llm: PRRT_kwDOSUeMrM6IW2DR -> author (The reviewer flagged a bug in `snippet.md.j2`; there’s no author reply yet, so the author needs to fix or respond.)
llm: PRRT_kwDOSUeMrM6IW2De -> author (A reviewer flagged a likely config issue (`template:` vs `pattern:`) and there’s no author reply yet, so the author needs to act.)
llm: PRRT_kwDOSUeMrM6IW2Dq -> author (A reviewer pointed out a config inconsistency and suggested changing `template:` to `pattern:`, so the PR author needs to update the file or respond.)
llm: PRRT_kwDOSUeMrM6IW2Dx -> author (A reviewer flagged a mismatch between the PR description and the actual files, asking for the page/generation rule or a description update; the author needs to respond or fix it.)
llm: pr-conversation -> author (A reviewer asked for bundling the changes together, so the author needs to respond or adjust the PR.)

PR #262
llm: PRRT_kwDOSUeMrM6ISkfg -> author (A reviewer requested a link change and there is no author reply yet, so the next action is on the PR author to update the reference or respond.)
llm: PRRT_kwDOSUeMrM6ISkgL -> author (A reviewer pointed out a likely KeyError and suggested a code change; the author needs to update the scenario or respond.)
llm: PRRT_kwDOSUeMrM6ISkge -> author (The reviewer pointed out a potential semantic-convention violation and asked for a code change; no author reply closed the thread.)
llm: PRRT_kwDOSUeMrM6ISkgy -> author (A reviewer raised a requested change/safety concern and there is no author reply yet, so the PR author needs to act.)
llm: PRRT_kwDOSUeMrM6ISkhF -> author (A reviewer requested a code change: use `span_kind` as the primary signal and fall back to `server.*` attributes only when needed.)

PR #257
llm: pr-conversation -> author (The last comment is from a reviewer/approver and includes requested follow-up changes to scenarios and `SystemInstructionPart`, so the author needs to act.)

PR #252
llm: PRRT_kwDOSUeMrM6HO1Cy -> author (Reviewer asked for additional reference scenario coverage and regenerated outputs; the author needs to implement and respond.)
llm: PRRT_kwDOSUeMrM6IKVVh -> author (A reviewer left a suggestion with no follow-up reply yet, so the author needs to apply or respond to it.)

PR #250
llm: PRRT_kwDOSUeMrM6HQjux -> reviewer (The author replied with a proposed interpretation and supporting example, so the thread is now waiting on the reviewer to confirm or push back.)
llm: pr-conversation -> reviewer (The author responded with a rationale for keeping `invoke_agent.common`, so the ball is back with the reviewer to accept that direction or continue the review.)

PR #238
llm: pr-conversation -> author (Latest comment is a reviewer’s substantive reply supporting the scoped approach, answering the author’s question and leaving the ball with the author if they want to proceed or follow up.)

PR #215
llm: PRRT_kwDOSUeMrM6Fl7mu -> none (The latest comment is a reviewer acknowledgement that the clarification is directionally aligned and does not ask for further action.)

PR #203
llm: PRRT_kwDOSUeMrM6HGVHV -> reviewer (The author answered by saying they moved the recommendation into the YAML note, so the next step is for the reviewer to confirm or close the thread.)
llm: PRRT_kwDOSUeMrM6HGVko -> reviewer (The reviewer asked for an `attributes.gen_ai.error` reference, and the author replied "Added."; the ball is now with the reviewer to confirm/resolve.)
llm: PRRT_kwDOSUeMrM6HGaQ9 -> reviewer (The author answered the question and clarified the note; the reviewer now needs to confirm or close the thread.)
llm: pr-conversation -> reviewer (The author posted a substantive update with new changes and no follow-up question, so the ball is back with the reviewers to re-check the revised PR.)

PR #202
llm: PRRT_kwDOSUeMrM6HFBTV -> reviewer (The author has replied with a decision and rationale, so the ball is back with the reviewer to accept it, push back, or resolve the thread.)

PR #201
llm: PRRT_kwDOSUeMrM6FY1gg -> reviewer (The author replied with a proposal and a question (“Would recommended work…?”), so the thread is back with the reviewer to answer or approve the level.)
llm: PRRT_kwDOSUeMrM6FY3VY -> reviewer (The author’s last comment asks for clarification and alignment on how to proceed, so the reviewer/maintainer needs to जवाब/confirm the approach.)
llm: PRRT_kwDOSUeMrM6H95-W -> external (The reviewer is waiting for a naming decision to be confirmed on the GenAI call and will update the thread afterward, so progress is blocked on an external discussion.)
llm: PRRT_kwDOSUeMrM6H9_Oc -> author (The reviewer suggested aligning the metric name and explicitly left the implementation choice to this PR, so the author needs to respond or update the change.)

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
llm: pr-conversation -> author (The latest comment is from the author and says they will come back with a plan to split the work, so the thread is still waiting on the author.)

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

