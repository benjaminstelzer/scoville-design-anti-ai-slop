---
format_version: 1
id: ADR-0013
status: accepted
created: 2026-09-02
accepted: 2026-09-02
scope: evaluation/holdout-execution
---

# Use job-granular resumable holdout execution

## Decision

Replace whole-attempt invalidation and monolithic 150-job restarts with:

- synthetic preflight for every materially different runner, output, and arm-
  materialization path;
- one preregistered, armblind, automatically checked sealed canary for each
  actually different end-to-end path;
- small immutable shards formed as complete arm-balanced randomization blocks;
- an immutable attempt receipt after every process and a terminal job receipt
  after every model response;
- resume by missing or explicitly retry-eligible job ID only;
- a fixed transport-retry budget only when no model response exists;
- no retry for an output merely because parsing, rendering, scoring, design, or
  another product check fails.

The complete state and receipt contract is in
`docs/evaluation/resumable-holdout-execution-contract.md`.

## Problem

The original whole-attempt rule wasted completed model work when a later
infrastructure or provider-capacity failure occurred. Earlier infrastructure
smokes also failed to cover the exact real-output and case-private paths before
bulk execution. Restarting all 150 jobs neither improves independence nor
measures the product more fairly.

## Drivers

- Detect infrastructure defects before material model-token spend.
- Never turn a bad model result into a retry candidate.
- Preserve arm balance, frozen Gold, blind custody, and exact package hashes.
- Resume safely after provider failures without inspecting case content or
  scores.
- Keep every attempt auditable and prevent duplicate terminal outputs.

## Considered alternatives

- Keep whole-attempt invalidation. This is simple but discards valid jobs and
  makes transient provider failures disproportionately expensive.
- Retry any failed job. This creates outcome-based selection because artifact,
  parser, render, or score failures can be product failures.
- Inspect real canary artifacts before continuing. This can expose holdout
  content and permit adaptive harness changes.
- Reduce evidence silently after a provider failure. This breaks the frozen
  schedule and can bias arms or cases.

## Consequences

- A job becomes terminal as soon as any model response exists, even when every
  downstream artifact or score check fails.
- Only allowlisted transport failures proven to occur before a model response
  can retry, with the same case, arm, repetition, model, and package.
- Canaries expose only automated infrastructure class and pass/fail; they count
  in the final sample and cannot trigger a contract change after unseal.
- Qualification remains incomplete while any preregistered job is
  `infrastructure_unresolved`; completed jobs are not rerun.
- A new execution-suite version is required because attempts governed by the
  old whole-attempt rule remain invalid and quarantined.

## Confirmation

Before another holdout call, validate the state machine, allowlist, retry
budget, atomic receipt commit, idempotent resume, corruption detection,
armblind canary report, and cost forecast with synthetic fixtures. An
independent SOL review returned GO only after terminal-on-response and
nonadaptive-canary controls were added.

## Revisit when

The provider offers a documented idempotent batch API with terminal per-job
receipts, or evidence shows the sharding/randomization block changes the frozen
comparison estimand.
