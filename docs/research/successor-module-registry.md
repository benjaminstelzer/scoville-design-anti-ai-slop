# Proposed professional-depth successor module registry

Date: 2026-09-02  
Status: historical accepted 23-leaf baseline; superseded by ADR-0022  
Authority for current implementation: ADR-0020 through ADR-0022 and
[`corporate-communication-and-boundary-gap-audit.md`](../audits/0003-corporate-communication-and-boundary-gap-audit.md)

This file freezes the proposed direct-route surface before `modules.yaml` or any
runtime reference changes. It is intentionally exact enough for SOL and Fable
to review routing, ownership, overlap, and missing capability.

## Registry rules

- Core selects every applicable leaf directly from task evidence.
- No leaf reads, requires, conflicts with, searches for, or simulates a sibling.
- A term alone is insufficient when the concern cannot change the result.
- Ordinary self-critique stays in Core. `deep_critique` is reserved for
  multi-domain, comparative, exception-heavy, localized, or proof-heavy work.
- Medium leaves own transformation and constraints, not the shared craft rules.
- Cross-owner tasks may select several leaves. Shared selection is not a hidden
  dependency.
- Status remains `stub` for new/split leaves until its open Terra High gates
  pass. Existing retained floors keep `retained-floor` while rewritten, but no
  new outcome claim transfers automatically from RC7.
- `requires: []` and `conflicts: []` stay empty in version one.
- Install-time source definitions live in non-routed
  `references/source-index.md`; full research provenance stays in
  `docs/research/`. Neither is a hidden expert route.

## Proposed signal enum

```yaml
signal_enum:
  - needs_brief_frame
  - needs_concept
  - complex_composition
  - typography
  - font_technology
  - writing_system
  - colour_system
  - reproduction
  - imagery
  - art_direction
  - data_story
  - spatial_story
  - relation_diagram
  - brand_system
  - ui_workflow
  - interaction_states
  - responsive_web
  - fixed_media
  - editorial_sequence
  - motion
  - sequence
  - production
  - handoff
  - deep_critique
  - rule_exception
  - culture_risk
  - privacy_risk
  - sustainability_claim
  - synthetic_evidence
  - source_audit
  - rights_provenance
  - license_attribution
  - named_style
  - cross_medium_style
```

## Signal definitions and negative boundaries

| Signal | Positive evidence | Does not trigger by itself |
| --- | --- | --- |
| `needs_brief_frame` | Required field is missing, contradictory, weakly authorized, or must be converted into explicit success/selection criteria | A complete supplied brief or ordinary restatement |
| `needs_concept` | The task asks for materially different ideas, concept territories, carriers, rough comparison, selection, or concept repair | Routine execution of an accepted direction |
| `complex_composition` | Hierarchy, grouping, grid, semantic spacing, negative space, reading order, crop relation, or a deliberate spatial exception can materially change the work | Any artifact merely because it has a layout |
| `typography` | Typeface roles, selection/combination, hierarchy, typesetting, microtype, or type repair is material | Any text string or minor copy edit |
| `font_technology` | Repertoire, OpenType/variation, optical instance, embedding, loading, fallback metrics, renderer, or font license/deployment can change the result | Ordinary type choice with known working fonts |
| `writing_system` | Mixed/non-Latin script, bidi, vertical, shaping, language-specific breaks, or unfamiliar-script safety is material | Locale mention with no typographic consequence |
| `colour_system` | Semantic colour roles, states/themes, contrast/non-colour cues, palette relationships, data colour, or colour repair is material | A single decorative colour preference |
| `reproduction` | Gamut, profile, output intent, spot/process, substrate, overprint, WCG/HDR, or cross-medium colour proof matters | “Print” when no colour/reproduction decision is open |
| `imagery` | Image selection, sequence, crop, photographic/illustrative role, documentary status, or image repair is material | An already-approved incidental image with no open decision |
| `art_direction` | A picture system, commission/capture/generation brief, controlled variation, or multi-image relation is required | Provider prompt syntax alone |
| `data_story` | Quantitative chart, table, dashboard, uncertainty, annotation, locale, or data-to-graphic handoff is material | A number used as ordinary copy |
| `spatial_story` | A map, projection, boundary, spatial normalization/classification, geoprivacy, or map alternative is open | Decorative map texture |
| `relation_diagram` | Typed nodes/edges, process, architecture, hierarchy, network, model parity, or notation is material | Ordinary page flow or decorative connector lines |
| `brand_system` | A change has identity, campaign, template, icon/pictogram/symbol-family, multi-touchpoint, governance, lifecycle, or recognition consequences | One supplied icon, colour, type, or layout choice with no system consequence |
| `ui_workflow` | Task flow, IA, navigation, form, interaction pattern, or product-system definition can change the outcome | Static marketing layout with no interaction task |
| `interaction_states` | State, permission, validation, error, recovery, stale/offline/conflict, or reversible/irreversible action intent is material | Hover polish alone |
| `responsive_web` | Web content or workflow must intentionally transform across available space, content pressure, zoom, or text expansion | Fixed print, fixed social graphic, or framework implementation mechanics alone |
| `fixed_media` | Fixed dimensions, physical/viewing context, poster, brochure, report, handout, presentation/slide deck, document, reusable template, face/fold, or fixed digital canvas changes the design | Any export or PDF alone |
| `editorial_sequence` | Pages/spreads, pacing, recurring anchors, folios, section transitions, or threaded content are material | A one-page grid only |
| `motion` | Change over time, kinetic type, animation, temporal data, continuity, interruption, or reduced/static equivalent is material | A static sequence description |
| `sequence` | Storyboard, ordered image/time states, beat structure, or cumulative temporal meaning is material | Editorial page order and still-image selection/order stay with Fixed Media or Imagery unless timing, animation, or storyboard behavior is material |
| `production` | Technical export, rebuildability, preflight, receiver/provider acceptance, format-specific semantic/access validation, or evidence beyond Core's ordinary create/render loop is material | Ordinary artifact creation, one intended render, or design advice with no technical delivery question |
| `handoff` | A receiver/provider needs authoritative source, variants, manifest, specifications, evidence, and acceptance state | Merely mentioning another team |
| `deep_critique` | Multi-domain audit, stable localization, comparison, parent-cause analysis, controlled rerender, disagreement, or proof state is required | Ordinary domain self-check |
| `rule_exception` | A departure is challenged, undeclared, cross-domain, or requires a rendered conventional control and deep comparison | A predeclared single-domain type/layout/colour/image exception with its owning leaf's intent, compensation, falsifier, and proof stays in that leaf |
| `culture_risk` | Living culture/community/identity, sacred or political symbol, stereotype, appropriation, contested place/name, or local authority is material | Generic “global” visual style |
| `privacy_risk` | Identifiable people, minors, bystanders, private location/data, releases, metadata, or re-identification risk is material | Public organizational contact data used as supplied |
| `sustainability_claim` | Environmental wording, seal, number, comparison, image, colour, or whole impression implies a benefit | Nature imagery with no plausible claim in context |
| `synthetic_evidence` | Generated, reconstructed, edited, or composite media may be mistaken for factual evidence or identity | Clearly fictional decorative illustration with no factual implication |
| `source_audit` | Material fact/claim/citation needs source inspection, independence, currentness, correction, or downstream reconciliation | A supplied non-consequential fact accepted by the brief |
| `rights_provenance` | Asset origin, rightsholders, releases, modifications, territory, duration, or depicted-right layers are open | Bibliographic inspiration with no shipped asset use |
| `license_attribution` | A font/image/data/code/media license, credit, notice, or survival through output must be resolved | A source citation that ships no licensed asset |
| `named_style` | A period, movement, vernacular, revival, or named visual direction needs interpretation and execution | Generic adjectives such as clean or premium alone |
| `cross_medium_style` | A selected style must preserve its mechanism across materially different media | One-medium rendering only |

## Proposed modules

The `sources` column names audit/curriculum clusters for authoring. Final source
IDs are generated only after each runtime rule cluster is independently worded
and mapped.

| ID | Status / intervention | `when_any` | `owns` | Source floor |
| --- | --- | --- | --- | --- |
| `brief-framing-and-criteria` | stub / focus | `needs_brief_frame` | `brief_frame`, `field_authority`, `required_content_manifest`, `degrees_of_freedom`, `selection_criteria`, `approval_authority` | Brief audit BF cluster; curriculum R-27/R-28 process floors |
| `concept-development-and-selection` | stub / focus | `needs_concept` | `concept_territories`, `concept_carriers`, `rough_comparison`, `concept_selection`, `concept_repair`, `originality_boundary` | Brief audit BF cluster and bounded parallel-prototyping evidence |
| `composition-and-layout` | retained-floor / external-verification | `complex_composition` | `visual_hierarchy`, `semantic_spacing`, `negative_space`, `spatial_system`, `layout_exception`, `content_fit` | Curriculum R-09 through R-13; Composition audit A-CL cluster |
| `typography-and-typesetting` | stub / external-verification | `typography` | `type_roles`, `glyph_differentiation`, `typeface_compatibility`, `type_hierarchy`, `typesetting`, `microtypography`, `type_exception` | Curriculum R-01 through R-08; Typography audit AT cluster |
| `font-technology-and-script-safety` | stub / external-verification | `font_technology`, `writing_system` | `font_technology`, `font_fallback`, `script_requirements`, `bidi_vertical`, `font_proof` | ADR-0016; Typography audit standards and current implementation sources |
| `colour-and-reproduction` | retained-floor / external-verification | `colour_system`, `reproduction` | `colour_roles`, `colour_access`, `gamut_boundary`, `reproduction_chain`, `colour_proof` | Curriculum R-14 through R-17; Colour audit sources |
| `imagery-and-art-direction` | retained-floor / external-verification | `imagery`, `art_direction` | `image_thesis`, `image_mode`, `shot_or_generation_brief`, `image_sequence`, `crop_system`, `image_treatment_integrity_floor` | Curriculum R-13 and R-18 through R-20; Imagery audit sources |
| `information-design-and-data-visualization` | stub / external-verification | `data_story` | `data_encoding`, `data_integrity`, `uncertainty_display`, `dashboard_information`, `data_handoff` | Curriculum R-21/R-22; Information audit chart/table/dashboard sources |
| `cartography-and-spatial-data` | stub / external-verification | `spatial_story` | `map_decision`, `spatial_encoding`, `map_normalization`, `cartographic_proof` | Information audit cartography, boundary, privacy, and culture sources |
| `diagrams-and-relational-information` | stub / external-verification | `relation_diagram` | `diagram_semantics`, `relation_encoding`, `edge_contract`, `diagram_proof` | Information audit diagram/model sources |
| `brand-and-visual-systems` | stub / focus | `brand_system` | `visual_identity_thesis`, `identity_grammar`, `icon_and_symbol_system`, `system_invariants`, `controlled_variation`, `brand_governance` | Curriculum R-23/R-24; Brand audit sources |
| `ui-workflow-and-interaction-design` | stub / external-verification | `ui_workflow`, `interaction_states` | `workflow_design`, `information_architecture`, `interaction_pattern_intent`, `state_recovery_intent`, `ui_system_definition`, `design_ui_record` | UI audit task/IA/form/state/system sources |
| `web-and-responsive-design` | stub / external-verification | `responsive_web` | `responsive_priority`, `responsive_transformation`, `density_disclosure`, `responsive_asset_intent`, `responsive_design_record` | Curriculum R-25; UI/Composition/Typography/Imagery responsive sources |
| `editorial-and-fixed-media-design` | stub / external-verification | `fixed_media`, `editorial_sequence` | `fixed_medium_contract`, `editorial_sequence`, `page_spread_system`, `presentation_document_template_system`, `fold_face_relationship`, `physical_design_constraints` | Curriculum R-05/R-09 through R-13/R-26; Composition and Production audits |
| `motion-and-sequence` | retained-floor / external-verification | `motion`, `sequence` | `motion_thesis`, `temporal_hierarchy`, `continuity_spine`, `kinetic_readability`, `reduced_equivalent` | Motion audit accessibility/craft/production sources |
| `media-production-and-handoff` | retained-floor / external-verification | `production`, `handoff` | `artifact_contract`, `authority_derivative_graph`, `format_validation`, `render_contract`, `production_preflight`, `handoff_record` | Curriculum R-17/R-26/R-30; Production audit MP cluster |
| `critique-and-validation` | stub / focus | `deep_critique`, `rule_exception` | `causal_critique`, `finding_record`, `generic_cliche_test`, `repair_priority`, `validation_rationale` | Curriculum R-27 through R-30; Critique audit A-CV cluster |
| `culture-and-representation` | stub / external-verification | `culture_risk` | `authority_boundary`, `representation_risk`, `cultural_protocol`, `contested_place_context` | Culture audit authority, community, representation, map/name sources |
| `people-privacy-and-media-integrity` | stub / external-verification | `privacy_risk`, `synthetic_evidence` | `participant_agency`, `consent_privacy`, `documentary_integrity`, `synthetic_evidence_boundary`, `metadata_privacy` | Culture/Imagery audit people, privacy, integrity, provenance sources |
| `sustainability-claims` | stub / external-verification | `sustainability_claim` | `environmental_claim_scope`, `lifecycle_boundary`, `substantiation_record`, `qualification_expiry` | Culture audit current claims/lifecycle/jurisdiction sources |
| `source-verification-and-evidence` | stub / external-verification | `source_audit` | `claim_registry`, `source_registry`, `evidence_relation`, `current_verification`, `correction_history` | Sources audit claim/evidence/currentness/correction sources |
| `asset-rights-and-attribution` | stub / external-verification | `rights_provenance`, `license_attribution` | `asset_registry`, `license_boundary`, `rights_layers`, `attribution_record`, `attribution_survival` | Sources/Culture/Production audit rights, license, credit, survival sources |
| `style-direction` | stub / focus | `named_style`, `cross_medium_style` | `style_interpretation`, `style_dna`, `anti_cliche_counterweight`, `medium_translation`, `style_proof` | Curriculum R-29; Style audit source and cultural/rights floors |

## Ownership collision rules

1. Typography owns typographic decisions. Composition owns macro spatial
   relationships. Their shared baseline or interval is resolved by the
   relationship causing the failure, not by load order.
   Typography always keeps a compact declared-fallback and actual-render floor;
   Font Technology loads only when repertoire, shaping, metric substitution,
   variation/features, deployment/embedding, or font license is materially open.
2. Web owns intended transformation. UI owns implementation mechanics and
   runtime proof. Composition, Typography, Colour, and Imagery keep their craft
   decisions when a web transformation affects them.
3. Composition owns the within-page spatial system. Fixed Media owns
   cross-page/slide sequence, recurring anchors, pacing, fixed viewing context,
   and template/page/spread/fold relations. Production owns file, preflight,
   receiver, and physical/provider proof. Resolve overlap by the relation that
   fails, not by medium name alone.
4. Information leaves own visual encoding. Data/statistical/cartographic/model
   authorities own factual and analytical correctness. Sources owns the durable
   evidence record.
5. Imagery classifies the image job and owns purpose, selection, crop, formal
   treatment, and a local no-invention stop. People/Privacy owns participant
   conditions plus documentary, constructed, and synthetic mode policy,
   permitted transformations, privacy, disclosure, and affected-person risk.
   Sources owns factual evidence. Asset Rights owns use-specific permission and
   attribution records. Culture owns authority and representational consequence.
   No leaf self-certifies legal, factual, documentary, or cultural clearance.
6. Brand owns identity grammar and governance. UI-system definition remains a
   Design concern in the UI workflow leaf; UI implements the incumbent system.
   Brand owns cross-touchpoint icon/pictogram/symbol family visual grammar,
   optical consistency, reduction, and system lifecycle. UI Workflow owns a UI
   icon's semantic job, state, accessible name, and interaction intent;
   Information leaves own data/map/diagram glyph semantics; Culture owns
   sensitive-symbol authority.
7. Style owns interpretation and cross-domain invariants. Craft leaves own the
   actual type, layout, colour, image, motion, and medium decisions.
8. Critique does not replace a domain leaf. It owns the deep finding and
   validation lifecycle when that lifecycle itself is material.

## Jurisdiction is a modifier, not a route

Current jurisdiction, provider, standard, contract, and receiver conditions are
captured after an applicable domain signal selects its owner. They may tighten a
binding floor, require current verification, add an authority, or stop release,
but they never select Culture, Privacy, Sustainability, or Asset Rights by
themselves. Model-free route fixtures must prove at least:

- an accessibility duty does not load Culture, Sustainability, or Asset Rights;
- a print-provider duty does not load those three leaves;
- a sustainability claim plus its jurisdiction loads Sustainability only among
  those risk leaves;
- a licensed asset with a territorial restriction loads Asset Rights, not
  Culture or Sustainability;
- a contested place-name duty loads Culture only when `culture_risk` is present;
- participant privacy/publicity law loads People/Privacy through `privacy_risk`,
  with Asset Rights additionally selected only when use permission is open.

## Exception routing fixtures

- A predeclared single-domain display-type exception with a local intent,
  compensation and proof selects Typography, not Critique (`C01`).
- A predeclared layout experiment that is challenged, crosses Fixed Media, and
  requires a rendered conventional control selects Composition, Fixed Media and
  Critique through `rule_exception` (`C04`).
- An undeclared or ambiguous cross-domain departure selects the owning leaves
  plus Critique only when the deep finding/control lifecycle can change the
  decision. Minor stylistic variation selects no Critique route.

## Expected common combinations

These are examples, not mandatory bundles:

- poster: Concept + Composition + Typography + Fixed Media; add Colour,
  Imagery, Style, or Production only when material;
- editorial publication: Composition + Typography + Fixed Media; add Imagery,
  Information, Brand, or Production as required;
- responsive marketing page: Composition + Typography + Web; add Style,
  Imagery, Colour, Brand, or UI implementation independently;
- web application: UI Workflow + Web, then the necessary craft leaves; active
  Scoville UI implements and proves the system;
- data report: Information + Typography + Composition + the actual medium;
- map: Cartography + the actual medium; add Culture for contested naming and
  Sources for material evidence;
- campaign system: Brand + Concept + selected craft/medium leaves;
- advertising/campaign format family: Concept + Brand plus the actual Web or
  Fixed medium, preserving one key visual, copy-image relation, content
  hierarchy, and controlled variation rather than cloning one hero layout;
- deep repair: owning domain plus Critique only when comparison, exception,
  localization, or validation complexity warrants it.

## Provisional load and phase contract

Before authored measurements exist, one task phase may load at most four expert
leaves and Core plus selected leaves may not exceed 15,000 `o200k_base` tokens.
Three remains the ordinary target. A task exceeding either limit splits into
separate model calls or user-visible phases with the compact Design record; a
logical heading inside one response does not unload prior context. After each
wave is authored, measured per-case and common-load budgets replace forecasts
before its canary. C08 and C19 are deliberately packed to three leaves; the
largest frozen cases use four.

The successor Core must replace RC7's “normally at most three” sentence with
this exact target, four-leaf exception, 15,000-token gate, and real separate-call
phase behavior.

`people-privacy-and-media-integrity` applies documentary and synthetic mode
policy even when no person is depicted; “people/privacy” names one branch, not
the entire activation boundary.

## Production architecture comparator

The proposed registry retains one selectively routed
`media-production-and-handoff` leaf because source authority, derivative hashes,
validation, rendering, proof labels, receiver state, and source-first repair are
shared across outputs. The route is now deliberately narrow: ordinary artifact
creation and intended rendering stay in Core or the artifact-format Skill.

Before authoring the production runtime or making its first Terra call, W-012
must compare two non-executable payload maps on the same route corpus and token
accounting:

1. one 2,800–4,000-token leaf with a compact common spine and clearly headed
   SVG/raster, print/PDF, document/presentation, motion, and Web/UI gates;
2. flat format leaves that each repeat the minimum standalone authority,
   derivative, repair, and receipt floor.

The unified leaf is retained only if the route corpus shows that technical
delivery tasks commonly need the shared spine and that unrelated format gates
do not materially dominate loaded context. Select format leaves if signals are
independent, routine co-loading is low, and duplicated floors remain smaller
and causally complete. This comparison is model-free. A change from the
reviewed one-leaf map changes ADR-0017 and requires a new focused SOL review;
Fable is included only if the user reauthorizes it.

## Review and implementation gate

ADR-0017 through ADR-0019 remain proposed until Fable's independent findings
are visibly reconciled, the user's explicit no-further-Fable waiver is recorded,
and fresh SOL returns `READY` with no unresolved Blocker or High against the
corrected exact registry, Audit 0002, active Plan, source/curriculum evidence,
and test contract. The waiver does not become Fable approval or product
evidence. Only then may this map replace executable `modules.yaml`.

## Validator migration required before authoring

The RC7 validator hardcodes fourteen module IDs, treats 1,800 tokens as a hard
error, assumes `references/sources-and-attribution.md` is both an expert and the
source registry, rejects every non-routed reference as an orphan, and enforces
the old 3,800/7,000 context ceilings. Those checks are historical and cannot be
silently applied to the reviewed successor.

Before runtime authoring, update and test the structural validator with
synthetic fixtures so it:

- validates the exact accepted twenty-three IDs and their order;
- permits exactly one declared non-routed `references/source-index.md`;
- resolves source headers and rule clusters through that index plus the
  repository rule-to-source map;
- supports a 1,800 warning target plus explicit provisional and measured
  per-leaf ceilings without accepting a missing measurement at a canary gate;
- can measure Core, index, every leaf, planned common combinations, and the
  largest permitted phased load once authored files exist;
- keeps duplicate ownership, unknown signals, sibling links, hidden
  dependencies, index drift, and unresolved source IDs as hard errors.

After each wave is authored and before that wave's canary, populate actual leaf
and common-load counts and enforce its measured budgets. The complete package
budget must pass before SkillOpt. New numeric budgets derive from authored
payloads and accepted case packing; they are not invented before prose exists or
copied from RC7 merely to make the new package pass.
