---
format_version: 1
id: ADR-0033
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/sealed-execution
---

# Authorize armblind sealed qualification execution

## Decision

Accepted from the user's explicit instruction on 2026-09-03: authorize the
independent custodian to unseal and stage the holdout armblind, execute the
preregistered real qualification-v5 sealed canaries, and, only after those
canaries pass every integrity, infrastructure, route, parity, render and
scoring gate, execute the remaining sealed holdout schedule.

The authorization is conditional and terminal-on-failure. Before the first
sealed provider call, the custodian must return the required armblind schedule,
classification, canary selection, runner-manifest and synthetic-path receipts.
Any canary, integrity or infrastructure failure stops further sealed execution
and contributes no broad qualification claim until the failure is resolved and
a new safe execution boundary is established.

This Decision does not authorize publication, installation, commit, push, tag
or release. Those actions remain separately prohibited.

## Problem

W-005 reached a verified zero-call v5 readiness boundary but could not access
or execute the independently sealed holdout without explicit authority. The
user has now supplied that authority while preserving the custody split and
the separate release boundary.

## Drivers

- Complete W-005 with real sealed evidence rather than open-canary inference.
- Keep holdout content hidden from the implementation context and scoring arm.
- Preserve arm parity, frozen packages and terminal failure semantics.
- Prevent a passed public canary from being mistaken for sealed qualification.
- Keep release and repository-publication actions outside this authorization.

## Considered alternatives

- Continue to stop before unseal. Rejected because it conflicts with the
  user's explicit authorization and cannot complete W-005.
- Unseal into the primary implementation context. Rejected because it breaks
  independent custody and contaminates the qualification boundary.
- Execute the full holdout before assessing canaries. Rejected because it
  removes the required early stop for runner, infrastructure or product
  failure.
- Treat the authorization as permission to publish or release. Rejected
  because the user explicitly kept those actions separately locked.

## Consequences

- The custodian may perform armblind unseal and zero-call staging immediately.
- Real sealed canaries may run only after all required zero-call custodian
  outputs validate against the frozen v5 controls.
- The remaining holdout schedule becomes executable only after every sealed
  canary gate passes.
- A failed canary or integrity check stops execution; authorization is not an
  instruction to retry an observed model outcome.
- W-005 was already in progress, so its immutable `Decisions` list cannot add
  ADR-0033 under the native format-version-1 lifecycle. The authorization is
  recorded in its mutable Evidence and Next action fields instead.

## Confirmation

Confirm the decision through an immutable authorization receipt bound to the
preauthorization gate and frozen package and suite manifests, followed by
armblind custodian receipts that disclose only allowed IDs, hashes, counts,
statuses and aggregate evidence. Confirm that zero sealed calls precede the
completed staging receipt, that canaries precede the remaining schedule, and
that no separately prohibited action occurs.

## Revisit when

A canary, integrity or infrastructure gate fails; the frozen package, suite,
model, reasoning effort, renderer, scorer or schedule changes; custody cannot
remain armblind; or publication, installation, commit, push, tag or release is
requested.
