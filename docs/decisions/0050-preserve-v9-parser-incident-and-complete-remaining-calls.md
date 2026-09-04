---
format_version: 1
id: ADR-0050
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/incident-adjudication
---

# Preserve the v9 parser incident and complete remaining calls

## Decision

Accepted automatically under the user's standing instruction to accept project
decisions, after the model-free incident validation preserved intact captures,
receipt chains and all 54 current frozen file bindings.

Resume only the outstanding preregistered local render corrections after the
custodian verifies that capture integrity, receipt chains, isolation and all
current authorization bindings remain intact. This is incident adjudication
under ADR-0049, not authority to change its frozen runner, Gold, packages,
schedule, call limits or authorization receipt.

Preserve the original four Unicode-related evaluation errors as harness errors
with no qualification credit. Preserve the separate transport with no terminal
agent message as infrastructure unresolved and do not retry it. Keep every raw
event, original score, failure receipt and visual verdict unchanged. Any later
occurrence of the same demonstrated parser limitation must remain explicitly
classified as a harness error rather than a product failure.

Complete only already eligible local repair slots through the unchanged bound
runner. Terminal jobs and the unresolved transport must not receive new calls.
Use the final report to distinguish complete execution accounting from product
qualification, which remains limited by harness errors, missing evidence and
observed product failures. No post-hoc corrected score replaces a frozen score.

## Problem

During the first repair pass, the route parser rejected valid raw JSONL because
Python `splitlines()` also separates U+0085 characters embedded inside JSON
strings. A model-free inventory found four affected repair responses with intact
terminal messages and usage. Splitting only at JSONL record boundaries parses
the preserved captures successfully; no original evidence was rewritten.

An attempted safe-boundary pause encountered a PermissionError while reading a
concurrently transitioning state file; the exact OS cause is unproven. The
controller was subsequently suspended. A separately captured transport ended
with `turn.completed` and usage but no terminal agent message. Its recorded
classification is unresolved infrastructure, not a proven timeout. A causal
link to suspension has not been established and must not be invented.

All 150 first responses were already captured before this incident. The pause
leaves 17 jobs eligible for bounded render corrections. Repeating the full
holdout or modifying frozen scoring after seeing outputs would test a different
protocol and would not repair the original evidence.

## Drivers

- Preserve the user's complete-run request without outcome retries.
- Keep harness failures separate from product performance.
- Verify observed capture isolation and stop on any new evidence-invalidating fault.
- Preserve frozen contracts and existing authorization enforcement.
- Report the failed pause watcher and unresolved transport without invented causality.
- Avoid turning complete execution into an unsupported qualification claim.

## Considered alternatives

- Patch the bound parser or rewrite its raw input during the run. Rejected
  because that would change the authorized frozen protocol after outcomes.
- Repeat affected jobs or restart all 150 jobs. Rejected because responses
  already exist and outcome retries are prohibited.
- Count parser false negatives as product failures. Rejected because their
  demonstrated cause is the harness.
- Replace frozen scores with post-hoc corrected scores. Rejected because that
  would erase the original measurement boundary.
- Leave all remaining corrections unexecuted despite proven capture isolation.
  Not selected if the incident audit proves intact bindings and independent
  evidence; mandatory if any such proof is missing.

## Consequences

- Continuation is conditional on a preserved model-free incident audit and
  current binding verification, not merely on a process still being available.
- The four known parser cases remain harness errors without qualification
  credit, and the missing-message transport remains unresolved without retry.
- Existing final response, artifact, render and usage evidence remains usable
  only within its individually verified boundary.
- Any new capture corruption, binding mismatch, authorization failure or
  unclassified infrastructure fault stops further calls again.
- W-002 is already in progress. Its immutable Decisions list cannot add this
  record; its mutable Evidence and Next action must record the adjudication.
- Publication, installation, commit, push, tag and release remain prohibited.

## Confirmation

Confirm the incident report hash; all 150 first responses; all receipt chains;
LF-valid raw captures and the four exact Unicode false negatives; preserved
original scores and usage; the separate missing-message transport and failed
pause watcher; current frozen and authorization bindings; no outcome retry; unchanged
runner, Gold and packages; bounded eligible-only continuation; and a final
ledger separating execution, product, render and harness results.

## Revisit when

The incident audit cannot prove isolation or intact bindings, a new fault has
different mechanics, raw evidence is incomplete, a remaining job would require
an outcome retry or frozen mutation, or claims would exceed the original
reviewer and measurement boundaries.
