# Reference audit: UI and interaction design

Date: 2026-09-02  
Status: W-011 research audit; executable package unchanged  
Scope: `references/ui-and-interaction-design.md`, the Design/UI composition
contract, the responsive-web medium architecture question, and the external
mechanism adoption priority

## 1. Current contract

### Route, ownership, evidence, and size

- **Activation:** the Design Direct Index selects this leaf for `UI workflow`,
  `responsive layout`, or `states`. `modules.yaml` maps those terms to
  `ui_workflow` and `interaction_states`. The file itself additionally claims
  navigation and defining/evaluating a UI design system, but neither currently
  has a direct router label or signal.
- **Status / intervention:** `retained-floor` / `external-verification`.
- **Owned concerns:** `workflow_design`, `screen_hierarchy`, `state_intent`, and
  `design_ui_record`.
- **Declared sources:** L-14, L-15, L-16, L-17, L-24, and L-26. L-14/L-24/L-26
  support exact web-accessibility, writing-system, and motion boundaries.
  L-15/L-16 are public-service principles, not a professional curriculum for
  information architecture, forms, interaction patterns, responsive systems,
  or design-system definition. L-17 broadens access questions but is
  reference-only. The current source set is therefore narrower than the claimed
  domain.
- **Evaluation:** SOL-B06 found a visually credible clinic UI with one collapsed
  heading and another arm that invented operational-looking contact details.
  R2/R3 repeats were clean, so no persistent SOL-specific teaching defect was
  admitted. The evidence supports model-independent truth, state, rendered-fit,
  and ownership floors; it does not prove specialist UX, IA, form, responsive,
  or design-system depth.
- **Composition evidence:** open UI routing passed the final 7/7 Train and 3/3
  Validation cases; the post-diagnosis v2 regression passed 4/4. It supports the
  current owner split and selective routing, not rendered product quality or
  holdout qualification.
- **Measured size:** 375 whitespace-delimited words, 2,870 bytes, approximately
  544 tokens by the audit's word-based proxy.

### Explicit behavior now supplied

| Mode | Current rule | Audit judgment |
| --- | --- | --- |
| Generation | Frame goal, consequences, entry/exit, decisions, information, owner system, states, content variation, input modes, access, trust, and real facts; prioritize the task; design states; recompose rather than shrink; use the incumbent system. | Strong minimum frame, but “complete state model” is checklist-shaped, IA/forms/pattern choice are absent, and the responsive rule lacks a transformation contract. |
| Critique | Walk entry to completion; inspect priority, labels, affordance, feedback, recovery, prevention, states, responsive order, focus/input, scaling, contrast, localization, and truth. | Good task-first sequence. It conflates Design judgment with UI-owned semantics and runtime proof, and supplies too little causal diagnosis. |
| Repair | Repair the workflow or parent component rule before polish; Core limits repair to the smallest coherent cause and requires rerender. | Correct priority. It needs explicit failure → cause → design repair → UI proof, plus preservation of working paths and state/data invariants. |
| Exception | Expressive styling may depart from convention when the task remains recognizable, states clear, and the deviation consistent; framework rules cannot overrule access/safety. | Useful, but exceptions are missing for specialized navigation, validation timing, dense data, responsive two-dimensional content, optimistic state, custom patterns, and owner-level system changes. |
| Verification | Render representative viewports, test critical interactions, apply exact standards in scope, and hand UI the canonical compact record. | The record is strong. The verb “test” over-assigns Design when UI is active: Design defines validation targets and interprets consequence; UI owns framework/runtime mechanics and proof. Design-only evidence must name those mechanics unverified. |

## 2. What is already strong

1. **The owner split is operational, not rhetorical.** Design owns task flow,
   priority, adaptive composition, intended state communication, and system
   direction. UI owns framework-valid implementation, component semantics,
   focus/input, announcements, responsive mechanics, and rendered interaction
   proof. ADR-0006 and both Skills use the same compact record.
2. **The incumbent system stays above either Skill.** The leaf correctly starts
   from platform/framework and existing tokens/components and reports a system
   gap instead of inventing a near-duplicate. This prevents parallel visual and
   interaction languages.
3. **The interface is framed as a task, not a screenshot.** Goal, consequence,
   entry/exit, decision points, required information, and operational truth are
   the right primary inputs.
4. **States are first-class.** Loading, empty, error, success, permission,
   offline, interruption, destructive action, focus, and selection are not left
   as implementation afterthoughts.
5. **Responsive design is correctly described as recomposition.** The explicit
   rejection of mere shrinking preserves priority, order, input context, and
   task completion across space changes.
6. **Critique starts with the whole flow.** Walking from entry to completion and
   fixing the workflow or parent component rule before polish is causal and
   scalable.
7. **Truth and safety outrank polish.** The prohibition on invented availability,
   addresses, emergency routes, policy, and support details directly answers
   SOL-B06.
8. **Evidence is scoped.** The leaf says public-service principles do not prove
   usability and exact accessibility sources apply only in their conformance
   scopes.

## 3. Missing professional capability

### Task flow, information architecture, and navigation

- Model **goal versus task versus interface step**. Record actors/roles,
  triggering conditions, entry channels, required knowledge/data, decisions,
  branches, side effects, dependencies, interruption/re-entry, cancellation,
  completion evidence, and downstream consequences. A screen list is not a
  task model.
- Distinguish **information architecture** (objects, relationships, taxonomy,
  labels, permissions, lifecycle, findability) from **navigation** (paths and
  controls through that structure) and from **task flow** (actions needed to
  reach an outcome). Do not copy the organization chart into the user's model.
- Diagnose information scent, ambiguous sibling choices, missing current
  location, trapped paths, destructive backtracking, lost filters/context,
  weak deep links, and search/navigation overlap. There is no universal
  three-click rule, seven-item limit, or correct depth. Validate consequential
  findability with representative tasks, tree/first-click testing, analytics,
  or observed use rather than intuition alone.
- Select whether a flow needs global/service navigation at all. A repeated,
  multi-task product may need persistent orientation; a linear end-to-end
  transaction may be clearer without competing navigation.

### Pattern selection, forms, and state/recovery

- Treat a UI pattern as a **contextual hypothesis**, not a component lookup.
  Compare task fit, object/data shape, frequency, risk, platform convention,
  incumbent support, access behavior, interruption, and recovery. Record why a
  familiar pattern fits, what would falsify it, and what the custom alternative
  buys.
- For forms, record why each datum is needed, who uses it, required versus
  optional status, sensitivity, accepted representations, dependencies,
  branching, persistence, confirmation, and completion evidence. Group
  questions by user task and semantic relationship, not database schema. Long
  forms may become logical stages, but “one thing per page” is a public-service
  starting point, not a universal command.
- Separate **input constraints**, **validation**, **eligibility/permission**,
  and **server failure**. Prevent impossible inputs without rejecting legitimate
  formats; avoid blaming the user for a system or policy condition. Preserve
  entered data and point to the repair. Validate when input is sufficiently
  complete for feedback to be actionable; do not punish unfinished input with
  premature errors. Submit-time, delayed inline, and asynchronous validation
  remain context-specific.
- Replace the canonical-state recital with a **state applicability model**
  derived from flow, data, permissions, connectivity, concurrency, latency,
  risk, and time. Include partial success, stale data, conflict, retry,
  cancellation, duplicate submission, and re-entry only when the task can
  produce them.
- Make optimistic UI conditional on reversibility and reconciliation. Never
  show success before an irreversible/high-risk operation commits. Prefer undo
  for safely reversible actions and confirmation for costly, irreversible, or
  hard-to-detect consequences; neither is universal.

### Responsive-web design and density

- The current leaf needs an explicit **transformation contract**: preserved
  task/content/state/recovery invariants; reorder, regroup, disclose, collapse,
  replace, reflow, or split decisions; action/status persistence; navigation
  transformation; dense-data fallback; typography/measure/line-break,
  within-/between-group spacing, negative-space, hierarchy, crop/image intent;
  and conditions that trigger each change. The transformation must preserve or
  deliberately revise relationships, not merely preserve component presence.
- Derive transformations from content pressure, available container/window,
  text expansion, zoom, localization/script, orientation, input, safe area, and
  platform—not a fixed phone/tablet/desktop matrix. Breakpoint numbers and CSS
  mechanisms belong to the incumbent system/UI implementation owner.
- Treat density as a task and role decision. Repeated expert work can justify a
  compact mode; high consequence, low familiarity, or touch use can require
  more separation and disclosure. “More whitespace” and “fit more” are both
  preferences until tied to performance, comprehension, access, or system
  language.
- Keep fixed print/media out of this domain. A responsive-web leaf should own
  intended transformation only; shared typography, composition, colour, and
  imagery remain in their domain leaves. Print/fixed-media intent belongs to a
  separate architecture decision, and export/preflight stays with Media.

### Design-system definition and Design/UI handoff

- Define a product UI system as more than tokens or a component catalog:
  principles and product language; semantic roles; component/pattern purpose,
  anatomy, variants, states, responsive intent, content constraints, and
  anti-patterns; accessibility intent; contribution/deprecation/governance;
  owners; evidence and maturity. A DTCG token file proves interchange syntax,
  not system quality.
- Distinguish **definition** from **implementation**. Design may diagnose the
  incumbent system and propose an owner-level change; it must not silently
  override it. UI maps an accepted decision to supported components/tokens,
  semantics, APIs, tests, and runtime behavior. A real constraint returns only
  the affected concern to Design.
- Keep Design's accessibility role exact: equivalent meaning, priority,
  non-colour/non-motion communication, expected recovery, and validation target.
  UI owns names/roles/relationships, focus, keyboard/touch/platform behavior,
  announcements, scaling mechanics, and conformance evidence.

### Generic UI-slop diagnosis and evidence ceilings

- Diagnose slop by **mismatch**, not fashion bans: a shell chosen before the
  product task; interchangeable sidebar/card/dashboard scaffolds; equal-weight
  containers without real relationships; cosmetic “personality” unrelated to
  domain; invented metrics/content; near-duplicate incumbent components;
  happy-path-only screens; unchanged structure across widths; or confident
  rationale absent from the rendered/interactive result.
- Give external mechanisms highest weight when they visibly improve type roles
  and actual typesetting, relational spacing, purposeful negative space,
  hierarchy/grouping/reading order, and subject-specific responsive
  composition. Do not import font-pairing, fixed scale, mandatory whitespace,
  or breakpoint recipes into this leaf; Typography and Composition own the
  source relationships and the responsive leaf owns their medium translation.
- Cards, gradients, rounded shapes, minimalism, dense tools, and familiar
  navigation are not defects by category. They fail when they do no semantic or
  task work, obscure states/actions, violate the owner system, or repeat as an
  unrelated default.
- Never claim “user-centered,” “intuitive,” “usable,” or “validated” from a
  heuristic pass, model judgment, accessibility scanner, or attractive render.
  These create hypotheses and bounded checks; observed task performance and
  representative users are different evidence.

## 4. Rule-quality audit

| Class | Rules that belong | Necessary correction or exception |
| --- | --- | --- |
| Binding constraints | Do not invent operational facts; required task/content/action/recovery survives; safety, privacy, access, and incumbent ownership are preserved; Design never claims UI implementation proof it did not observe. | Fail closed or escalate when policy, eligibility, support, emergency, permission, or current system behavior is unknown. |
| Evidence-bounded rules | Apply WCAG/platform requirements in exact scope; use semantic form grouping and names; preserve reflow/function under applicable criteria; use user evidence only for the population/tasks actually studied. | A technique, pattern example, automated scan, one participant, or one viewport never proves full conformance or usability. |
| Contextual conventions | Familiar navigation, one primary action, staged forms, inline errors, persistent actions, optimistic updates, undo, confirmations, responsive breakpoints, cards, drawers, tabs, and design tokens can be effective. | Select by task, risk, frequency, platform, owner system, and evidence. Each can be wrong in a different context. |
| Numeric starting points | Three clicks, seven nav items, one thing per page, fixed device widths, specific target sizes, response-time bands, spacing scales, and card counts can seed a test or come from an owner standard. | Never universalize them. Quantitative floors come only from the applicable standard/platform/system; other numbers need a tested population, task, environment, and override. |
| Preferences | Visual restraint, density, animation amount, card use, navigation visibility, progressive disclosure, and “clean” presentation. | Judge by intended effect, product character, task cost, and access—not seniority theater or taste persona. |
| Justified exceptions | Custom interaction, deep navigation, two-dimensional data, delayed/asynchronous validation, dense expert mode, hidden secondary action, unusual responsive transformation, or local system extension. | Declare the gain, preserve recognition/access/recovery, keep a conventional escape or equivalent where needed, use the canonical owner, and test the risky condition. |
| Reject as slogans/cargo cult | “Three clicks,” “one focal point,” “one thing per page,” “mobile first always,” “disable invalid actions,” “skeletons beat spinners,” “never horizontal scroll,” “all states,” “44 px everywhere,” “cards/gradients are AI slop,” or “tokens make a design system.” | These erase context, standards scope, platform behavior, and legitimate exceptions. |

The current leaf avoids most numeric cargo cult. Its main rule-quality defect is
underspecification: broad verbs such as “design,” “recompose,” “make explicit,”
and “test” do not yet tell the agent which variables, causes, owner, or evidence
close a professional UI decision.

## 5. Specialist Skill prior art

The GitHub search covered UX/product behavior, interaction design, IA/navigation,
forms/validation, state/recovery, responsive strategy, design systems, rendered
proof, and anti-generic UI review. No inspected Skill is authority for the whole
domain; useful mechanisms are distributed.

Per `adoption-priority.md`, comparison weight is not feature breadth or
popularity. It is visible type/typesetting quality, spacing relationships,
negative-space function, hierarchy/reading order, and subject-specific
responsive composition. None of the inspected Skills supplies cross-subject,
rendered evidence strong enough to adopt a fixed typography, pairing, spacing,
or composition recipe.

| Skill | Pinned inspection | License | Mechanism worth learning from | Do not copy or generalize |
| --- | --- | --- | --- | --- |
| [`product-design-and-ux`](https://github.com/magnus919/agent-skills/blob/de968dfdfb5ac92336a4915dad4bb56a27fe0207/product-design-and-ux/SKILL.md) | `de968dfdfb5ac92336a4915dad4bb56a27fe0207`, 2026-09-02 | MIT | Strongest direct comparator: evidence-to-decision trace, distinct IA/task/state/interface-contract lanes, pattern tradeoffs, recovery, responsive conditions, handoff acceptance, and explicit usability/access ceilings. | Its sibling dependencies and templates are repository architecture, not proof that every task needs that ceremony; do not copy wording or assume its uninspected sources establish every rule. |
| [`interaction-design`](https://github.com/rastian/interaction-design-skills/blob/a3f092f9bd183eef8c25ec5ea7f0bb97505b94d3/SKILL.md) | `a3f092f9bd183eef8c25ec5ea7f0bb97505b94d3`, 2026-08-31 | No repository license detected; reference-only | Makes words, visual cues, physical/input context, time, and behavior one interaction model; covers flows, feedback, states, recovery, and handoff. | Large practitioner compendium with hard response-time, target-size, disabling, confirmation, and direction recipes; principles are often presented as universals without source-level scope. |
| [`information-architecture`](https://github.com/rampstackco/claude-skills/blob/a67dd34c609f034c0cfd736a348659bbdf1605bf/skills/information-architecture/SKILL.md) and [`design-system`](https://github.com/rampstackco/claude-skills/blob/a67dd34c609f034c0cfd736a348659bbdf1605bf/skills/design-system/SKILL.md) | `a67dd34c609f034c0cfd736a348659bbdf1605bf`, 2026-08-28 | MIT | Independent IA and system signals support flat routing; useful separation of structure/navigation from foundations/components/patterns/governance. | Six-layer/atomic taxonomies, “tokens are the source of truth,” screenshot-everything, preferred component counts, and mandatory artifacts are one process, not universal professional law. |
| [`responsive-design`](https://github.com/akillness/jeo-skills/blob/2b2e424a46e92f10849d0c9e1dbda0170974f0a8/.agent-skills/responsive-design/SKILL.md) | `2b2e424a46e92f10849d0c9e1dbda0170974f0a8`, 2026-09-01 | File declares MIT; no repository-level license detected | Exact-domain evidence for a direct responsive route: classify page, component/container, dense-data, media, or reflow pressure before proposing mechanics; keep route-outs explicit. Its pressure-source model can preserve subject-specific type, spacing, grouping, and content relationships better than a device matrix. | It is implementation-strategy oriented, mandates a three-reference preload, and overstates mobile-first/intrinsic-layout defaults. It does not demonstrate professional typesetting or spatial quality across subjects. Design must own intended recomposition; UI owns queries, breakpoints, semantics, and proof. |
| [`stark`](https://github.com/f0d010c/stark/blob/ff94e5b4e1c98d259f3cde9f806406c4528deed4/SKILL.md) | `ff94e5b4e1c98d259f3cde9f806406c4528deed4`, 2026-07-26 | Apache-2.0 | Platform/product routing, small reference bundles, task/state/recovery brief, and post-render gates; recognizes responsive adaptation as a separate failure mode. | Large runtime surface, many reference routes, and combined Design/UI/code ownership. Its “two skills/two references” caps and product-specific structure preference are project policy, not evidence. |
| [`Agave UI design`](https://github.com/nachiketkumar/ui-design-skill/blob/6ab8ca8a2065d97847506bb71cec610be2380936/SKILL.md) | `6ab8ca8a2065d97847506bb71cec610be2380936`, 2026-03-01 | MIT | Makes project-system adaptation and the “does this belong to this product?” anti-template question explicit. | Seniority persona, “taste” authority, one-focal-point and colour-count rules, fixed 375/768/1200 viewports, universal 44 px, removal ideology, radius formulas, and fashion bans are precisely the cargo cult this audit rejects. |

Prior art supports a direct responsive-web leaf and a source-bounded interaction
leaf, but not a monolithic taste checklist. The strongest comparator uses
observable behavior contracts and routes mechanics/access outward.

## 6. Authoritative research and learning sources

Audit-local IDs below are proposed ledger additions or refinements; they do not
modify the executable source map.

| ID | Source, version/date, status | Claim supported | Limit and reuse status |
| --- | --- | --- | --- |
| UI-01 | ISO [9241-110:2020](https://www.iso.org/standard/75258.html), interaction principles; ISO [9241-210:2019](https://www.iso.org/standard/77520.html), confirmed current in 2025 | Task suitability, self-descriptiveness, expectation conformity, learnability, controllability, use-error robustness, engagement, and human-centred lifecycle/context are distinct, contextual principles. | ISO standards are copyrighted and not a UI recipe. The accessible preview supports principle-level synthesis only; full conformance or method claims require the standard. |
| UI-02 | GOV.UK Service Manual, [map the whole problem](https://www.gov.uk/service-manual/design/map-a-users-whole-problem) and [scope transactions as users see them](https://www.gov.uk/service-manual/design/scoping-your-service); USWDS [Design Principles](https://designsystem.digital.gov/design-principles/), living public-service guidance inspected 2026-09-02 | Begin with a recognizable user outcome, include wider/offline journey and organizational dependencies, and test assumptions with real users. | Government-service scope; public guidance cannot prove another product's users or usability. OGL/site terms and U.S. government terms apply; synthesize with scope. |
| UI-03 | Larson & Czerwinski, [CHI 1998 breadth/depth study](https://www.microsoft.com/en-us/research/publication/web-page-design-implications-memory-structure-scent-information-retrieval/); NN/g, [three-click rule is false](https://www.nngroup.com/articles/3-click-rule/), 2019; USWDS [Header guidance](https://designsystem.digital.gov/components/header/) | Information scent, task labels, orientation, and breadth/depth tradeoffs matter more than an arbitrary click limit; navigation should reflect user tasks rather than organization structure. | CHI study is old and task/site-specific; ACM reuse is restricted. NN/g is practitioner guidance and proprietary. No source establishes one universal hierarchy shape. |
| UI-04 | W3C WAI [Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/), updated 2026; GOV.UK [form structure](https://www.gov.uk/service-manual/design/form-structure) and [validation recovery/timing](https://design-system.service.gov.uk/patterns/validation/); Seckler et al., [CHI 2014 form study](https://research.google/pubs/designing-usable-web-forms-empirical-evaluation-of-web-form-improvement-guidelines/), N=65 | Ask necessary data, group and label relationships, provide instructions/progress, preserve input, associate actionable errors, and treat timing as part of the interaction. Combined form improvements affected completion, submissions, eye movements, and satisfaction in the tested study. | GOV.UK's one-question and submit-time patterns are context defaults, not universal. CHI tested a bundle of 20 changes, so it does not prove each isolated rule; ACM copyright, reference-only. W3C document terms apply. |
| UI-05 | W3C [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [ARIA APG introduction](https://www.w3.org/WAI/ARIA/apg/about/introduction/), and GOV.UK [pattern library](https://design-system.service.gov.uk/patterns/), current pages inspected 2026-09-02 | Quantitative access floors apply only in exact scope; interaction patterns need purpose, keyboard/semantic behavior, and context adaptation; APG examples are informative, not a full design system or production code. | Accessibility conformance does not establish usability or design quality. GOV.UK patterns are public-service examples. W3C terms/OGL apply. |
| UI-06 | W3C [Reflow understanding](https://www.w3.org/WAI/WCAG21/Understanding/reflow); Microsoft [responsive layouts](https://learn.microsoft.com/en-gb/windows/apps/develop/ui/layouts-with-xaml) and [window-based breakpoints](https://learn.microsoft.com/en-us/windows/apps/design/layout/screen-sizes-and-breakpoints-for-responsive-design), current platform docs 2026 | Preserve information/function under zoom/reflow; responsive systems may reposition, resize, reflow, reveal/hide, replace, or re-architect based on available window/content pressure. | WCAG's 320 CSS px/400% boundary is a scoped web conformance condition, not a complete responsive design system. Microsoft values/mechanisms are Windows-specific and proprietary reference material. |
| UI-07 | GOV.UK [contribution criteria](https://design-system.service.gov.uk/community/contribution-criteria/); USWDS [maturity model](https://designsystem.digital.gov/maturity-model/) and [component lifecycle](https://designsystem.digital.gov/components/lifecycle/); DTCG [Format 2025.10](https://www.designtokens.org/tr/2025.10/format/) | A system needs evidence, uniqueness, reuse, versatility, ownership/lifecycle, documentation, and code/design alignment; token exchange syntax is only one technical layer. | Government systems have specific governance contexts. DTCG 2025.10 is a stable Community Group report, not a W3C Recommendation; Community Final Specification Agreement applies. |
| UI-08 | W3C [evaluation-tool limits](https://www.w3.org/WAI/test-evaluate/tools/selecting/), [WCAG conformance](https://www.w3.org/WAI/WCAG22/Understanding/conformance.html), and [involving users](https://www.w3.org/WAI/test-evaluate/involving-users/), current pages inspected 2026-09-02 | Automated tools cannot determine accessibility alone; machine and human evaluation cover different claims; user evaluation and standards evaluation complement but do not substitute for each other. | A small user sample does not generalize to a population or all disabilities; conformance still does not guarantee universal usability. W3C terms apply. |
| UI-09 | Jung et al., [UI-Bench](https://arxiv.org/abs/2508.20410), 2025 preprint; Imteyaz et al., [Design Theater](https://arxiv.org/abs/2607.22928), 2026 preprint | Bounded evidence that text-to-app outputs can converge in layout, that expert pairwise design judgment can separate outputs, and that confident rationale often fails to appear in implementation, especially for functional requirements. | Preprints, selected tools/prompts, author-defined metrics, and no universal taxonomy of “AI slop.” ArXiv availability is not reuse permission; reference and cite only unless license is verified. |

The strongest contradiction is productive: platform/service pattern libraries
offer useful defaults, while empirical and standards sources repeatedly bound
them by context. The Skill should therefore compile a task-specific decision
and falsifier, not repeat a “best practices” list.

## 7. Applied Dos and Don’ts

### Frame the task and IA

- **Do** state the intended outcome, actor/role, consequence, trigger, entry,
  required knowledge/data, decisions, branches, side effects, interruption,
  recovery, exit, and completion evidence. **Do not** begin with a dashboard,
  sidebar, card grid, screen count, or component catalog. [UI-01, UI-02]
- **Do** model domain objects, relationships, lifecycle, labels, permissions,
  findability, and cross-channel dependencies before choosing navigation.
  **Do not** mirror an organization chart or call a sitemap a task flow. [UI-02,
  UI-03]
- **Do** evaluate navigation by information scent, current location, expected
  destination, backtracking cost, deep links, search, and representative tasks.
  **Do not** optimize raw click count or top-level item count. Repair ambiguous
  labels/grouping/structure before adding another menu. [UI-03]

### Select patterns and design forms

- **Do** compare consequential patterns against task frequency, object/data
  shape, risk, platform convention, incumbent support, access, interruption,
  and recovery; record the disconfirming condition. **Do not** choose a pattern
  because it is familiar, novel, fashionable, or present in a component
  catalog. [UI-01, UI-05]
- **Do** justify every requested form datum, accept legitimate representations,
  group related choices semantically, expose required/optional status, preserve
  progress, and provide completion evidence. **Do not** translate the database
  schema into a questionnaire or collect sensitive data merely because storage
  exists. Route legal/privacy duties to the correct expert. [UI-04]
- **Do** distinguish invalid input from eligibility, permission, unavailable
  service, or backend failure. State what happened, what remains preserved, and
  the next repair/recovery. **Do not** blame the user or clear unaffected data.
  [UI-01, UI-04]
- **Do** choose validation timing after identifying when the value is complete,
  whether feedback can be acted on, request cost, risk, and announcement/focus
  behavior. **Do not** display errors while the user is still composing input.
  Submit-time validation is a safe public-service default; delayed inline or
  asynchronous feedback is an exception to prove, not prohibit. [UI-04]

### Model states and recovery

- **Do** derive states from flow × data × permission × connectivity × latency ×
  concurrency × risk. Specify trigger, visible meaning, available actions,
  persistence, exit, and recovery for each applicable state. **Do not** populate
  a ceremonial default/hover/loading/empty/error/success matrix for unaffected
  components. [UI-01; bounded state-model rationale]
- **Do** keep orientation stable while making meaningful change perceptible;
  preserve input and next action; distinguish no data, no results, filtered
  empty, unavailable, permission denied, stale, conflict, partial success, and
  system failure when they differ operationally. **Do not** make them one generic
  empty/error card. [UI-01, UI-05]
- **Do** use undo for safely reversible changes, confirmation for costly or
  irreversible consequences, and optimistic updates only when rollback and
  reconciliation are clear. **Do not** add confirmation to every action, disable
  controls without explaining the unmet condition, or announce success before
  commit. [UI-01, UI-04]

### Define responsive-web transformation

- **Do** write preserved invariants and explicit transformations: reorder,
  regroup, disclose, collapse, replace, reflow, split, retain action/status,
  adapt navigation, or change dense-data presentation. **Do not** say
  “responsive,” provide three scaled mockups, or shrink the desktop hierarchy.
  [UI-06; `medium-architecture-question.md`]
- **Do** name which type roles, measure, line breaks, within-group and
  between-group spaces, edge relationships, negative-space functions, focal
  hierarchy, reading order, and crops survive or change. **Do not** swap to a
  fixed font pairing/scale, apply one spacing ramp mechanically, or demand more
  whitespace. Recompose the subject-specific relationships and render them with
  real copy. [`adoption-priority.md`; UI-06]
- **Do** derive pressure points from content/container/window, text expansion,
  zoom, localization/script, orientation, input, and system constraints. **Do
  not** prescribe device brands or universal breakpoints. UI maps the accepted
  transformation to framework queries/breakpoints and proves it. [UI-06;
  ADR-0006]
- **Do** preserve task, required content, state, recovery, and access under
  adaptation. Two-dimensional tables/maps/editors may justify scoped horizontal
  interaction or alternate presentation. **Do not** hide required content merely
  to pass an overflow screenshot. [UI-05, UI-06]
- **Do** keep shared type/colour/image/composition rules in their expert leaves
  and Print/fixed intent outside responsive-web. **Do not** duplicate fixed-page,
  trim/bleed, print proof, or provider preflight here. Media owns export/proof.

### Define and hand off a UI system

- **Do** define principles, semantic roles, pattern/component purpose, anatomy,
  variants, applicable states, responsive intent, content constraints,
  exceptions, lifecycle, contribution, deprecation, owners, and evidence. **Do
  not** call a token file, Figma library, or code package alone a mature design
  system. [UI-07]
- **Do** reuse an incumbent component/pattern unless evidence supports an
  owner-level extension or replacement. Record gap, intended effect, allowed
  variation, migration/deprecation, and validation target. **Do not** create a
  near-duplicate or override tokens locally to force the mockup. [UI-07;
  ADR-0006]
- **Do** hand UI only the canonical decision record. Design owns intended flow,
  hierarchy, state presentation/recovery, responsive transformation, and system
  decision; UI owns components/tokens, semantics, focus/input, announcements,
  mechanics, and proof. **Do not** silently redesign around a framework limit;
  return the affected concern to Design. [ADR-0006; UI Skill]

### Critique generic UI slop causally

- **Do** ask whether the structure, content, system, states, and adaptation are
  specific to this product task and whether the rationale exists in the actual
  artifact. **Do not** score distinctiveness by font novelty, gradient absence,
  card count, asymmetry, or a “senior designer” gut check. [UI-09; SOL baseline]
- **Do** inspect actual typesetting, relationship-specific spacing, trapped or
  decorative gaps, edge tension, hierarchy, reading order, and whether negative
  space separates, paces, frames, directs, or intensifies. **Do not** reward
  “clean whitespace,” one spacing scale, or a fashionable type pairing without
  a visible subject/task effect. [`adoption-priority.md`]
- **Do** report failure → task/design cause → affected user decision → smallest
  parent repair → exact Design/UI evidence. Example: repetitive cards may be
  caused by an unmodeled object hierarchy; repair the hierarchy and pattern,
  not merely card radius. **Do not** decorate a shell-first design to make it
  “less AI.” [UI-01, UI-09]
- **Do** preserve a conventional card grid, sidebar, dense table, or restrained
  visual language when it fits the domain and system. **Do not** replace useful
  familiarity solely for novelty. Genericness is interchangeability without
  task reason, not a component category. [UI-05, UI-09]

### Proof boundary

- **Do** let Design define validation targets and judge visual/task consequence;
  let UI render supported conditions, exercise behavior, inspect semantics,
  focus/input/announcements, and report exact evidence. **Do not** call source,
  a static mockup, one screenshot, a scanner, or an accessibility tree alone
  `interaction-tested`, `responsive`, `usable`, or `accessible`. [UI-05, UI-08;
  ADR-0006]

## 8. Architecture recommendation

### Decision: split interaction design from responsive-web design

The independent routing signals and ownership boundary now justify two flat,
directly routed Design leaves in a successor package:

1. **`ui-workflow-and-interaction-design`**  
   Signals: UI workflow, task/user flow, IA, navigation, form, validation,
   interaction pattern, state, error, recovery, permission, design-system
   definition/audit.  
   Owns: task model, information architecture, navigation/pattern decision,
   form intent, state/recovery intent, screen hierarchy, UI-system definition,
   and the concern-level Design/UI record.
2. **`web-and-responsive-design`**  
   Signals: website/web app responsive design, mobile/narrow/wide adaptation,
   reflow, reorder, disclosure, density, responsive navigation, container
   relationships, text expansion/zoom, responsive image/layout intent.  
   Owns: preserved web-task/content/state invariants and intended
   transformation across available space and use conditions, including
   preservation/translation of type, spacing, negative space, hierarchy,
   reading order, and crop relationships defined by shared domain leaves. It
   does **not** redefine their base rules or own framework breakpoints/queries,
   component semantics, focus/input, announcements, or rendered interaction
   proof; those stay with UI.

This is not a Design/UI split—the existing cross-Skill owner contract remains.
It is a medium split inside Design. A native-app flow can load the interaction
leaf without web-specific material. A responsive editorial/marketing page can
load shared composition/type/image plus the web leaf without a full application
state curriculum. A responsive web form commonly loads both.

- **Current measured payload:** approximately 544 proxy tokens.
- **First complete candidates:** approximately 2,800–3,800 tokens for
  interaction/IA/forms/states/systems and 2,000–3,000 for responsive-web. These
  are coverage estimates, not budgets; author full professional payloads first,
  then measure and ablate.
- **Expected load frequency:** interaction medium for application, form,
  navigation, state, and UI-system work; responsive-web medium-high only for
  explicit web/adaptation concerns. Static/fixed design loads neither unless it
  truly has UI behavior or responsive-web transformation.
- **Common combinations:** interaction + responsive-web for web applications;
  interaction + typography for forms/localization; interaction + culture or
  sources for privacy/consent/current policy; responsive-web + composition,
  typography, colour, or imagery for visual transformations; either Design leaf
  + Scoville UI when framework implementation/proof is requested.
- **No Print duplication:** `print-and-fixed-media-design` remains a separate
  cross-audit architecture question. This audit routes fixed composition to
  shared visual domains and production/export to Media.

The split is implementation-gated. `modules.yaml` currently forbids new IDs
under W-002, so a later architecture decision must add exact signals, generated
index entries, ownership checks, and migration. Until then, deepen the current
leaf in the two clearly headed lanes rather than omitting either. Candidate A
(one larger leaf) remains the strongest comparator; candidate C (ownership-only
stub) is rejected because Design must remain capable standalone and because
workflow/IA/form/responsive judgment is not implementation mechanics.

No smallest tested non-inferior payload exists. Admit the split only if open
routing proves independent selection and outcome ablation shows that web-only,
native interaction-only, and combined tasks retain all decisions and handoff
fields without hidden cross-reading.

## 9. Tests and claim ceiling

### Smallest open Terra High falsification set

1. **Generate / workflow and IA:** design a multi-role service with several
   entry channels, permissions, repeat tasks, interruption, and one linear
   transaction. Require task/object/decision model, IA/navigation rationale,
   pattern alternatives, recovery/completion evidence, and no invented user
   research or operational facts. Failure if it starts with screens/chrome,
   copies the organization structure, or uses click-count Gold.
2. **Generate / form and states:** design a consequential multi-step form with
   conditional questions, sensitive data, slow validation, save/re-entry,
   partial backend failure, and an irreversible final action. Require datum
   intent, grouping, state applicability, timing rationale, preserved input,
   recovery, confirmation/undo boundary, and culture/source escalation where
   needed. Failure if it lists every stock state or validates unfinished input.
3. **Critique / generic UI slop:** inspect two rendered dashboards: one
   conventional but task-specific and one visually fashionable but shell-first,
   fictitious, state-incomplete, and invariant across widths. Require
   observation → cause → consequence → parent repair; preserve the conventional
   winner. Failure if it bans cards/gradients/fonts or rewards novelty alone.
4. **Repair / responsive recomposition:** repair a desktop-only web workflow
   under long localized content, 400% zoom/reflow, narrow/wide containers,
   keyboard/touch, dense data, and an error state. Seed weak line breaks,
   uniform spacing, trapped gaps, decorative whitespace, and hierarchy/crop
   collapse at narrow width. Design must specify preserved type/spatial/task
   invariants and subject-specific transformations; UI must implement and prove
   framework mechanics. Failure if the answer supplies three scaled layouts,
   fixed font/spacing/breakpoint recipes, hides required content, or Design
   claims interaction proof.
5. **Design-system ownership:** an incumbent system lacks a component/state and
   a Design record proposes an owner-level addition. Require gap evidence,
   purpose/anatomy/variants/states/content/responsive intent, governance and
   migration, canonical record, UI implementation feedback loop, and no local
   near-duplicate.

Run current combined leaf, two-leaf candidate, current Core only, and a compact
non-split comparator on identical prompts. Generation, critique, and repair must
each appear. Test routing separately: native flow loads interaction only;
responsive content page loads web only plus shared visual experts; responsive
form loads both; fixed print loads neither; strict implementation/proof routes
to UI, not another Design leaf.

### Required evidence

- Deterministic: structured task/state/transformation contract completeness;
  source/content preservation; route/read trace; incumbent component/token
  references; no duplicate owner; stable canonical handoff fields.
- Rendered/runtime: representative populated states; affected viewports/window
  and container sizes; short/long/localized content; zoom/text scaling; relevant
  themes; focus/input handoff; announcements; error/recovery; before/after
  screenshots plus interaction trace. UI owns this evidence.
- Human/domain: task walkthrough by qualified reviewer; tree/first-click or
  representative findability testing where IA claims matter; form completion
  observation; users with relevant disabilities for usability evidence;
  product/legal/operations owners for policy, eligibility, and sensitive data.
- Research boundary: heuristic inspection can falsify obvious task/design
  defects but cannot manufacture user needs, prevalence, comprehension, or
  satisfaction.

### Claim ceiling

Passing supports only that the tested model created traceable task, IA, form,
state, recovery, system, and responsive decisions; preserved the Design/UI
owner split; caught the seeded failure families; and used bounded evidence
labels. It cannot establish usability, preference, conversion, accessibility
conformance, safety, legal/privacy compliance, design-system adoption, or
superiority across untested products, users, platforms, languages, frameworks,
and media. One reviewer and rendered simulations do not replace representative
users or deployed behavior.

## 10. Priority (P0–P3)

### P0 — ownership, truth, access, and consequential recovery

1. Correct the verification wording: Design defines/inspects intended outcomes;
   UI owns semantics, focus/input, announcements, framework mechanics, and
   rendered interaction proof when active. Design-only must name each unverified
   mechanic.
2. Retain and strengthen the no-fabrication floor for policy, eligibility,
   availability, contacts, emergency/support routes, permissions, privacy, and
   success state. High-consequence unknowns need an owner/source gate.
3. Require recovery and preserved input/progress for applicable form/state
   failures; never present success before irreversible commit or blame a user
   for a system condition.
4. Prevent access overclaims: a mockup, screenshot, scanner, or one interaction
   path cannot establish conformance or usability.

### P1 — professional all-round capability

1. Add task/object/decision flows, IA/navigation/findability, contextual pattern
   selection, and causal critique/repair.
2. Add form intent/grouping, validation timing, state applicability, partial/
   stale/offline/conflict outcomes, error prevention, and recovery.
3. Add the responsive transformation contract and direct
   `web-and-responsive-design` route while preserving subject-specific
   type/typesetting, spacing, negative space, hierarchy, reading order, and
   crops—and excluding Print/fixed and UI mechanics.
4. Define UI-system scope, governance, lifecycle, incumbent-first extension,
   and Design/UI constraint loop.
5. Replace fashion-based anti-slop language with task/system/state/responsive and
   rationale-to-artifact mismatch tests.

### P2 — selective loading and efficiency

1. Add and test the two flat route signals/ownership sets; preserve a combined
   comparator until non-inferiority is shown.
2. Compress only after each leaf passes generation, critique, repair,
   exception, handoff, and proof-boundary cases. Remove history, repeated
   examples, and model-prior exposition first.
3. Add tool-specific tree tests, accessibility scanners, viewport harnesses, or
   design-system adapters only when the execution environment and owner project
   supply canonical seams.

### P3 — enrichment only

- Historical HCI principle catalogs, exhaustive pattern atlases, platform style
  tours, fixed device matrices, and collections of “good UI” screenshots may aid
  education but do not close a current evidence-backed outcome gap. Keep them
  outside ordinary payloads.
