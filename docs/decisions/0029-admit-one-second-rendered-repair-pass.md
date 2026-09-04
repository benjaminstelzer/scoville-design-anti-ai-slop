---
format_version: 1
id: ADR-0029
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: evaluation/second-rendered-repair-pass
---

# Admit one second rendered repair pass

## Decision

Recommended: preserve W-020 as a failed admission under ADR-0028 and create a
separate follow-on gate for the existing Wayfinding result. Permit exactly one
Terra Medium Call C with the unchanged v3 package, exact Wayfinding Call-B
source and report, and its parent render. Retain the exact Wayfinding plus
Cartography route. Change only the remaining `S-ENT-01` occlusion of `NODE
GAL-B` and `Gallery B`, then parent-render the result once. Permit no package
edit, retry, fourth call, reserve or SkillOpt proposal.

Call C is eligible because Call B passed exact routing, source structure,
topology, IDs, content and evidence boundaries, while its first post-repair
render exposed one remaining visible defect that the child could not inspect
inside that call. If Call C passes every final dimension, the admitted set is
PK2-A Call B, Wayfinding Call C and Mark Call B. W-005 may then use at most two
parent-rendered repair passes after an initial artifact call, with identical
maximum call count, renderer, image access, stop rules and budget for every
comparator arm. First-call routing and artifact outcomes remain separately
scored and cannot be rescued retrospectively.

## Problem

ADR-0028 admitted one parent-rendered repair call per case. PK2-A and Mark
passed, but the Wayfinding repair moved the original arrival panel and central
collisions while leaving `S-ENT-01` over the Gallery B node label. The package,
route, source contract and deterministic gates remain valid. The failed final
render means W-005 cannot resume under ADR-0028.

The Skill's Studio loop already permits up to two coherent repair passes. A
child call can inspect the supplied prior render but cannot inspect the artifact
it creates before returning. The missing observation is therefore the first
post-repair render, not another domain rule or route correction.

## Drivers

- Preserve the failed ADR-0028 result rather than relabeling it as success.
- Test the existing two-repair-pass Studio limit without editing the package.
- Keep the second repair restricted to one rendered defect and the same owner.
- Maintain equal tool access and maximum call budgets across later comparator
  arms.
- Avoid benchmark-specific package prose or an evaluator-authored artifact fix.

## Considered alternatives

- Stop with the candidate unqualified. This is the lowest-cost option but does
  not meet the requested objective of completing development and qualification.
- Edit Core or the Wayfinding expert and run a new v4 regression. Rejected as
  the current failure is a post-repair visible overlap, not a demonstrated
  package ownership or instruction defect.
- Hand-edit the SVG in the parent. Rejected because it would prove evaluator
  craft rather than the admitted Skill-mediated repair mechanism.
- Repeat Call B. Rejected because ADR-0028 forbids retry and the result is
  already immutable evidence.

## Consequences

- One additional Terra Medium provider call is required before broad
  qualification can resume.
- W-020 remains a visible failed gate and receives no retroactive pass.
- A passing Call C supports only the bounded two-repair-pass mechanism and the
  three named open cases; it does not prove general visual competence.
- W-005 comparator arms must receive the same maximum three-call sequence even
  when an arm finishes earlier, while reporting unused calls and first-call
  results separately.
- A failed Call C leaves the candidate unqualified and authorizes no further
  repair.
- No sealed call, publication, installation, commit, push, tag or release is
  authorized.

## Confirmation

Confirm by accepting this Decision. Implementation is confirmed only when the
Wayfinding Call-B source, report and render hashes match the W-020 record; one
and only one exact Terra Medium Call C receives those artifacts on manifest
`81530628273139A1518B9D44A309CF10ED6FE41585E35A0D6C54C236F547D6DF`;
the exact Wayfinding plus Cartography route, topology, IDs, wording and evidence
boundaries remain intact; and the single final parent render has no remaining
collision or occlusion.

## Revisit when

Any Call-B artifact or render hash changes, Call C selects another owner,
changes more than the remaining visible occlusion, fails its final render,
requires a package edit, or equal three-call parity cannot be maintained in
W-005.
