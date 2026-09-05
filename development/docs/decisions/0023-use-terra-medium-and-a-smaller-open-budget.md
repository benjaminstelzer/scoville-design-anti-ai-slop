---
format_version: 1
id: ADR-0023
status: superseded
created: 2026-09-02
accepted: 2026-09-02
scope: evaluation/model-and-cost
superseded_by: ADR-0024
---

# Use Terra Medium and a smaller open budget

## Decision

Use exact `gpt-5.6-terra` with reasoning `medium` for the remaining open
28-leaf implementation tests and SkillOpt checks. Replace the 16-call High
allocation with at most 14 new Medium calls: ten named cases, one classified
coverage reserve and three case-paired SkillOpt calls. No sealed call or
unallocated retry is included.

Set hard new-work ceilings to 2,000,000 provider-total tokens and 500,000
uncached-input-plus-output tokens. An ordinary call reaching 160,000 provider-
total or 50,000 uncached-plus-output stops the lane before another call. Execute
one call at a time and inspect route, trace, artifact, render and usage before
continuing.

One Terra High call was started after a successful dry-run and interrupted at
the user's model change before the wrapper wrote raw events, status or usage.
It provides zero product evidence; possible provider billing is unknown and is
reported separately rather than estimated.

## Problem

The accepted W-015 contract fixed Terra High. The user then explicitly required
Terra Medium to reduce token use while its first High canary was still running.
Continuing or silently editing a started Work Item would violate both user
authority and the frozen evaluation contract.

## Drivers

- Cost and latency should be bounded before broad coverage.
- Exact professional coverage remains more important than compressing runtime
  references below their safe content floor.
- Early one-at-a-time inspection prevents repeating a harness or routing defect.
- Cross-model behavior is empirical; Medium results are claimed only for the
  exact Medium configuration.

## Considered alternatives

- Finish the running High call. Rejected by the user's immediate model change.
- Keep sixteen Medium calls. Rejected because two reserve slots can be removed
  without dropping a named capability case or the three planned SkillOpt pairs.
- Use Spark for routing. Rejected for this lane because the named cases include
  visual judgment and image inputs.

## Consequences

- W-015 is cancelled without product evidence and replaced by W-016.
- Existing 28-leaf static validation remains valid; only the provider contract
  and claims change.
- No comparison with High, SOL, Fable or Opus is inferred from Medium results.

## Confirmation

The machine call matrix rejects any reasoning value other than `medium`, any
allocation above fourteen, missing per-call inspection, or historical/
interrupted calls receiving qualification credit.

## Revisit when

Medium cannot execute an essential visual case within the hard per-call ceiling
or the user explicitly authorises another model, effort or budget.
