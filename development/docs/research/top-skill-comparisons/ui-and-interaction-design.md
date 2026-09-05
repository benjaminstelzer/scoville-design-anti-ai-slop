# Stage-two Skill comparison: UI and interaction design

Date: 2026-09-02
Capture: 2026-09-02T13:41:58Z
Target: `references/ui-and-interaction-design.md` and its expert-depth audit
Method: `reference-audit-method.md`, Stage two

Local successor baselines: [UI workflow](../../../../scoville-design-anti-ai-slop/references/ui-workflow-and-interaction-design.md) and [responsive Web](../../../../scoville-design-anti-ai-slop/references/web-and-responsive-design.md),
[expert-depth audit](../reference-audits/ui-and-interaction-design.md), and
[medium architecture decision](../medium-architecture-question.md)

This is a bounded current GitHub and public-Skill comparison. A repository
entered the ranking only when an exact UI, interaction, product-behavior,
information-architecture, form, state, or design-system Skill and an E1 or
higher artifact were both inspectable. Stars rank qualifying repositories.
They do not measure the exact Skill, its routing accuracy, design quality, or
adoption. General frontend repositories were searched but did not substitute
for an exact Design owner.

## Decision

The three qualifying repositories found are `rampstackco/claude-skills`,
`mblode/agent-skills`, and `magnus919/agent-skills`. Rampstack has the largest
exact-domain repository reach and the best separable routing surface for IA,
forms, and design-system governance. Mblode has the strongest synthetic
boundary tests between product behavior, UI appearance, animation, and deep
typography. Magnus has the strongest framework-neutral task, state, recovery,
and responsive behavior contract.

None of the exact evidence includes a rendered multi-viewport UI produced by
the Skill and reviewed for typography, spacing rhythm, negative-space
function, hierarchy, subject-specific composition, or task success. The
candidate artifacts establish written coverage, evaluability, and fixture
specific routing expectations. They do not establish visibly better design.
The current Scoville audit remains the stronger target because it combines the
missing behavioral depth with an explicit Design versus UI implementation
boundary and a higher visual-proof priority.

The architecture decision is unchanged. Design should eventually route
independently to `ui-workflow-and-interaction-design` and
`web-and-responsive-design`. UI or framework implementation remains a
separate owner. The two leaves share typography, composition, colour, imagery,
accessibility, and evidence rather than copying their rules.

## Qualification and star ranking

E1 is an inspectable example or output artifact. E2 is a reproducible test,
evaluation, or deterministic check. E3 requires independent evaluation or
external adoption evidence that supports capability. No ranked candidate has
E3 evidence. Stars and registry installs remain popularity signals only.

| Rank | Repository and exact path | Stars at capture | Pin, activity, and relevant update | Exact license and asset status | Evidence level and what it proves |
| --- | --- | ---: | --- | --- | --- |
| 1 | [`rampstackco/claude-skills`, `skills/information-architecture/SKILL.md`](https://github.com/rampstackco/claude-skills/blob/a67dd34c609f034c0cfd736a348659bbdf1605bf/skills/information-architecture/SKILL.md), [`skills/form-strategy/SKILL.md`](https://github.com/rampstackco/claude-skills/blob/a67dd34c609f034c0cfd736a348659bbdf1605bf/skills/form-strategy/SKILL.md), [`skills/multi-step-form-design/SKILL.md`](https://github.com/rampstackco/claude-skills/blob/a67dd34c609f034c0cfd736a348659bbdf1605bf/skills/multi-step-form-design/SKILL.md), and [`skills/design-system/SKILL.md`](https://github.com/rampstackco/claude-skills/blob/a67dd34c609f034c0cfd736a348659bbdf1605bf/skills/design-system/SKILL.md) | 813 | Active, not archived. Repository pin `a67dd34c609f034c0cfd736a348659bbdf1605bf`. The inspected Skills last changed in [`e5bc675199916b257bb1c8e73cd7620488996666`](https://github.com/rampstackco/claude-skills/commit/e5bc675199916b257bb1c8e73cd7620488996666) on 2026-08-10. Repository pushed 2026-08-28. | Root [MIT](https://github.com/rampstackco/claude-skills/blob/a67dd34c609f034c0cfd736a348659bbdf1605bf/LICENSE). The exact directories contain repository-authored Markdown templates, not separately licensed visual or data assets. External research methods and implementation systems retain their own authority and rights. | **E1.** IA and design-system audit templates, form plans, tables, and worked structures are inspectable. They prove concrete deliverable coverage and selective routing. They do not prove usability, implementation correctness, responsive behavior, or visual quality. |
| 2 | [`mblode/agent-skills`, `skills/ui-design/SKILL.md`](https://github.com/mblode/agent-skills/blob/ac090cd9dc16346258763fa9cbff1c29dd466277/skills/ui-design/SKILL.md) with [`evaluations/merge-routing.json`](https://github.com/mblode/agent-skills/blob/ac090cd9dc16346258763fa9cbff1c29dd466277/skills/ui-design/evaluations/merge-routing.json) and [`evaluations/refine-ai-ui.json`](https://github.com/mblode/agent-skills/blob/ac090cd9dc16346258763fa9cbff1c29dd466277/skills/ui-design/evaluations/refine-ai-ui.json) | 100 | Active, not archived. Repository pin `ac090cd9dc16346258763fa9cbff1c29dd466277`. The Skill last changed in [`b5743a23b633a131170c58bb9cc77c093521ca39`](https://github.com/mblode/agent-skills/commit/b5743a23b633a131170c58bb9cc77c093521ca39) on 2026-09-01. The routing evaluation last changed in `ce31a830e0449096db3a0f731401670ba7cf6696` on 2026-08-12. Repository pushed 2026-09-02. | Root [`LICENSE.md`, MIT](https://github.com/mblode/agent-skills/blob/ac090cd9dc16346258763fa9cbff1c29dd466277/LICENSE.md). The exact evidence uses repository-authored JSON and synthetic TSX fixtures. No separate data or asset license was found. | **E2.** Structured evaluations and source fixtures make routing, state, recovery, accessibility, and anti-slop expectations reproducible. They prove the test contract exists. No run result, rendered before-and-after artifact, visual regression, user result, or independent review was found. |
| 3 | [`magnus919/agent-skills`, `product-design-and-ux/SKILL.md`](https://github.com/magnus919/agent-skills/blob/de968dfdfb5ac92336a4915dad4bb56a27fe0207/product-design-and-ux/SKILL.md) with [`evals/evals.json`](https://github.com/magnus919/agent-skills/blob/de968dfdfb5ac92336a4915dad4bb56a27fe0207/product-design-and-ux/evals/evals.json) | 65 | Active, not archived. Repository pin `de968dfdfb5ac92336a4915dad4bb56a27fe0207`. The Skill last changed in [`035e58d3e39690361596901ab8f17222ab9baf02`](https://github.com/magnus919/agent-skills/commit/035e58d3e39690361596901ab8f17222ab9baf02) on 2026-09-02. The evaluation last changed in `d68c1b3552360af931311b8aa56674bdb0125263` on 2026-08-03. Repository pushed 2026-09-02. | Root [`LICENSE.md`, MIT](https://github.com/magnus919/agent-skills/blob/de968dfdfb5ac92336a4915dad4bb56a27fe0207/LICENSE.md). The exact directory contains repository-authored templates, references, and synthetic evaluations. No separate data or visual asset license was found. | **E2.** Five evaluation cases, assertion lists, and fillable task, state, and interface contracts are inspectable and reproducible as an evaluation specification. They prove behavioral coverage and clear ownership. No harness result, actual participant evidence, implemented UI, or rendered visual proof was found. |

## Candidate 1: Rampstack IA, forms, and design-system Skills

### Claimed scope and observed mechanism

Rampstack divides the domain into several flat signals rather than one general
UI prompt. The IA Skill moves from audience tasks and content objects to
sitemap, labels, navigation, taxonomy, URLs, search, cross-linking, and change
control. Form Strategy and Multi-step Form Design isolate collection purpose,
field grouping, validation, progression, and handoff. Design System separates
tokens, primitives, patterns, templates, documentation, governance, and
adoption.

The templates are the main evidence. The
[`ia-document-template.md`](https://github.com/rampstackco/claude-skills/blob/a67dd34c609f034c0cfd736a348659bbdf1605bf/skills/information-architecture/references/ia-document-template.md)
forces an audience-task statement, sitemap, navigation variants, content
types, taxonomy, search, locale handling, open questions, and sign-off. The
[`system-audit-template.md`](https://github.com/rampstackco/claude-skills/blob/a67dd34c609f034c0cfd736a348659bbdf1605bf/skills/design-system/references/system-audit-template.md)
adds inventory, documentation drift, governance, adoption, risk, and backlog.
This is useful artifact completeness. It is not proof that the structure or
system serves its users.

### What is better than the current Scoville reference

- IA, form strategy, multi-step form design, and system governance have
  independent route signals rather than being buried in a single UI checklist.
- Missing inputs remain visible in the deliverable instead of being silently
  invented.
- Governance, deprecation, adoption, documentation drift, and product-team
  contribution are explicit design-system concerns.
- The IA artifact joins content objects, labels, findability, URLs, search,
  locale, and migration rather than reducing IA to a navigation component.
- The templates can become inspectable handoff records even when no browser or
  framework is available.

### Reject or revise

- Do not import three-click reachability, four-to-seven top-level items,
  two-to-three-word labels, category counts, tag counts, menu placement, page
  sizes, or contextual-link counts as universal design rules.
- Do not make the six-layer IA framework or four-layer design-system model a
  mandatory ontology. The artifact should use only distinctions that alter a
  decision or owner.
- Token counts and statements such as one source of truth do not prove system
  quality. A system can require platform-specific authorities with controlled
  transformation and traceability.
- The design-system Skill crosses into implementation inventory and
  accessibility checks without defining the handoff boundary. Scoville Design
  should define intended roles, relationships, states, variants, and
  governance. Scoville UI or Code should implement and test components,
  semantics, focus, input, announcements, and runtime behavior.
- No exact artifact shows responsive recomposition, form recovery, visual
  hierarchy, typography, spacing rhythm, negative-space function, or
  subject-specific composition.

## Candidate 2: Mblode `ui-design`

### Claimed scope and observed mechanism

The Skill supports Direction, Build, Audit, Options, Scaffold, Retrofit, and
Componentize modes. It explicitly routes changes to capability, object,
consequence, and reversibility to `product-design`, motion craft to
`ui-animation`, and deep type concerns to `typography-audit`. Its evaluation
fixtures cover an invite form that loses data and permits double submission, a
destructive-action ownership split, a pricing-page audit, a mobile interaction
route, and several generic-AI-UI challenges.

The strongest evidence is not a finished screen. It is the causal routing
contract. For example, the invite-form fixture expects file-level diagnosis of
premature data clearing, missing pending state, unchecked failure, and a
missing accessible name. The anti-slop fixtures require earned gradients,
named logos, real screenshots, and useful browser framing to remain while
unsupported decorative layers and repeated calls to action are removed.

### What is better than the current Scoville reference

- Capability and recovery decisions are separated from appearance and line
  implementation through explicit evaluation cases.
- Audit is not allowed to become an unsolicited redesign. The fixtures test
  preservation as well as removal.
- Generic-looking UI is treated as a causal diagnosis. Evidence-backed brand
  material and content are protected while sourceless furniture is removed.
- Expected behavior includes loading, pending, failure, empty, keyboard, touch,
  mobile, and typography route-outs instead of a happy-path screenshot.
- Considered-but-rejected findings are part of the evidence, which reduces
  pressure to manufacture defects.

### Reject or revise

- The Skill combines visual direction, implementation, audit, responsive work,
  and componentization. That breadth would erase the Scoville Design versus UI
  implementation boundary.
- Fixed palette, type, spacing, radius, breakpoint, mobile-size, skeleton, and
  state recipes must not become Design rules. Applicability comes from the
  task, data, permissions, risk, platform, content, language, and runtime.
- “Every async component needs every state” is too broad. The state model must
  record the force that makes a state applicable and why omitted states cannot
  occur.
- Tailwind classes, breakpoint mechanics, component code, accessible names,
  focus behavior, and rendered browser proof belong to UI or Code when those
  owners are active. Design owns the required behavior and acceptance
  consequence.
- The JSON evaluations show what an evaluator should expect, not that the
  Skill produced or repaired a screen. They provide no visible typography,
  spacing, negative-space, composition, or responsive-quality evidence.

## Candidate 3: Magnus `product-design-and-ux`

### Claimed scope and observed mechanism

This is the cleanest exact-domain owner. It defines user-facing behavior from
validated evidence and approved scope, then stops before brand, pixels, CSS,
components, ARIA, and framework implementation. The sequence is evidence
trace, IA, content and cognitive demand, task flow, applicable states,
recovery, pattern tradeoffs, authorized usability work, interface contract,
and engineering handoff.

The [`task-flow-state-model.md`](https://github.com/magnus919/agent-skills/blob/de968dfdfb5ac92336a4915dad4bb56a27fe0207/product-design-and-ux/templates/task-flow-state-model.md)
records actor action, decision, side effect, persistence, recovery,
cancellation, re-entry, permissions, stale data, conflict, retry, and
deduplication. The
[`interface-contract.md`](https://github.com/magnus919/agent-skills/blob/de968dfdfb5ac92336a4915dad4bb56a27fe0207/product-design-and-ux/templates/interface-contract.md)
adds validation timing, responsive and inclusive intent, telemetry purpose,
open decisions, owners, and resolution gates. It explicitly routes semantic,
ARIA, WCAG, and test details to accessibility rather than presenting a design
table as conformance proof.

### What is better than the current Scoville reference

- States are derived from forces in the actual flow rather than copied from a
  standard list.
- Partial commit, retry, deduplication, permission, ownership, stale data,
  conflict, cancellation, re-entry, and irreversible actions have explicit
  record fields.
- Interaction patterns are hypotheses with alternatives, tradeoffs, evidence,
  and disconfirming conditions.
- Responsive intent is framed across width, zoom, text expansion, orientation,
  input, reduced motion, connectivity, and interruption, not only device
  labels and breakpoints.
- The Skill forbids invented research participants, quotes, observations, and
  outcomes while still permitting an authorized study plan.

### Reject or revise

- The evaluation's five-to-eight participant expectation is a contextual
  formative-study hypothesis, not a universal usability sample rule.
- “Few top-level destinations” and frequency-driven depth can guide a
  comparison, but cannot approve an IA without domain, safety, novice/expert,
  locale, and task evidence.
- Concrete spacing and sizing tokens in the interface-contract evaluation can
  pull the owner below decision altitude. Design may name relationships and
  supported system roles. UI owns exact framework tokens unless the design
  system itself is the requested artifact.
- The sibling Skill graph is one repository architecture, not a dependency
  requirement for Scoville.
- No included result shows a completed form, navigation, responsive layout,
  type hierarchy, spatial rhythm, or real usability outcome.

## Weighted adoption comparison

| Required concern | Rampstack | Mblode | Magnus | Current Scoville position and decision |
| --- | --- | --- | --- | --- |
| Workflow and task model | Audience tasks drive IA, but end-to-end side effects and recovery are dispersed. | Fixture cases expose capability and ownership boundaries, mainly from implementation in hand. | Strongest task, actor, decision, side-effect, persistence, recovery, and handoff record. | Adapt the Magnus causal record. Keep current context-first framing and do not require a large artifact for a small reversible surface. |
| IA and navigation | Strongest separate route for content objects, labels, taxonomy, URLs, search, and migration. | UI audit can find navigation defects but does not own the whole IA. | Strong evidence trace and task-based hierarchy without tying IA to chrome. | Split IA, navigation model, task flow, and rendered navigation behavior. Design owns the first three. UI implements the last. |
| Forms and validation | Strong separate form and multi-step signals with templates. | Strong implementation findings for pending, failure, data loss, and accessible naming. | Strongest validation timing, persistence, partial commit, retry, timeout, and re-entry model. | Combine form intent and recovery into the workflow leaf. Route controls, semantics, announcements, focus, input, and runtime validation to UI. |
| States and recovery | Pattern inventory includes states but tends toward checklist completeness. | Strong synthetic defects and owner splitting. | Best applicability field and explicit omitted-state rationale. | Require default, loading, empty, error, partial, stale, conflict, permission, optimistic, offline, interrupted, success, and recovery only where a named force makes each possible. |
| Design-system intent | Best governance, deprecation, documentation, adoption, and risk coverage. | Strong incumbent-system preservation and componentization route. | Maps behavior to an approved system without owning component code. | Design owns roles, relationships, variants, states, governance, and change intent. UI owns component APIs, tokens in code, semantics, focus, input, responsive mechanics, and rendered proof. |
| Typography and hierarchy | Templates inventory type roles but provide no typesetting evidence. | Direction and audit mention type, while deep issues route out. No visible result exists. | Deliberately excludes visual styling. | Preserve the shared typography leaf. Test actual language, copy, role hierarchy, measure, fallback, and renderer. No candidate visibly proves improvement. |
| Spacing and negative space | System templates inventory spacing tokens rather than relationship consequences. | Anti-slop eval protects earned structure and removes unsupported furniture, but gives no render. | Intentionally outside behavioral scope. | Design must distinguish within-group, between-group, section, edge, and sequence space, plus separation, pacing, framing, direction, and intensity. UI implements the supported values. |
| Responsive design intent | IA templates name desktop and mobile navigation choices, often as pattern menus. | Responsive guidance reaches implementation and fixed mobile recipes. | Best environment and interruption contract without device-only breakpoints. | Future responsive Design leaf should record preserve, reflow, reorder, collapse, disclose, transform, crop, scroll, and defer decisions. UI chooses queries and implementation. |
| Subject-specific composition | Little beyond content inventory. | Preserves real brand evidence and discourages unsupported layers. | Outside its deliberate scope. | Current Brief, Style, Typography, Composition, Colour, and Imagery owners remain authoritative. No ranked artifact proves several subjects or media. |
| Evidence | Fillable E1 templates. | E2 synthetic eval specifications and fixtures, no observed run. | E2 eval specifications and templates, no observed run. | Require behavior records, renders, interaction proof, access tests, and user evidence as separate lanes. Do not convert one lane into another. |

## Architecture and mechanisms to synthesize

### Future `ui-workflow-and-interaction-design` leaf

1. Start from user, context, content objects, required decisions, permissions,
   risk, incumbent system, and observable completion.
2. Distinguish IA, navigation model, task flow, and on-screen navigation. Use
   only the representation that changes the decision.
3. Record each step's actor action, decision, side effect, persistence,
   cancellation, re-entry, and recovery.
4. Derive states from actual forces. For each state, record trigger, visible
   consequence, allowed action, exit, recovery, evidence, and why any commonly
   expected state is not applicable.
5. For forms, define collection purpose, field necessity, grouping, validation
   timing, preservation, partial success, retry, duplicate prevention,
   permission, timeout, and confirmation before control styling.
6. Compare interaction patterns as hypotheses. State where a choice fails and
   what evidence would overturn it.
7. Hand UI an observable interface contract. Do not prescribe framework code,
   ARIA syntax, focus implementation, breakpoints, or component libraries.

### Future `web-and-responsive-design` leaf

1. Record the relationships that must survive, including task priority,
   reading order, type roles, group spacing, negative-space function,
   protected crops, comparison structure, controls, and state visibility.
2. Choose among preserve, reflow, reorder, collapse, progressive disclosure,
   alternate composition, bounded two-dimensional access, crop, scroll, or
   defer based on actual failure pressure.
3. Test width, container, height, zoom, text expansion, language, direction,
   orientation, input, keyboard, reduced motion, safe areas, connectivity,
   interruption, and dynamic-content extremes as applicable.
4. Keep visual, programmatic, and focus order distinct. A visual reorder cannot
   silently reverse meaning or task access.
5. Route media queries, container queries, framework components, live DOM,
   focus, input, announcements, and performance proof to UI or Code.

### Evidence package

- behavior artifact for IA, task, states, forms, recovery, and open decisions
- at least one rendered wide and narrow state set using real content
- typography specimen at actual language, copy, size, measure, and fallback
- spacing and negative-space review tied to grouping and task consequence
- keyboard, pointer, touch, zoom, text expansion, and assistive-technology proof
  where applicable
- user or operational evidence labeled separately from source, render, and test
  evidence
- `Not verified` for every unavailable lane

## Reject from the executable package

- fixed navigation counts, click counts, label lengths, field counts, steps,
  breakpoints, viewport lists, spacing scales, type scales, radii, and target
  sizes presented as universal
- “all states” without applicability and impossible-state reasoning
- token presence or component inventory presented as a design-system quality
  score
- device labels presented as responsive design intent
- automatic mobile stacking, hiding, centering, larger type, hamburger menus,
  cards, or horizontal scrolling without task and content evidence
- broad frontend implementation ownership inside the Design reference
- screenshots presented as functional, access, user, or deployed proof
- evaluator assertion files presented as passing executions or visible quality
- invented participants, findings, analytics, operational data, or research
  results
- imported prose, repository-specific Skill dependencies, or mandatory
  framework and browser tooling

## Search exclusions and limits

- `wshobson/agents` had 39,350 stars and exact UI-design files, but no example,
  output, fixture, test, or evaluation artifact was found in the exact UI
  plugin path. It remains E0 for this comparison and cannot displace an E1
  qualifier.
- High-star general frontend repositories, including broad implementation and
  aesthetic Skills, were not treated as workflow or interaction Design merely
  because they build interfaces. A rendered landing page or component test
  does not prove IA, form strategy, state applicability, recovery, or a clean
  Design-to-UI ownership boundary.
- `Owl-Listener/designer-skills` and several exact checklist repositories had
  more reach than some qualifiers, but no exact E1 artifact was found during
  the bounded inspection.
- Lower-star exact repositories such as `rastian/interaction-design-skills`,
  `akillness/jeo-skills`, and `mary13/pair-design-agent-skill` supplied useful
  routing language but did not outrank the qualifying set by repository stars.
- Search used GitHub repository, commit, tree, and contents APIs, GitHub and web
  search, and skills.sh on 2026-09-02. Authenticated GitHub code search was
  rate-limited during the session. Private, renamed, deleted, service-hosted,
  recently published, and poorly indexed Skills may be absent. The ranking is
  current and bounded, not globally exhaustive.
- The cheapest decision-changing next evidence is a common brief implemented
  by all three Skills. It should include a multi-step form, partial failure,
  permission change, stale data, long translated content, desktop and narrow
  recomposition, and an incumbent design system. Blind review should score
  task completion, recovery, hierarchy, type, spacing, negative space,
  responsive preservation, access, and unauthorized scope separately.
