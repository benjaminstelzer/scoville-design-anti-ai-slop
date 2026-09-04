---
format_version: 1
id: ADR-0034
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/holdout-recovery
---

# Replace the unrecoverable holdout under fresh custody

## Decision

Accepted automatically under the user's standing instruction to accept project
decisions: replace the two intact but undecryptable original holdout tranches
with a newly authored and encrypted holdout generation under the current
independent Custodian. Keep the original ciphertexts and receipts immutable as
historical non-product evidence; do not overwrite, decrypt, reconstruct or
score them.

The replacement uses the already frozen qualification-v5 packages, Terra High
target, run-matrix semantics, arm parity, renderer and scorer contracts. It
receives new tranche filenames, opaque manifests, hashes, custody keys and a
fresh zero-call authorization chain. The current Custodian must retain the new
keys only in its private continuation context through staging, canaries and any
conditionally admitted remaining execution.

No replacement case content, expected answer, source artifact or key may enter
the implementation context or shared evidence. Real provider calls remain
forbidden until the replacement generation independently passes all six
armblind zero-call requirements. ADR-0033's canary-first authorization and the
separate prohibition on publication, installation, commit, push, tag and
release remain unchanged.

## Problem

The original AES-256-GCM ciphertext and opaque-manifest hashes still validate,
but both decryption keys existed only in a prior private Custodian context that
is no longer available. No authorized recovery artifact exists. Therefore the
original sealed cases cannot be authenticated, staged or executed, and
pretending to reconstruct their keys or contents would invalidate custody and
qualification evidence.

## Drivers

- Complete real sealed qualification without weakening custody separation.
- Preserve the failed custody handoff as visible evidence rather than hiding it.
- Avoid exposing or inventing secrets in the primary implementation context.
- Reuse the already validated v5 execution contract without changing package
  behavior after benchmark outcomes.
- Ensure the new keys remain live long enough to finish the admitted sequence.

## Considered alternatives

- Recover the original keys from shared files, logs or parent context. Rejected
  because no authorized artifact exists and such a search risks secret leakage.
- Guess or reconstruct the keys or sealed content. Rejected because it is
  cryptographically infeasible and would fabricate evidence.
- Treat the public canary as sufficient qualification. Rejected because it does
  not satisfy W-005's sealed-holdout Acceptance.
- Stop the project permanently. Rejected because a fresh independent holdout
  can restore the intended evidence boundary without changing the product.
- Overwrite the original archives. Rejected because it destroys the audit trail
  and can confuse historical and replacement evidence.

## Consequences

- The original two tranches remain quarantined and contribute zero product
  evidence.
- Replacement creation adds time and provider-independent authoring work but no
  product-code change.
- All replacement manifests, schedules and canaries are preregistered before
  outcomes are observed.
- Any contamination, custody, integrity, synthetic-path or canary failure stops
  the replacement lane.
- W-005 was already in progress, so its immutable `Decisions` list cannot add
  ADR-0034; mutable Evidence and Next action record the recovery instead.

## Confirmation

Confirm that the original archive hashes remain unchanged; the blocker receipt
continues to show zero calls and no unseal; replacement filenames and hashes are
distinct; authenticated round-trip, tamper rejection and plaintext cleanup
pass privately; all six armblind zero-call outputs bind the new generation; and
only then the exact preregistered canary shard becomes executable.

## Revisit when

The original private Custodian context becomes securely recoverable before any
replacement provider call, the replacement custody boundary fails, or the
frozen v5 package, model, renderer, scorer or run-matrix contract must change.
