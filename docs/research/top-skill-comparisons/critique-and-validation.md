# Stage-2 GitHub Skill comparison: critique and validation

**Capture:** 2026-09-02T13:47:00Z  
**Decision served:** identify the three most-starred current, qualifying exact-domain Skills with E1+ evidence for visual/design critique, audit, repair, and validation; compare them with [the current executable](../../../references/critique-and-validation.md) and [the expert-depth audit](../reference-audits/critique-and-validation.md).  
**Ranking rule:** stars rank repositories only after exact-domain and evidence qualification. Popularity, evidence strength, visible craft, finding validity, disagreement handling, and licence safety remain separate.  
**Adoption lens:** [adoption-priority.md](../adoption-priority.md), prioritizing visible typography, spacing/rhythm, negative space, hierarchy, subject-specific composition, controlled before/after evidence, and localized causal findings.

## Result

Three qualifying repositories were found in the bounded current search.

| Rank by current stars | Repository and exact Skill | Stars at capture | Evidence level | What the evidence actually establishes |
|---:|---|---:|---|---|
| 1 | [mohitagw15856/pm-claude-skills — `figma-design-critique-pm`](https://github.com/mohitagw15856/pm-claude-skills/blob/aa71bee8d20b7febdfd49f3aa96f26f316344628/skills/figma-design-critique-pm/SKILL.md) | 1,330 | **E1 textual** | A committed example shows the requested goal-alignment, observation, impact, evidence-basis, and designer-question output. It does not include the reviewed screen, stable locations, executed repair, or visual proof. |
| 2 | [jiahuiqu17/paper-signal — `paper-signal-audit`](https://github.com/jiahuiqu17/paper-signal/blob/7567ff05f93fe525bf886b3a0dce36903ab8c43b/skills/paper-signal-audit/SKILL.md) | 108 | **E2 contract / E1 visual** | Committed poster outputs, QA/preservation records, manifests, route cases, schemas, validators, and a runnable eval harness support a narrow image-audit and targeted-regeneration workflow. Human outcome evidence remains self-authored and style-specific. |
| 3 | [KyaniteLabs/tastecheck — `tastecheck-pass`](https://github.com/KyaniteLabs/tastecheck/blob/b3cb1155e076feb6176ee210eb62f3b03363337a/skills/tastecheck-pass/SKILL.md) | 7 | **E2 contract / E1 visual, effectiveness blocked** | Inspectable before/after and responsive artifacts plus deterministic evidence-ledger/gate machinery exist. The repository's own paired/diversity receipts fail because judged runs are absent; it explicitly does not establish effectiveness. |

Popularity and evidence diverge sharply. Rank 1 demonstrates a useful critique output schema but no visual artifact. Rank 2 has the strongest artifact-grounded finding/repair loop. Rank 3 has the most explicit fail-closed evidence and disagreement infrastructure, while its own negative receipts prevent an effectiveness claim. None combines stable cross-medium localization, ADR-0007 verdicts, separate severity/confidence, intent evidence, false-positive triage, parent-cause repair, controlled renders, preservation, and honest human disagreement.

## Search and qualification boundary

Authenticated GitHub code and repository search covered `design critique`, `visual audit`, `design review`, `critic`, `before after`, `repair validation`, `visual comparison`, `visual regression`, `preference`, `disagreement`, `finding`, `severity`, `confidence`, and `SKILL.md`. Exact Skill files, examples/outputs, screenshots, tests/evals, receipts, current metadata, path history, and licence/asset records were inspected at pinned commits.

Qualification required a directly usable instruction for visual/design critique, audit, repair, or release validation plus an inspectable example/output or reproducible deterministic evidence mechanism. Generic code review, plan review, registry mirrors, README claims, and design Skills with only a repository hero image were E0. A visual-diff tool without design finding or repair ownership was not substituted for a Critique Skill. The search is bounded, not globally exhaustive.

### High-star near-misses and exclusions

| Repository | Stars at capture | Why it was not ranked |
|---|---:|---|
| [anthropics/knowledge-work-plugins — design critique](https://github.com/anthropics/knowledge-work-plugins/blob/77961df00a4626bc3b83850064289decd5a3b977/design/skills/design-critique/SKILL.md) | 23,822 | Exact prose but E0: no Skill-scoped audit output, test, repair artifact, or evaluation was found. |
| [paperclipai/companies — plan design review](https://github.com/paperclipai/companies/tree/main/gstack/skills/plan-design-review) | 860 | Reviews implementation plans, not rendered design artifacts; domain mismatch. |
| [julianoczkowski/designer-skills — design review](https://github.com/julianoczkowski/designer-skills/blob/c259656c76d9758d7ead46b0d2f125cbe84f8665/design-review/SKILL.md) | 536 | Exact and operational, but no Skill-scoped critique report, annotated render, repair comparison, or test was committed. Repository hero art is not review evidence. |
| [vibeeval/vibecosystem — art director](https://github.com/vibeeval/vibecosystem/tree/main/skills/art-director) | 530 | Broad UI/design repository with extensive tests, but no inspected artifact tied to an exact design-critique Skill. Unrelated test volume cannot elevate critique evidence. |
| [coinbase/cds — design-to-code](https://github.com/coinbase/cds/tree/master/skills/cds-design-to-code) | 498 | Source-fidelity implementation guidance, not a general visual critique/repair lifecycle; no exact Skill output was inspected. |
| [metedata/pdf-proof](https://github.com/metedata/pdf-proof/blob/8ba4cf66645958d2b25eec874afe0a0442287b9e/SKILL.md) | 76 | Strong E1 coordinate-localized PDF value proof, but it validates exact text occurrences rather than design quality, cause, repair, or disagreement. Its locate→readback mechanism is useful prior art, not an exact-domain ranking substitute. |

## Rank 1 — PM Figma design critique

### Snapshot, state, licence, and evidence assets

- **Current snapshot:** [`aa71bee8d20b7febdfd49f3aa96f26f316344628`](https://github.com/mohitagw15856/pm-claude-skills/tree/aa71bee8d20b7febdfd49f3aa96f26f316344628), committed 2026-08-25T10:58:00Z.
- **Latest exact-Skill change:** `fb85a1cb552de8c6aac16eb143247791d53a7eff`, 2026-06-08T13:01:36Z.
- **State:** active; GitHub archived flag false.
- **Licence:** root MIT covers Skill and committed textual example. No separate data/asset licence applies to the inspected example; it is fictional output text. Repository-wide eval results are not attributed to this Skill and were not used as E2 evidence.

### Scope, mechanism, and actual proof

The Skill critiques a Figma design from a product-manager perspective. It requires user goal, business goal, requirements, metric, and constraints; then records goal alignment, a concrete observation, hypothesized user/business impact, evidence basis, and a question for the designer. The committed dashboard example visibly demonstrates that text structure and honestly labels one causal claim as a hypothesis.

The example does not include the source Figma frame or screenshot, so its statements about above-the-fold position, contrast, and missing context cannot be independently checked. It has no stable frame/element anchor, confidence, source version, repair artifact, controlled rerender, or regression evidence. E1 therefore covers output form/completeness only.

### Adoption-priority visual lens

There is no visible typography, spacing, negative-space, hierarchy, or composition evidence. The Skill intentionally excludes aesthetic critique, so it cannot improve Scoville's primary visual lens. Its outcome framing may reduce taste comments, but unsupported statements such as “this layout ... will reduce mobile conversion” can still convert reviewer inference into a behavioral fact.

### Better mechanism and original synthesis

Adapt the compact **goal/requirement → observation → conditional effect → evidence basis → owner question** chain. It improves the current leaf by forcing every consequential effect to name its basis and by making missing product evidence discussable rather than silently certain.

Reject fixed approval labels, “one primary recommendation” as a universal limit, business metrics as the default authority for visual work, automatic conversion claims, image-free critique of visible properties, and a PM-only boundary that suppresses type/spacing/composition when those are material.

## Rank 2 — Paper Signal Audit

### Snapshot, state, licence, and evidence assets

- **Current snapshot:** [`7567ff05f93fe525bf886b3a0dce36903ab8c43b`](https://github.com/jiahuiqu17/paper-signal/tree/7567ff05f93fe525bf886b3a0dce36903ab8c43b), committed 2026-08-12T03:30:23Z.
- **Latest exact-Skill change:** `56a28dc755210a100b5f0aaa4af9a3a64b2b15d5`, 2026-08-11T12:45:40Z.
- **State:** active; GitHub archived flag false.
- **Licence:** root MIT covers Skill, scripts, manifests, QA, and repository-authored generated documentation examples. Each example carries an asset record. The inspected Edinburgh selected output declares no source photograph or external reference, identifies built-in ImageGen, and records visible text. Other examples include generated or reference assets with their own provenance; MIT does not erase underlying third-party rights.

### Scope, mechanism, and actual proof

The exact Audit Skill inspects minimal-zine posters, photo restyles, editorial images, and series. It requires original-size and thumbnail review, preservation/manifest evidence, explicit route/composition mode, subject and text integrity, full-size craft inspection, series continuity, ranked findings, and one correction path per failed image. Repair changes one failure class, protects accepted subject/text/material/crop, and saves prompt/output as versioned siblings.

Committed outputs, earlier/selected versions, QA records, manifests, preservation records, schemas, validator tests, and a run/judge harness support E2 contract and E1 visual evidence. The harness deliberately requires reviewer-backed assertions rather than inferring success from filenames. The QA remains repository-authored; no independent professional panel or external adoption evidence was found.

### Adoption-priority visual lens

The inspected `Edinburgh After Rain` output demonstrates subject-specific photographic treatment, a strong low-page focal strip, active upper negative space, controlled two-tone hierarchy, sparse exact type, and an asymmetric crop. Other series examples provide composition variation rather than one generic card system. This is stronger visible craft evidence than the other ranked candidates.

The range is intentionally one narrow material/editorial language. Sparse monospaced labels, paper texture, single signal ink, and large quiet fields cannot become general style rules. Its finding table identifies an image but does not stably localize the region/element, separate severity from confidence, type intent evidence, support ADR-0007 verdicts, or preserve reviewer disagreement.

### Better mechanism and original synthesis

Adapt four mechanisms:

1. inspect **actual artifact at target detail plus a diagnostic thumbnail/sequence view**;
2. bind findings to protected subject/text/fact/crop/material records;
3. correct one parent failure class, version the prompt/output, and compare the sibling result;
4. make missing or incomplete series artifacts block a “validated” claim.

Original synthesis should generalize those mechanisms to stable medium-specific anchors and the shared Scoville finding record. Reject the style vocabulary, anti-AI motif blacklist as universal taste, three verdicts (`Pass`, `Pass with refinements`, `Regenerate`) as substitutes for ADR-0007, hard 9/12 scoring, fixed automatic-fail categories outside this product, “never patch with code” as a cross-medium law, and self-authored QA as independent proof.

## Rank 3 — TasteCheck Pass

### Snapshot, state, licence, and evidence assets

- **Current snapshot:** [`b3cb1155e076feb6176ee210eb62f3b03363337a`](https://github.com/KyaniteLabs/tastecheck/tree/b3cb1155e076feb6176ee210eb62f3b03363337a), committed 2026-08-08T01:12:38Z.
- **Latest exact-Skill change:** `0f45ca7f066922f229a77048791dc5d054415231`, 2026-07-13T22:27:37Z.
- **State:** active; GitHub archived flag false.
- **Licence:** root MIT covers Skills, tools, site code, samples, screenshots, and receipts. Bundled Hanken Grotesk/Bricolage fonts are OFL 1.1. Redaction font redistribution terms are not established in the repository and must be rechecked or the font replaced; font binaries must not be imported casually.

### Scope, mechanism, and actual proof

`tastecheck-pass` is a final rendered-frontend gate, not a free-form critique. It requires a real artifact/spec, a row per applicable check with `skill`, `check_id`, `status`, `reason`, `remediation`, `evidence`, and `provenance`, then a deterministic SHIP/HOLD verdict. Failures receive owner, repair, rerun, acceptance rule, and predecessor. Browser, zoom, keyboard, theme, reduced-motion, cold-load, and design-system checks remain separate rows.

The repository contains responsive screenshots, an inspectable generic before and editorial after, scripts/contracts, fixtures for fabricated evidence and insufficient quorum, immutable receipts, and deterministic validators. Crucially, its current summary reports zero paired records, failed paired/diversity gates, no judged lift, and effectiveness blocked. That honest negative result is stronger epistemic evidence than an unsupported success claim, but it supports the gate machinery—not design improvement.

### Adoption-priority visual lens

The before/after visibly improves subject specificity, typographic hierarchy, measure, grouping, edge logic, density, and negative-space use. The after uses a serif/sans/mono role system, large asymmetric headline, relational spacing, and topic-specific kitchen copy rather than a gradient/card template. These are inspectable examples, not proof that `tastecheck-pass` caused the result. The examples also embed one editorial house direction and do not test other subjects/media or disagreement over deliberate alternatives.

### Better mechanism and original synthesis

Adapt the **immutable evidence row + fail-closed missing evidence + owner/repair/rerun/acceptance** mechanism. Its fabricated-evidence, missing-quorum, tie, and synthesis-disagreement fixtures are useful models for preserving reviewer state and refusing consensus inflation. Also retain its explicit admission that failed or absent judged receipts block effectiveness.

Reject the mandatory 19-Skill dependency chain, SHIP/HOLD as the general critique verdict, fixed 320px/400% and specific release checks outside their governing standards/context, against-spec consistency as design quality, automatic baseline ownership, one editorial style as anti-generic truth, and a release gate that collapses domain findings into one owner.

## Comparative capability matrix

| Capability | Current Scoville reference + audit | PM Figma Critique | Paper Signal Audit | TasteCheck Pass |
|---|---|---|---|---|
| Target/evidence packet | Planned artifact/version, brief, medium, states, evidence, exclusions | Goals/requirements/metric; no frozen render | Manifest/preservation/actual images | Real artifact/spec/evidence rows |
| Localization | Planned global/system/local stable anchors with uncertainty | General screen concern; no stable anchor in example | Image-level only; visible observations | Check ID and evidence link, not region localization |
| Observation→effect→cause→repair | Full causal record planned | Observation→user/business effect→question; weak cause/repair proof | Observation→why→targeted correction; one failure class | Failure row→owner/repair/rerun/acceptance |
| Verdict/severity/confidence | ADR-0007 verdicts; separate severity/confidence/priority | On-track labels + impact; no confidence | Pass/regenerate + severity; no confidence | SHIP/HOLD + pass/fail; no critique verdict taxonomy |
| Intent/exception | Documented/inferred/unknown intent + conventional control | Constraints requested; no exception proof | Route/composition intent inferred or supplied | Against-spec orientation; exceptions weak |
| Preservation | Explicit frozen preservation set | What works, but not a repair contract | Strong subject/text/crop/material preservation | Spec and passing rows; no local preserved-strength record |
| Controlled repair validation | Same-context before/control/after + original-failure rerun | None demonstrated | Versioned targeted regeneration and QA | Fix failed row and rerun; paired effectiveness data absent |
| Disagreement | Preserve individual reviewers; no fake consensus | Not addressed | One self-authored review | Quorum/tie/disagreement fixtures, but no completed judged receipts |
| Visible type/spacing/composition | Required as primary lens | None | Strong narrow editorial examples | Strong example transformation, causal attribution unproven |
| Claim ceiling | One reviewer, domain escalation, no taste/user/market proof | Evidence basis named but example predicts behavior | Self-review and style-range limits | Explicitly blocks effectiveness; strongest negative-evidence honesty |

## Adoption decision

### Adopt or adapt

1. **One immutable finding record.** Combine target/version and stable anchor with exact observation, authority, conditional effect, ADR verdict, severity, confidence, likely cause, smallest repair, preserve set, validation, evidence state, and remaining unknowns.
2. **Evidence basis and owner question.** From the PM Skill, make every user/business effect declare whether it is observed, researched, inferred, or unknown; route missing evidence to the person/test that can answer it.
3. **Target plus diagnostic views.** From Paper Signal, inspect full-resolution intended context and thumbnail/sequence/alternate context. Use actual type, spacing, negative space, hierarchy, crop, and density—not rubric terminology—as evidence.
4. **One parent-cause repair with version siblings.** Preserve protected choices, change the canonical cause, rerender under frozen conditions, reproduce the original failure, inspect affected consumers and unrelated regressions, then stop.
5. **Fail-closed disagreement/receipt protocol.** From TasteCheck, preserve immutable per-reviewer verdict/rationale, ties, insufficient quorum, fabricated-evidence detection, and negative results. Absence of judged receipts remains absence, not “pending success.”

### Reject

- universal taste scores, pass/regenerate or SHIP/HOLD as the only verdicts, and high/medium/low without separate impact and confidence bases;
- appearance-based claims about conversion, comprehension, emotion, usability, accessibility, production, or market success;
- fixed critique counts, severity recipes, viewport sets, visual thresholds, style bans, motif lists, or one before/after as general Gold;
- invented intent, forced bounding boxes, source selectors inferred from pixels, and baseline/mask changes that erase an inconvenient finding;
- automatic redesign, multi-Skill dependency chains, edits during critique mode, or a release gate overriding domain owners;
- external prose, sample art, datasets, fonts, or fixtures whose licence/provenance is absent, restricted, or narrower than the intended reuse.

## Evidence and claim limits

- Stars are popularity only. No ranked Skill has E3 independent evaluation of the exact critique/repair mechanism.
- Rank 1's E1 is a textual example without the reviewed artifact; no visual observation can be verified from it.
- Paper Signal's examples and QA are narrow, repository-authored, and style-specific. They demonstrate inspectable craft and a workflow, not universal visual judgment or reviewer agreement.
- TasteCheck's before/after is not a causal evaluation of `tastecheck-pass`; its own effectiveness receipts explicitly fail/await evidence. That negative evidence must remain visible.
- Visual inspection covered representative committed artifacts, not every example. No Skill was executed locally, no repair was rerun, and no independent reviewers were recruited in this pass.
- The comparison cannot support expert equivalence, complete finding coverage, universal taste, usability/accessibility conformance, market preference, production readiness, or causal business/user improvement.
- Mechanisms may inform original synthesis. Exact wording, assets, fonts, and datasets remain subject to their licences and underlying rights.

**Stage-2 conclusion:** Scoville should synthesize the PM Skill's explicit evidence basis, Paper Signal's preservation-aware targeted rerender, and TasteCheck's immutable fail-closed receipts. It should retain ADR-0007's richer verdict/intent model, stable cross-medium localization, separate severity/confidence, and a strict one-reviewer claim ceiling rather than importing their narrower labels, recipes, or dependency chains.
