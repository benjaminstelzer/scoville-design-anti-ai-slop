---
format_version: 1
id: ADR-0037
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/execution-authorization
---

# Enforce hash-bound v6 execution authorization

## Decision

Accepted automatically under the user's standing instruction to accept project
decisions: qualification-v6 must fail closed inside its canonical runner until
one valid execution-authorization receipt exists. Reporting
`sealed_calls_authorized=false` in a readiness file is not an enforcement
mechanism.

Keep read-only help and preauthorization validation available. Require the
authorization receipt before every command that registers or acquires runtime
state, decrypts or stages private material, renders or evaluates a private
artifact, or can reach a provider. The runner itself verifies the receipt and
all bound current artifacts before the command performs any effect.

The receipt binds the suite and decision IDs, the current zero-call readiness
and validation receipts, runner manifest, schedule, canary preregistration,
Design and UI package manifests, exact authorization scope, authorization time
and supplied user statement. Its scope is the six preregistered v6 canary
shards followed by the remaining holdout only after all six pass. Any missing,
stale, malformed, mismatched or broader receipt rejects execution.

Use one separately tested finalizer as the only receipt writer. It may run only
after the current user explicitly authorizes v6 sealed execution and only while
runtime jobs, plaintext run files, provider calls and sealed calls remain zero.
Before that authorization, the finalizer and tests exist but the live receipt
does not.

## Problem

The first v6 zero-call generation recorded an unauthorised state in its
manifests and validators, but `sealed_runner.py` did not consume that state.
Direct `register`, `prepare` or `call` invocation could therefore bypass the
documented gate whenever custody keys were present. This is an authorization
defect even though no job or provider call occurred.

## Drivers

- Make the user authorization boundary executable rather than descriptive.
- Reject direct runner invocation through the same canonical path.
- Bind authority to the exact frozen suite and package evidence.
- Preserve zero-call and zero-plaintext state before authorization.
- Keep canary-first fail-stop behavior enforceable after authorization.
- Avoid secrets or plaintext in authorization artifacts and logs.

## Considered alternatives

- Rely on operator procedure and readiness prose. Rejected because direct
  runner invocation bypasses prose.
- Add an environment-variable boolean. Rejected because it is unbound,
  unauditable and easy to set accidentally.
- Gate only `call`. Rejected because registration, acquisition, decryption,
  staging and private rendering are also protected state transitions.
- Add an external wrapper while leaving the runner unchanged. Rejected because
  the unwrapped canonical runner would remain a second bypass path.
- Create the receipt before user approval but mark it pending. Rejected because
  presence would blur authority and enlarge the trusted state.

## Consequences

- Existing v6 readiness hashes must be regenerated after the runner and tests
  change; encrypted cases, schedule, canaries and package snapshots stay
  unchanged.
- No live authorization receipt exists until an explicit current-user v6
  authorization is supplied.
- The runner rejects all protected commands before keys, plaintext, runtime
  state or provider transport are touched when authorization is absent or bad.
- Holdout shards remain closed until all six canary outcomes are terminal and
  passing under the frozen gate.
- W-005 was already in progress, so its immutable `Decisions` list cannot add
  ADR-0037; mutable Evidence records the repair and validation.
- Publication, installation, commit, push, tag and release remain outside this
  authorization.

## Confirmation

Confirm tests for absent, malformed, tampered, stale, wrong-suite, wrong-scope
and over-broad receipts across registration, acquisition, preparation, call,
evaluation, private rendering and render recording. Confirm exact current hash
bindings, canary-only admission before aggregate pass, holdout rejection before
six passes, finalizer rejection without supplied explicit authorization, zero
runtime jobs, zero plaintext files, zero calls and no live receipt before user
approval.

## Revisit when

The runner command surface changes, a bound manifest changes, the receipt
format changes, canary aggregation becomes independently persisted, the user
authorizes a different scope, or any protected command can produce an effect
before receipt verification.
