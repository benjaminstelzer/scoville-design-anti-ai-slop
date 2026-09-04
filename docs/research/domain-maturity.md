# Design domain maturity ledger

Date: 2026-09-02  
Status: W-015 source-grounded 28-leaf implementation candidate

This ledger prevents a broad competency map from becoming a broad competence
claim. Maturity states are cumulative:

1. `mapped`: professional scope and owner are identified;
2. `source-grounded`: routed guidance can map consequential claims to verified
   sources with explicit limits;
3. `behavior-tested`: generation, critique, and repair cases pass;
4. `production-tested`: relevant real media/vendor/platform constraints pass;
5. `human-validated`: blinded intended-context review supports the exact claim.

No domain may be described above its observed state. A source-grounded domain
is not yet a qualified design capability.

| Domain | Baseline state | Principal ledger sources | Version-one claim ceiling before tests | Missing qualification |
| --- | --- | --- | --- | --- |
| Brief diagnosis, research, concept generation | source-grounded | L-01, L-15, L-16, L-18, L-19 | Can route a source-grounded process; no outcome claim | Original generation cases, alternative quality, selection and revision evidence |
| Design history, style analysis, and visual-language synthesis | source-grounded baseline | L-01, L-10, L-33, L-34, L-35 | Can distinguish term classes, source and translate selected well-documented lineages, and prevent preset/cliché substitution; no exhaustive or global-style mastery claim | Sourced profile review, non-Western and vernacular authority, contemporary drift checks, multi-medium generation/critique/repair, and blinded human validation |
| Composition, hierarchy, grids, spatial relationships | source-grounded | L-01, L-10, L-13 | Can explain scoped principles and exceptions | Static/editorial/web generation, critique, repair, deliberate-exception review |
| Latin typography and typesetting | source-grounded | L-01, L-02, L-04, L-05, L-06, L-08, L-09, L-12 | Can guide and critique with license/source limits | Rendered multi-medium type cases and human review |
| Multiscript typography and localization | source-grounded | L-04, L-06, L-24 | Can require script-specific evidence and avoid Latin defaults | Native-reader review, fallback/font coverage, RTL/vertical/line-breaking cases |
| Colour as perception and visual system | source-grounded | L-01, L-14, L-17, L-23, L-32 | Can distinguish contrast, harmony, semantics, and technical colour scope | CVD review, gamut/reproduction cases, human colour-system judgment |
| Imagery, photography, illustration, and art direction | source-grounded baseline | L-01, L-10, L-17, L-18, L-28, L-36 through L-45 | Can direct, select, sequence, generate, critique, repair, document, and prepare imagery with rights/truth/access/reproduction gates; no expert-equivalent, global-rights, or guaranteed-consistency claim | Twelve-case blinded photography/illustration/campaign/factual/crop/print/consistency/access/rights/repair suite; tool-specific consistency, current provider/legal checks, supplier specifications, and human art-direction validation |
| Information design and data visualization | source-grounded | L-19, L-23, E-17 when added | Can select and critique basic chart/figure communication with uncertainty and access limits | Misleading-chart, narrative, interaction, uncertainty, map, dashboard, and handoff cases |
| Corporate Design and visual identity systems | source-grounded | `SRC-BRAND-CANON`, `SRC-CORPORATE-DESIGN-CONFORMANCE`, `SRC-BRAND-ARCHITECTURE` | Can create and audit a visual identity system and preserve binding incumbent CI; no generic Corporate Identity strategy or recognition claim | Greenfield system, strict conformance, contradictory-authority, rollout, governance and stakeholder validation |
| Logo and identity-mark form | source-grounded | `SRC-MARK-DESIGN`, `SRC-BRAND-EVIDENCE`, `SRC-ASSET-RIGHTS` | Can generate, critique and repair bounded mark forms and optical variants; no trademark or market-distinctiveness claim | Equal-fidelity mark mechanisms, contextual stress, rights review and human identity judgment |
| Communication and instructional/explanatory design | source-grounded | `SRC-COMMUNICATION-CANON`, `SRC-COMMUNICATION-CLARITY`, `SRC-INSTRUCTIONAL-COMMUNICATION` | Can structure message/visual relations and design an explanation or procedure from authoritative content; no universal comprehension or safety claim | Misreading, explanation, procedure, access-equivalent and participant comprehension cases plus qualified safety acceptance |
| Advertising and campaign art direction | source-grounded | `SRC-AD-CREATIVE-CANON`, `SRC-AD-CREATIVE-EVIDENCE`, `SRC-AD-ETHICS-CURRENT` | Can design and diagnose a persuasive visual platform and placement-native campaign family; no persuasion or business-outcome claim | Equal-fidelity creative mechanisms, whole-impression, CI, placement and controlled outcome evidence |
| Editorial and multi-page systems | source-grounded | L-01, L-08, L-09, L-27 | Can reason about page systems, pacing, navigation, typography, and production boundaries | Long-document content fitting, sequencing, navigation, copy/image rhythm, print/PDF production cases |
| Web and UI design judgment | source-grounded | L-14, L-15, L-16, L-17, L-24, L-26 | Can define hierarchy, workflow, adaptive composition, state presentation, and visual critique; UI implements when active | Solo/composed/opt-out traces, rendered workflow cases, user/access review |
| Motion, sequence, and temporal communication | source-grounded baseline | L-19, L-25, L-26, L-27, E-16 | Can frame hierarchy, pacing, essentiality, reduced motion, and evidence needs; no production-ready motion claim | Kinetic type, transition, narrative timing, continuity, audio relation, export and human temporal review |
| Print and fixed-media production | source-grounded baseline | L-01, L-17, L-27 | Can identify colour, bleed, trim, resolution, substrate and preflight questions; no current vendor-readiness claim | Current print-provider checks, PDF/X workflow, proofing, finishing, material and failure cases |
| Packaging graphics and SKU systems | source-grounded | `SRC-PACKAGING-GRAPHICS`, `SRC-PRODUCTION-PRINT` | Can generate critique and repair panel/SKU graphics on authoritative supplied geometry; no structure regulation barcode production or shelf-effect claim | Flat/assembled/SKU/thumbnail cases, physical mockup, regulatory/barcode/provider lanes and human choice evidence |
| Physical wayfinding and signage systems | source-grounded | `SRC-WAYFINDING-SYSTEMS`, `SRC-CARTOGRAPHY`, `SRC-DATA-ACCESS-LOCALE` | Can generate critique and repair physical journey/decision/sign-family intent from approved names and spatial truth; no installed-system claim | On-site route prototypes, unfamiliar/access users, safety/jurisdiction, fabrication and post-occupancy evidence |
| Accessibility and semantic equivalence | source-grounded | L-03, L-14, L-17, L-26, L-29, L-31 | Can enforce a functional floor, equivalent meaning, and medium-specific evidence routing | Non-web floor matrix, disability-led review, generated/critique/repair cases across formats |
| Culture, representation, ethics, IP, privacy, sustainability | source-grounded at professional-principle level | L-10, L-18, L-19, L-30 | Can identify risk, authority, missing local evidence, and required consultation; cannot declare cultural safety from generic knowledge | Diverse culture/script fixtures, community authority, jurisdiction, sustainability and consequence review |
| Critique, rationale, stakeholder collaboration | source-grounded | L-01, L-10, L-18, L-19, E-10, E-12, E-14 | Can structure evidence-calibrated critique and decision rationale | Localization/false-positive calibration, blind reviewer agreement, repair success, stakeholder transfer |
| Asset provenance, licensing, handoff and governance | source-grounded policy | L-18, P-01, ADR-0003 | Can preserve rights/evidence boundaries and route technical handoff | External-material receipts, asset ledger, installer-bundled attribution, receiver reproduction tests |

## Version-one rule

A routed reference may ship only when its domain is at least `source-grounded`
and every consequential rule maps to a ledger source. A merely `mapped` domain
may appear only as a bounded risk/owner/evidence stub; it cannot supply
specialist production advice. W-005 advances states only from recorded
generation, critique, repair, production, and blinded human evidence.
