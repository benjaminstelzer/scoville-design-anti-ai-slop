# Research source: building a market-leading general design Skill

Date: 2026-09-01  
Status: internal canonical research source  
Derived records: `AUDIT-0001`, `PLAN-0001`, and `ADR-0001` through `ADR-0005`

## Research question

What knowledge, architecture, ownership model, and evidence are required to
build a standalone Agent Skill that can both create and evaluate high-quality
graphic, editorial, brand, web, and UI design, while composing safely with a
framework-focused Scoville UI Skill?

## Direct finding

No reviewed public Skill combines all required properties: general
graphic-design knowledge, original concept generation, typography and
composition depth, UI and interaction design, critical judgment, deliberate
rule exceptions, production awareness, source licensing, progressive
disclosure, standalone operation, optional family composition, and rendered
qualification. The strongest mechanisms are distributed across several Skills
and learning sources. The opportunity is not another style recipe; it is a
source-grounded design operating system whose claims remain tied to observable
results.

The recommended architecture is staged and broad-and-deep:

1. a compact artifact contract and multi-route Core;
2. a complete brief-to-concept-to-system-to-render-to-critique-to-revision
   cycle;
3. specialist knowledge loaded only when it can change the task;
4. cross-media stress for content, localization, accessibility, culture,
   sequence, production, and provenance;
5. qualification by domain, with no general superlative beyond controlled
   evidence.

## Evidence synthesis

### Public Skill landscape

Anthropic's [frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)
provides strong subject-grounded direction and critique, while its
[canvas-design](https://github.com/anthropics/skills/blob/main/skills/canvas-design/SKILL.md)
targets static artifacts. [Impeccable](https://github.com/pbakaus/impeccable)
has the most mature reviewed UI craft and critique routing.
[UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
demonstrates searchable design data. [Design Atelier](https://github.com/shaunandrews/agent-skills/blob/c6da55f4430422f2d46620f36e88c371727d72d7/skills/design-atelier/SKILL.md)
demonstrates a useful brief-to-reference-to-system workflow. The
[Vercel Web Design Guidelines Skill](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md)
demonstrates compact audit routing. Style-system collections demonstrate
packaging, but not general design intelligence.

[Taste Skill](https://github.com/Leonxlnx/taste-skill) is the strongest newly
identified direct anti-slop frontend comparator. Its useful mechanisms are
brief inference, variance/motion/density controls, honest design-system
mapping, audit-first redesign, mechanical preflight, and an optional
image-to-analysis-to-implementation pipeline. It is not a substitute for the
proposed general Design Skill: the current default is experimental, monolithic,
limited to selected frontend surfaces, combines design and implementation
ownership, and expresses many contextual preferences as fixed bans or numeric
recipes. Its repository examples are useful demonstrations, but no independent
benchmark or sealed holdout was found at the pinned research snapshot
`ccbc15639c97057cbfcf32ecebc38ef716e4bb37`; the published research folder
currently addresses LLM output laziness rather than design or typography
foundations.

Across the reviewed landscape, common weaknesses are UI-only scope, style
selection before problem definition, prescriptive taste rules, absent source
licensing, no distinction between source checks and visual proof, shallow
production knowledge, and critique systems that are stronger than generation.
The detailed comparison and limitations are recorded in the audit and source
ledger.

### Grounded knowledge base

[Graphic Design and Print Production Fundamentals](https://opentextbc.ca/graphicdesign/)
is the strongest directly reusable introductory backbone because it combines
process, formal elements, composition, grids, typography, colour systems, and
production under CC BY 4.0. John T. E. Richardson's open book
[The Legibility of Serif and Sans Serif Typefaces](https://link.springer.com/book/10.1007/978-3-030-90984-0)
is an essential corrective: the evidence does not support a universal
serif-versus-sans legibility winner; actual letterforms, spacing, size,
medium, users, and conditions matter.

[WCAG 2.2](https://www.w3.org/TR/WCAG22/) supplies scoped normative web
criteria, not a universal aesthetic checklist. The UK
[Government Design Principles](https://www.gov.uk/guidance/government-design-principles)
and [USWDS principles](https://designsystem.digital.gov/design-principles/)
ground UI decisions in needs, context, evidence, iteration, and coherent
systems. Open perceptual research such as the
[Gestalt review by Wagemans et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC3482144/)
supports grouping and organization concepts while warning against treating
descriptive mechanisms as numeric layout laws.

Mixed-license practitioner books remain valuable for learning but are not a
copy source. The source policy prefers CC BY 4.0, CC0, standards, and original
synthesis; screens ShareAlike material; and keeps NonCommercial,
NoDerivatives, and all-rights-reserved expression reference-only.

### Complete professional competency map

The [NASAD communication-design competencies](https://nasad.arts-accredit.org/wp-content/uploads/sites/3/2022/10/AD-BFA-CommunicationDesign-10-18-2022.pdf),
[ICoD professional guidance](https://www.theicod.org/resources/Professional-Code-of-Conduct/professional-performance),
[RGD AccessAbility](https://accessability.rgd.ca/), and
[AIGA Designer 2025](https://educators.aiga.org/aiga-designer-2025/) reveal
important gaps beyond attractive visual craft. An allround designer also needs:

- brief diagnosis, research, problem framing, alternatives, prototypes, and
  stakeholder rationale;
- semiotics, narrative, visual rhetoric, culture, representation, and ethics;
- information architecture, diagrams, data visualization, wayfinding, and
  spatial/distance conditions;
- temporal and sequential design, motion, transitions, and sound-aware
  coordination where relevant;
- content topology, localization, script coverage, language expansion, and
  semantic alternatives for non-visual access;
- production ecology across screen, print, export, colour, resolution,
  materials, packaging, and handoff;
- brand systems, governance, asset provenance, IP, privacy, sustainability,
  economic feasibility, and social consequence;
- collaboration, critique, explanation, and evidence-calibrated confidence.

The first implementation does not have to pretend equal production depth in
every specialist field. It must route the competence, expose its boundary, and
qualify each public claim.

### Rules and exceptions

Rules need authority types: binding constraint, functional floor,
evidence-backed default, craft heuristic, convention, and experiment. A
constraint is not waived by taste. A craft heuristic can be broken when the
intent is named, communication and accessibility survive, compensating
structure exists, the real artifact is inspected in context, and the whole
result is demonstrably stronger despite the cost. This avoids both mechanical
checklists and post-hoc rationalization.

### Design and UI ownership

When both Skills are active and applicable, Design owns design-system
definition, art direction, hierarchy, workflow arrangement, typography,
colour, spacing, imagery, and design critique. UI owns faithful framework and
incumbent-system implementation, components, tokens, responsive behavior,
interaction states, accessibility mechanics, and rendered interface proof.
An existing project system outranks both. UI retains a bounded Greenfield
fallback when Design is absent, inactive, inapplicable, or excluded. Neither
Skill depends on the other.

### Evidence limits

Current design benchmarks—including
[DesignProbe](https://arxiv.org/abs/2404.14801) and
[AesEval-Bench](https://arxiv.org/abs/2603.01083)—support using image-grounded
evaluation, but also document unresolved weaknesses in layout, fonts,
aesthetic judgment, and defect localization. Automated scoring can support
contrast, dimensions, overflow, or asset checks. It cannot prove that a design
is beautiful, appropriate, or production-ready. Representative artifacts must
be rendered and judged at intended size and context with a declared human
rubric.

### Comparative good/bad and before/after evidence

Useful same-task comparisons exist, but their rights and evidentiary strength
differ. The open chapter
[Technical Writing: Basic Design](https://openoregon.pressbooks.pub/technicalwriting/chapter/basic-design/)
contains a licensed same-page redesign. The
[W3C Before and After Demonstration](https://www.w3.org/WAI/demos/bad/)
provides annotated functional accessibility pairs for the same fictional site.
Commercial before/after books by Lisa Graham and John McWade provide strong
pedagogy but remain reference-only. Apple's
[designer-feedback work](https://github.com/apple/ml-rldf) contains rich
preferred/rejected and critique-to-revision pairs but its dataset is CC
BY-NC-ND. [TASTE](https://huggingface.co/datasets/purvanshi/TASTE) and
[UICrit](https://github.com/google-research-datasets/uicrit) provide broader
human preference or critique evidence with asset-level license caveats.

[DesignPref](https://arxiv.org/abs/2511.20513) reports low binary preference
agreement even among trained designers. Pairwise evaluation therefore cannot
collapse all visual judgment into one objective label. Tests must separate
functional Gold, craft judgment, subject-specific concept, and preference;
preserve vote margin and rationale; and allow a legitimate no-decisive-winner
result.

No third-party books, screenshots, comparison images, or datasets are stored in
the repositories. They remain cited research or, if actually inspected and
permitted, local-only material in a separate evaluation workspace. Decisive
tests use original same-brief pairs with seeded defects, deliberate good rule
breaks, and genuine tradeoffs. They score discrimination, critique, and repair
separately.

## Architecture derived from the evidence

The [Agent Skills specification](https://agentskills.io/specification) supports
progressive disclosure. The Core therefore owns activation/applicability,
authority and composed handoff, brief invariants, modes, typed rules, the
functional accessibility floor, exception timing, provenance/evidence gates,
and multi-route selection. Focused references own substantial domain
knowledge. Several references may be loaded for a mixed task; unrelated
references and the attribution source stay out of routine context. There is no
required sibling-Skill load, deep reference chain, or load-all route. The
proposed measured ceilings are 1,500 `o200k_base` tokens for Core, 3,800 for an
ordinary single-domain active context, and 7,000 for an ordinary mixed context
with up to three references.

Design behavior uses one generative and critical loop:

1. preserve constraints and inspect the actual artifact or brief;
2. diagnose purpose, audience, content, context, medium, and existing owners;
3. state a design hypothesis and limited materially different directions;
4. select and explain a direction using subject-specific reasons;
5. build hierarchy, typography, composition, colour, imagery, interaction, and
   production as one system;
6. render in representative states and contexts;
7. critique observed evidence by severity, function, tradeoff, and intent;
8. revise the whole, then validate source, access, media, and handoff claims.

## Qualification contract

Qualification separates discovery/routing, content and ownership, factual and
source fidelity, visual outcome, framework conformance, and evidence honesty.
The final holdout contract, opaque manifest, human-review protocol, pair schema,
comparator parity, and claim templates freeze before implementation; train and
`valid_unseen` freeze before SkillOpt proposals. SkillOpt may optimize routing,
ownership, functional, source, exception/evidence, deterministic production,
and context-cost objectives, but never a model/VLM aesthetic score. Visual
generation, critique, and repair outcomes require blinded human review at
intended size and context. Comparisons cover no-Skill, Design-only, UI-only,
composed, and relevant scope-fair public-Skill arms on exact hashes. Benchmark
defects are quarantined symmetrically and never repaired by editing frozen Gold
after outcomes are known.

## Risks and controls

| Risk | Control |
| --- | --- |
| Encyclopedic Core and wasted context | Compact Core, multi-route references, read-trace tests, measured context cost |
| Taste presented as law | Typed rules, scoped sources, counterexamples, explicit exception protocol |
| Arbitrary exception rationalization | Predeclared generated intent, documented/inferred/unknown existing intent, compensation, rendered control |
| Licensing contamination | Use-specific external-material classes, original synthesis, bundled attribution, separate source/asset receipts |
| UI ownership conflict | Observable applicability, concern-level precedence, compact handoff, incumbent system above both |
| Attractive demo mistaken for competence | Frozen comparator suite, multiple media, sealed holdout, human visual rubric |
| Specialist overclaim | Qualified-domain ledger and explicit boundaries |
| Western/Latin-script bias | Script, culture, localization, distance, and representation stress cases |

## Research limits and stop condition

The broad search covered public Agent Skills, open and accessible books,
typography, composition, accessibility, perception, professional curricula,
ethics, UI principles, licensing, design-model evaluation, comparative pairs,
brand systems, data visualization, scripts, motion, editorial work,
photography, wayfinding, packaging, and colour technology. Further broad search
results were predominantly mirrors, recipes, derivative bundles, or repeated
reading lists. Remaining gaps are maturity gaps: specialist art direction,
brand architecture, native-reader validation, current vendor production,
packaging fabrication, and human outcome evidence. The domain ledger bounds
them instead of filling them with unsupported rules.

## Records

- Full audit: `docs/audits/0001-design-skill-audit.md`
- Source and license ledger: `docs/research/source-ledger.md`
- Comparative reference assessment: `docs/research/comparative-reference-material.md`
- Domain maturity: `docs/research/domain-maturity.md`
- Pre-implementation evaluation contract: `docs/evaluation/preimplementation-contract.md`
- Durable implementation plan: `docs/plans/0001-build-and-qualify-scoville-design.md`
- Ownership, exception, source, disclosure, staged-capability, and qualification
  Decisions: `docs/decisions/0001-*.md` through `docs/decisions/0009-*.md`
