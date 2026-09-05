---
format_version: 1
id: ADR-0028
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: evaluation/rendered-repair-admission
---

# Admit parent-rendered repair before broad qualification

## Decision

Recommended: preserve the failed v3 one-call evidence and use each of its three
frozen outputs as Call A in one bounded parent-rendered repair pair. Inject the
exact Call-A source and parent render into exactly one Terra Medium Call B per
case on the unchanged v3 package. Then parent-render the result once. Permit no
package edit, SkillOpt, retry, third call or reserve.

Call B must retain the exact repaired ownership route: Packaging plus
Typography for PK2-A, Wayfinding plus Cartography for the physical map, and
Mark only for the settled mark mechanisms. It may repair only the observed
render or source/report contradiction. All three final artifacts must pass
structure, exact route, visual quality, evidence alignment and context gates
before W-005 resumes.

If this admission gate passes, visual generation and repair lanes in W-005 may
use the same parent-mediated two-call mechanism only with identical renderer,
image access, call budget and stop rules for every comparator arm. First-call
routing and ownership remain separately scored and cannot be rescued by Call B.

## Problem

The accepted ADR-0027 repair made all three exact routes pass, but the one-call
artifacts still failed rendered professional quality or source/report
alignment. The child model had no view of its generated output. Adding more
task-specific prose would encode the three benchmarks while leaving the missing
render observation unchanged. Starting the broad suite would violate the
accepted admission gate.

## Drivers

- The Skill already requires creation, rendering, inspection, repair and exact
  evidence labels.
- W-018 proved that parent-render injection can expose and repair a visual
  defect without granting browser or renderer access to the child workspace.
- The v3 first calls and renders are immutable and already provide valid Call-A
  evidence, so repeating them would add stochastic cost without new proof.
- Qualification arms require equal tool access and budgets.
- Exact route failures must remain visible even when a later artifact repair
  succeeds.

## Considered alternatives

- Add another layer of Packaging, Wayfinding and Mark prompt rules, then run a
  v4 one-call suite. Rejected because the remaining failures are visible-output
  defects and this would encode benchmark symptoms without supplying the
  missing observation.
- Start W-005 despite the failed v3 visual gate. Rejected because ADR-0027
  explicitly requires all three dimensions to pass first.
- Treat the earlier W-018 smoke as sufficient. Rejected because it used one
  development canary and cannot prove these three current outputs.
- Stop with an unqualified package. This preserves evidence but does not meet
  the requested objective.

## Consequences

- At most three additional Terra Medium calls precede broad qualification.
- The current v3 package and exact-route results remain unchanged.
- A successful pair proves only these open repair paths, not general visual
  competence or causal superiority.
- Later W-005 two-call comparisons must pay the same call and renderer budget
  for every arm and report first-call and final outcomes separately.
- Any failed final dimension keeps W-005 paused and remains visible.
- No sealed call, publication, installation, commit, push, tag or release is
  authorized.

## Confirmation

Confirm by accepting this Decision. Implementation is confirmed only when the
three existing Call-A sources and renders are hash-verified, each receives one
and only one exact Terra Medium repair call on manifest
`81530628273139A1518B9D44A309CF10ED6FE41585E35A0D6C54C236F547D6DF`,
and all three final parent renders plus route, structure, evidence and context
checks pass without another package change or provider call.

## Revisit when

Any Call-A artifact or render hash changes, Call B selects a different owner,
one final render still fails, the repair needs a package edit, or equal
two-call/tool parity cannot be maintained across W-005 comparator arms.
