---
format_version: 1
id: ADR-0030
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: evaluation/v4-suite-and-open-parity-canary
---

# Create a v4 suite with three-call arm parity

## Decision

Recommended and accepted under the user's standing authorization to accept
Plan Decisions automatically: preserve `qualification-v3` and all three failed
holdout attempts as immutable evidence, then create a new `qualification-v4`
execution suite for the current Design and UI candidates.

The v4 schedule must distinguish all 156 preregistered matrix executions from
the 150 runnable jobs: the six executions for the quarantined
`HD-14B8E6D9` case remain registered but ineligible. A runnable job is one
case, arm and repeat tuple. Every renderable job receives the same arm-neutral
maximum of three sequential model-response calls:

1. Call A creates or changes the candidate artifact.
2. The parent renders it; Call B is eligible only for a localized observed
   defect and receives the immutable source, report and render.
3. The parent renders again; Call C is eligible only for a remaining localized
   defect and receives the immutable Call-B source, report and render.

The job stops at the first passing final render or after Call C. Unused calls
disappear and are reported; they are not replaced. First-call route, artifact
and evidence results remain separately scored. Text-only or otherwise
non-renderable jobs stop after Call A. The same renderer, image access, repair
prompt shape, stop rules and call eligibility apply to every comparison arm.

Transport attempts are separate from repair calls. Each call is terminal on
any model response and may use the ADR-0013 maximum of three provider attempts
only for an allowlisted transport failure before a response, with the frozen
backoff. Outcome-based retries remain forbidden.

Before the v4 sealed suite is frozen, run one public Wayfinding repair canary
with exact `gpt-5.6-terra` and reasoning `high` against both `no_skill` and the
current Design arm. Run one arm at a time. Each arm receives the same maximum
three-call mechanism, and each source and parent render is inspected before a
later call. The open canary may spend two to six model-response calls and no
retry reserve. A failure stops v4 admission.

This Decision authorizes the local synthetic work and the bounded public open
canary. It does not authorize unsealing holdout content or making a real sealed
canary or holdout call. ADR-0014's separate execution authorization remains in
force, as do the prohibitions on publication, installation, commit, push, tag
and release.

## Problem

`qualification-v3` binds obsolete RC7 snapshots and its failed attempts cannot
be resumed as product evidence. Its matrix declares 156 executions while its
runner and cost contract operate on 150 because one six-execution case is
quarantined; that distinction is implicit rather than schema-checked. The
current v3 candidate also admits up to two parent-rendered repair passes, so a
one-response job model no longer gives comparator arms equal tool and call
opportunity.

Mutating v3 would erase the provenance of its three infrastructure failures.
Starting the sealed suite without first proving the new call-slot state
machine at Terra High would repeat the prior infrastructure-first risk.

## Drivers

- Preserve every failed attempt and its zero-product-evidence boundary.
- Bind final qualification to the current package hashes and exact Terra High.
- Make 156 registered versus 150 runnable executions explicit and validated.
- Separate artifact repair calls from pre-response transport attempts.
- Give every arm identical maximum render and repair opportunity.
- Prove the state machine on public material before sealed spend.

## Considered alternatives

- Resume qualification-v3. Rejected because its package snapshots and suite
  identity are obsolete and its attempts were explicitly invalidated.
- Mutate v3 in place. Rejected because it would obscure historical evidence.
- Give only the Design arm repair calls. Rejected because visual comparison
  would confound Skill effect with tool and call access.
- Allocate three calls to every job unconditionally. Rejected because textual
  jobs need no renderer and outcome-independent extra calls add cost without
  parity value.
- Start with sealed canaries. Rejected because ADR-0014 requires a separate
  authorization and the new state machine is not yet synthetically or openly
  proven.

## Consequences

- A new local suite root, contract, matrix and immutable snapshots are needed.
- Maximum model-response calls depend on the sealed artifact-path schedule and
  must be computed without exposing case content to the implementation lane.
- Maximum provider attempts are the call-slot maximum multiplied by three;
  the receipt schema must keep both dimensions distinct.
- The open canary supplies mechanism and Terra High transfer evidence only,
  not holdout or cross-person qualification.
- W-005 remains paused until W-022 passes; its started Decisions and
  dependencies remain unchanged.

## Confirmation

Confirm with model-free schema and state-machine tests; exact current Design
and UI manifests; an explicit `registered_executions: 156`,
`quarantined_executions: 6`, and `runnable_jobs: 150` invariant; exact
call-slot and provider-attempt receipts; and the arm-balanced public Terra High
Wayfinding canary with every source, route, usage and parent-render hash
recorded.

## Revisit when

The current package hash changes, the public canary exposes a product or
harness defect, the sealed custodian cannot derive renderability without
leaking content, equal arm treatment cannot be enforced, or the user changes
the final model or authorization boundary.
