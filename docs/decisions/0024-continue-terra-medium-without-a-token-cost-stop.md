---
format_version: 1
id: ADR-0024
status: accepted
created: 2026-09-02
accepted: 2026-09-02
scope: evaluation/model-and-cost
supersedes: ADR-0023
---

# Continue Terra Medium without a token cost stop

## Decision

Continue the unfinished 28-leaf open evaluation with exact
`gpt-5.6-terra` at reasoning `medium`. Remove automatic provider-total,
uncached-input-plus-output and monetary cost stops under the user's explicit
instruction to ignore the cost stop.

Keep one call at a time and inspect route, trace, artifacts, rendered evidence,
claims and usage before the next call. Preserve the eight unexecuted named
cases and up to three case-paired SkillOpt calls. Add no retry or reserve call
without new user authority. Track all usage even though it no longer stops the
lane.

Do not rerun or retroactively regrade D28-EH1 or D28-CI1. Their failures,
artifacts, visual defects, usage and zero qualification credit remain visible.

## Problem

ADR-0023 stopped W-016 when D28-CI1 exceeded its ordinary provider-total
ceiling. The user then explicitly instructed the project to ignore that cost
stop and continue. The prior accepted Decision and Work Item cannot be edited
in place without erasing their historical contract.

## Drivers

- The user explicitly authorizes continued provider use despite the prior stop.
- Terra Medium remains the selected effort level.
- One-at-a-time inspection still prevents a repeated harness or benchmark
  defect from consuming a batch.
- Failed evidence must remain failed rather than becoming a reason to rewrite
  Gold after output.

## Considered alternatives

- Resume W-016 and ignore its Acceptance. Rejected because that would make the
  durable contract false.
- Restore Terra High. Rejected because the user selected Medium.
- Rerun the two failed cases. Rejected because their reserve is consumed and
  their observed failure is already decisive.
- Run all remaining calls as a batch. Rejected because early inspection remains
  required.

## Consequences

- ADR-0023 is superseded and W-016 is cancelled as historical stopped work.
- W-017 owns the remaining eight named Medium cases and eligible SkillOpt work.
- Usage is reported cumulatively but is not an automatic stop condition.
- A malformed harness or unclassified result still stops before the next call;
  this is an evidence-integrity stop rather than a cost stop.

## Confirmation

The active matrix must name `gpt-5.6-terra` and `medium`, list the eight
remaining named cases, preserve the three prior Medium calls and failures, set
no token or monetary ceiling, and allocate no retry or reserve. Execution logs
must show no overlapping calls.

## Revisit when

The user introduces a new budget, model, effort level or stopping rule, or an
unclassified harness failure prevents honest continuation.
