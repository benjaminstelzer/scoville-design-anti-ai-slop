# W-012 open Terra High call plan

Date: 2026-09-02  
Status: active W-012 execution contract; calls require the gates below  
Model: exact `gpt-5.6-terra`, reasoning `high`

## Purpose

Prevent a later large-batch surprise while preserving professional outcome
coverage. Model-free checks own routing positives/negatives, schema, source IDs,
read graphs, hashes, syntax, deterministic artifact invariants, and renderer
health. Open model calls are packed around coherent artifacts so several leaves
can be falsified independently in one terminal response.

Every provider request counts, including failed transport after a request,
SkillOpt arms, and retries. A model response is terminal even when the artifact
or score fails. No next call runs until the preceding response, read graph,
artifact, render, deterministic checks, and token receipt are inspected.

`leaf-contract-matrix.yaml` is the canonical machine-readable case, mode, wave,
leaf, dimension, and budget mapping. Run
`python docs/evaluation/validate_open_call_matrix.py` after every change to this
Plan or that matrix. The validator rejects a missing dimension, case/leaf drift,
noncanonical mode, future-wave canary dependency, changed hard call total, or
any credited case/leaf/dimension without its own non-empty falsifiable
assertion.

## Frozen ceilings and stop gates

| Lane | Planned calls | Reserve | Hard maximum |
| --- | ---: | ---: | ---: |
| Coverage-complete package and ownership | 22 | 5 | 27 |
| SkillOpt and focused non-inferiority checks | 15 | 4 | 19 |
| **W-012 total** | **38** | **8** | **46** |

- Expected provider-total tokens: about **3.2 million**, using 70,000 per call
  as a planning estimate from the six earlier Terra open responses, whose mean
  was about 64,217. This is a forecast, not a promise.
- Hard provider-total token ceiling: **5.0 million** for W-012.
- Expected uncached-input-plus-output tokens: about **1.5 million** based on the
  earlier observed ratio. Hard ceiling: **2.75 million**.
- Stop immediately before request 47, before either hard token ceiling, or when
  the remaining reserve cannot cover a known failing route.
- Provisional pre-authoring load gate: normally three expert leaves, at most
  four, and Core plus selected leaves at most 15,000 `o200k_base` tokens. Exceed
  either only through a separate model call/phase; headings inside one response
  do not unload context. Measured wave budgets replace forecasts before canary.
- Re-authorize with the user before increasing a call or token ceiling. A hard
  behavior miss is not repaired by spending the reserve blindly.
- Existing Codex receipts do not expose a direct USD charge. Before C01, record
  whether the host/account is subscription-covered or directly metered. If a
  nonzero direct metered charge would occur, calculate the expected and hard
  maximum cost from the then-current official account price and request user
  approval before the first billable call. Do not invent a dollar estimate.
- Fable review cost is outside W-012 and retains the Ask-Claude Skill's separate
  USD 10 ceiling per consultation.

## Model-free prerequisite matrix

Before C01, all of these pass without a model call:

1. exact signal enum, positive routes, near-neighbor negatives, and ownership;
2. jurisdiction-modifier fixtures with no cross-risk fan-out;
3. no sibling reads, `requires`, or `conflicts`;
4. source-header and consequential-cluster resolution;
5. rule-type and numeric-scope linting;
6. Core, leaf, common-combination, and phase token accounting;
7. local links, package layout, generated index drift, and Skill Creator checks;
8. renderer/parser/security canaries for every artifact format used below;
9. Design-only, UI-only fallback, composed, and opt-out route fixtures;
10. immutable case inputs, acceptance assertions, render conditions, and
   per-leaf credit recorded before any output is visible.

## Coverage calls

The first call of each implementation wave is its canary and counts toward the
leaf contract. A row can credit several leaves only when each has separate
predeclared failure and acceptance assertions. One attractive aggregate result
cannot pass all selected leaves.

Case IDs are stable identities, not execution order. Execute by wave:
`C01,C03`; `C06,C02,C04,C05,C07,C08,C09,C10`; `C11,C12,C13`;
`C14,C15,C16,C17`; then `C18,C19,C20,C21,C22`.

| ID | Wave and task | Selected Design leaves | Canonical mode and independent acceptance |
| --- | --- | --- | --- |
| C01 | A canary: fixed 1200 × 1600 SVG Latin reading specimen with real copy, settled licensed fonts, one predeclared single-domain display exception, intended-size and unchanged proportional thumbnail views | Composition, Typography, Fixed Media | `generate`; type roles/compatibility/setting, semantic spacing/hierarchy, and fixed-canvas/viewing intent each have separate assertions; the declared type exception stays in its owning leaves and does not select deep Critique, Font Technology, Production, or Asset Rights |
| C02 | Read-only critique of a source-bounded styled responsive Latin page with weak adjacent hierarchy, rivers, bad punctuation/numerals, and one valid expressive exception | Typography, Web, Style | `critique`; localize type, responsive and style causes separately, describe the smallest repairs, preserve the valid exception, and make no edit or runtime-proof claim |
| C03 | Repair a mixed Arabic/Latin notice plus supplied Japanese vertical annotation using controlled fonts after selecting the supported font, shaping and fallback plan | Font Technology | `repair`; make the font-technology decision explicit, detect script/direction/repertoire/shaping/fallback, reject Latin defaults, render actual text, and escalate native quality without claiming it |
| C04 | Generate a public-event poster with a predeclared off-grid title experiment that is challenged through a rendered conventional control | Composition, Fixed Media, Critique | `generate`; the cross-domain control requirement activates `rule_exception`; test counterstructure, negative-space job, intended gain/cost/falsifier, final-size render, and no preference inflation |
| C05 | Repair a four-page editorial family with long/short content, protected crop, recurring anchors, one faulty parent token, and one intentional asymmetry | Composition, Typography, Fixed Media, Critique | `repair`; page/spread/strip continuity, breaks, parent-cause change, preservation, and print-intent record |
| C06 | B canary: frame an incomplete consequential brief, generate materially different concept mechanisms and comparable roughs, then select by hard gates with one utility-artifact exception | Brief Framing, Concept Development | `generate`; field authority and unknowns stay separate from concept carriers, rough comparison, selection, and concept repair |
| C07 | Create a professional 1980s retro-computing event webpage, explicitly disambiguated from generic synthwave and tested at narrow/wide sizes | Style, Web, Typography, Composition | `style-direction`; sourced style sense and production cause, subject relation, anti-cliché removal test, responsive recomposition, type and spacing quality |
| C08 | Repair an inaccessible cliché-heavy Web-Brutalist service interface while preserving a source-bounded raw-data relation | Style, UI Workflow, Web | `repair`; preserve the style invariant, repair task/state/recovery/responsive causes, test the exception, and hand UI mechanics to Scoville UI |
| C09 | Generate a responsive consequential multi-step service workflow with IA, roles, permissions, validation timing, partial/stale/offline/conflict states, and recovery | UI Workflow, Web | `generate`; no fabricated facts, complete applicable state model, intentional responsive transformation, system-governance record, and no runtime-proof claim |
| C10 | Repair responsive form states through composed Design plus Scoville UI in an incumbent framework/design system | UI Workflow, Web | `repair`; Design record stays canonical, UI implements mechanics and proof, no duplicate/simulated Skill reads, fallback and opt-out remain valid |
| C11 | C canary: repair a role-based campaign colour system across screen, dark/forced states, office print and a named print destination with a seeded transform/overprint defect | Colour | `repair`; role/state/theme/destination decision, causal critique, redundant cues, transform-chain repair, scoped proof and no universal print recipe |
| C12 | Repair a photo-led story using a supplied contact sheet, documentary constraints, responsive crops, text relation, one prohibited invention, and a participant condition | Imagery, People/Privacy, Web | `repair`; image job/selection/crop stays separate from mode policy, participant conditions and source evidence; no factual or permission overclaim |
| C13 | Repair an identity and campaign rollout with a weak variable grammar across mark, icon/pictogram family, dense template, small context, co-brand, localization, expiry and migration | Brand | `repair`; approved inputs, identity and icon/symbol grammar, optical/semantic family stress, controlled variation, causal system repair, lifecycle/governance, and bounded recognition claim |
| C14 | D canary: repair a supplied responsive figure and exact-value route using rates, intervals, missing/suppressed data, locale variants and one legitimate non-zero or transformed-scale condition | Information Design, Web, Typography | `repair`; source/transform parity, chart/table decision, causal critique/repair, bounded scale exception, uncertainty, locale/access, responsive transformation and type hierarchy |
| C15 | Repair or replace a supplied map using counts, populations, boundary vintage, uncertainty and one contested place name after comparing a chart alternative | Cartography, Culture, Source Verification | `repair`; normalization/projection/boundary diagnosis, smallest map-or-form repair, place-name authority, a scoped jurisdictional naming exception or claim boundary, source state, and no neutrality/cartographic-expertise claim |
| C16 | Repair a relational diagram generated from a typed process/system model with seeded reversed/merged edges and proximity ambiguity | Diagrams | `repair`; model parity, causal critique, edge repair, key/geometry, accessible structured alternative, notation claim boundary and proof |
| C17 | Repair a kinetic-typography/data sequence with weak holds, interruption/reverse failure, flashing risk and missing reduced/static equivalent | Motion, Typography | `repair`; temporal thesis/decision, causal critique and repair, reading holds, continuity, exact safety/claim boundary, equivalence and timed evidence |
| C18 | E canary: rebuild and hand off a live-text SVG, raster variants, print/PDF derivative, tagged document or presentation derivative, and one package-face or sign/display job record with seeded font/profile/resource/reading-order defects | Media Production, Fixed Media, Colour | `repair`; authority/derivative hashes, source-first repair, template/page/slide/read-order assertion, syntax/render/semantic/export/provider evidence separation, specialist packaging/wayfinding stop, and no render-as-production proof |
| C19 | Read-only critique of a fixed campaign poster with a cross-page/format relation and one challenged off-grid exception | Composition, Fixed Media, Critique | `critique`; localize within-page versus cross-format causes, test fixed-medium pacing/context, propose the smallest repair and compensation, and make no edit or preference/proof overclaim |
| C20 | Repair a documentary-versus-synthetic public image with bystander/minor, location metadata, generated reconstruction and disclosure choices | People/Privacy, Imagery, Source Verification | `repair`; mode policy, permitted operations, consent/privacy/metadata, factual evidence, smallest repair, claim boundary and visual-treatment ownership remain distinct |
| C21 | Repair an environmental campaign with quantitative comparison, certification mark, nature-coded whole impression, lifecycle omission and expiry | Sustainability, Source Verification, Colour, Imagery | `repair`; exact claim/implication, baseline/scope/lifecycle/evidence/tradeoff/expiry, smallest truthful visual repair, proof and no legal-clearance claim |
| C22 | Repair and hand off a font/image/data package with layered rights, territory/duration limits, dependent claims/captions/credits and broken output attribution | Asset Rights, Source Verification, Media Production | `repair`; stable claim/source/asset IDs, use-specific rights, attribution compilation/survival, dependent correction, proof and fail-closed unknowns |

## Coverage accounting

- Every proposed leaf appears in at least one row and every contract dimension
  resolves in the machine-checkable leaf matrix.
- Canonical modes are exactly `generate`, `critique`, `repair`, and
  `style-direction`. Exception and claim boundary are separate dimensions.
- C01, C06, C11, C14, and C18 are the five wave canaries; they are not extra
  calls.
- C09 and C10 cover Design-only and composed ownership. UI-only fallback and
  opt-out routing are model-free unless a changed UI response path requires one
  of the five coverage reserves.
- A call that fails one leaf can still provide evidence for another only when
  the artifact and frozen assertion for that other leaf remain valid. The
  failure stays visible.

## SkillOpt call allocation

SkillOpt begins only after C01 through C22 pass their hard behavior or an
explicitly accepted bounded failure state. It gets at most eight proposal
groups, each with one candidate call and one focused non-inferiority call:

1. Core and route wording;
2. Typography plus font safety;
3. Composition plus fixed medium;
4. Style plus responsive web;
5. UI workflow and Design/UI ownership;
6. Colour, imagery and brand;
7. information, cartography, diagrams and motion;
8. production, sources, rights, culture, privacy and sustainability.

The fifteen planned calls support at most seven complete candidate plus
non-inferiority pairs and one additional candidate exploration. An eighth
candidate cannot be promoted without assigning one SkillOpt reserve call to its
focused non-inferiority pair. The four SkillOpt reserve calls may repair a transport/infrastructure failure or
repeat one changed high-risk group. They may not open a ninth optimization
group. A proposal is rejected if it saves tokens but loses a rule type,
failure-cause-repair mechanism, exception, owner boundary, proof requirement,
or independently falsifiable leaf assertion.

The eight groups are scheduling opportunities, not a promise to optimize every
leaf. Each candidate/non-inferiority pair must reuse one frozen coverage case;
a proposal may change only leaves directly credited by that case, and every
changed leaf must have a case-specific assertion in the pair. Leaves without a
valid paired case remain coverage-complete and unoptimized.

## Reporting

After every call, append exact model/effort, selected files, response status,
provider-total/cached/uncached/output tokens, artifact hashes, renders,
deterministic results, leaf assertions, failure class, and remaining budget to
the open-evidence ledger. Report coverage and SkillOpt spending separately.
