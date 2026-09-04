# Modular application architecture

Date: 2026-09-01  
Status: accepted pre-implementation synthesis  
Related: `ADR-0011`, `ADR-0012`, `PLAN-0001`

## Product priority

Scoville Design is evaluated as an applying designer, not as a design-history
encyclopedia. Its ordered outcomes are:

1. design;
2. distinguish strong, weak, defective, generic, and clichéd work;
3. improve through targeted rendered revision;
4. apply style DNA professionally and creatively;
5. use theory and history only when they change one of the first four.

## Three-layer mechanism

### Artifact-centred Studio Loop

The Core runs the same small loop across media:

```text
frame → form materially different hypotheses when needed → make → render
→ observe → judge → repair → verify
```

The loop may enter at critique or repair. It does not require a ceremonial full
process for a small task. A case-local Design Dossier records only consequential
brief invariants, design decisions, evidence, exceptions, render observations,
and unresolved risks.

### SOL Behavioral Delta Experts

GPT-5.6 SOL's existing knowledge is the baseline. Expert content is atomic and
classified as:

- `focus`: knowledge is present but inconsistently applied;
- `correction`: a repeatable shortcut, misconception, cliché, or failure needs
  counter-steering;
- `teaching`: sourced knowledge or procedure remains missing after smaller
  interventions fail;
- `external-verification`: current, project-specific, local, licensed,
  disputed, or otherwise unsafe-to-recall facts must be retrieved.

The package is profiled and qualified only on a frozen SOL configuration. It
does not speculate about hidden training data or claim other-model parity.

### Contrastive Style Compiler

A named style is converted into controllable decisions for structure,
typography, colour/light, image, material, rhythm, density, motion, and one
subject-specific signature. It also records nearest confusable directions,
false stereotypes, useful familiar signifiers, protected functional floors,
and target-medium translation.

History is retrieved only when it resolves identity, ambiguity, provenance,
anachronism, or repair. A request for recognizable “1980s neon/ASCII/VHS” may
use familiar signs strongly, but must still create a coherent subject-specific
system and survive hierarchy, typography, accessibility, and rendering checks.

## Package structure

```text
scoville-design-anti-ai-slop/
├── SKILL.md
├── modules.yaml
├── agents/openai.yaml
├── references/
│   ├── brief-and-concept.md
│   ├── composition-and-layout.md
│   ├── typography-and-writing-systems.md
│   ├── colour-and-reproduction.md
│   ├── imagery-and-art-direction.md
│   ├── information-and-data.md
│   ├── brand-and-visual-systems.md
│   ├── ui-and-interaction-design.md
│   ├── motion-and-sequence.md
│   ├── style-direction.md
│   ├── media-production-and-handoff.md
│   ├── critique-and-validation.md
│   ├── culture-ethics-and-provenance.md
│   └── sources-and-attribution.md
├── scripts/
│   ├── build-module-index.*
│   ├── validate-package.*
│   └── route-probe.*
└── tests/
    └── evaluation-cases.json
```

The final module set is determined by SOL baseline evidence. This tree is a
bounded initial map, not permission to fill every file with textbook prose.
Specialist style/history leaves are added only when a reproducible failure or
task requires them.

## Module manifest

`modules.yaml` is the only hand-edited routing source. At minimum, every module
declares:

```yaml
id: typography-and-writing-systems
path: references/typography-and-writing-systems.md
owns: [type-roles, typographic-hierarchy, typesetting]
capabilities: [generate, critique, repair, style-direction]
when_any: [text-primary, typography-requested, typography-defect-visible]
unless: [text-incidental-and-unchanged]
requires: []
conflicts: []
intervention_classes: [focus, correction, external-verification]
admission: retained-floor
source_ids: [L-01, L-02, L-04]
sol_evidence_ids: []
owner: scoville-design
last_reviewed: 2026-09-01
volatility: stable
```

A build script generates the compact direct module index inside `SKILL.md`.
The model therefore selects a set of direct references without following a
reference-to-reference chain. A validator rejects any generated-index drift.

Version one uses the exact module IDs accepted in ADR-0008 plus
`style-direction`. `requires` must be empty for every expert leaf; shared Core
gates replace transitive dependencies. `conflicts` must also be empty in
version one; applicability and the accepted owner ladder resolve selection.
`when_any` and `unless` values come from one enumerated signal catalogue in
`modules.yaml`. Unknown signals, non-empty dependencies/conflicts, duplicate
owners, and orphan files fail validation.

W-007 freezes this maximum map and its stable IDs. W-008 may not add, remove, or
rename an ID. It assigns one status:

- `admitted`: a demonstrated SOL behavioral delta;
- `retained-floor`: a sourced constraint, functional floor, provenance rule,
  or external-verification route that is not eligible for prompt ablation;
- `stub`: a bounded risk/owner/evidence route without specialist advice;
- `withheld`: not shipped or advertised in version one.

## Runtime routing

1. Activate Design only when the task requires design judgment or the user
   invokes it.
2. Classify operation modes, artifact, medium, implicated decisions, existing
   visual owner, constraints, supplied references, and evidence available.
3. Select all necessary experts, not the first matching expert.
4. Load declared requirements only; never load neighboring experts for
   completeness.
5. If required context exceeds the hard budget, narrow or phase the task rather
   than silently omitting expertise.
6. Synthesize expert moves through the Studio Loop and the user's brief.
7. Load provenance details only for verification, attribution, asset rights,
   or maintenance.

If a task needs more than three experts, divide it into named phases. Each
phase loads no more than three experts, carries forward only the compact Design
Dossier, and drops prior expert prose. Required knowledge is never silently
omitted to satisfy the budget.

## Expert payload contract

An expert module is description-only and must not ship unless it contains:

- scope, owner, non-owner, and activation signals;
- observable inputs and failure signatures;
- a decision procedure;
- generation actions;
- critique discriminators;
- repair operators;
- style-direction effects where applicable;
- rule strength, valid exceptions, and counterexamples;
- rendered or deterministic verification;
- source IDs and SOL behavioral evidence IDs;
- explicit unknowns and specialist escalation.

`critique-and-validation` owns only cross-domain method: observation order,
evidence types, prioritization, comparison, render checks, and uncertainty.
Typography, colour, layout, imagery, and other domain discriminators remain in
their owning experts.

The canonical operation modes are `generate`, `critique`, `repair`, and
`style-direction`. Briefing and definition are stages of `generate`;
`exception` is a gate, not a mode. Legacy uses of design/revision are aliases
only and are not valid manifest capability values.

## Extensibility

Extensions are build-time, namespaced leaf contributions using the same module
API. They cannot mutate the Core, create expert-to-expert chains, overwrite an
owner silently, or auto-discover other installed Skills. A new module is not
advertised until its source, SOL delta, routing, context cost, and operation
modes pass. Released contract versions are immutable and reversible.

## Required evidence

### Routing and context

- direct Skill-to-module paths only;
- all required and no forbidden module reads in host traces;
- single-, multi-, negative-, collision-, and missing-extension routes;
- exact UTF-8 and `o200k_base` payload counts;
- no claim about total cost or latency without end-to-end measurement.

### SOL delta

- no-Skill, Core-only, token-matched generic checklist, selected expert,
  full-bundle, wrong-expert, and expected-expert ablation controls;
- repeatable failure before a correction/teaching payload is admitted;
- shortest non-inferior payload retained;
- unseen target improvement without non-target regression;
- model or materially changed prompt/configuration invalidates the profile.

### Applied design

- separate lanes for generation, discrimination, critique, repair, and style
  execution;
- real editable artifacts through the appropriate format/tool owner plus
  rendered inspection, not advice alone;
- mechanical checks only for mechanical claims;
- blind human review for hierarchy, coherence, appropriateness, craft,
  recognizability, cliché load, and repair improvement;
- a capability-bounded mode when sources, evidence, or specialist knowledge are
  insufficient.

The Core permits at most two repair passes. Each pass repeats the same
observation list and protected-dimension checks. Stop earlier when no material
defect remains, evidence is missing, the requested change is preference-only,
or the next pass would repeat a failed move. Any unresolved regression or risk
is reported rather than rationalized.

## Artifact and render contract

| Artifact class | Preferred source | Proof surface |
| --- | --- | --- |
| Web or UI | HTML/CSS/framework source; UI owns framework implementation when active | Browser screenshots at required viewports and states |
| Vector graphic, logo, icon, diagram | SVG or other tool-native vector source | Raster preview at intended size plus vector/source inspection |
| Raster illustration or generated image | Original PNG/TIFF or tool-native source when available, plus art-direction/provenance record | Original-size image inspection and target-crop previews |
| Presentation | PPTX or tool-native slide deck | Per-slide renders and representative projected/small-screen views |
| Document, report, form, or template | DOCX or tool-native editable document; PDF only when fixed output is the actual deliverable | Page renders plus source/structure checks |
| Print/fixed layout | Editable source where the format tool supports it plus print PDF | Rasterized proof, dimensions, trim/bleed/safe-area and production checks |
| Motion | Tool-native source when available plus MP4/GIF or target export | Key frames and real-time playback with reduced/static alternative where applicable |

When a renderer or format owner is unavailable, produce the best authorized
source artifact, mark visual quality `unverified`, name the missing proof, and
ask for a render or appropriate tool. Source inspection never substitutes for
seeing the artifact. Format Skills own their native files and deterministic
render helpers; Design owns the art direction and visual judgment.

## Design-to-UI record

For consequential composed work, Design emits the ADR-0006 fields as a compact
portable block in the response or a user-authorized project record:

```yaml
schema: scoville.design-direction/v1
concern: ...
decision: ...
intended_effect: ...
authority_and_source: ...
preserved_constraints: [...]
allowed_variation: [...]
exception_and_compensation: null
validation_target: ...
evidence_status: ...
```

UI consumes it only when it is present in current context or a named project
file. Neither Skill searches for or requires the other.

## Honest boundaries

- A complete competency map is not proof of complete competence.
- A model explaining a rule is not proof it can apply it.
- Self-critique is not independent visual evidence.
- A smaller selected payload is not proof of lower total cost.
- Qualification on SOL is not qualification on Fable or Opus.
- A style can be recognizable and still be badly designed; both dimensions
  must pass.
