# Pre-implementation qualification contract

Date: 2026-09-01  
Status: frozen; execution amended by ADR-0013 and model target by ADR-0014 on 2026-09-02  
Owners: project qualification; independent holdout custodian `/root/design_holdout_custodian`

This record freezes what must be decided before implementation. It contains no
sealed holdout prompts, images, expected answers, or restricted external
material. “Market-leading” is the user's personal ambition and quality
direction, not an acceptance criterion or public factual claim.

## Product priority

Evaluate in this order:

1. original professional generation from brief, content, and medium;
2. discrimination among effective, mediocre, defective, generic, and clichéd
   work;
3. targeted repair followed by rendered reassessment;
4. recognizable, coherent, non-template style execution;
5. theory/history retrieval only when it improves one of the first four.

Knowledge recall or historical description is not a substitute outcome. When
the user requests an artifact, advice or a style description alone does not
pass: Design must direct the appropriate format/tool owner to produce an
editable artifact and inspect a render.

## Model scope

All baseline measurement, SkillOpt optimization, promotion, and qualification
uses only the exact frozen GPT-5.6 SOL configuration. The one-time Fable 5.1
Plan/gap review is process evidence, not product evidence. Opus 5 is not run.
Do not state or imply parity for untested models.

## Gate outputs

Before W-002 starts, W-007 must record hashes for:

1. accepted source, ownership, exception, routing, and evaluation Decisions;
2. the exact reference route matrix and context budgets;
3. the domain-maturity and allowed-claim ledger;
4. the original-fixture schema and external-material receipt schema;
5. the SkillOpt grader specification;
6. the human-review protocol and report schema;
7. the comparator parity and benchmark-defect protocol;
8. an independently held opaque final-holdout manifest.

## Core gates

These stay active whenever Design is active; no routed reference may be needed
to preserve them:

- explicit owner and incumbent-system precedence;
- purpose, audience, content, medium, lifecycle stage, and observation boundary;
- binding constraints and functional accessibility/equivalent-meaning floor;
- generate, critique, repair, and style-direction mode boundary;
- declared versus inferred exception rule;
- knowledge and asset provenance floor;
- rendered-evidence and uncertainty boundary;
- multi-select route decision.

The canonical operation modes are `generate`, `critique`, `repair`, and
`style-direction`. Exception handling is a gate, not a fifth mode. A repair run
allows at most two rendered passes and repeats the same observation/protected-
dimension checks after each pass. Missing format or render tooling produces a
best-effort source artifact plus an explicit `visually unverified` boundary,
never a claim inferred from source alone. The artifact-class source/render
table in `docs/research/modular-application-architecture.md` is part of the
W-007 freeze.

## Reference route matrix

`R` is required, `C` is conditional when the concern is material, and `F` is
forbidden unless the task explicitly expands. `Core` is always present.

| Task | Required routes | Conditional routes | Forbidden by default |
| --- | --- | --- | --- |
| Diagnose an ambiguous brief and create directions | brief-and-concept | culture-ethics-and-provenance; affected domain after direction selection | sources-and-attribution |
| Interpret or apply a named era, movement, style, aesthetic, or material direction | brief-and-concept; style-direction | culture-ethics-and-provenance for regional, vernacular, living-culture, or appropriation risk; a future SOL-qualified direct style leaf | unrelated style/history leaves; ui-and-interaction-design unless the artifact is interactive |
| Static poster, ad, or social graphic | brief-and-concept; composition-and-layout; typography-and-writing-systems | colour-and-reproduction; imagery-and-art-direction; media-production-and-handoff | ui-and-interaction-design |
| Editorial spread or multi-page publication | brief-and-concept; composition-and-layout; typography-and-writing-systems | imagery-and-art-direction; media-production-and-handoff; culture-ethics-and-provenance | ui-and-interaction-design |
| Visual identity or brand system | brief-and-concept; brand-and-visual-systems | typography-and-writing-systems; colour-and-reproduction; imagery-and-art-direction; culture-ethics-and-provenance | ui-and-interaction-design unless a digital product is in scope |
| Data visualization or infographic | information-and-data | typography-and-writing-systems; colour-and-reproduction; culture-ethics-and-provenance | brand-and-visual-systems unless brand fit is requested |
| Greenfield webpage or UI design | brief-and-concept; composition-and-layout; ui-and-interaction-design | typography-and-writing-systems; colour-and-reproduction; imagery-and-art-direction | media-production-and-handoff unless export or non-web media is relevant |
| Existing framework UI implementation only | none unless design judgment is requested | ui-and-interaction-design for design audit; active UI Skill owns implementation | brand-and-visual-systems; motion-and-sequence; media-production-and-handoff |
| Motion graphic or temporal sequence | brief-and-concept; motion-and-sequence; composition-and-layout | typography-and-writing-systems; colour-and-reproduction; media-production-and-handoff | ui-and-interaction-design unless interactive UI motion is in scope |
| Packaging or fixed-media adaptation | brief-and-concept; media-production-and-handoff; composition-and-layout | typography-and-writing-systems; colour-and-reproduction; imagery-and-art-direction; brand-and-visual-systems; culture-ethics-and-provenance | ui-and-interaction-design |
| Wayfinding or distance communication | brief-and-concept; composition-and-layout; information-and-data | typography-and-writing-systems; colour-and-reproduction; media-production-and-handoff; culture-ethics-and-provenance; brand-and-visual-systems | ui-and-interaction-design unless interactive |
| Presentation, document, report, form, or template system | brief-and-concept; composition-and-layout; typography-and-writing-systems | information-and-data; colour-and-reproduction; imagery-and-art-direction; media-production-and-handoff; culture-ethics-and-provenance | ui-and-interaction-design unless interactive controls are in scope |
| Critique an existing artifact | critique-and-validation; only affected domain routes | media-production-and-handoff when production readiness is claimed | brief-and-concept unless the brief is missing or contradictory |
| Source, asset, or attribution audit | culture-ethics-and-provenance; sources-and-attribution | media-production-and-handoff | visual craft routes unless design quality is separately requested |
| Unnamed or novel artifact class | brief-and-concept; composition-and-layout; one primary content expert | media-production-and-handoff only when delivery readiness is requested; other experts only for named decisions | load-all; ui-and-interaction-design unless the artifact is interactive |

Complex projects may exceed three references across distinct phases. Each
additional read needs a named decision it can change. There is no load-all
route and no reference-to-reference chain.

No phase loads more than three expert references. Rows with more than three
material concerns are executed as named direction, system-development, and
production/validation phases. Only the compact Design Dossier crosses the
phase boundary; earlier expert prose does not. The route validator enumerates
every required and conditional phase set, measures it, and fails any case that
silently omits a required expert.

The authoring source is `modules.yaml`; a build step generates the compact
direct module index in `SKILL.md`. The runtime never follows an expert file to
another expert file. Every selected expert must declare generation, critique,
repair, and style-direction capabilities it actually supports. Module content
is classified as `focus`, `correction`, `teaching`, or
`external-verification`, with source and SOL evidence IDs.

## Context budgets

Measure UTF-8 Skill files with `o200k_base`:

- Core: at most 1,500 tokens;
- generated direct module index inside Core: at most 450 of those tokens;
- each ordinary expert reference: at most 1,800 tokens unless a separate
  measured Decision authorizes a larger specialist leaf;
- ordinary single-domain active context: at most 3,800 tokens;
- ordinary mixed context with up to three references: at most 7,000 tokens;
- any exceptional phase above three references: record required decisions,
  loaded tokens, and why staged reads could not preserve the outcome.

Route correctness and behavioral quality are hard gates. A shorter candidate
does not win by omitting needed ownership or knowledge.

The validator calculates the exact Core-plus-selected-expert total for every
required and conditional phase in the route matrix. If a row cannot fit, the
Plan must phase it or change a measured budget before W-007; the exceptional
path cannot become a routine workaround.

## Original pair preregistration

Every candidate Gold pair records before any model run:

- pair ID, author/custodian, date, fixture hashes, and split;
- shared brief, content, dimensions, medium, audience, and constraints;
- mutation class: functional, craft, concept, `generic-cliché`, production,
  exception, or true tradeoff;
- exact seeded change and affected rubric dimension;
- expected direction or explicit no-decisive-winner expectation;
- deterministic receipt where applicable;
- prevalidation reviewer count, votes, margin, rationales, and uncertainty;
- license/asset receipt for every included font, image, icon, template, and data
  item.

Concept and exception pairs without a preregistered valid margin are treated as
tradeoffs, not directional Gold.

`generic-cliché` pairs are directional only when the professional variant
preserves the same brief and required content while the seeded variant weakens
subject specificity or adds a preregistered, observed SOL default pattern.
Score concept specificity and cliché load separately from general preference.
Do not label an unconventional but coherent choice as slop merely because it
breaks a convention.

## Sealed holdout contract

The independent custodian records in the repository only:

- suite version, creation date, opaque case IDs, split membership;
- fixture and manifest hashes, rubric version, and near-duplicate/disjointness
  result;
- custodian identity or stable role and access ledger;
- holdout-internal duplicate check;
- later unseal date and reason.

Prompts, images, expected results, grader details, and source artifacts remain
outside the working repositories and unavailable to implementers and SkillOpt.
After Train and `valid_unseen` exist, the custodian checks cross-split
disjointness and near-duplicates without exposing holdout content and records
the receipt before optimization. A holdout authored, inspected, or predictable
by the Skill writer is not reported as implementation-unseen.

A priority lane with fewer than five sealed cases is reported as a smoke test,
not qualification. Domain-level claims additionally require sufficient open
Validation evidence; a 30-case holdout cannot establish specialist competence
across every mapped design domain merely by containing one example.

Execution and resume follow
[`resumable-holdout-execution-contract.md`](resumable-holdout-execution-contract.md).
ADR-0013 changes only canary, sharding, receipt, and pre-response transport
handling. ADR-0014 changes the next execution suite from historical SOL XHigh
to Terra High. Neither changes cases, arms, Gold, rubrics, package hashes, or
human-review rules.

## SkillOpt grader specification

Allowed optimization objectives:

- activation and route selection;
- one-owner composition and opt-out behavior;
- binding and functional requirements;
- factual/content/source fidelity;
- declared versus inferred exception behavior;
- evidence honesty and appropriate uncertainty;
- deterministic contrast, geometry, overflow, dimension, resolution,
  structure, asset, and production checks;
- context-token cost after every hard behavior gate passes.

Prohibited optimization objectives:

- model- or VLM-scored beauty, taste, originality, art direction, composition,
  typography quality, or overall aesthetic preference;
- a proxy that rewards verbosity, rubric-shaped language, or agreement with
  the same model that proposes candidates.

## Human visual review

For a cross-person improvement claim, use at least three independent relevant
reviewers. A design reviewer records either at least three years of relevant
professional practice or formal design study plus at least one year of applied
work. A domain reviewer may instead qualify through relevant production
practice, native-language/script competence, disability lived experience, or
other task-specific authority; the report names that basis. Reviewers may not
have authored the candidate or fixture. If only one reviewer is available,
report only that person's preference under the named rubric. Reviewers receive
the same brief and intended-size/context render, blind arm identity, randomized
left/right order, and no implementation rationale before voting.

W-008 module admission may use one qualified reviewer with a recorded
rationale because it creates no public visual-quality claim. W-005 remains the
only gate for cross-person improvement claims and requires the multi-reviewer
protocol above.

Record per dimension:

- brief fidelity and required content;
- functional communication and accessibility;
- concept specificity and memorability;
- style-term classification, historical/contextual fidelity, structural rather
  than signifier-only coherence, and avoidance of stereotype or unsupported
  cultural invention when a direction is named;
- executable style capability across generation, critique, repair, and
  medium translation; descriptive recognition alone does not pass;
- hierarchy and composition;
- typography;
- colour and imagery;
- interaction/workflow where relevant;
- production fitness where relevant;
- overall preference plus confidence and rationale.

For a multi-reviewer directional win, at least two thirds of non-abstaining
reviewers must prefer the same arm, the vote margin must be at least one third,
and no majority may identify a regression in a protected functional dimension.
Otherwise report no decisive winner. Preserve vote margin, disagreement,
abstention, and no-decisive-winner. Repair
success requires a blind improvement over the supplied artifact without a
regression in a protected dimension. Critique scoring measures observation
accuracy, localization, consequence, false positives, priority, uncertainty,
and preservation of strong choices.

Before the full run, pilot one functional pair, one craft pair, one deliberate
exception, and one true tradeoff. The report schema must preserve disagreement.

## Comparator parity

Freeze exact model, reasoning effort, host, tools, network state, prompt,
artifact inputs, time/context budget, repeat count, Skill/package hash, and
comparator commit for each arm. Preserve the unoptimized Design hash and the
current pre-rescope UI hash. Compare a public Skill only inside its declared
scope. Randomize output identity for human review. Report no-Skill,
pre-SkillOpt Design, optimized Design, current UI fallback, revised UI fallback,
composed Design+UI, and relevant competitor arms separately; use the old UI arm
only on scope-fair fallback/regression cases and do not average unrelated
domains into one rank.

Taste Skill is a required public comparator for landing-page, portfolio, and
existing-site redesign cases that fall inside its declared scope. Pin its exact
commit and the exact installed Skill hash before generation. Run its default v2
arm separately from any `gpt-taste` or `image-to-code` arm; do not treat the
suite as one interchangeable prompt. Do not include it in dashboard, dense
product-UI, data-table, multi-step-flow, native-mobile, static-graphic, print,
packaging, or general brand-system rankings that its main Skill does not claim.
Its public examples are demonstrations, not Gold, and its self-described
production-test rules do not replace the frozen human rubric.

## Local external comparison lane

In addition to original open and sealed cases, run the useful sourced
before/after and preference pairs identified by the research as a separate
local-only external-validation lane. No external image, screenshot, book page,
dataset row, prompt, or reconstructive output enters either repository or a
public evidence artifact.

Use each source only for the narrow claim its evidence supports:

- W3C BAD for its annotated functional accessibility barriers and repairs;
- the A. Dawn Journal pair for the source's alignment/hierarchy lesson;
- TASTE, UICrit, Vibe Design Arena, or comparable released datasets for
  preference/critique calibration only after item, screenshot, generator, and
  model-input terms are recorded in an external-material receipt;
- Apple RLDF and other NC/ND material only as unshared local evaluation or
  method reference when the exact use is permitted; no derived artifact or
  source-reconstructive result is published;
- commercial before/after books and previews as human learning/reference, not
  copied fixtures or model-training material.

Permitted external pairs may enter the SkillOpt `train` split with their
existing source/human labels after a use-specific receipt. They never enter
`valid_unseen`, the independent sealed holdout, or a qualification comparator;
after training they are diagnostics rather than independent evidence. Their
role cannot broaden a claim beyond the pair's source-defined criterion. Store
any permitted cache only under
`Z:\Projekts\AI\scoville-design-eval-local\external-pairs` and keep a receipt

Split external Train rows by source group and run exact, perceptual, semantic,
and prompt/content near-duplicate checks against all later splits. Record an
ablation with and without the external rows. Redact source bytes and
reconstructive model output from optimizer logs and public reports. The same
model may not create the aesthetic Gold it is optimized to satisfy.

## Benchmark defects

A suspected broken case is quarantined symmetrically across all arms. An
adjudicator other than the Skill author records the defect and evidence. Gold
is never edited in place after outcomes are known, and no replacement enters
the same frozen suite. A corrected case requires a new suite version and a full
rerun of affected comparisons.

## Claim templates

- Deterministic: “Package and routing contract passed N/N cases on these exact
  hashes.”
- Behavioral: “On model/host X, Skill arm Y improved or preserved dimension Z
  over control under rubric R.”
- Human single-reviewer: “Reviewer A preferred Y on N cases under rubric R.”
- Human multi-reviewer: report votes, margin, disagreement, confidence, and
  scope; never state universal design superiority.
- Unqualified domain: state the current maturity level and missing evidence.

Neither successful qualification nor competitor comparison is phrased as
objective market leadership. The personal ambition remains the development
direction.
