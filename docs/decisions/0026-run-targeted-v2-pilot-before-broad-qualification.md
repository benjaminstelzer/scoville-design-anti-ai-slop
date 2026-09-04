---
format_version: 1
id: ADR-0026
status: accepted
created: 2026-09-02
accepted: 2026-09-03
scope: evaluation/targeted-pilot-and-skillopt
---

# Run a targeted v2 pilot before broad qualification

## Decision

Before W-005 broad qualification, run a small open development pilot under
exact Terra Medium and the accepted v2 route contract. Cover only three causes
that remain unresolved after W-018:

1. a staged one-SKU Packaging + Typography repair that must exclude Composition;
2. a compact physical Wayfinding + Cartography repair that must exclude
   Diagrams, Instructional and UI;
3. a subject-specific Mark mechanism generation that must produce materially
   different professional forms rather than generic glyph variants.

Run all three baselines first from exact manifest
`CD3931B3E56E0EA86CF2C355E5243C77BFC2F0DA47899545BC870B8E57D03A28`;
accept no edit between them. Use the parent render/inject loop only when visible
artifact feedback is needed. Inspect each call before the next. A classified
product failure may allow the next distinct baseline; any unclassified harness,
benchmark or integrity defect stops the whole pilot.

If the unchanged package passes a case, make no Skill change. SkillOpt is
eligible only when the W-019 failure matches that cause's preregistered W-017
owner/signature: Packaging over-reads Composition, Wayfinding substitutes
Diagrams/Instructional for Cartography, or Mark collapses materially different
mechanisms into generic near-variants. A new signature, benchmark ambiguity or
harness defect stops that optimization lane. One eligible proposal branches
from the same frozen parent manifest and is limited to Core plus the owning or
incorrectly selected leaves, followed by one same-condition paired development
rerun and relevant deterministic negatives. This is not causal or qualification
proof under stochastic sampling.

Keep accepted proposal diffs isolated until all eligible lanes finish. Merge
only compatible passed diffs, then run all three cases once as an integrated
regression on the merged manifest; there is no repair call in this final gate.
If no proposal is accepted, the three baseline results are the final set. Reject
and revert a proposal whose paired rerun fails any required dimension; no second
proposal is allowed. Reject task-noun encoding, always-load expansion, ownership
weakening, context regression or wording-only improvement.

## Problem

W-017 could not qualify the candidate, while W-018 proved that several failures
were caused by missing render feedback or incorrect Gold. Two true route defects
remain for Packaging and Wayfinding, and Mark generation remained visually
generic despite exact routing. Running the complete qualification matrix before
these focused causes pass would repeat avoidable cost and ambiguity.

## Drivers

- The user requested Terra Medium, fast per-call inspection and SkillOpt.
- Skill changes need same-condition paired development evidence rather than
  post-hoc intuition.
- Passing unchanged behavior must not be turned into unnecessary prompt growth.
- Professional visual quality requires rendered artifact evidence.
- Every Skill must remain standalone and task-scoped.

## Considered alternatives

- Begin the full W-005 suite now. Rejected because three known root causes remain.
- Optimize all affected leaves at once. Rejected because attribution would be
  lost and context/routing could broaden.
- Treat the W-018 BO smoke as qualification. Rejected because it is a reused
  development fixture and explicitly zero-credit.
- Add stronger imperative prose without a baseline. Rejected because current
  clauses already support the blind v2 contract.

## Consequences

- All baselines share one exact parent manifest and precede every edit.
- At most one SkillOpt proposal and one paired rerun occur per eligible cause.
- Packaging remains staged; no timeout extension is used.
- Every proposal is evaluated on exact route, rendered outcome, owner/stop,
  claim boundary and context cost separately.
- If proposals are merged, a final no-repair three-case integrated regression
  protects earlier passes and exposes cross-proposal regression.
- W-005 remains blocked unless all three final cases pass every required
  dimension.

## Confirmation

Freeze at most 18 provider calls before execution: up to six Terra calls for
three two-call baselines; up to three exact-model/effort SkillOpt optimizer
calls; up to six Terra calls for three two-call paired reruns; and exactly three
single-call integrated regressions if at least one proposal is merged. Unused
conditional calls disappear; there is no retry reserve. Every call runs alone
and gets a receipt before the next.

Each baseline has frozen prompt/input/package/route/render contracts and a
receipt. A SkillOpt proposal records exact editable files, parent manifest,
diff, rationale and rejection gates. The paired rerun changes only the isolated
proposal package; input, prompt, renderer and scoring remain fixed. A proposal
or paired rerun that fails route, visual, ownership, evidence, context or
deterministic regressions is rejected and reverted with no second proposal.
Package, v2 route, 39 deterministic routes, Design/UI boundary, Skill Creator,
Plan, local links and manifest checks pass after every accepted change and on
the merged candidate.

## Revisit when

Any baseline exposes a harness defect, the current package passes all three
causes without optimization, or a proposed change cannot be isolated to one
demonstrated cause.
