---
format_version: 1
id: ADR-0045
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/failure-adjudication
---

# Adjudicate the v7 route-set mismatch before changing the package

## Decision

Accepted automatically under the user's standing instruction to accept project
decisions: preserve qualification-v7 as failed historical evidence and perform
one model-free independent arm-blind contract review of the already sealed
Canary-2 evidence before any package or benchmark change.

The review may compare the private brief, frozen Gold, package owner rules,
authenticated read set and terminal route only inside Custodian control. Its
public output is limited to a classification, supporting contract relation,
sanitized owner IDs only when disclosure cannot reveal a private case fact,
hashes, counts and a next safe action. It must make no provider call, retry,
render, package edit, Gold edit or v7 continuation and must leave no plaintext.

If the review establishes a Gold defect, preserve v7 and create a new suite
version after a separately recorded Gold correction. If it establishes a
package defect, require a source-cleared public falsifier before changing the
package. If it remains indeterminate, create a source-cleared public boundary
regression that exposes no private fact and permits one no-retry Terra High call
only after zero-call preflight. No outcome permits resuming v7.

## Problem

Canary 2 stopped after the candidate read three authenticated experts against
two frozen Gold experts. The terminal route report aligned with all three reads,
so self-report or provenance extraction does not explain the mismatch. The
arm-blind first adjudication cannot yet distinguish a package over-read from a
missing Gold owner without opening the protected contract relation more deeply.

## Drivers

- Preserve fail-stop and immutable evidence.
- Separate product behavior from benchmark integrity.
- Keep private cases, keys and plaintext under Custodian control.
- Avoid patching from one sealed outcome or editing Gold after output.
- Permit only evidence that can change the next decision.

## Considered alternatives

- Remove the third authenticated read from scoring. Rejected because it is real
  captured behavior.
- Add the third owner to v7 Gold. Rejected because post-outcome Gold editing is
  prohibited and the contract has not been adjudicated.
- Patch the package immediately. Rejected because a private benchmark defect is
  still viable.
- Retry Canary 2 or continue later shards. Rejected by the authorization and
  fail-stop contract.
- Disclose the private brief for root-side review. Rejected because custody is a
  qualification invariant.

## Consequences

- Qualification-v7 remains failed at Canary 2 with no continuation.
- The next operation is model-free and private under Custodian control.
- Any correction requires a new suite version; v7 scores and Gold stay intact.
- W-005 remains in progress and its immutable Decisions list cannot add
  ADR-0045; mutable Evidence records the review.
- Publication, installation, commit, push, tag and release remain unauthorized.

## Confirmation

Confirm the v7 fail-stop hashes, exact 3-versus-2 contract relation, terminal
alignment, immutable Gold and package, zero calls/retries/renders during review,
zero plaintext after review, bounded public output and no later shard start.

## Revisit when

The arm-blind review returns a terminal classification, private-source clearance
rules change, or a future suite introduces a different route-scoring contract.
