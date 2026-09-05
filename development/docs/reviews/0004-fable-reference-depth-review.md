# Fable 5.1 expert-reference depth review

Date: 2026-09-02  
Model requested: `claude-fable-5-1`  
Effort: `high`  
Session: `a876fe37-0aa0-47d9-94dc-ab00bdf22915`  
Cost reported by wrapper: USD 3.7276155  
Mode: read-only; no edits or sealed content

## Scope and context

Fable read the Design Core, module registry, all fourteen runtime references,
source and rule ledgers, maturity and Terra evidence, the relevant Decisions,
and the current UI ownership contract. It reviewed each leaf as selectively
loaded task instruction, not as an encyclopedia. It was asked to preserve flat
direct routing, the 1,800-token ordinary-leaf ceiling, typed breakable rules,
source-independent runtime behavior, and the Design/UI ownership split.

Fable's two cross-cutting findings were:

1. accepted Decisions require rule types, but no leaf visibly labels binding
   constraints, evidence-bounded rules, conventions, heuristics, preferences,
   or deliberate exceptions;
2. the expert-depth contract requires failure signatures and causal diagnosis,
   but no leaf consistently maps `signature -> cause -> smallest repair`.

These are review findings, not product evidence. They must be reconciled with
the independent per-reference Research audits before implementation.

## Per-reference findings

### `brief-and-concept.md`

Keep the bounded stub. Existing territory generation and the logo-swap test are
operational. Add a concept-carrier step, format-set survival test, three small
repair moves, and an exemption for utility artifacts where a forced visual
thesis would become decoration. Define specificity and distinctiveness through
observable subject evidence rather than style novelty.

### `composition-and-layout.md`

Retain one leaf and deepen it. Add signatures and repairs for equal spacing,
box-everything layouts, tangents, false alignment, centred-everything,
indistinguishable levels, scaled-not-recomposed variants, and unrelated
orphans. Add medium distinctions and explicit multi-page/spread pacing. Add
blur/squint and greyscale diagnostic views without turning scan patterns or
Gestalt into laws.

### `typography-and-writing-systems.md`

Current distinctions and source boundaries are sound, and one open Terra Latin
critique passed, but the leaf mostly names axes without procedures. Fable
recommended two direct leaves: `typography-and-typesetting` plus
`writing-systems-and-localization`.

Urgent additions include character confusability for safety-critical strings,
fallback metric drift, finish signatures with causal repairs, page/column break
quality, correctly scoped WCAG type criteria, medium-specific font licensing,
pairing and optical-size discipline, numerals and real font features, and
binding script constraints for shaping, casing, bidi, CJK, Thai/Lao, marks,
vertical text, and native-reader escalation. A 45–75-character Latin measure
may appear only as a contextual heuristic with render evidence and explicit
non-applicability to captions, tables, or CJK.

### `colour-and-reproduction.md`

Retain and deepen. Add a value-first role method, dark-mode role remapping,
failure signatures, a concrete CVD inspection procedure, exact WCAG criterion
scope, and a print/reproduction question block covering gamut clipping, spot
versus process, rich versus single black, ink limits, overprint, substrate,
paper white, dot gain, provider profiles, soft proof, and physical proof. Add
L-45 as current print authority; do not teach harmony wheels.

### `imagery-and-art-direction.md`

Keep the existing generation method. Add illustration abstraction and mark-
system direction, text-over-image compensation, technical placed-size and crop
fitness, a consistency inspection method, and a default prohibited-invention
list for generated/factual imagery. Reconcile the source-range mismatch between
the maturity ledger and runtime registry.

### `information-and-data.md`

Retain and deepen. Add diagram direction and edge semantics, map normalization,
bar-versus-line baseline distinctions, table-as-valid-form guidance, log-scale
disclosure, small-multiple choice, category order, locale-aware formatting,
and dashboard priority that does not turn every metric into an equal tile.

### `brand-and-visual-systems.md`

Keep the bounded stub. Add the reproduction floor for marks: minimum-size
tests, one-colour and reversed forms, reduction to favicon/app icon, hairline
and gradient survival, and similarity/trademark escalation. Clarify that brand
identity invariants span touchpoints while product UI system application stays
with the UI domain.

### `ui-and-interaction-design.md`

Retain and deepen modestly. Add navigation and pattern-selection decisions,
form intent, empty states, density and responsive-transformation choices, plus
common UI-slop signatures. Tag focus, target size, zoom/reflow, contrast, and
interaction checks as UI-owned implementation proof when UI is active; Design
owns intended communication and priority, not those mechanics.

### `motion-and-sequence.md`

Retain but correct accessibility urgently. Add WCAG 2.3.1 and 2.2.2 binding
floors and distinguish them from AAA guidance. Add kinetic-type reading holds,
loop/final-hold logic, vestibular-risk signatures, and the boundary between
Design's temporal intent and UI's interaction mechanics. Add L-14 to sources.

### `media-production-and-handoff.md`

Keep the strong artifact table and evidence labels. Add print questions for
bleed, trim, PDF/X, embedding/outlining, effective resolution, black,
overprint, dielines, transparency, and actual provider proof; add SVG live-text
versus outlines, profiles, raster variants, and tagged-document/reading-order
checks. Resolve whether packaging and wayfinding are real bounded stubs or
withheld, because current prose does not support their documented mapping.

### `critique-and-validation.md`

Keep the method stub. Add finding localization, one finding per cause, and the
rendered-control requirement for intent first claimed during critique. Unify
the three competing verdict vocabularies across Core, ADR-0007, and this leaf.
Preserve the one-reviewer and no-universal-taste-oracle boundary.

### `culture-ethics-and-provenance.md`

Retain. Add current-verification floors for maps, borders, flags, and place
names; image metadata and location/privacy disposition; minors and bystanders;
and third-party marks, products, and buildings in mockups. Replace or ground
the abstract phrase about power hidden by aesthetic neutrality.

### `sources-and-attribution.md`

Retain but avoid growth. Add an actual fact-check procedure, asset-permission
record, and compact attribution shape. The registry can be shortened to fund
these actions. NC, ND, and SA consequences require explicit escalation without
turning the leaf into a Creative Commons textbook.

### `style-direction.md`

Keep the existing compiler and avoid a named-style atlas. Add one dominant
lineage plus declared secondary influences, an anachronism/production-
technology consistency check, and an incumbent-brand invariant line. Remove
the SOL-ablation history from runtime prose.

## Cross-reference findings

- Editorial and multi-page ownership is incomplete: composition should own
  pacing/spreads and typography should own page/column break quality.
- Packaging and wayfinding are documented as routed stubs but not supported by
  runtime prose or source routing.
- UI-proof mechanics are not consistently tagged as UI-owned when both Skills
  apply.
- Motion lacks the source that contains its binding accessibility floor.
- Core, ADR-0007, and the critique leaf use competing judgment vocabularies.
- The imagery source range is inconsistent across registry, rule map, and
  maturity ledger.
- L-45 is present in the source ledger but absent from applicable colour and
  production modules.
- Typography lacks rule-source clusters for microtypography and numerals.
- Brand and UI need a one-line boundary for identity systems versus product UI
  systems.
- Font-loading/fallback mechanics need a Design-intent versus UI-implementation
  boundary.

## Fable priority order

1. Split and deepen typography, especially script constraints, confusability,
   fallback drift, causal repair, page breaks, WCAG scope, and licensing.
2. Correct motion accessibility scope.
3. Add visible rule typing and one judgment vocabulary.
4. Add composition failure signatures, medium distinctions, and multi-page
   structure.
5. Add colour reproduction, CVD procedure, and L-45.
6. Tag UI-owned proof and expand responsive-recomposition decisions.
7. Add imagery prohibited-invention and source reconciliation.
8. Add culture map/metadata/third-party-rights floors.
9. Add information-design diagram, map, and baseline guidance.
10. Add production print/export/tagged-document checks and settle packaging and
    wayfinding status.

## Do not bloat

Fable considered these existing mechanisms strong enough to preserve largely
as written:

- media-production artifact table and evidence labels;
- imagery generation method;
- brief/concept territory method after two small additions;
- style-direction compiler after removing evaluation metadata;
- critique method skeleton;
- source registry, which should become more actionable rather than longer.

## Claim boundary

After the proposed changes, the package could claim source-grounded and typed
applied guidance for tested scopes. It still could not claim native-reader,
font-engineering, print-vendor, CVD-user, cultural, legal, or cross-person
qualification; expert equivalence; global style mastery; or market-quality
output. Fable did not perform the requested exact-domain public-Skill prior-art
search, so those findings must come from the independent per-reference Research
audits.
