> [!NOTE]
> Open non-draft PRs grouped by who is expected to act next. Draft PRs are listed separately. The grouping is partly performed by an LLM ([source](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/.github/scripts/pull-request-dashboard/dashboard.py)) and could contain mistakes.

## Waiting on maintainers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [Clarify that billed token counts should be reported for Cohere usage (#211)](https://github.com/open-telemetry/semantic-conventions-genai/pull/211) ✅ | trask |  | ✅ | ✅ | 3d |
| [Generalize the `gen_ai.provider.name` description (#212)](https://github.com/open-telemetry/semantic-conventions-genai/pull/212) ✅ | trask |  | ✅ | ✅ | 3d |
| [Relax `gen_ai.provider.name` on `gen_ai.client.operation.duration` to Conditionally Required (#214)](https://github.com/open-telemetry/semantic-conventions-genai/pull/214) ✅ | trask |  | ✅ | ✅ | 3d |
| [Clarify GenAI span duration (#216)](https://github.com/open-telemetry/semantic-conventions-genai/pull/216) ✅ | trask |  | ✅ | ✅ | 3d |
| [Clarify GenAI conversation ID fallbacks (#219)](https://github.com/open-telemetry/semantic-conventions-genai/pull/219) ✅ | trask |  | ✅ | ✅ | 2d |
| [Change `gen_ai.request.top_k` type to int and split out `gen_ai.retrieval.top_k` (#217)](https://github.com/open-telemetry/semantic-conventions-genai/pull/217) ✅ | trask |  | ✅ | ✅ | 2d |
| [Fix automated Copilot review guidance (#222)](https://github.com/open-telemetry/semantic-conventions-genai/pull/222) ✅ | trask |  | ✅ | ✅ | 2d |

## Waiting on approvers

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: model agent-to-agent handoff as execute_tool span (#98)](https://github.com/open-telemetry/semantic-conventions-genai/pull/98) | Krishnachaitanyakc | lmolkova | ✅ | ✅ | 4d |
| [semconv for a2a protocol (#195)](https://github.com/open-telemetry/semantic-conventions-genai/pull/195) | eternalcuriouslearner |  | ✅ | ✅ | 2d |
| [Update dependency aqua:grafana/flint to v0.22.4 (#227)](https://github.com/open-telemetry/semantic-conventions-genai/pull/227) | app/renovate |  | ✅ | ✅ | 9h |
| [semconv for compaction (#162)](https://github.com/open-telemetry/semantic-conventions-genai/pull/162) | eternalcuriouslearner | lmolkova, JWinermaSplunk | ✅ | ✅ | 6h |

## Waiting on authors

| PR | Author | Assignees | CI | Conflicts | Age |
|---|---|---|:---:|:---:|:---:|
| [gen-ai: add optional byte_size to multimodal content parts (#143)](https://github.com/open-telemetry/semantic-conventions-genai/pull/143) | Mandark-droid |  | ✅ | ❌ | 20d |
| [gen-ai: make multimodal content optional and add stripped_reason (#144)](https://github.com/open-telemetry/semantic-conventions-genai/pull/144) | Mandark-droid |  | ✅ | ❌ | 20d |
| [Add gen_ai.server.inter_token_latency metric (#164)](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) | Jwrede |  | ✅ | ❌ | 13d |
| [Update dependency google-genai to v2 (#112)](https://github.com/open-telemetry/semantic-conventions-genai/pull/112) ✅ | app/renovate |  | ❌ | ✅ | 12d |
| [gen-ai: add evaluation operation name and gen_ai.evaluate.internal span (#185)](https://github.com/open-telemetry/semantic-conventions-genai/pull/185) | hippoley |  | ❌ | ✅ | 11d |
| [Add experimental GenAI context selection event (#190)](https://github.com/open-telemetry/semantic-conventions-genai/pull/190) | caioribeiroclw-pixel |  | ❌ | ✅ | 9d |
| [Add prompt versioning and variable support to GenAI attributes (#179)](https://github.com/open-telemetry/semantic-conventions-genai/pull/179) | steverao | lmolkova | ✅ | ✅ | 9d |
| [Update dependency google-adk to v2 (#173)](https://github.com/open-telemetry/semantic-conventions-genai/pull/173) | app/renovate |  | ❌ | ✅ | 4d |
| [Add gen_ai.agent.request.size and gen_ai.agent.response.size metrics (#202)](https://github.com/open-telemetry/semantic-conventions-genai/pull/202) | pvlsirotkin |  | ✅ | ✅ | 4d |
| [Add gen_ai.workflow.steps metric (#203)](https://github.com/open-telemetry/semantic-conventions-genai/pull/203) | pvlsirotkin |  | ✅ | ✅ | 4d |
| [Add gen_ai.agent.invocation.duration and gen_ai.tool.execution.duration metrics (#201)](https://github.com/open-telemetry/semantic-conventions-genai/pull/201) | pvlsirotkin |  | ✅ | ✅ | 3d |
| [gen-ai: add gen_ai.response.id to deepeval evaluation result event (#184)](https://github.com/open-telemetry/semantic-conventions-genai/pull/184) | hippoley |  | ✅ | ✅ | 3d |
| [Add workflow node convention (#188)](https://github.com/open-telemetry/semantic-conventions-genai/pull/188) | RKest |  | ✅ | ❌ | 1d |
| [Add modality, cache, and phase breakdowns for token usage (#197)](https://github.com/open-telemetry/semantic-conventions-genai/pull/197) | trask | lmolkova | ✅ | ✅ | 1d |
| [Clarify scope of `gen_ai.client.operation.duration` metric (#215)](https://github.com/open-telemetry/semantic-conventions-genai/pull/215) | trask |  | ✅ | ✅ | 12h |
| [Replace Jupiter notebook with models with python file and add CI check that json schemas are up-to-date (#226)](https://github.com/open-telemetry/semantic-conventions-genai/pull/226) | lmolkova |  | ✅ | ✅ | 7h |
| [Clarify MCP context propagation (#220)](https://github.com/open-telemetry/semantic-conventions-genai/pull/220) ✅ | trask |  | ✅ | ✅ | 17m |

## Draft pull requests

| PR | Author | Updated |
|---|---|:---:|
| [proposal: agent.threat.detection.* attributes + event (closes #132) (#165)](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) | eeee2345 | 9d |
| [genai: add `gen_ai.token.cache` and `gen_ai.token.reasoning` metric attributes (#96)](https://github.com/open-telemetry/semantic-conventions-genai/pull/96) | Nik-Reddy | 2d |

<details>
<summary>Diagnostics</summary>

```text
PR #226
llm: PRRT_kwDOSUeMrM6F-lOV -> author (The reviewer raised a docstring issue, and the author replied that they will update it in a follow-up, so the author still has the next action.)

PR #220
llm: PRRT_kwDOSUeMrM6GEcAk -> author (Reviewer asked whether other keys should be prefixed; the author needs to जवाब/adjust the docs.)

PR #215
llm: PRRT_kwDOSUeMrM6Fl7mu -> author (Latest reviewer comment continues the design discussion and leaves an open choice on metric naming/bucketing, so the PR author needs to respond or implement a direction.)

PR #203
llm: PRRT_kwDOSUeMrM6FJXxu -> author (A reviewer flagged inconsistent wording and requested standardization; the PR author needs to update the metric text.)
llm: PRRT_kwDOSUeMrM6F5cXU -> author (The reviewer asked for a more concrete definition of "step" and suggested possible convention changes, so the author needs to respond or update the PR.)

PR #202
llm: PRRT_kwDOSUeMrM6FJWY9 -> author (The reviewer asked to standardize the wording in `model/gen-ai/metrics.yaml`, so the PR author needs to make the text change and reply.)
llm: PRRT_kwDOSUeMrM6FJWZf -> author (Reviewer asked to standardize the user-facing phrasing in `model/gen-ai/metrics.yaml`, so the PR author needs to update the text or respond.)
llm: PRRT_kwDOSUeMrM6F5gYd -> author (Reviewer asked for a refinement and there is no author reply yet, so the author needs to respond or update the docs.)

PR #201
llm: PRRT_kwDOSUeMrM6FYxtF -> author (The reviewer raised a clarification request, and the author replied that they will add the missing explanation, so the author still has the next action.)
llm: PRRT_kwDOSUeMrM6FY1gg -> reviewer (The author replied with a proposal and a question, leaving the ball with the reviewer to confirm whether `recommended` or `required` is acceptable.)
llm: PRRT_kwDOSUeMrM6FY5Vy -> reviewer (The reviewer asked for an additional attribute, and the author replied that it was added; the next step is for the reviewer/maintainer to verify or acknowledge the change.)
llm: PRRT_kwDOSUeMrM6FY3VY -> reviewer (The author replied with a question and requested alignment on the approach, so the next action is for the reviewer/maintainer to clarify whether metric validation can be wired up or confirm the proposed path.)
llm: pr-conversation -> author (Reviewer requested fixes and no follow-up from the author is shown, so the author needs to respond or update the PR.)

PR #197
llm: PRRT_kwDOSUeMrM6E-Ear -> reviewer (The author answered the question and pointed to the added metric change, so the ball is back with the reviewer to confirm or continue review.)
llm: PRRT_kwDOSUeMrM6FkB2H -> author (Reviewer asked for specifics and added follow-up evidence; the ball is back with the PR author to respond to the modality question.)
llm: PRRT_kwDOSUeMrM6F1og7 -> none (The latest reviewer comment acknowledges the point and defers the change to later, with no action requested from the author or anyone else in this thread.)
llm: PRRT_kwDOSUeMrM6F1nUT -> author (The latest comment is from a reviewer/approver and asks a design question about whether to add phases, so the PR author needs to respond or update the proposal.)

PR #190
llm: PRRT_kwDOSUeMrM6EO3Gw -> author (The reviewer raised a wording inconsistency and asked to consider aligning it; no author reply is present, so the author needs to act.)
llm: pr-conversation -> author (Reviewer asked the PR author to fill out the template and sign the CLA, so the author needs to act next.)

PR #188
llm: PRRT_kwDOSUeMrM6EP5P6 -> reviewer (The reviewer asked where the behavior would come from; the author replied with concrete implementation and example evidence, so the ball is back with the reviewer to assess or respond.)
llm: PRRT_kwDOSUeMrM6EP9-D -> reviewer (The author replied with the requested investigation and scenario updates, so the ball is back with the reviewer to review or respond.)
llm: PRRT_kwDOSUeMrM6F5pCw -> author (A reviewer asked a question and passed the ball to the PR author to confirm or respond.)

PR #185
llm: PRRT_kwDOSUeMrM6DuuPn -> author (The reviewer raised a substantive naming inconsistency and asked for alignment, so the PR author needs to respond or make a change.)
llm: PRRT_kwDOSUeMrM6E_Amb -> author (A reviewer requested a concrete change (“we need a verb here”), so the PR author needs to update the line and reply.)
llm: PRRT_kwDOSUeMrM6E_COY -> author (The reviewer asked for clarification and a prototype, and there is no author reply yet, so the author needs to respond.)
llm: pr-conversation -> author (The only comment is from a reviewer and presents a design idea about linking evaluation results to spans; it isn’t an acknowledgement or closing remark, so the author should respond.)

PR #184
llm: pr-conversation -> author (A reviewer issued a changes-requested review noting changes were lost in a force-push, so the author needs to update the PR and respond.)

PR #179
llm: PRRT_kwDOSUeMrM6EP0dp -> author (Reviewer asked to add reference scenarios for supported APIs, so the PR author needs to implement or respond.)
llm: pr-conversation -> author (A reviewer asked the PR author to update the PR body and template, so the ball is with the author.)

PR #173
llm: pr-conversation -> author (The latest reviewer comment reports a CI snapshot mismatch and explicitly asks for investigation/update before the PR can land, so the author needs to act next.)

PR #164
llm: PRRT_kwDOSUeMrM6C-3Kb -> author (Reviewer asked for justification and suggested changing the metric definition; the author needs to respond or adjust the PR.)
llm: pr-conversation -> author (The reviewer clarified the requested direction, so the author needs to update the metric description or respond to that feedback.)

PR #144
llm: PRRT_kwDOSUeMrM6BMiXX -> author (A reviewer flagged a runtime/schema mismatch and asked the author to either add validation or reword the constraint; no author reply has resolved it yet.)
llm: PRRT_kwDOSUeMrM6F1EMU -> author (The reviewer asked the PR author to split this work into a separate PR and narrow the current PR’s scope, so the author needs to respond or make the requested change.)

PR #143
llm: PRRT_kwDOSUeMrM6BMbLE -> author (Reviewer requested a reference scenario update for the docs convention change, so the PR author needs to add it or respond.)
llm: PRRT_kwDOSUeMrM6F0-FD -> author (A reviewer asked how instrumentation would capture `FilePart` and `UriPart`, so the PR author needs to जवाब/implement or clarify.)
llm: PRRT_kwDOSUeMrM6F1BCw -> none (The only comment is a reviewer thumbs-up with no follow-up request, so the thread is effectively closed.)
llm: PRRT_kwDOSUeMrM6F1Aqk -> author (The last comment is from the reviewer/approver and it explains the concern rather than closing it, so the author needs to respond or adjust the PR.)

PR #112
llm: pr-conversation -> author (Reviewer requested changes: the PR depends on google-adk relaxing its google-genai constraint and then bumping google-adk, so the author needs to update the PR or wait on that dependency.)

PR #98
llm: PRRT_kwDOSUeMrM6E9NFw -> reviewer (The author has already responded to the reviewer’s question with a substantive explanation; the ball is back with the reviewer to confirm, object, or close the thread.)

```

</details>

_Approvers may [force a refresh](https://github.com/open-telemetry/semantic-conventions-genai/actions/workflows/pull-request-dashboard.yml)._

