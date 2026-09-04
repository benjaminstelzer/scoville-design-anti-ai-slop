---
format_version: 1
id: ADR-0046
status: superseded
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/suite-versioning
superseded_by: ADR-0047
---

# Replace the defective v7 case in a fresh v8 suite

## Decision

Accepted automatically under the user's standing instruction to accept project
decisions: preserve qualification-v7 and its Gold unchanged as failed historical
evidence, quarantine the adjudicated defective private case, and create a fresh
qualification-v8 zero-call suite with one newly authored source-cleared private
replacement case and newly frozen controls.

Do not retry the v7 case or reuse any v7 score. Keep the other source-cleared
private cases only if their encrypted source and Gold integrity remain valid,
then re-encrypt all v8 content, generate new opaque manifests, arm-balanced
shards, Canary preregistration, schedule, runner manifest, readiness receipts and
authorization policy. Reset the v8 matrix to 30 cases, 150 jobs and zero runtime
progress. Execution requires a separate fresh current-user authorization after
all zero-call and adversarial gates pass.

The replacement case must be authored without using v7 output, must not reproduce
the private defective brief, and must have its route Gold independently checked
against every selected owner's positive and exclusion rules before sealing.

## Problem

ADR-0045 established that v7 Canary 2 failed because frozen Gold required a
secondary owner whose explicit exclusion applies to that private brief. Editing
v7 Gold after seeing output or retrying the case would invalidate the immutable
qualification boundary. Removing it without replacement would also alter the
preregistered coverage and matrix.

## Drivers

- Preserve immutable failed evidence and no-retry semantics.
- Remove an invalid benchmark contract without tuning to model output.
- Keep the intended 30-case, 150-job, arm-balanced qualification shape.
- Recheck positive and negative owner rules before any provider call.
- Require a new hash-bound authorization for a new suite version.

## Considered alternatives

- Correct v7 Gold in place and resume. Rejected because post-outcome editing and
  continuation are prohibited.
- Retry the same private case under corrected Gold. Rejected because it is an
  outcome retry and the case is now adjudicated.
- Drop the case and run 29 cases. Rejected because it changes preregistered
  coverage and the frozen matrix.
- Patch the package. Rejected because the arm-blind review found no package
  defect.
- Treat the v7 candidate as a pass. Rejected because v7 Gold was invalid and
  cannot award product evidence retrospectively.

## Consequences

- Qualification-v7 remains failed and closed.
- v8 starts at zero with fresh encrypted custody and no inherited score.
- One independently checked source-cleared case replaces the quarantined case.
- No v8 model call or unseal is permitted by this Decision.
- W-005 remains in progress; its immutable Decisions list cannot add ADR-0046,
  so mutable Evidence records the transition.
- Publication, installation, commit, push, tag and release remain unauthorized.

## Confirmation

Confirm v7 immutability, replacement-case independence and source clearance,
Gold positive/exclusion review, 30 cases, 150 jobs, arm balance, fresh encryption
and manifests, full fail-closed zero-call tests, zero runtime jobs/plaintext and
the absence of live v8 authorization.

## Revisit when

The v8 zero-call gates fail, replacement-case independence cannot be established,
or a future adjudication identifies another benchmark-contract defect.
