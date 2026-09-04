# Reference audit: `critique-and-validation`

Date: 2026-09-02

Method: [Per-reference expert-depth audit method](../reference-audit-method.md)

Research mode: Scoville Research, mixed Development and Academic route, with a
bounded single-coordinator Brainstorm pass

Freshness boundary: public sources and repositories inspected through
2026-09-02

**Research contract and conclusion.**

This audit asks what the Critique leaf must contribute beyond Terra High's
prior knowledge so that a deep visual audit, design comparison, deliberate
exception judgment, and repair validation are localized, causally useful, and
honest about evidence and disagreement. It covers scope and intent evidence,
finding localization, observation-to-repair reasoning, verdicts, severity,
confidence, false positives, preservation, controlled renders, human review,
and repair proof. It does not turn critique into usability research, legal or
accessibility certification, production approval, stakeholder consensus, or an
automatic taste score.

**Conclusion:** retain one directly routed Critique and Validation leaf and
deepen it into a coverage-complete finding-and-repair lifecycle. Keep maturity
status `stub` until leaf-specific Terra and human evidence supports promotion;
do not treat that status or the 1,800-token cost target as a coverage ceiling.
The current 623-token leaf already has the right causal spine—whole-result
reading, `observation -> likely effect -> severity -> smallest coherent
correction`, preservation, parent-cause repair, same-context comparison, and a
single-reviewer ceiling. It lacks ADR-0007's accepted verdict vocabulary,
stable finding anchors, separate severity and confidence, explicit
false-positive handling, a preservation contract, controlled-render metadata,
and a closed repair-validation loop. Those concerns share one finding's
lifecycle and should not be split without independent routing evidence. They
are `P1` gaps.

The bounded Brainstorm compared three architecture mechanisms in section 8. It
was one coordinated pass; no isolated or independent generation is claimed.

## 1. Current contract

### Router, ownership, maturity, evidence, and size

| Field | Current contract |
| --- | --- |
| Direct route label | `deep visual critique, cliche test, design exception, comparison, render validation` |
| Activation signals | `deep_critique`, `rule_exception` |
| Status | `stub` |
| Intervention | `focus` |
| Owned concerns | `causal_critique`, `generic_cliche_test`, `repair_priority`, `validation_rationale` |
| Declared sources | L-01, L-10, L-18, L-19, E-10, E-12, E-14 |
| Declared module evidence | `SOL-B01`, `SOL-B05` in `modules.yaml`; reference prose additionally names generic-cliche, typography, and deliberate-exception baselines |
| Domain maturity | `source-grounded`; not behavior-, production-, or human-validated |
| Current size | 2,909 UTF-8 bytes; 623 `o200k_base` tokens |
| Package cost target | 1,800 tokens for one ordinary expert leaf; the current audit method makes this a cost target, not a correctness ceiling |

Activation is intentionally narrow. Ordinary self-critique stays in Core, and
a bounded typography, colour, source, license, privacy, or jurisdiction audit
routes to its owning domain. The Critique leaf is for a deep cross-domain
review, explicit comparison, generic/cliche discrimination, challenged rule
exception, or rendered repair rationale.

The leaf is a method owner, not a substitute for domain authority. A finding
about typography, accessibility, production, data, culture, rights, or UI
behavior still needs that concern's expert or external authority when
material. Version-one `requires` and `conflicts` remain empty, so the leaf must
not follow links into another expert or imply a dependency.

### Current operational rules

**Inputs and evidence**

- Require brief, artifact or render, intended medium/context, required content,
  existing owner/system, constraints, and known evidence.
- Name missing evidence when only source or screenshot exists.
- Do not infer interaction, production, permission, or intent from appearance.

**Critique**

- Read purpose, first impression, specificity, hierarchy, tone, and task path
  as a whole before inspecting domain causes.
- Write findings as observation, likely effect, severity, and smallest coherent
  correction; mark fact, inference, heuristic, or preference.
- Preserve what works, prioritize task/meaning/access failures and structural
  causes before polish, and avoid flat taste lists.
- Distinguish generic work from minimal, conventional, or accessible work.

**Repair and comparison**

- In `critique`, describe rather than apply the repair.
- In `repair`, change the parent cause while protecting content and strong
  choices.
- Render before and after at identical size/context; judge task success,
  specificity, hierarchy, access, and production regressions separately.
- Stop when sufficient; redesign is not automatically better.

**Exceptions and validation**

- Preserve a documented exception only when intent, functional floors,
  compensating structure, and whole-result quality support it.
- Reject a post-hoc rationale when the same deviation appears unintentionally
  elsewhere.
- One reviewer is one reviewer's judgment; no self-score, VLM score,
  popularity signal, or one comparison becomes consensus or market proof.

### Accepted local epistemic contract not yet fully reflected

ADR-0007 requires one verdict set:

`defect | tradeoff | attributed preference | intentional exception |
unverifiable`

It also distinguishes binding constraint, functional floor, evidence-backed
default, craft heuristic, and convention; treats experiment as a workflow
state, tradeoff as an evaluation outcome, and preference as attributed
non-defect evidence; distinguishes documented, inferred, and unknown intent;
and requires a conventional rendered control for challenged or undeclared
exceptions. The current reference gestures toward most of this but does not
carry the accepted vocabulary or control contract into each finding.

### Current evaluation boundary

- The SOL baseline found strong generic-cliche, typography, and deliberate
  exception judgments in neutral, Core, and checklist arms. This argues against
  a broad critique textbook, not for deleting a professional evidence floor.
- `SOL-B01` is the smoke poster and `SOL-B05` the annual report in the rendered
  findings table. Neither ID proves routed Critique-leaf behavior. The module
  evidence mapping therefore does not trace cleanly to its stated critique
  cases.
- The package's generic landing critique used Core only. Terra's successful
  typography critique correctly loaded only Typography. Neither run exercised
  this leaf.
- The four-pair W-005 pilot supports the semantic distinction among a
  functional defect, craft defect, deliberate exception, and no-winner
  tradeoff. It used one model and local fixtures; selective routing was
  unstable on two pairs and no three-reviewer panel existed.
- Terra's poster-repair evaluation exposed three false-positive sources outside
  the artifact: a literal scorer mistook supplied terminology for a new claim,
  the read-graph budget was impossible, and the renderer guard misclassified a
  normal SVG namespace. A credible critique system must allow `unverifiable`
  or harness/capture defect instead of converting every failed check into a
  design defect.

The evidence supports routing and epistemic design, not qualified visual
critique, reliable localization, repair effectiveness, or human agreement.

## 2. What is already strong

1. **Mode authorization is explicit.** `critique` is read-only; only an
   authorized `repair` changes an artifact. This closes the earlier RC4
   ownership failure.
2. **The route is consequence-based.** Generic words such as `audit`, `review`,
   and `design` do not load the leaf. Domain-only audits remain with their
   domains.
3. **The whole precedes the parts.** Purpose, first impression, specificity,
   hierarchy, tone, and task path prevent an audit from becoming a list of
   isolated spacing comments.
4. **Domain coverage is broad without claiming every domain.** The leaf prompts
   a cause scan across concept, content, composition, type, colour, imagery,
   data, interaction, style, access, and production while respecting external
   owners.
5. **The causal finding spine is useful.** Observation, likely effect,
   severity, and smallest coherent correction are more actionable than a score
   or unexplained rule citation.
6. **Working choices are protected.** Naming what works and why it must survive
   is a real repair constraint, not praise padding.
7. **Priority is not a flat checklist.** Task, meaning, access, and structural
   causes precede polish.
8. **The generic-cliche test is subject-grounded.** It asks whether concept,
   copy, imagery, and composition contain subject evidence and correctly
   separates generic from minimal, conventional, or accessible.
9. **Repair targets the parent cause.** The leaf rejects symptom-by-symptom
   patching and unnecessary redesign.
10. **Before/after conditions are already recognized.** Same-size and
    same-context rendering is the right beginning of causal comparison.
11. **Exceptions have compensating structure.** Documented intent cannot
    override functional floors or whole-result quality.
12. **The claim ceiling is honest.** One reviewer, a VLM, popularity, and a
    single comparison cannot create consensus or market-quality proof.

These mechanisms should remain recognizable. Compression is appropriate only
after the complete finding lifecycle has passed open tests; the audit does not
justify a universal aesthetic rubric, a taste atlas, or an automatic score.

## 3. Missing professional capability

### Evaluation contract and evidence packet

- Every audit needs a named target and version: source/master, render or proof,
  intended medium and size, audience/task, brief or acceptance criteria,
  incumbent system, required content, states/variants, and known approvals.
- Record which evidence is actually available: editable source, static render,
  runtime state, interaction trace, production proof, owner rationale, user
  evidence, and domain authority. A screenshot cannot prove source structure,
  interaction, hidden states, print output, permission, or intent.
- Scope needs inclusions, exclusions, representative examples, and missing
  states. “Review the website” is not a complete sample contract; a single
  screen cannot support a whole-product verdict.
- Freeze the artifact/version and evidence packet before a comparison. Later
  source, renderer, font, fixture, viewport, copy, or baseline changes create a
  different comparison unless explicitly controlled.

### Finding localization and global/local relationship

- A finding needs a stable anchor suited to the medium: page/artboard/frame,
  viewport/state, named region, element/layer/source ID where reliable, visible
  text cue, timecode/frame, or normalized region. A bounding box is useful for
  visible local evidence but is not mandatory or sufficient.
- Whole-artifact findings should be labeled `global`; repeated system defects
  should identify representative instances and the shared owner rather than
  invent one local box.
- Source lines are evidence only when the render-to-source mapping is known.
  Conversely, a screenshot region does not prove the CSS token, component, or
  production cause.
- Localization uncertainty is separate from verdict confidence. UICrit found
  that asking a model to generate critique and bounding boxes together hurt
  comment quality, while grid overlays could worsen localization. The method
  should permit a second localization pass or an honest unresolved anchor.

### Unified finding vocabulary

Use one record across critique, comparison, and repair:

| Term | Meaning and required boundary |
| --- | --- |
| `finding_id` | Stable identifier across report, repair, and retest. Do not renumber silently after deduplication. |
| `scope/location` | Artifact version plus global, repeated-system, or exact local anchor and state. Never imply precision that the evidence does not support. |
| `observation` | Directly visible, measured, parsed, or supplied fact. Keep interpretation and cause out of this field. |
| `authority` | Binding constraint, functional floor, evidence-backed default, craft heuristic, convention, or named owner preference. Untyped numbers remain heuristics. |
| `likely_effect` | Conditional consequence for the stated audience, task, meaning, access, production, or system. It is not observed user behavior unless such evidence exists. |
| `verdict` | Exactly `defect`, `tradeoff`, `attributed preference`, `intentional exception`, or `unverifiable`. |
| `severity` | Consequence if the finding is true: `critical`, `major`, `moderate`, `minor`, or `not-rated`. `Critical` requires a binding-floor/release-blocking or material-harm basis; preference and insufficient evidence normally use `not-rated`. |
| `confidence` | Strength of the weakest consequential inference: `high`, `medium`, `low`, or `unknown`, plus a short basis. It is not severity. |
| `cause` | Smallest shared decision, rule, token, asset, component, content, workflow, approval, or production owner that explains the observed pattern. Mark it inferred until evidence supports it. |
| `smallest_repair` | Minimum coherent change to the owning cause, with affected instances and escalation if ownership is external. It is a proposal in critique mode. |
| `preserve` | Required content, intent, working cues, approved system choices, data, rights, access, dimensions, behavior, and deliberate variation that must remain. |
| `validation` | Original failure reproduction, controlled before/after or conventional control, exact checks, regression scope, evidence status, and remaining unknowns. |

`Priority` is action order, not another name for severity. It considers
severity, confidence, reach, dependencies, reversibility, and repair sequence.
A high-severity/low-confidence finding usually needs urgent verification, while
a moderate, high-confidence parent cause may be repaired before many local
symptoms.

### Verdict discrimination

- **Defect:** a demonstrated mismatch with a binding constraint, functional
  floor, documented intent, or sufficiently supported objective; name the
  violated authority and observed consequence.
- **Tradeoff:** the choice produces a real gain and accepted cost with no
  decisive winner under the supplied priorities. Do not disguise an avoidable
  defect as a tradeoff.
- **Attributed preference:** a named person or audience prefers an option
  within a stated scope. It is evidence, but not an objective defect or
  consensus.
- **Intentional exception:** documented or sufficiently supported intent bends
  a heuristic/convention while protected functions survive and compensating
  structure produces the claimed gain. Intent invented during critique cannot
  qualify it.
- **Unverifiable:** target, render, context, state, authority, intent, or proof
  is missing or contradictory. State the cheapest evidence that would change
  the verdict; do not downgrade uncertainty into `minor`.

### Severity, confidence, and false positives

- Severity needs an impact basis and affected scope. A visually dramatic issue
  can be low severity; a subtle data, access, rights, or production defect can
  be critical.
- Confidence should qualify observation-to-effect and effect-to-cause links.
  Direct measurement can make the observation certain while the user effect or
  parent cause remains tentative.
- Common false-positive families need explicit checks: wrong artifact/version,
  incomplete crop, transient loading or animation frame, missing font/asset,
  renderer or colour-profile difference, mismatched viewport/DPR/zoom/theme/
  locale/data, stale or unapproved baseline, intentional variation, heuristic
  overreach, source-only inference, and evaluator preference.
- A pixel or structural diff proves change under its capture contract, not
  defect, cause, task impact, or design quality. A passing diff proves only that
  the compared pixels met the declared gate; it cannot prove interaction,
  access, production, or user outcome.
- Preserve original receipts when a scorer, renderer, baseline, or harness is
  corrected. Reclassification must not rewrite the initial evidence.

### Intent and deliberate exceptions

- Record intent as `documented`, `inferred`, or `unknown`, with owner/source and
  date/version. An existing brief, design record, owner statement, or
  predeclared experiment outranks a rationale invented after criticism.
- A generated experiment records intended effect, bent principle, protected
  functions, expected gain, accepted cost, and falsifier before rendering.
- An undeclared or challenged exception needs a conventional rendered control
  when material. Compare whole-result quality and the claimed gain, not merely
  whether the exceptional element attracts attention.
- An intentional exception can still contain a defect in execution. Verdicts
  apply to the stated finding, not to the entire artifact.

### Controlled comparison and rendered proof

- Before/after, variant, or baseline comparisons must freeze all material axes:
  required content, artifact version, dimensions, crop, scroll origin,
  viewport, DPR/scale, zoom, renderer/browser/OS/font engine, font and asset
  versions, colour profile, theme, locale/script, fixture/data/time, state,
  animation/motion point, safe area, and masks/exclusions as applicable.
- Use intended size/context plus a diagnostic alternate. For print, projection,
  signage, motion, and physical output, route to the actual proof, device,
  venue, or supplier rather than substituting a browser screenshot.
- Any mask, crop, tolerance, normalization, or baseline update needs a reason
  and an approval/evidence state. Silent masking can erase the defect being
  tested.
- Pairwise preference is not repair validation. Re-run the original failure,
  check the intended improvement, inspect unrelated protected dimensions, and
  report regressions independently.

### Preservation and smallest coherent repair

- Freeze a preservation set before repair: exact required content and data,
  strong hierarchy/cues, documented intent and exceptions, approved design
  system, accessibility and rights floors, dimensions, behavior, and unrelated
  regions.
- Diagnose `failure -> observed pattern -> owning cause -> smallest coherent
  repair -> affected consumers -> controlled rerender/retest -> evidence and
  approval state`.
- Repair the canonical rule/token/component/content/asset where failures repeat;
  local override is justified only when the cause and exception are local.
- Compare the change surface. Unaffected protected regions should remain
  source- or render-equivalent where the medium permits; otherwise explain the
  unavoidable collateral change.
- Stop when the stated failure is resolved without a material regression.
  Additional polish requires new authority, not momentum.

### Human review, disagreement, and aggregation

- Capture reviewer identity/role, relevant expertise, audience perspective,
  evidence seen, and individual verdict/rationale. Keep reviews independent
  until their first judgments are recorded when a cross-person claim matters.
- Merge duplicate observations only after preserving each reviewer's verdict,
  severity, confidence, and rationale. Agreement on location does not imply
  agreement on effect, cause, or repair.
- Disagreement is data: it may indicate preference, a true tradeoff, ambiguous
  intent, different audience priorities, missing domain evidence, or evaluator
  error. Do not average it into fake certainty or use majority vote as a global
  taste oracle.
- One reviewer may produce a useful professional audit but only one reviewer's
  findings. Cross-person directional claims require the frozen reviewer and
  margin protocol; user behavior, comprehension, culture, accessibility,
  legal, or production claims need their own authority.

### Boundary between critique and other validation

- Design critique can identify and prioritize candidate usability effects; it
  does not replace task observation or user research.
- Accessibility, data, source, license, rights, culture, jurisdiction, and
  production findings require the exact standard, source, authority, or proof.
- Design validation can report visual and causal evidence. It cannot certify
  market quality, conversion, trust, recognition, consensus, legal compliance,
  or physical production readiness from appearance.

## 4. Rule-quality audit

| Class | Rules that belong | Boundary |
| --- | --- | --- |
| Binding constraints | Preserve the user's mode and authorization, supplied content and facts, accepted owner/system, explicit brief, rights, applicable access or legal floors, target dimensions, immutable receipts, and production authority. Use ADR-0007's verdict set. | Binding only from the actual owner, accepted repository decision, contract, applicable standard, jurisdiction, or production authority. A critique heuristic cannot override them. |
| Evidence-bounded rules | A localized render can support an observation; interaction traces can support observed behavior; target participants can support task/comprehension/preference claims; controlled before/after can support the exact changed result; multiple independent reviewers can support bounded agreement. | Match the claim to the evidence. Screenshot, source, diff, VLM, reviewer, user, and production proof are not interchangeable. |
| Contextual conventions | Whole-to-part review, critique sessions, severity labels, finding templates, annotated screenshots, bounding boxes, before/after plates, baseline approval, and independent review before reconciliation. | Select by task stage, medium, risk, audience, and team workflow. No one format or ceremony is universally required. |
| Heuristics or numeric starting points | A short prioritized list, several representative states, qualitative severity, confidence labels, diagnostic alternates, or pixel tolerance can start a review. | Counts, scales, viewport numbers, thresholds, and reviewer numbers are project/protocol choices unless a governing contract supplies them. The frozen three-reviewer rule applies only to this project's cross-person claim. |
| Preferences | A named reviewer, commissioner, stakeholder, or audience may prefer a direction, density, tone, rhythm, or level of polish. | Attribute owner, audience, and scope; do not relabel preference as defect, standard, market fact, or consensus. |
| Justified exceptions | A heuristic or convention may be bent when the intent is documented or supportable, protected functions survive, compensating structure exists, the gain and accepted cost are explicit, and a material challenged exception survives a conventional control. | Binding floors require their owning exception authority; critique cannot waive truth, access, rights, required content, or production safety. |
| Reject | Universal taste scores, “more polished is better,” “consistency always wins,” “the designer intended it,” “pixel-perfect means correct,” fixed viewport/threshold/severity recipes, one-reviewer consensus, and post-hoc exception stories. | These collapse evidence, preference, context, and authority into unsupported rules. |

### Slogans, cargo-cult numbers, and unsupported universals to reject

- “Every finding needs a bounding box.” Global/system findings do not; uncertain
  localization must remain uncertain.
- “Critical, major, minor” without an impact, scope, and authority basis.
- “High confidence” because the observation is visible when effect and cause are
  still inferred.
- “Three findings” or “ten findings” as a quality target. Deduplicate by cause
  and report every material blocker, not a quota.
- “Three viewports,” “0%/1%/5% diff,” “44 px,” “65–75 characters,” or another
  public Skill's numbers as universal review law.
- “The before/after proves the repair” when content, crop, renderer, font,
  state, or baseline changed.
- “The diff passed, so the design is correct” or “the diff failed, so the design
  regressed.” A diff is a change detector under one contract.
- “Experts agree” from one reviewer, an aggregate score, or majority vote that
  erased preference ownership.
- “Intentional” inferred only after a defect is named.
- “Generic” used as a synonym for minimal, conventional, accessible, restrained,
  or personally disliked.
- “Redesign” as the default correction when one parent token, rule, content
  relation, or production setup owns the failure.

## 5. Specialist Skill prior art

### Search boundary

GitHub code/web search and public Skill indexes were searched on 2026-09-02
with variants of `design critique`, `design review`, `visual audit`, `design
critic`, `before after`, `repair validation`, `visual comparison`, `visual
regression`, `preference`, `disagreement`, and `SKILL.md`. Actual Skill files
were inspected at pinned repository commits; repository licenses were checked
through GitHub metadata and license files. Popularity was not used as quality
evidence.

Exact-domain Skills exist for UI critique, design review, visual regression,
and design-to-code fidelity. None found in the bounded search combines
ADR-0007-style verdicts, intent evidence, separate severity/confidence,
cross-medium causal repair, preservation, and explicit human disagreement.

| Skill and pinned basis | License | Mechanism worth learning from | Do not copy or generalize |
| --- | --- | --- | --- |
| Anthropic [`design-critique`](https://github.com/anthropics/knowledge-work-plugins/blob/77961df00a4626bc3b83850064289decd5a3b977/design/skills/design-critique/SKILL.md), `anthropics/knowledge-work-plugins` commit `77961df00a4626bc3b83850064289decd5a3b977`, committed 2026-09-01, inspected 2026-09-02 | Apache-2.0 | Requires design, context, stage, and optional focus; separates usability, hierarchy, consistency, access, strengths, and priority; asks for specific evidence and alternatives. | A description can substitute for a render, first-impression timing is fixed, findings lack stable locations/cause/confidence/evidence state, and UI checks risk appearance-based interaction or access claims. Do not copy its template as validation proof. |
| OneWave-AI [`claude-design-critic`](https://github.com/OneWave-AI/claude-skills/blob/82859c0ebaff803889be6ca2efa0834ba8787773/claude-design-critic/SKILL.md), commit `82859c0ebaff803889be6ca2efa0834ba8787773`, committed 2026-08-11, inspected 2026-09-02 | MIT | Requires a goal, concrete instances, file/section/selector localization, prioritized fixes, token references, preserved strengths, and a re-audit offer. | “Never purple,” anti-AI phrase/style bans, premium-versus-generated house taste, fixed quick-win timing, copy rewriting, frontend-only ownership, and automatic implementation handoff are not general critique evidence. |
| Juliano Czkowski [`design-review`](https://github.com/julianoczkowski/designer-skills/blob/c259656c76d9758d7ead46b0d2f125cbe84f8665/design-review/SKILL.md), `designer-skills` commit `c259656c76d9758d7ead46b0d2f125cbe84f8665`, committed 2026-07-06, inspected 2026-09-02 | Apache-2.0 | Insists on the actual running render plus brief/source, records screenshot filenames, checks real states and responsive recomposition, localizes findings, and distinguishes must/should/could plus preservation. | Mandatory project writes, tool order, fixed three breakpoints, mobile-first and numeric typography rules, broad source-code review, and frontend assumptions exceed critique mode and do not generalize to print, editorial, motion, or supplied static work. |
| FluxonLab [`visual-regression-review`](https://github.com/FluxonLab/Skillry/blob/f61cc19f83a403ec028282779039b673024c025e/plugins/testing-and-qa/skills/56-visual-regression-review/SKILL.md), `Skillry` commit `f61cc19f83a403ec028282779039b673024c025e`, committed 2026-08-28, inspected 2026-09-02 | MIT; repository metadata says `NOASSERTION`, but the pinned license explicitly covers original `plugins/*/skills/` | Makes baseline ownership, human approval, state coverage, renderer flakiness, deterministic fixtures, stale baselines, and no-mutation safety explicit. | Fixed viewport minima, component-plus-page universality, threshold claims, every-PR CI rules, and UI-test tooling are engineering conventions, not design-quality or cross-medium laws. |
| voidmatcha [`design-to-code-fidelity`](https://github.com/voidmatcha/frontend-niche-skills/blob/7d751596845846ab07200bc7ea9c60c0c98c5985/skills/design-to-code-fidelity/SKILL.md), commit `7d751596845846ab07200bc7ea9c60c0c98c5985`, committed 2026-08-02, inspected 2026-09-02 | Apache-2.0 | Separates reference, capture, comparison, and evidence adapters; freezes a rich comparison matrix; declares masks/tolerances; reports evidence tiers and unknowns; diagnoses setup before calling a mismatch a defect. | Design-to-code fidelity is narrower than design critique. Its scripts, Figma/web adapters, artifact tree, tier names, diff metrics, and PR gate should not become mandatory or imply that source fidelity equals effective design. |

### Prior-art conclusion

The strongest practical comparator is not another universal critic. It is the
combination of the current causal stub with fidelity-style evidence tiers and
render controls. Public Skills repeatedly improve traceability by forcing
screenshots, locations, and baselines, but they also show the main traps:
frontend-only scope, fixed numbers, aesthetic house rules, writes during review,
and fidelity presented as quality. No searched Skill solves professional
disagreement or verifies that its proposed repair improves the intended result.

## 6. Authoritative research and learning sources

The IDs below are audit-local. Existing ledger IDs are shown where applicable.
“Original synthesis” permits newly written, source-bounded instruction; it does
not permit copying protected prose, figures, screenshots, datasets, or designs.

| ID | Source, version/date, status | Claim supported | Limit and reuse boundary |
| --- | --- | --- | --- |
| A-CV-01 / L-01 | Ken Jeffery et al., [*Graphic Design and Print Production Fundamentals*](https://opentextbc.ca/graphicdesign/), 2015, CC BY 4.0 except credited material | Brief-led design process, formal and production inspection, critique vocabulary, iterative correction, and preservation of communication purpose. | Introductory foundation, not a validated finding schema or taste authority. Original synthesis allowed with attribution and embedded-item checks. |
| A-CV-02 / L-10 | Sachant et al., [*Introduction to Art: Design, Context, and Meaning*](https://open.umn.edu/opentextbooks/textbooks/introduction-to-art-design-context-and-meaning), 2016, CC BY-SA 4.0 | Whole-to-part formal analysis, context, meaning, interpretation, and criticism vocabulary. | Educational and acknowledged scope/cultural limits; descriptive analysis is not proof of audience effect. Link/reference by default because adapted expression may invoke ShareAlike. |
| A-CV-03 / ADR-0007 | Local accepted decision, *Refine rule and exception epistemics*, accepted 2026-09-01 | Binding local vocabulary for authority types, intent states, verdicts, experiment records, exception controls, tradeoffs, and attributed preference. | Repository authority, not external empirical proof. It governs the future candidate unless superseded through the repository's decision process. |
| A-CV-04 | Alabood et al., [“A systematic literature review of the Design Critique method”](https://doi.org/10.1016/j.infsof.2022.107081), *Information and Software Technology* 153 (2023), peer-reviewed systematic review; full text inspected | Design critique varies by project goal/context; preparation, critique session, and post-processing recur; domain experts and stakeholders provide different evidence; critique is iterative and does not replace usability testing. | HCI/UX study method, not all graphic-design practice. The proposed ten-step process was not itself empirically validated. Copyrighted/restricted; reference-only. |
| A-CV-05 / E-12 | Duan et al., [UICrit paper](https://doi.org/10.1145/3654777.3676381), UIST 2024, peer-reviewed, paper CC BY-ND 4.0; [expanded dataset repository](https://github.com/google-research-datasets/uicrit), archived 2026, dataset CC BY 4.0 with underlying RICO screenshot terms separate | Critiques can be grounded to UI regions; expert comments used expected standard, observed gap, and repair; human filtering removed invalid model comments; staged comment then localization prompts avoided one form of task overload. | Paper's 3,059 critiques/983 screens used seven designers and one annotator per screen; expanded repository differs. Single-screen mobile UI, fair rater agreement in one task, poor bounding-box performance, and no implemented-repair outcome. Paper is NoDerivatives; dataset/screenshots are not distributable fixtures by default. |
| A-CV-06 / E-02 | An et al., [AesEval-Bench](https://arxiv.org/abs/2603.01083), arXiv preprint v1, 2026; full relevant methods/results inspected, redistribution license not established | Separates overall aesthetic judgment, region selection, and precise localization; current VLMs show material gaps, with localization harder than global judgment. | Preprint using selected dimensions, synthetic perturbations, Crello-derived designs, and human annotations. It does not validate causal critique, repair, or the target Terra model. Reference-only until publication, data, and license are verified. |
| A-CV-07 / E-14 | Peng, Bigham & Wu, [DesignPref](https://arxiv.org/abs/2511.20513), arXiv preprint v1, 2025; full paper inspected, dataset license not established | 12,000 UI pairwise comparisons from 20 professional designers showed substantial preference disagreement (`alpha = 0.25` for binary preference); rationales exposed different weighting of contrast, density, and hierarchy. | Generated UI preference, not defect truth, functional outcome, or all design domains. Preprint and identity-linked judgments; reference-only and no artifact reuse without a verified release. |
| A-CV-08 | Jacobsen, Hertzum & John, [“The Evaluator Effect in Usability Studies”](https://doi.org/10.1177/154193129804201902), 1998, peer-reviewed proceedings article; restricted abstract inspected | Four evaluators analyzing the same four sessions shared only 20% of 93 problems; 46% appeared for one evaluator; severe-problem selections also diverged. | Small dated usability-study setup, not visual design preference. Abstract-level, copyrighted, reference-only evidence that one evaluator and severity ranking are incomplete. |
| A-CV-09 | Hertzum & Jacobsen, [“The Evaluator Effect: A Chilling Fact About Usability Evaluation Methods”](https://doi.org/10.1207/S15327590IJHC1304_05), 2001, peer-reviewed review of 11 studies; abstract inspected, copyrighted | Substantial evaluator effects span methods, novice/expert evaluators, problem severities, detection, and severity; reported pair agreement ranged from 5% to 65%. | Usability evaluation, not a design-aesthetics agreement coefficient or mandate for one reviewer count. Abstract-level, reference-only. |
| A-CV-10 | Ko et al., [Criticmate](https://doi.org/10.1145/3772318.3790929), CHI 2026 peer-reviewed open-access paper; full accessible ACM record inspected, exact reuse license not established | A stagewise perception -> comprehension -> projection process exposed editable intermediate evidence; in a six-practitioner formative study and 26-participant controlled study, it produced more concrete/balanced single-screen UI critique than a single-pass baseline while retaining human intervention. | Single-screen mobile UI and one implemented research system; residual grounding errors remained and experts found the full process unnecessary for some simple screens. Reference-only unless exact license is verified. |
| A-CV-11 | Playwright, [Visual comparisons](https://playwright.dev/docs/test-snapshots), living official documentation inspected 2026-09-02, repository Apache-2.0; Android Developers, [Screenshot testing](https://developer.android.com/training/testing/ui-tests/screenshot), updated 2026-03-05, page CC BY 2.5 and code Apache-2.0 unless noted | Baseline/render comparison requires environment control; OS, browser, fonts, hardware, scale, state, and thresholds can change results; a failed image comparison may be intended and tolerances can hide defects or create noise. | Web and Android tooling, not general design quality. No fixed threshold, viewport, or golden approval rule transfers automatically. Original synthesis allowed within respective terms. |
| A-CV-12 / E-05 | W3C WAI, [Before and After Demonstration](https://www.w3.org/WAI/demos/bad/), status 2012, and [WCAG-EM 2.0](https://www.w3.org/TR/wcag-em-2/), W3C Group Note 2026-07-23, W3C terms | Worked same-site barrier/repair examples; evaluation scope, representative sample, complete processes, exact findings, reruns after repair, and bounded conformance statements. | Accessibility conformance only. BAD is old and incomplete; WCAG-EM is an endorsed Group Note, not new normative requirements, and sampled evaluation alone cannot prove whole-product conformance. Reference and original synthesis under W3C terms. |
| A-CV-13 | Mirabito, Tchatchouang Kayo & Goucher-Lambert, [Feature, specification and evidence framework for communicating design rationale](https://doi.org/10.1017/dsj.2024.19), *Design Science* 10 (2024), peer-reviewed, CC BY 4.0 | Rationale records benefit from linking a feature/decision, specification, and evidence; study found rationale content and depth vary and can be missing, supporting explicit documented-versus-unknown intent. | Mainly engineering/student reports plus five industry reports, not a visual exception-validation experiment. Original synthesis allowed with attribution. |
| A-CV-14 / E-10 | Apple, [RLDF repository](https://github.com/apple/ml-rldf/tree/be0d7f816ded6fa5111035f34f69b077072ba9a3), commit `be0d7f816ded6fa5111035f34f69b077072ba9a3`, committed 2026-01-06; code under Apple sample-code terms, dataset CC BY-NC-ND 4.0 | Twenty-one designers supplied rankings, comments, sketches, and direct revisions; the release links original/improved HTML and renders, showing that critique and direct repair can be separate evidence modalities. | Synthetic UI generation/training study and provider claims; not a universal critique method or commercially reusable fixture. Dataset cannot be adapted and is noncommercial. Reference-only. |
| A-CV-15 | Jakob Nielsen, [Severity Ratings for Usability Problems](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/), practitioner article 1994, copyrighted | Severity can consider frequency, impact, and persistence; a single evaluator's severity is unreliable and rating can be separated from issue discovery. | Usability-specific convention and dated 0–4 scale, not binding visual-design taxonomy. Learn from dimensions; do not copy the scale or turn estimates into observed frequency. |

### Contradictions and resolved boundaries

- Public Skills often require every critique to be immediate and exhaustive;
  UICrit and AesEval show that critique generation, localization, and scoring
  are separable error surfaces. Result: one finding record, but staged
  observation/localization/classification when needed.
- Public Skills use fixed severity scales and exact priority labels; evaluator
  studies and DesignPref show substantial detection, severity, and preference
  disagreement. Result: separate severity, confidence, verdict, and attributed
  preference; preserve individual reviews.
- Screenshot/fidelity Skills treat diffs as gates; official Playwright/Android
  guidance and local Terra false positives show environment and harness
  sensitivity. Result: freeze comparison conditions and diagnose capture before
  declaring a design defect.
- Design-rationale sources support recording intent, while ADR-0007 forbids
  intent first invented during critique. Result: `documented`, `inferred`, or
  `unknown` intent plus a conventional control for material challenged
  exceptions.
- Before/after examples support repair explanation but do not prove causal or
  user benefit by themselves. Result: reproduce the original failure, test the
  target improvement, and audit protected dimensions separately.

## 7. Applied Dos and Don'ts

| Concern | Do | Don't | Failure -> cause -> smallest repair | Basis |
| --- | --- | --- | --- | --- |
| Scope and target | Freeze artifact/version, brief, medium, size, audience/task, required content, states, owners, evidence, inclusions, exclusions, and sample basis. | Do not claim a whole-product or final-production audit from one screenshot or an undefined target. | Findings conflict or cannot be reproduced -> scope/version drift -> bind the exact target and downgrade unsupported coverage. | A-CV-04/11/12; Core evidence boundary |
| Whole-to-part reading | State purpose, first impression, specificity, hierarchy, tone, and task path before local findings; then connect local evidence to the global result. | Do not begin with a generic checklist or infer the whole from the most salient blemish. | Accurate local comments miss the main failure -> no global model -> restate the communication/task path and re-prioritize only findings that affect it. | A-CV-01/02/10 |
| Location | Anchor each finding to artifact version and global/system/local location using the medium's stable identifiers; mark uncertain location. | Do not fabricate selectors, source lines, bounding boxes, or precision; do not force a box around a global problem. | Repairer cannot find or maps the wrong element -> unstable/false anchor -> add a visible cue plus stable ID or rerun localization separately. | A-CV-05/06/10 |
| Observation | Describe only what is visible, measured, parsed, or supplied; attach the exact render/source/evidence state. | Do not hide effect, cause, or taste inside “obviously,” “confusing,” “unprofessional,” or “off.” | Team debates the premise -> observation mixed with judgment -> rewrite the inspectable fact first, then state conditional effect. | A-CV-01/02/05 |
| Effect | Tie the likely consequence to the stated audience, task, meaning, access, production, or system; label inference. | Do not report gaze, comprehension, behavior, emotion, conversion, or market effect without corresponding evidence. | Claimed impact cannot be substantiated -> reviewer intuition became user fact -> lower confidence and name the needed participant/behavior evidence. | A-CV-04/05/08/09 |
| Verdict | Use exactly `defect`, `tradeoff`, `attributed preference`, `intentional exception`, or `unverifiable`. | Do not use “issue” as a catch-all or convert missing evidence into a minor defect. | Preference or ambiguity enters defect queue -> no verdict boundary -> reclassify with owner/evidence and remove unsupported severity. | ADR-0007; A-CV-07/08/09 |
| Severity and confidence | Rate consequence and evidential confidence separately, each with basis; use priority only for action order. | Do not let high visual salience imply severity, or direct observation imply causal confidence. | Low-confidence claim blocks release -> severity/confidence conflation -> verify the consequential inference first or mark `unverifiable`. | A-CV-08/09/15; ADR-0007 |
| Intent | Record documented, inferred, or unknown intent with source. For generated experiments, predeclare effect, bent principle, protected functions, gain, cost, and falsifier. | Do not invent intent after criticism or treat designer authorship as evidence that every visible choice is intentional. | Defect is excused post hoc -> rationale created during critique -> restore candidate-defect/unverifiable status and compare a conventional control. | ADR-0007; A-CV-13 |
| Exception | Preserve an exception when protected functions survive, compensating structure is visible, and the whole result demonstrates the claimed gain. | Do not reject every deviation or accept an exception merely because it attracts attention. | Intentional break looks like accident or harms the task -> compensation/gain absent -> repair execution or return to the conventional control. | ADR-0007; W-005 local evidence |
| Generic-cliche | Test whether subject evidence survives logo/noun changes and whether concept, content, image, and composition form a specific system. | Do not equate generic with minimal, conventional, restrained, familiar, accessible, or disliked. | Artifact could represent any unrelated subject -> no subject-specific thesis/evidence -> repair the concept or one load-bearing content/visual relationship, not surface novelty everywhere. | Current test; A-CV-01/02 |
| Cause | Infer the smallest owner that explains the repeated pattern and state confidence: decision, rule, token, component, content, asset, workflow, approval, or production setup. | Do not call the visible symptom the cause or assert source ownership from pixels alone. | Same defect recurs after local fixes -> parent owner unchanged -> inspect source/system evidence and repair the canonical cause once. | Current repair rule; A-CV-05/10/13 |
| Repair | Propose or apply only the smallest coherent authorized change, list affected consumers and escalation, and freeze a preservation set first. | Do not redesign by default, patch every instance, erase deliberate variation, or edit in critique mode. | Repair “improves” one area but changes content/system/intent -> preservation absent -> revert collateral changes and repair the parent cause within the frozen set. | Core; current leaf; A-CV-14 |
| Render control | Compare under identical material conditions and document viewport/size, scale, crop, renderer, fonts/assets, state, locale/theme/data/time, motion point, profiles, masks, and tolerance as applicable. | Do not compare mismatched screenshots or silently normalize/mask differences. | Diff is noisy or misses the defect -> uncontrolled environment/mask -> stabilize the material axis and retain both original and corrected receipts. | A-CV-11; Terra harness evidence |
| Before/after proof | Reproduce the original failure, show intended and diagnostic renders, test the claimed gain, and inspect protected dimensions and unrelated regressions separately. | Do not call “after looks better” causal, user, access, interaction, or production proof. | Repair passes the hero comparison but fails another state -> validation sampled only the edited view -> add the affected state/process and repair or downgrade evidence. | A-CV-11/12/14 |
| False positives | Check artifact/version, crop/state, loading/font/asset, renderer/profile, baseline approval, heuristic authority, intent, and preference before `defect`. | Do not overwrite a baseline, grader, or receipt to make a finding disappear. | Test failure is not an artifact failure -> harness/capture/baseline cause -> quarantine or reclassify the signal and rerun against immutable evidence. | A-CV-05/11; SOL/Terra evaluation |
| Strength preservation | Name effective choices and why they are load-bearing; carry them into the preservation set and regression checks. | Do not add praise as padding or replace a strong specific cue merely to make a repair visible. | Repair becomes generic or loses hierarchy -> strong cue was not protected -> restore it and isolate the actual failing relation. | Current leaf; A-CV-01/14 |
| Reviewer disagreement | Record independent reviewer verdicts, roles, evidence, and rationales before reconciliation; classify preference/tradeoff/audience split explicitly. | Do not erase dissent with a mean score, majority taste, or consensus wording unsupported by protocol. | Aggregated report contradicts individual evidence -> reconciliation collapsed different constructs -> restore per-reviewer records and route the disagreement to the relevant owner/test. | A-CV-07/08/09/10 |
| Claim ceiling | Report exact evidence state and unresolved authority; route user, access, legal, culture, data, or production claims to their owners. | Do not certify usability, accessibility, compliance, market quality, consensus, or production readiness from design critique alone. | Review is treated as approval -> evidence label/owner missing -> downgrade the statement and obtain the narrow missing authority. | Core; A-CV-04/12; L-18/19 |

## 8. Architecture recommendation

### Decision: retain one leaf and make the finding lifecycle complete

Keep `critique-and-validation` as one directly routed `focus` leaf. Deep
critique, comparison, exception judgment, parent-cause repair, and validation
operate on the same finding record and preservation set. Splitting them now
would duplicate target/evidence/intent context, create cross-leaf handoff loss,
and risk separate verdicts for the same cause.

The candidate should retain maturity status `stub` until behavior evidence
changes, but maturity cannot force incomplete instruction. Draft the smallest
payload that preserves these inseparable clusters:

1. **Target and evidence contract:** artifact/version, brief, context, sample,
   render/source/runtime/production evidence, missing proof.
2. **Staged inspection:** whole-result model, exact observation, stable
   localization, domain/owner route, and global/local relation.
3. **Unified finding record:** authority, likely effect, ADR verdict, severity,
   confidence, cause, smallest repair, preserve, validation, unknowns.
4. **Exception and preference epistemics:** documented/inferred/unknown intent,
   conventional control, gain/cost/falsifier, attributed preference, tradeoff.
5. **Controlled comparison:** immutable before/control/after identities,
   material render axes, masks/tolerances, false-positive triage.
6. **Repair validation:** reproduce failure, change parent cause, inspect
   affected consumers and preserved dimensions, rerender/retest, stop when
   sufficient.
7. **Human and claim boundary:** independent reviewer records, disagreement,
   domain escalation, exact evidence state, no consensus/user/market/production
   inflation.

The 1,800-token ordinary-leaf figure is a cost target. Exceed it when the
tested professional floor cannot be expressed safely within it. Compress only
through clause/cluster ablation that shows no regression in finding validity,
verdict discrimination, localization, preservation, repair, or proof.

### Routing and cost record

| Measure | Current evidence and decision |
| --- | --- |
| Measured leaf size | 623 `o200k_base` tokens and 2,909 UTF-8 bytes at this audit. Measure the candidate again; do not fail it solely for exceeding 1,800 tokens. |
| Expected load frequency | Unknown and intentionally limited. RC7 routing passes prove route stability on named cases, not population frequency. Core-only generic critique and domain-only typography critique show the leaf should not load for ordinary self-critique or one bounded domain. Do not invent a percentage. |
| Common independent co-loads | Deep audits may co-load one to three material domain leaves; rendered repair may additionally route production, and UI implementation stays with UI. Load only independently signaled concerns and phase work when more than three are material. |
| Smallest tested non-inferior payload | Unknown. Test a coverage-complete arm first, then ablate finding clusters. A smaller arm is non-inferior only if it loses no material criterion, verdict, exception, repair mechanism, owner, false-positive defense, preservation rule, or proof requirement. |
| Split threshold | Repeated route traces must show independently selectable critique-versus-validation signals, low routine co-load, stable exclusive owners, and no shared parent-cause/preservation record. Current evidence shows the opposite. |

The older frozen preimplementation record called 1,800 a maximum; the current
audit method and W-011 direction make it a cost target and require coverage
first. Any executable change must update the governing package decision/freeze
through its own authorized lifecycle rather than silently violating old hashes.

### Bounded alternatives considered

| Direction | Evidence label | Benefit | Load-bearing risk and cheapest falsifier | Disposition |
| --- | --- | --- | --- | --- |
| One coverage-complete finding-and-repair lifecycle with internally staged observation/localization/classification/validation | `Recombination` | Combines established critique, localization, ADR verdicts, render controls, preservation, and disagreement handling without losing one finding's causal chain. | Risk: staging adds ceremony or overload without better findings. Falsify with the open cases in section 9 plus cluster ablation; remove a stage only if validity, localization, verdict, repair, and proof remain non-inferior. | **Recommend** |
| Keep the 623-token stub and rely on Core/domain knowledge | `Established` | Lowest read cost; SOL and Terra already produce strong ordinary critiques. | Risk: deep cases still lack stable anchors, accepted verdicts, confidence, false-positive triage, and controlled repair proof. Falsify by showing the current arm matches the complete arm across seeded ambiguous-intent, harness-noise, disagreement, and regression cases. | Comparator, not default decision. |
| Split `design-critique` and `visual-validation` into separate flat leaves | `Established` | Could save tokens when a task needs only qualitative critique or only automated visual regression. | Risk: most repair/exception cases need shared target, intent, cause, preservation, and before/after evidence, causing routine co-load and divergent verdicts. Falsify with route traces showing independent signals, low co-load, and clean ownership across repeated tasks. | Defer until routing evidence supports it. |

The challenged load-bearing assumption is that more structure necessarily
improves critique. UICrit found that combining comment generation and bounding
box localization reduced comment quality, and Criticmate participants found a
full staged process unnecessary for some simple screens. The architecture
therefore keeps ordinary critique in Core, uses this leaf only for deep or
exception/validation work, and permits localization as a separate internal pass
rather than a forced box in every finding.

## 9. Tests and claim ceiling

### Smallest open Terra High falsification set

Use current versus candidate arms with the same Terra High model, reasoning,
public fixtures, brief, co-loaded domains, renderer, and deterministic checks.
Freeze complete first-wave inputs and artifact identities. Keep cases open;
do not use sealed holdout material. Blind qualified human reviewers to arm and
variant identity.

| Case | Minimal public task | What would falsify the proposed change |
| --- | --- | --- |
| Generation: deliberate exception with predeclared validation | Generate a one-page public-event poster from exact supplied copy and identity. The brief predeclares one off-grid title experiment with intended gain, protected reading/access floors, accepted cost, and falsifier. Route Composition plus Critique because the exception is material. Render the intended size and a conventional aligned control; return the design record and evidence, not a universal winner. | Candidate invents intent after rendering, loads a critique textbook into ordinary design, erases the exception by default, accepts it without compensating structure/control, loses required content, turns reviewer preference into defect, or claims audience success from one review. |
| Critique: deep multi-artifact audit with ambiguous intent and harness noise | Audit a supplied three-artifact family containing a global hierarchy defect, two local symptoms of one token cause, one documented exception, one plausible but undocumented deviation, one reviewer preference, one true tradeoff, one source-only hidden-state unknown, and one intentionally mismatched renderer capture. Do not edit. | Candidate misses/false-localizes material findings, duplicates symptoms, invents source/intent, uses a verdict outside ADR-0007, conflates severity/confidence, calls the capture mismatch a design defect, omits preserved strengths, or reports consensus. |
| Repair: parent cause and controlled before/after | Repair an authorized responsive document/UI family where one canonical spacing/type token creates clipping in two contexts while a deliberate asymmetry and unrelated strong cue must remain. Freeze exact content, state, fonts/assets, viewport/size, and baseline; update the parent cause, render affected contexts and a diagnostic alternate, and validate preserved regions. | Candidate patches instances, redesigns unrelated areas, changes content or baseline, compares mismatched conditions, silently masks a regression, loses the exception/strong cue, reports user/access/production proof without authority, or continues polishing after the target failure is resolved. |

### Deterministic checks

- `critique` produces no artifact/source/baseline mutation; `repair` touches only
  authorized targets.
- Exact supplied content, data, dimensions, claims, approved assets/tokens,
  owner constraints, and artifact hashes/IDs remain unless explicitly in the
  repair set.
- Every material finding has stable ID, artifact version, scope/location,
  observation, authority, likely effect, ADR verdict, severity, confidence and
  basis, cause state, smallest repair, preserve set, validation target, and
  unknowns.
- Verdict values are exactly `defect`, `tradeoff`, `attributed preference`,
  `intentional exception`, or `unverifiable`; experiment is not a verdict and
  preference is attributed.
- `critical` has a supplied binding-floor/material-harm/release-blocking basis;
  insufficient evidence is not `minor`, and confidence is not copied from
  severity.
- Every local anchor resolves against the named artifact/render; global and
  repeated-system findings are not forced into invented bounding boxes.
- Documented, inferred, and unknown intent remain separate; no critique-created
  intent qualifies an exception.
- Duplicate local symptoms map to one parent cause where fixture truth says so;
  independent failures remain separate.
- Comparison manifest fixes material content/render axes and declares every
  crop, mask, tolerance, exclusion, normalization, and baseline approval.
- The original failure reproduces before repair; the after result checks the
  target and protected dimensions; deliberate variants and unaffected regions
  remain source/render-equivalent where defined.
- Capture, parser, source, domain, and harness failures are classified
  separately from visual defects, with original and corrected receipts kept.
- Candidate retains canonical module ID, signals, owners, and no dependency or
  expert-to-expert read. Record token/read-graph cost; exceeding 1,800 alone is
  not failure.

Deterministic checks can prove record completeness, enum use, exact content,
source identity, anchor resolution, render conditions, syntax, pixel/geometry
differences, preserved hashes, and migration scope. They cannot prove intended
audience effect, visual quality, preference, correct cause, exception success,
usability, accessibility, culture, legality, production readiness, or
consensus.

### Required render or production evidence

- Generation: intended-size poster and conventional control at identical
  conditions; diagnostic thumbnail/distance view; source parse and exact-copy
  receipt; documented experiment before render.
- Critique: immutable source/render set with artifact/version labels, exact
  local anchors, whole-family overview, intended context and diagnostic
  alternate, plus the deliberately mismatched capture retained for
  false-positive diagnosis.
- Repair: before/after and affected-context renders at identical conditions,
  diff or annotated comparison where useful, original-failure reproduction,
  protected-region/content receipts, and explicit unrelated-regression review.
- Interaction, assistive-technology, print, projection, signage, animation,
  colour, device, or vendor claims require the actual runtime, user, proof,
  device, venue, or supplier evidence. A generic screenshot is not a substitute.

### Human and domain authority

- One qualified design reviewer may judge family cohesion, hierarchy,
  specificity, exception compensation, and visible repair in an open internal
  case; report it as one review.
- Cross-person directional claims require at least the frozen three independent
  qualified reviewers and margin/disagreement protocol. Record individual
  verdicts before reconciliation; do not expose earlier reviewer choices.
- The design owner/commissioner owns intent, acceptance priorities, approved
  exceptions, and release decisions.
- Target users or audience participants own task success, comprehension,
  recognition, and preference evidence; observed behavior outranks reviewer
  prediction for those claims.
- Accessibility, data/domain, culture/community, legal/rights, and production
  specialists own their respective consequential conclusions.
- A second inspection or domain test is required when a high-severity result
  rests on low-confidence inference. Disagreement remains visible rather than
  being forced into consensus.

### Admission and claim ceiling

Do not promote the leaf from `stub` after one pass. Admit only the smallest
rule cluster that improves repeated or cross-case behavior without regressing
ordinary Core-only critique, domain routing, creative exceptions, preservation,
or cost. Keep corrected harness evidence separate from product evidence.

Even passing all three cases would support only a source-bound deep-critique
and repair-validation process for the tested artifact classes. It would not
support:

- a universal taste, beauty, polish, genericness, or quality score;
- expert equivalence or complete finding coverage;
- consensus, market preference, conversion, trust, emotion, comprehension, or
  task success without corresponding human evidence;
- causal proof that a repair improved user or business outcomes;
- whole-product usability or accessibility conformance from sampled visual
  review;
- legal, rights, cultural, data, security, safety, or production approval;
- correct intent when it is undocumented, or stakeholder alignment beyond
  recorded owner evidence;
- a fixed severity scale, reviewer count, viewport set, diff threshold,
  tolerance, or number of findings for every context;
- generalization from single-screen UI datasets to editorial, print, motion,
  identity, spatial, or physical design;
- independent or original Brainstorm generation.

## 10. Priority

**Overall priority: `P1`.**

The current leaf does not contain a clear `P0` instruction. It already keeps
critique read-only, names missing evidence, refuses appearance-based intent and
production inference, preserves working choices, compares before/after, bounds
exceptions, and rejects one-reviewer consensus. The risk is incomplete applied
capability and inconsistent classification, not an active instruction to cause
rights/access harm or destructive production change.

| Priority | Work justified by this audit |
| --- | --- |
| `P1` | Carry ADR-0007's exact verdict and intent vocabulary into the leaf; add target/evidence packet, stable location/global-system anchors, authority, separate severity/confidence/priority, false-positive triage, preservation set, parent-cause chain, controlled comparison manifest, repair validation, human disagreement, and exact escalation/claim boundaries. Correct leaf-specific SOL evidence mapping when authorized. |
| `P2` | Optimize internal staging and reporting density only after open cases show non-inferiority; add optional machine-readable finding records or visual-diff adapters only when a real consumer and independent routing signal exist. |
| Not now | Universal aesthetic rubric, numeric taste score, forced bounding box for every finding, fixed severity/viewport/threshold recipes, automated baseline approval, default multi-agent jury, hidden usability/user-research claim, critique-mode edits, or split leaves without independent route evidence. |

Next decision-changing action: after W-011 authoring is authorized, author one
coverage-complete candidate leaf without a hard token cap and run the three
open Terra cases plus cluster ablation. Preserve Core-only and domain-only
critique routes as negative controls. Compress only after exact coverage and
selective routing pass. This audit makes no executable change and does not
alter the Plan, Decisions, benchmark Gold, or sealed holdout material.
