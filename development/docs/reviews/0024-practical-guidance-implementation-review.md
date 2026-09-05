# Independent practical-guidance implementation review

Date: 2026-09-05. User request: ask Astra and Fable to review the implemented PLAN-0007. Both received the same self-contained consultation independently, with no previous adviser answers. This is implementation review, not a repeat of the Plan review.

## Reviewed state and reviewer identity

Repository HEAD: `daca8892cfb19c321e717b8c627af2987b9e1fff`; the implementation is uncommitted. The runtime's reviewed source/build manifest is `1F2CD88F80964FC6ED71C6B4A346A93322B9818FE3B9471DFF466074AF7840CE`. The consultation, source diff, 54-file hash inventory, original implementation report, Fable adapter response and structured Astra record are retained under `Z:/Projekts/AI/output/scoville-design-plan-0007-implementation-review/`. The coordinator verified zero drift across those 54 files before recording this review. The original report is preserved as `reviewed-implementation.md` before adding a dated review notice to the current report.

| Adviser | Requested configuration | Result |
| --- | --- | --- |
| Astra | `gpt-6-astra`, `xhigh`, fresh context, `/root/astra_implementation_0007_review` | **Not ready for complete PLAN-0007 closure.** No confirmed blocker in the 23 runtime texts; one required evidence gap and one small artifact defect. |
| Fable | `claude-fable-5-1`, `high`, new persistent session `b52ad620-4148-4cfb-93a9-59a84f35e6b7`, customizations disabled | **Ready with minor changes.** Runtime text acceptable; narrow two coverage claims and clarify evidence/cost reporting. |

Fable's adapter reports `reported_model: null`, so requested identity is not independent backend identification. It completed successfully in 538,511ms, 78 turns, with cost USD 5.85968425 and no permission denials. The skill's USD10 ceiling was not raised. Astra used the host subagent, not a separately sandboxed runtime. The complete Fable answer is in `fable.json`; the complete Astra reply remains in the task conversation, with a faithful structured record in `astra.md`.

Consultation outcome: **complete**, meaning both advisers returned answers. This does not mean both approved the existing completion claim.

## Astra findings and coordinator verification

### A1 — P2: required coupled typesetting operation is unexercised

Confirmed independently by the coordinator. The new [Typography operation](../../../scoville-design-anti-ai-slop/references/typography-and-typesetting.md:103) compares a narrower measure at unchanged size, then considers leading and retains the original setting. The PG-02 candidate instead declares `body and caption family only`; its two settings hold size18px, leading29px and measure648px constant (`output/design-plan7-trials/PG-02/candidate/main.html:19,65`). The baseline likewise holds its setting dimensions constant. The font substitution and family comparison are real; they do not demonstrate the additional measure/leading operation required by contract row04 and W-001.

Smallest adequate next action: preserve PG-02 and freeze an explicit narrow PG-02 supplement with identical exact text and paragraph count in both arms. Exercise measure at constant size, a reasoned leading decision, and the untouched setting alongside. Use the agreed P1 baseline/candidate sequence; evaluate only the missing subquestion. Until then that subquestion is **unverified**. The original repetition ambiguity is disclosed, not a second confirmed content violation.

### A2 — P3: Waiting carries a continue instruction

Confirmed in source and the saved screenshot. `output/design-plan7-trials/PG-11/candidate/main.html:25` leaves “A clear signal to continue.” visible below Waiting; `output/playwright/design-plan7/followup-v2/PG-11-candidate-status-100.png` shows both together. This is an artifact-level semantic inconsistency; the actual animation, interruption and final-state evidence still exists. No Motion instruction defect is established.

Smallest adequate next action: make a separately named coordinator derivative with a neutral, removed or state-dependent subtitle, then capture Waiting and Ready. Preserve the original and identify the correction as coordinator work. No new provider run is needed for this fix.

## Fable findings and coordinator verification

| Finding | Verified disposition |
| --- | --- |
| F1: PG-02 does not exercise coupled size/measure/leading | Confirmed; agrees with A1. Fable suggests narrowing the report/acceptance or adding PG-02S. The coordinator rejects retroactively weakening the started Work Item's authored acceptance: a reporting caveat cannot discharge its required P1 subquestion. This is the substantive reason for adopting Astra's more conservative closure judgment. |
| F2: PG-06 reports zero candidate reasoning tokens versus 773 baseline | Counts confirmed in both receipts and the candidate's final `events.jsonl` usage event. Both requested effort `high`. Record this as **reported reasoning-token asymmetry**, not a confirmed change in configured effort or proof that no reasoning occurred. Its causal relation to the axis-fill defect is unknown. No unchanged-result rerun is justified. |
| F3: size reporting should distinguish targets and ceilings | Confirmed with a numerical correction: three leaves and **17**, not Fable's 15, declared common loads newly exceed their advisory ceilings. Baseline common-load exceedances were zero. All remain advisory; this is no structural validation failure. No threshold change or extra ADR is necessary merely to report the existing result honestly. |
| F4: no paired case establishes an improvement | Accept the narrow meaning: no demonstrated beneficial arm difference attributable to the added text. Do not adopt the literal claim that there was no arm difference; PG-06 has a candidate-only render defect and PG-02 differs in repetition. Successful baseline outputs and useful explicit instruction are not causal improvement evidence. |
| F5: Cartography covers point labels, while the original audit also proposed line/area labels | Confirmed. Audit row09 explicitly mentions distinguishing point, line and area labeling. The new procedure, Esri supplement and PG-08 demonstrate point-label placement across scales; the reviewed contract wording is less explicit about feature classes. Record **point-label application only; line/area-specific guidance and application not established here**, rather than treating the whole audit suggestion as demonstrated. Resolve that scope disposition explicitly in follow-up; do not infer a defect in the correct point-label guidance. |
| F6: Fable could not verify Adobe after two timeouts | A reviewer coverage limit, not evidence that the source is invalid. Astra independently verified the relevant official Adobe mechanics; Fable verified Esri. Existing source records are not changed to claim a successful Fable fetch. |
| F7: all retained texts were final before the last candidate; none revised | Not a confirmed defect. The observations do not require an arbitrary revision count or prove all texts were written before any inspection. Retain/revise/omit is a decision, not a quota. No instruction defect requiring a text revision was demonstrated. The thematic overlap between the lending-desk teaching fragment and PG-T1 is disclosed as Fable's concern; Brief was absent from PG-T1 exposure and no direct fixture reuse was established. |

Advisory leaf ceilings, from the actual YAML and token receipts:

| Leaf | Baseline | Candidate | Ceiling |
| --- | ---: | ---: | ---: |
| Composition | 1858 | 2134 | 2100 |
| Colour | 1827 | 2063 | 2000 |
| Imagery | 1926 | 2175 | 2100 |

The 17 common-load IDs are C01, C02, C04, C05, C07, C08, C09, C11, C12, C14, C17, C21, D28-EH1, D28-CI1, D28-CI2, D28-AD1 and D28-BO1. The existing overall result of 42 advisory notices remains correct. The thresholds were neither raised nor converted to hard gates.

## Strengths and coverage

Both reviewers support the practical runtime additions: owner-specific operations, restrained arithmetic, preserved legitimate conventions/expressive alternatives, no newly compulsory general record, and no confirmed runtime-text blocker. Both found PG-06's original error and separate repair honestly retained, and PG-12S's explicit coverage correction useful. Positive evidence includes actual shared-source crops, mark repair, exact panel symbols/coordinates, approach-dependent arrows, read-only critique, prototype edit/reload and sampled motion/reveal behavior. Neither adviser established general model superiority.

Astra read all 23 additions and diff context, Core, relevant Typography context, Plan/contract, scripts, freezes, source/implementation/build/token/check records. It independently hash-checked all 54 review-bound files, 28 prompt/answer/artifact records and 54 render records, plus PLAN-0006 W-004. It visually inspected representatives from every artifact family, several baselines/controls, PG-06 before/after, PG-12S, PG-T1 and sampled interaction/motion captures. It read PG-16. No new browser interaction, continuous video playback, provider execution or test rerun occurred.

Fable read the full diff, Plan/contract/report, evaluation scripts, trial/check/token/final-build records, Core, selected audit sections and budget policy. It inspected 21 PNGs, the follow-up runtime receipt, selected answers and PG-06 source. Its explicit unchecked areas include videos, raw event transcripts, several baseline/control variants, PG-T1 720/1000/control, direct PLAN-0006/PROJECT_INDEX inspection, baseline build and runtime bytes. Fable's source/build parity statements rely on supplied records/code; they are not independent hash execution. Its tools did not run scripts. Neither reviewer saw the other's response.

## Current conclusion and follow-up

The 23 changes are supported as useful practical instructions. The stronger statement that every required mechanism is fully evidenced and PLAN-0007 has no remaining local evidence gap is **not confirmed**. The original technical checks still passed, but do not resolve A1. The coordinator's earlier blanket completion statement was too broad.

Open actions are A1's targeted P1 typesetting evidence, A2's bounded artifact correction, and explicit handling of the narrower Cartography scope. This review also supplies the corrected token-cost and reasoning-usage qualifications above. No runtime instruction, acceptance criterion, original trial or package byte was changed during this review. No new evaluation/provider generation, installation or publication is represented as completed. The historical Plan remains as reviewed; this follow-up record and the report's dated notice make the challenged closure and concrete remaining actions visible without silently rewriting earlier evidence.
