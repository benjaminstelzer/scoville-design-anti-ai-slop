# Stage-two Skill comparison: Web and responsive design

Date: 2026-09-02  
Capture: 2026-09-02T14:33:27Z  
Target: proposed `web-and-responsive-design` medium leaf  
Method: `reference-audit-method.md`, Stage two

Local decision inputs: [medium architecture question](../medium-architecture-question.md),
[UI and interaction expert-depth audit](../reference-audits/ui-and-interaction-design.md),
and [external-mechanism adoption priority](../adoption-priority.md).

This is a bounded current GitHub and public-Skill comparison. A repository was
ranked by captured GitHub stars only after it supplied an exact Skill or a
directly usable responsive-web instruction, plus E1 or higher evidence. A Skill
that only mentions mobile support inside a broad frontend or UI catalog did not
qualify. Stars remain a repository-popularity signal. They do not prove that the
exact Skill was installed, followed, rendered, accepted, or independently
preferred.

## Decision

The three star-ranked qualifiers are `pbakaus/impeccable`,
`sickn33/agentic-awesome-skills`, and `wshobson/agents`.

Only Impeccable provides a named adaptation workflow. `design-spatial` qualifies
narrowly because it supplies an exact multi-width web-layout audit and repair
mechanism, not because it teaches responsive recomposition. `responsive-design`
is an exact implementation tutorial with worked code, but it does not establish
the design intent that the proposed Scoville leaf must own.

No ranked candidate fully covers the required professional mechanism:

1. identify content, task, type, spatial, crop, state, and access invariants
   before changing layout
2. locate pressure from real content and use conditions rather than device names
3. select a subject-specific transformation instead of scaling or applying a
   stock mobile pattern
4. preserve or deliberately revise hierarchy, typesetting, spacing rhythm,
   negative-space function, reading order, and crop meaning
5. hand framework mechanics and runtime proof to Scoville UI without giving up
   Design ownership of the intended transformation

The proposed `web-and-responsive-design` leaf should therefore use an original
transformation contract. It should adapt Impeccable's context comparison,
`design-spatial`'s localized failure evidence, and `responsive-design`'s
container and intrinsic-layout vocabulary. It must reject their device grids,
fixed visual recipes, framework dependencies, and quality overclaims.

## Qualification and star ranking

Evidence levels follow the audit method. E1 means an inspectable example or
output artifact. E2 means a reproducible test, evaluation, or deterministic
check. E3 requires relevant independent evaluation or external adoption
evidence. Tests and scripts were inspected, not executed in this comparison.

| Rank | Repository and exact path | Stars at capture | Pin, activity, and latest relevant update | License and asset boundary | Evidence level and demonstrated scope |
| --- | --- | ---: | --- | --- | --- |
| 1 | [`pbakaus/impeccable`, `skill/reference/adapt.md`](https://github.com/pbakaus/impeccable/blob/c0f495212236129c2e92aaf7714a3a9914569d13/skill/reference/adapt.md) | 64,894 | Active, not archived. Repository pin `c0f495212236129c2e92aaf7714a3a9914569d13`, pushed 2026-09-02. The web adaptation reference last changed in [`c11cc7b58ce69c0723b2c7eb804a45279d06c52e`](https://github.com/pbakaus/impeccable/commit/c11cc7b58ce69c0723b2c7eb804a45279d06c52e) on 2026-07-09. | Root [Apache-2.0](https://github.com/pbakaus/impeccable/blob/c0f495212236129c2e92aaf7714a3a9914569d13/LICENSE). The exact reference contains no bundled image or font asset. Repository-authored scripts and fixtures follow the root license. Project content, third-party fonts, images, and test devices keep their own rights. | **E2, bounded.** The reference has inspectable CSS and HTML examples. Browser-detector tests and an inspectable [`first-viewport-column-overflow` fixture](https://github.com/pbakaus/impeccable/blob/c0f495212236129c2e92aaf7714a3a9914569d13/tests/fixtures/antipatterns/first-viewport-column-overflow.html) provide reproducible evidence for selected checks. This proves mechanism and detector behavior for named cases, not good responsive hierarchy, crop choice, spacing, or general visual quality. |
| 2 | [`sickn33/agentic-awesome-skills`, `skills/design-spatial/SKILL.md`](https://github.com/sickn33/agentic-awesome-skills/blob/7eb694978762421c30855d80de73d1a909a8c335/skills/design-spatial/SKILL.md) | 45,855 | Active, not archived. Repository pin `7eb694978762421c30855d80de73d1a909a8c335`, pushed 2026-09-02. Skill metadata last changed in [`df08c3f9cad7dec3aff91914a3cf6fb1e810a52c`](https://github.com/sickn33/agentic-awesome-skills/commit/df08c3f9cad7dec3aff91914a3cf6fb1e810a52c) on 2026-07-29. The audit script entered in [`72ea16f0b7fbf4ec65c3bcf645d608f47380ed59`](https://github.com/sickn33/agentic-awesome-skills/commit/72ea16f0b7fbf4ec65c3bcf645d608f47380ed59) on 2026-07-01. | Root [MIT](https://github.com/sickn33/agentic-awesome-skills/blob/7eb694978762421c30855d80de73d1a909a8c335/LICENSE). Skill frontmatter names the MIT upstream `connerkward/ckw-design-skill`. The exact directory bundles one JavaScript audit, not visual assets. The aggregation repository's license and stars do not establish independent authorship or adoption of the mirrored Skill. | **E2, audit only.** [`layout-audit.js`](https://github.com/sickn33/agentic-awesome-skills/blob/7eb694978762421c30855d80de73d1a909a8c335/skills/design-spatial/scripts/layout-audit.js) is a reproducible deterministic browser check and overlay for overflow, collision, contrast, target size, alignment, spacing variation, and balance. The Skill requires screenshots at several widths. No included output fixture, false-positive study, responsive-generation evaluation, or independent visual review was found. |
| 3 | [`wshobson/agents`, `plugins/ui-design/skills/responsive-design/SKILL.md`](https://github.com/wshobson/agents/blob/a30778f8c4e6b0a87567941b7cca4f534bf642b6/plugins/ui-design/skills/responsive-design/SKILL.md) | 39,351 | Active, not archived. Repository pin `a30778f8c4e6b0a87567941b7cca4f534bf642b6`, pushed 2026-09-01. The Skill and consolidated worked examples last changed in [`be57c0b2e3c05c528ca6132b87410b385718775f`](https://github.com/wshobson/agents/commit/be57c0b2e3c05c528ca6132b87410b385718775f) on 2026-05-22. Three deeper references last changed in `56848874a27cf0812b20a067ff3cf4eb8e0a7858` on 2026-01-19. | Root [MIT](https://github.com/wshobson/agents/blob/a30778f8c4e6b0a87567941b7cca4f534bf642b6/LICENSE). The exact Skill directory contains Markdown and code examples, with no bundled image, font, or evaluation asset. Framework and browser support claims remain external facts, not licensed assets or verified outputs. | **E1.** [`details.md`](https://github.com/wshobson/agents/blob/a30778f8c4e6b0a87567941b7cca4f534bf642b6/plugins/ui-design/skills/responsive-design/references/details.md) and the breakpoint, container-query, and fluid-layout references contain inspectable CSS, React, and Tailwind examples. They prove example coverage only. No exact-Skill render, behavior test, visual evaluation, or independent review was found. |

## Candidate 1: Impeccable `adapt`

### Claimed scope and observed mechanism

The command begins with source context and target context. It asks about device,
input, screen, connection, use situation, and platform expectations before
choosing a strategy. Its central instruction is correct: adaptation is a new
context decision, not pixel scaling. It then offers layout, interaction,
content, and navigation changes for mobile, tablet, desktop, print, and email.
The web section adds content-driven breakpoints, pointer and hover queries, safe
areas, responsive image selection, art-directed `<picture>` crops, and real-
device checks.

### What is better than the current proposed leaf input

- Source-versus-target assumptions are explicit instead of hidden inside a
  viewport list.
- Input capability, connection, orientation, and use context are first-class
  pressures rather than afterthoughts.
- Art-directed sources distinguish crop or composition change from resolution
  selection.
- The command names preservation failures such as hover-only operation, lost
  core functionality, and blind device breakpoints.
- Real-device and browser differences stay outside screenshot-only confidence.

### Adoption-priority result

The context comparison is worth adopting. The transformation advice is mostly
generic. It does not require a type-role and measure decision, relationship-
specific spacing, negative-space function, focal hierarchy, protected reading
order, crop subject, or state invariant before moving elements. A page could
obey the command and still become a conventional single-column stack with weak
hierarchy and no subject-specific character.

### Reject or bound

- Reject 320/768/1024 categories, three-breakpoint expectations, universal
  44-pixel targets, 16-pixel text, 600-pixel email width, and fixed device
  testing lists as Design rules. Use the applicable standard, platform,
  incumbent system, actual content, and current support evidence.
- Reject automatic single-column mobile, two-column tablet, bottom navigation,
  hamburger navigation, sticky header, sidebar persistence, and card-converted
  tables. Each is an alternative whose task, content, state, and access
  consequences must be compared.
- Reject "do not use different information architecture" as a universal.
  Navigation and disclosure may change while the domain model, required
  content, task, and findability remain coherent.
- Keep print and email outside this leaf. They need independent medium
  contracts and proof owners.
- Do not let Design claim browser, input, or interaction proof merely because
  the command lists devices. When Scoville UI is active, UI owns that runtime
  evidence.

## Candidate 2: mirrored `design-spatial`

### Claimed scope and observed mechanism

The Skill demands rendered screenshots at several widths, an intentionally
fresh critique, a narrow-width overflow check, DOM localization of offending
elements, repair, and another render. Its deterministic script returns JSON
and adds visual overlays. It distinguishes hard gates, likely defects, and
aesthetic signals, although it then overstates several metrics as objective.

The strongest responsive contribution is diagnostic. It names common parent
causes for horizontal overflow, including `100vw`, non-shrinking flex or grid
children, unbreakable strings, fixed widths, negative margins, and edge-pinned
absolute content.

### What is better than the current proposed leaf input

- A failure is localized in the actual render instead of remaining a generic
  "check mobile" instruction.
- The render, inspect, repair, and rerender loop is operational.
- Narrow intermediate widths are tested, not only nominal endpoint devices.
- DOM evidence can distinguish a parent sizing failure from a cosmetic child
  symptom.
- The Skill explicitly says deterministic gates are insufficient for visual
  quality.

### Adoption-priority result

The mechanism can detect overflow and some geometry. It cannot decide whether
the hierarchy survives, whether a line break weakens meaning, whether spaces
separate or pace correctly, whether an image crop protects its subject, or
whether an alternate dense-data representation preserves the task. The script
does not supply responsive recomposition. It supplies evidence after an owner
has defined the intended transformation.

### Reject or bound

- Reject "no horizontal overflow, no exceptions." Tables, maps, editors,
  timelines, comparison surfaces, and canvases can require bounded
  two-dimensional access.
- Reject blanket `overflow-x: clip`. It can hide required content and does not
  repair the parent cause.
- Reject fixed target sizes, collision percentages, alignment tolerances,
  spacing coefficients, optical centers, and balance bands as universal
  verdicts.
- Reject a separate judge as a mandatory dependency. Use an independent review
  when available and retain an honest single-agent path.
- Treat an overlay as a locator, not a Design decision. Geometry cannot infer
  semantic hierarchy, cultural reading, perceived weight, useful asymmetry,
  negative-space purpose, or crop meaning.
- Browser scripting, responsive mechanics, focus/input behavior, and runtime
  proof belong to Scoville UI when it is active.

## Candidate 3: `responsive-design`

### Claimed scope and observed mechanism

The Skill routes to worked examples for container queries, fluid type and
spacing, Grid, Flexbox, intrinsic sizing, responsive navigation, tables,
images, feature queries, reduced-motion preferences, and breakpoint tests. Its
best rule says to find breakpoints where content fails. It also distinguishes
component container pressure from page viewport pressure.

### What is better than the current proposed leaf input

- Progressive disclosure separates a compact trigger from detailed technique.
- Container queries and intrinsic layouts make component context explicit.
- The breakpoint reference includes a small script for locating content
  overflow rather than selecting a device name first.
- The references cover art-directed image sources, logical properties,
  reduced-motion and reduced-data preferences, and several dense patterns.
- Worked CSS and React examples make the implementation vocabulary concrete.

### Adoption-priority result

The examples are implementation recipes. Fluid type and spacing are calculated
from numeric endpoints without asking whether the type roles, measure,
line breaks, group relations, or focal hierarchy remain correct. Container
queries change layout at widths, but the Skill does not define what content,
task, state, reading order, crop, or negative-space relationship must survive.
The result can be technically adaptive and still look compressed, generic, or
compositionally incoherent.

### Reject or bound

- Reject its common breakpoint scale, fixed grid columns, minimum card widths,
  fluid scales, viewport ranges, and target sizes as portable Design rules.
- Reject mobile-first as a mandatory creative process. Output should work from
  constrained conditions upward, but the design process may begin from the
  dominant use context, the hardest state, a content model, or parallel
  compositions.
- Reject automatic clamp-based type and spacing. Values must serve actual
  copy, role, measure, leading, relationship, density, and intended tension.
- Reject implementation ownership in the Design leaf. It can name container
  versus viewport intent and acceptable transformations, but framework tokens,
  queries, components, semantic behavior, and browser proof belong to UI.
- Do not infer accessibility from logical properties, a preference query, or
  target-size advice. Reflow, zoom, keyboard, focus, announcements, contrast,
  language expansion, and assistive use require applicable proof.

## Weighted adoption comparison

| Required concern | Impeccable `adapt` | Mirrored `design-spatial` | `responsive-design` | Decision for Scoville Design |
| --- | --- | --- | --- | --- |
| Content-pressure recomposition | Compares source and target contexts, then chooses familiar target patterns. It rarely derives changes from actual content relationships. | Detects narrow-width symptoms and parent CSS causes. It does not design the replacement composition. | Uses content breakage and container width, but examples mainly switch columns or directions. | Require an explicit pressure map, preserved invariants, alternatives, and a selected transformation with a disconfirming condition. |
| Typography | Mentions larger text, fluid values, and responsive images, with little typesetting analysis. | Detects a few text-size or overflow symptoms but cannot judge type roles or line quality. | Provides fluid type formulas and fixed scales without actual copy analysis. | Shared Typography owns roles, face choice, measure, leading, breaks, tracking, and fallback. The web leaf owns how accepted type relationships persist or change under pressure. |
| Spacing and negative space | Mostly asks for more touch spacing or a target layout pattern. | Measures variation and balance but cannot infer relationship or negative-space function. | Supplies fluid spacing tokens and gaps without subject meaning. | Preserve within-group, between-group, section, edge, and sequence relations. Name whether space separates, paces, frames, directs, or intensifies before changing it. |
| Hierarchy and reading order | Prioritizes content but can collapse priority into hiding or disclosure recipes. | Fresh critique can notice a weak focal point, while metrics cannot establish semantic order. | Grid and navigation examples alter presentation but do not record hierarchy invariants. | Record importance, narrative, task, visual, source, focus, and announcement order separately. Transformation must preserve or intentionally reconcile them. |
| Crop and media preservation | Best of the three. It distinguishes resolution selection from art-directed crop sources. | Can notice bounds and overflow, not subject loss or crop meaning. | Provides responsive-image syntax and aspect-ratio examples, with little art-direction reasoning. | Record protected subject, focal relationship, acceptable crop envelope, alternate source need, intrinsic dimensions, and proof at affected contexts. |
| Accessibility | Covers input capability and real devices, but uses several fixed targets and patterns. | Offers useful overflow and contrast checks, with overbroad gates. | Includes logical properties and user-preference queries, but not a complete access contract. | Design preserves access intent and specifies targets. UI owns semantic, focus, input, announcement, reflow, zoom, and runtime evidence when active. Neither automated checks nor screenshots establish conformance or usability. |
| Subject-specific character | Context questions can preserve an existing world, but the transform library is generic. | Can warn against bland averages, with no responsive subject examples. | Generic component recipes dominate. | Responsive work must retain the concept's distinguishing type, spatial, image, rhythm, density, and interaction relationships. A recognizable stock mobile pattern is not a successful translation by itself. |
| Evidence | Best combined examples and deterministic fixtures, but no responsive-quality evaluation. | Best localized runtime evidence, but no validated false-positive rate or responsive-generation test. | Worked code only. | Combine a predeclared transformation record, multi-context renders, runtime evidence from UI, and bounded human judgment. Keep every unrun claim `Not verified`. |

## Stronger recomposition mechanism below the star cutoff

`jakubkrehel/skills` had 4,756 stars and therefore ranked below the three
qualifiers. Its exact [`better-layout` Skill](https://github.com/jakubkrehel/skills/blob/267330e1adfc66a718fb65fa6918c1f06d0a689e/skills/better-layout/SKILL.md)
is E1. Its two progressive references give inspectable good and bad code for
content-driven breakpoints, container queries, long and unbreakable content,
pseudo-localization, RTL mirroring, safe areas, overflow, grouping, shared
edges, and `Not verified` states.

This lower-star candidate is more useful for pressure testing than the ranked
implementation tutorial. It still does not prove rendered visual quality,
typesetting, negative-space causality, crop preservation, or several subject
types. Adapt its stress conditions and unknown-state reporting, not its fixed
spacing ratios, action rules, margins, clearances, or pattern preferences.

## Direct contract implications for `web-and-responsive-design`

### Route boundary

Route this leaf only when a task asks for responsive web intent, cross-width
web composition, narrow or wide adaptation, reflow, content pressure,
container-driven transformation, responsive image or crop intent, responsive
navigation intent, or critique and repair of those concerns.

Do not route it for:

- a fixed poster, print page, slide, social image, packaging face, or other
  fixed-ratio artifact
- a native application flow without a web-responsive concern
- framework breakpoint syntax, CSS implementation, component semantics,
  focus/input, announcements, browser testing, or runtime proof alone
- typography, composition, imagery, colour, or accessibility in isolation
- generic requests for polished, modern, mobile-friendly, or accessible output
  without an actual web transformation concern

A responsive marketing or editorial page commonly loads this leaf plus
Composition, Typography, and Imagery. A responsive application flow commonly
loads this leaf plus `ui-workflow-and-interaction-design`. A task requesting
framework implementation or proof also activates Scoville UI, which keeps its
own standalone fallback when Design is absent or inapplicable.

### Required transformation record

Before proposing widths or queries, the leaf should produce the smallest useful
record:

1. **Source condition:** actual container or window, content, state, input,
   language, zoom or text scale, orientation, and incumbent system.
2. **Pressure signature:** the first observable loss, such as broken measure,
   weak hierarchy, crop damage, trapped space, collision, ambiguous order,
   lost state, or task blockage.
3. **Preserved invariants:** required content, task, state, recovery, access,
   type roles, essential reading order, spatial relations, concept character,
   and protected crop subject.
4. **Candidate operators:** reflow, reorder, regroup, split, disclose, replace,
   wrap, scroll within a bounded surface, change density, change navigation,
   change media source or crop, or alter line and space behavior.
5. **Selected transformation:** why it resolves the pressure while preserving
   the invariants, plus the condition that would disconfirm it.
6. **Allowed variation:** what may legitimately differ by context, including
   density, measure, line breaks, crop, disclosure, navigation, or interaction
   presentation.
7. **Proof target and owner:** what Design must judge visually and what UI must
   implement and prove at runtime.

Breakpoints follow the accepted transformation. They do not define it.

### Content-pressure matrix

The leaf should inspect only applicable pressure lanes:

| Pressure lane | Design question | Required preservation or deliberate change |
| --- | --- | --- |
| Content and language | What fails with real short, long, translated, dynamic, missing, error, or unbreakable content? | Preserve meaning, task, state, and useful hierarchy. Change measure, wrapping, grouping, disclosure, or container only with a named consequence. |
| Type and reading | Which role, measure, line break, leading, paragraph rhythm, or annotation relationship fails first? | Preserve typographic role and reading continuity. Refit type relationships through the Typography expert, not a generic clamp scale. |
| Space and density | Which within-group, between-group, section, edge, or sequence interval loses its function? | Preserve grouping and intended tension. Do not make every interval smaller or add uniform whitespace. |
| Hierarchy and order | Do importance, narrative, task, visual, source, focus, and announcement orders still agree where they must? | Preserve completion and comprehension. Reconcile deliberate visual reorder with semantic and interactive order through UI. |
| Image and crop | Does the protected subject, relation, gesture, label, or contextual clue survive? | Choose crop, aspect behavior, or alternate source through Imagery. Do not rely on `object-fit: cover` as art direction. |
| Navigation and action | Does the task, current location, primary action, status, and recovery remain available? | Change the pattern only after comparing disclosure cost, recurrence, state, and incumbent support. |
| Dense and two-dimensional content | Can the content reflow without destroying comparison, scale, topology, or manipulation? | Permit bounded horizontal interaction, alternate views, detail expansion, or task-specific reduction. Never hide required content to satisfy an overflow screenshot. |
| Capability and environment | What changes under keyboard, touch, pointer, hover absence, orientation, safe area, reduced motion or data, slow delivery, zoom, and text scaling? | Design specifies the intended accessible consequence. UI selects supported mechanics and records runtime proof. |

## Failure to cause to repair and proof

| Failure signature | Likely parent cause to test | Smallest Design repair | Required proof and owner |
| --- | --- | --- | --- |
| Desktop composition merely becomes one long narrow stack | No content hierarchy or transformation decision was made before stacking | Rebuild groups from task, narrative, and content relationships. Compare regroup, reorder, disclosure, and alternate pattern options. Preserve concept character. | Design compares populated renders for hierarchy, rhythm, and task continuity. UI proves source, focus, state, and interaction behavior. |
| Headline wraps into an accidental weak shape or overwhelms the narrow view | Type size was fluidly scaled without role, measure, copy, or line-break control | Return to Typography. Set role, measure, preferred break opportunities, size and leading relationship, then recompose adjacent elements. | Design inspects actual copy at affected contexts. UI proves zoom and text-scaling behavior. |
| Every gap shrinks uniformly and groups become ambiguous | One spacing ramp replaced relationship-specific spacing | Restore within-group, between-group, section, edge, and sequence roles. Change only the pressure-causing intervals. | Design compares grouping, rhythm, trapped gaps, edge tension, and intended density in renders. |
| Narrow layout has unused decorative emptiness while key content is cramped | Negative space was treated as a global amount rather than a function | Reassign space to separation, pacing, framing, direction, or intensification. Remove emptiness with no observable role. | Design judges focal path and content pressure at intended sizes. No numeric whitespace score is sufficient. |
| Image remains technically responsive but loses its subject or meaning | Resolution switching or `cover` was mistaken for art direction | Protect subject and relationship, define an acceptable crop envelope, or request an alternate source and composition. | Design and Imagery inspect the actual crop at affected contexts. UI proves source selection and intrinsic sizing. |
| Toolbar, tabs, labels, code, or data create horizontal overflow | Parent cannot shrink, content is unbreakable, edge content is pinned outward, or the surface is inherently two-dimensional | Repair the parent sizing or wrapping rule. If two-dimensional access is essential, define a bounded scroll or alternate representation with preserved orientation and task. | UI measures the affected containers at content-pressure points and tests keyboard, touch, focus, and announcements. Design judges whether the alternate representation preserves the task. |
| Mobile navigation hides orientation, state, or a recurring action | A familiar compact pattern was chosen without modeling frequency, location, disclosure cost, and state | Compare persistent, disclosed, local, search, or task-specific alternatives against the incumbent system and actual workflow. | Design walks entry to completion and interruption. UI proves focus, dismissal, deep-link, back, and announcement behavior. |
| Visual order changes but keyboard or reading order becomes incoherent | CSS reordering or placement was used without a semantic-order contract | Align source order with the stable task and reading sequence. Use visual variation only where UI can preserve programmatic and focus meaning. | UI inspects the accessibility tree, focus order, announcements, and interaction. Design judges intended reading and emphasis. |
| Layout passes endpoint screenshots but fails between them or under localization | Device endpoints replaced continuous content-pressure inspection | Sweep meaningful container ranges and stress real long, translated, dynamic, and error content. Add a transform only where a failure begins. | UI supplies viewport and container evidence plus content fixtures. Design reviews the first-failure and repaired states. |
| Incumbent framework cannot express the accepted transformation | Design silently changed intent to fit available components | Keep the intended effect and record the exact system gap, constraint, allowed variation, and validation target. | UI reports supported alternatives or an owner-level extension. Design accepts a changed intent only through the canonical decision record. |

## Mechanisms to synthesize and claims to withhold

### Adopt through original Scoville wording

1. Compare source and target assumptions before selecting a responsive move.
2. Find pressure with real content, container ranges, language expansion, zoom,
   orientation, state, input, and environment rather than device names.
3. Separate viewport, container, intrinsic-content, capability, and user-
   preference causes before choosing mechanics.
4. Record preserved invariants and candidate transformation operators before
   breakpoints or code.
5. Use deterministic overlays and DOM measurements as failure locators. Keep
   visual, task, crop, type, and spacing judgment with Design.
6. Distinguish resolution selection from art-directed source or crop change.
7. Render, inspect, repair, and rerender. Preserve explicit `Not verified`
   status for every unrun condition.
8. Use framework implementation feedback to refine the Design record without
   silently transferring design-system authority to UI.

### Retain or add beyond all three candidates

- type roles, actual-copy measure, leading, line breaks, paragraph rhythm, and
  fallback behavior from Typography
- within-group, between-group, section, edge, and sequence spacing from
  Composition and Typography
- negative space as separation, pacing, framing, direction, or intensification
- subject-specific hierarchy, counterstructure, density, rhythm, and expressive
  exceptions rather than a generic clean mobile shell
- protected crop subject, acceptable crop envelope, and alternate-source intent
  from Imagery
- distinct importance, narrative, task, visual, source, focus, and announcement
  orders
- required content, state, recovery, permission, and access invariants
- a canonical Design/UI record with proof ownership and unverified mechanics

### Reject from the executable package

- device grids and named phone, tablet, or desktop widths as universal rules
- fixed column counts, card widths, margins, safe areas, spacing scales, type
  scales, touch targets, line lengths, and testing matrices without applicable
  authority and context
- automatic single-column stacking, hamburger menus, bottom navigation, card
  conversion, sticky controls, or hidden secondary content
- framework-specific Tailwind, React, Bootstrap, or CSS syntax in the Design
  leaf
- automatic `clamp()` for type or spacing without actual-copy and relationship
  analysis
- blanket overflow clipping and universal no-overflow gates
- pixel balance, spacing variation, collision, or detector totals presented as
  hierarchy or taste
- one screenshot per named device presented as responsive, accessible, usable,
  or complete proof
- mandatory browser, external catalog, live network, or second-agent dependency
  for normal Design operation

## Test and evidence implications

The smallest decision-changing open Terra High set for this leaf should use the
same real content and incumbent system in each arm:

1. **Generate:** a responsive editorial or marketing page with distinctive
   type, imagery, asymmetry, and long localized content. Require preserved style
   DNA, type and spatial invariants, crop decisions, and non-generic narrow and
   wide compositions.
2. **Critique:** a polished desktop and mobile pair that passes overflow checks
   but loses hierarchy, grouping, measure, negative-space function, crop
   meaning, and task continuity. Require observation to cause to parent repair.
3. **Repair:** a desktop-only application workflow with dense data, error and
   partial states, long labels, 400 percent zoom or reflow, keyboard and touch,
   and an incumbent component system. Require a Design transformation record
   and UI-owned implementation proof.
4. **Route:** responsive content page loads this leaf plus only needed shared
   visual experts. Native interaction loads no web leaf. Fixed print loads no
   web leaf. Framework-only implementation loads UI. A responsive form can load
   web, interaction, and UI without duplicate ownership.

Deterministic checks can verify route/read trace, preservation fields, no new
claims, no fixed breakpoint prescription, no hidden required content, and
stable Design/UI ownership. Rendered review must inspect first-failure widths,
intermediate containers, short and long content, localization, zoom and text
scaling, relevant states, themes, orientation, and crops. UI owns the runtime
trace. Qualified human review remains necessary for task fit, hierarchy,
typesetting, spacing, negative space, image meaning, and subject-specific
character.

Passing this set would support only the tested model, prompts, content, media,
and failure families. It would not establish usability, accessibility
conformance, preference, conversion, framework compatibility, or superiority
across untested products, users, languages, browsers, devices, and conditions.

## Search exclusions and limits

- `nextlevelbuilder/ui-ux-pro-max-skill` had 124,153 stars. It contains broad
  UI and styling Skills plus responsive references and infrastructure tests,
  but no dedicated responsive-web Design Skill or exact responsive visual
  evaluation was found. Broad catalog coverage did not meet the exact-domain
  rule.
- `addyosmani/agent-skills` had 91,636 stars. Its frontend UI engineering Skill
  and general eval suite are broader than responsive recomposition. No exact
  responsive leaf with an exact E1 output or evaluation was found.
- `vercel-labs/agent-skills` had 30,745 stars. `web-design-guidelines` is broad
  review guidance rather than a responsive recomposition Skill, and no exact
  responsive output evidence was found.
- `fengshao1227/ccg-workflow` had 5,869 stars and an `adapt/SKILL.md` derived
  from Impeccable. The exact directory contains one instruction file, no code
  example fence, output, fixture, test, or visual artifact. It remains E0 and
  cannot displace a qualifier. Repository stars also do not provide independent
  evidence for the mirrored mechanism.
- `jakubkrehel/skills` and `am-will/codex-skills` qualified at E1 but ranked
  below the three selected repositories by stars. The latter also hardcodes
  device widths, columns, type sizes, and target sizes, and GitHub exposed no
  root license for the captured revision.
- Flutter-specific responsive Skills were excluded because this medium leaf is
  for web design. Native adaptive design remains a separate route question.
- Public search used authenticated GitHub code, repository, contents, tree, and
  commit APIs, plus web search. Code search was capped per query and ranking was
  frozen at the capture timestamp. Private, renamed, deleted, poorly indexed,
  non-English, registry-only, and newly published Skills may be absent. The
  comparison does not claim global exhaustiveness.

The cheapest next evidence is the three-case Terra High generation, critique,
and repair set above, with blind artifact ordering and the same content,
incumbent system, constraints, render matrix, and reviewer rubric for every
candidate payload.
