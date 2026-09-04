---
format_version: 1
id: ADR-0022
status: accepted
created: 2026-09-02
accepted: 2026-09-02
scope: architecture/28-leaf-map
---

# Adopt the 28-leaf all-round design map

## Decision

Supersede the accepted 23-leaf successor map with 28 flat direct leaves by
adding:

- `logo-and-identity-mark-design`
- `instructional-and-explanatory-design`
- `advertising-and-campaign-art-direction`
- `packaging-graphics-and-sku-systems`
- `physical-wayfinding-and-signage-systems`

Keep Corporate Design in Brand and general Communication in the non-owning Core
record. Keep all leaves independently usable with empty `requires` and
`conflicts` and no sibling reads.

Packaging owns panel/face, assembled-state and SKU graphic systems only on
authoritative supplied geometry. Physical Wayfinding owns route, destination-
hierarchy, decision-point and sign-family systems while site/domain owners
retain destination names. Advertising owns persuasive visual platforms and
campaign variants, not strategy, copy, media buying or outcomes. Instructional
owns explanation structure and comprehension proof, not factual or safety
authority. Mark owns formal identity-mark construction and optical variants,
not brand governance or trademark clearance.

## Problem

The 23-leaf candidate distributes general craft well but lacks five
independently routable professional practices. Folding them into Brand, Concept
or Fixed Media would create monoliths and hide distinct states, proofs and stop
boundaries.

## Drivers

- The Skill must create, critique and repair all-round professional graphic
  design rather than list topics.
- Each new practice passed parent-cause, contrast-route, owned-state,
  distinct-proof, stop-boundary and applied-token-value tests.
- Public Skills provide useful mechanisms but no inspected competitor supplies
  complete evidence for these combined capabilities.
- SOL High review accepted the corrected architecture after exact-hash review.

## Considered alternatives

- Keep 23 leaves and deepen current generalists. Rejected because Packaging,
  physical Wayfinding, Mark, Instructional and Advertising have independent
  causal transformations and proofs.
- Add a broad Environmental Graphics leaf. Rejected until non-navigational
  spatial/exhibition territory has its own source and proof basis.
- Add a Communication Design leaf. Rejected by ADR-0021.
- Add structural packaging, architecture or safety-signage competence. Rejected
  as qualified disciplines outside the Design Skill's authority.

## Consequences

- Fixed Media no longer owns packaging panels/SKU systems and retains ordinary
  pages, spreads, slides, documents, posters, folds and fixed surfaces.
- Wayfinding does not absorb app navigation, standalone cartography, isolated
  signs or non-navigational environmental graphics.
- The generated index ceiling becomes 1,200 tokens; Core remains 1,500; target
  three and maximum four selected leaves remain; complete loaded context stays
  at or below 15,000 tokens and is measured before provider calls.
- Source ledger, rule map, routes, fixtures, manifests and UI ownership evidence
  change together.

## Confirmation

Model-free positive and near-neighbour negative fixtures cover every new leaf.
Exact Terra High open cases exercise its generation or repair, context render,
ownership and specialist stop. Historical 23-leaf calls remain visible but do
not qualify the new manifest.

## Revisit when

A new leaf cannot route independently, duplicates more than its standalone
integrity floor, or fails to improve the applicable generation/diagnosis/repair
case at acceptable context cost.
