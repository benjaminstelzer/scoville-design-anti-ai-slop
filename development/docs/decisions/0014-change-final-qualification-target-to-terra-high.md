---
format_version: 1
id: ADR-0014
status: accepted
created: 2026-09-02
accepted: 2026-09-02
scope: evaluation/model-target
---

# Change final qualification target to Terra High

## Decision

Run every future model-based test, open transfer check, sealed canary, and
holdout job with exact model `gpt-5.6-terra` at reasoning effort `high`. Do not
run additional SOL, Fable, or Opus behavior tests for this release candidate.

Existing SOL XHigh results remain historical development, routing, and
optimization evidence for their exact runs only. They do not qualify Terra
High and cannot be pooled with Terra results.

## Problem

The package was developed and optimized against SOL, but the user changed the
required final test executor to Terra High. A sealed holdout under SOL would no
longer answer the requested model-specific question. Assuming transfer from SOL
without direct evidence would overstate qualification.

## Drivers

- The user's explicit model and reasoning requirement.
- Lower-cost staged testing before a large holdout.
- Exact model-specific evidence rather than family-level inference.
- Preservation of honest historical records.

## Considered alternatives

- Finish the SOL holdout. This no longer tests the requested executor.
- Treat SOL evidence as interchangeable with Terra. This is unmeasured.
- Run SOL and Terra. This duplicates cost and conflicts with the requested
  single target.

## Consequences

- The holdout requires a new execution-suite identity with Terra High frozen
  before unseal; case content, arms, Gold, rubrics, and package snapshots remain
  unchanged unless another Decision says otherwise.
- Terra must pass a small open transfer and cost gate before any sealed call.
- README and reports distinguish historical SOL evidence from pending or final
  Terra evidence.
- SOL-driven W-008 knowledge admission remains package-development history;
  any Terra-specific regression found by open transfer testing is recorded and
  repaired only through a new package candidate and its own validation.

## Confirmation

Record the exact Terra model, reasoning, host, CLI, package hashes, token usage,
and output-path evidence in the open transfer gate. Then freeze the resumable
Terra execution suite and require separate authorization for its real canaries.

## Revisit when

The user selects another executor or asks for cross-model qualification.
