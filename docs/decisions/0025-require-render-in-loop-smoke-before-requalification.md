---
format_version: 1
id: ADR-0025
status: accepted
created: 2026-09-02
accepted: 2026-09-02
scope: evaluation/render-and-routing
---

# Require a render-feedback smoke gate before requalification

## Decision

Do not run another broad behavioral suite on the current harness. First prove a
parent-mediated two-call development loop on the frozen current package:

1. Call A receives the seeded before render as a hashed `-i` image, performs the
   bounded source repair and returns a candidate artifact without seeing its new
   render.
2. A parent-owned pinned renderer creates candidate render 1 under frozen
   conditions.
3. Call B receives candidate source plus render 1 as a hashed `-i` image, records
   a render-specific observation and makes one targeted repair.
4. The same parent renderer creates render 2, which the independent evaluator
   inspects for the target repair and protected-content regressions.

This is explicitly not same-call visual inspection. Image-path, Base64, ANSI or
shell output never counts as image evidence. The smoke is development evidence
only and cannot qualify the Skill or enter a sealed holdout.

The renderer runs only in the parent, from a read-only parent-owned location.
Freeze helper, Edge executable, renderer version, viewport, profile/config,
font/input and output hashes; use absolute paths, no network, an output-root
guard and before/after integrity checks. Model workspaces cannot alter the helper
or renderer. Every future comparison arm receives identical render/injection
access and conditions.

Separately rederive route contracts symmetrically for all ten W-017 tasks in two
blind frozen phases. In phase 1, a fresh adjudicator receives each anonymized
task plus Core, the generated direct index and compact canonical ownership
summaries for all 28 leaves, then selects its own candidate leaves. In phase 2,
it receives the full ownership clauses only for that self-selected set and
records required owners, forbidden owners and either one exact valid set or
narrowly reasoned alternate exact sets. If all full ownership clauses fit the
frozen context, they may replace the two phases. The selector/adjudicator sees
no observed routes, Gold, receipts, statuses, verdicts, failure summaries or
case IDs. Freeze both phases' instructions, inputs and outputs before unblinding;
never widen an allowed list to fit observed behavior. W-017 remains immutable.

## Problem

W-017 completed with no case passing every dimension. Four cases routed exactly
but failed visible quality after evaluator-only rendering. Other cases exposed
Gold/ownership conflicts or genuine over-reading. The restricted child could
write SVG but had no tool that returned a newly created render as image content,
so source validation repeatedly certified artifacts with collisions, clipping,
generic forms or misleading geometry. D28-PK1 also timed out after repeated
artifact and validation work.

## Drivers

- Professional design claims require inspection of rendered artifacts.
- The chosen mechanism must work in the actual strict CLI configuration.
- One early canary is cheaper and more informative than another broad suite.
- Renderer access must not become mutable prompt leakage or a Skill dependency.
- Routing Gold must follow canonical ownership rather than observed leaf count.
- Existing failures must stay immutable and visible.

## Considered alternatives

- Same-call local rendering. Rejected until an actual tool can return generated
  image content to the child; writing a PNG alone is not visual inspection.
- A writable workspace helper. Rejected because the evaluated model could alter
  its own evidence instrument.
- Add more prose rules without repairing the proof loop. Rejected because the
  repeated failure occurred after source creation and before visual inspection.
- Increase timeout and rerun PK1. Rejected because render access does not solve
  its scope size and no retry is authorized.
- Rewrite only disputed Gold after seeing W-017. Rejected as asymmetric outcome
  leakage.

## Consequences

- W-018 first tests the frozen package before any Skill wording change.
- A passing smoke attributes the targeted repair gain to visual feedback and is
  not evidence that the Skill text needed modification.
- A failing smoke may justify a versioned change only at its demonstrated cause.
- The next packaging case is smaller or staged rather than given more timeout.
- Route reconciliation covers all ten tasks blind and produces a new versioned
  contract; W-017 remains unchanged.

## Confirmation

Provider-free preflight must validate parent renderer/helper isolation and exact
hashes. The smoke receipt must bind Call A input-image/source/output hashes,
render-1 hash and conditions, Call B image-input/source/output hashes, its
render-specific observation and targeted diff, render-2 hash, and independent
confirmation that the defect is gone without protected-content regression.
Both calls use exact Terra Medium, one at a time, with separate usage receipts.

The route adjudication receipt must bind phase-1 anonymized inputs, all-28
index/ownership summaries, instructions and self-selected candidates; phase-2
full-clause inputs and exact-set outputs; and final unblinding hashes for all ten
cases. Changed expectations require owner reasoning, not observed-route
similarity.

## Revisit when

The evaluated host gains a native image-content tool for newly created local
renders, or the product scope stops requiring editable visual artifacts.
