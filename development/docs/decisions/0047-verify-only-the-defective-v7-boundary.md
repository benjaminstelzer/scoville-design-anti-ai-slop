---
format_version: 1
id: ADR-0047
status: superseded
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/targeted-verification
supersedes: ADR-0046
superseded_by: ADR-0049
---

# Verify only the defective v7 boundary

## Decision

The user explicitly rejected a complete 150-job rerun as unnecessary token
expenditure. Supersede ADR-0046 and verify only the adjudicated defective v7
contract boundary.

Stop and retire the partial v8 zero-call build without provider calls or private
plaintext. Under Custodian control, author the corrected Gold relation
independently from model output, preserve v7 Gold and evidence unchanged, and
rescore the immutable v7 Canary-2 candidate output against that corrected
relation as diagnostic evidence only. Do not award retrospective qualification
credit and do not rerun the private case.

If the corrected diagnostic route is exact and terminal-aligned, close the
defect as benchmark-only with zero new model calls. If a package mismatch
remains, permit only one newly authored source-cleared public boundary regression
after zero-call preflight, with one Terra High call, no outcome retry and no
sealed content. Do not create or execute another full holdout suite.

## Problem

ADR-0046 would have rebuilt and rerun the complete 150-job matrix even though
ADR-0045 isolated one invalid Gold relation. That would spend substantial tokens
on unaffected lanes and repeat evidence that is not needed to decide whether the
specific package boundary is defective.

## Drivers

- Follow the user's explicit proportional-verification direction.
- Spend no model tokens when immutable evidence can answer the question.
- Preserve v7 Gold, output and fail-stop evidence.
- Distinguish diagnosis from qualification credit.
- Keep any public falsifier source-cleared and bounded to one call.

## Considered alternatives

- Rebuild and rerun all 150 jobs. Rejected by the user as token waste.
- Edit v7 Gold and declare the existing result passed. Rejected because Gold is
  immutable after outcome and retrospective credit is invalid.
- Retry the private Canary. Rejected by the no-outcome-retry contract.
- Skip all checking. Rejected because the corrected owner relation still needs
  to be compared with the captured route.
- Patch the package immediately. Rejected because no package defect is yet
  established.

## Consequences

- No complete new sealed-holdout claim will be made.
- W-005 can report only accumulated and targeted qualification evidence, with
  the incomplete full holdout explicit.
- The partial v8 build contributes zero product evidence and is retired without
  execution.
- A public provider call occurs only if model-free corrected rescoring leaves a
  package mismatch.
- Publication, installation, commit, push, tag and release remain unauthorized.

## Confirmation

Confirm the user's direction, ADR-0046 supersession, zero v8 calls/jobs/plaintext,
immutable v7 evidence, independently corrected contract, diagnostic rescore,
honest no-retrospective-credit label and at most one source-cleared public call
only if needed.

## Revisit when

The user later requests a complete sealed qualification, the corrected contract
cannot be resolved arm-blind, or the targeted public regression establishes a
package defect requiring a bounded repair.
