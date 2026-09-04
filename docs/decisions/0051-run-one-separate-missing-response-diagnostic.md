---
format_version: 1
id: ADR-0051
status: superseded
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/missing-response-diagnostic
superseded_by: ADR-0052
---

# Run one separate missing-response diagnostic

## Decision

After the frozen holdout finishes, run one separately identified diagnostic
replay of J-6F04714F845A's slot-2 task. The user requested this repetition and
asked that a diagnosis without an identifiable Skill defect remove the
infrastructure case as an acceptance blocker.

Use the same model, effort, pinned CLI, package snapshots, prior artifact and
localized repair request. Clone inputs outside the original runtime. Preserve
prompt bytes where safe; any necessary cloned-path substitutions must be
explicitly recorded. Freeze a narrow diagnostic authorization and input/tool
hash receipt before the sole provider call. Allow no retry or repair loop.

The diagnostic never replaces transport 171, adds qualification credit, or
changes original raw events, scores, state or the frozen 150-job denominator.
If the diagnostic provides a usable completion without an identifiable Skill
defect, treat this case as a user-accepted infrastructure exception. Report that
acceptance separately from the original unresolved measurement. Other relevant
Skill failures or missing qualification evidence remain subject to their own
assessment; this exception cannot turn unrelated failures into passes.

## Problem

Transport 171 contains valid events and usage but no terminal agent message.
Its cause remains indeterminate. One independent diagnostic can test whether
the same task now completes, but cannot prove the original failure's cause.

## Drivers

- Address the user's request without repeating the full holdout.
- Distinguish a diagnostic repetition from an official outcome retry.
- Preserve original evidence and the user's explicit acceptance exception.
- Avoid attributing an unexplained transport failure to the Skill.

## Considered alternatives

- Replace the original result with the diagnostic. Rejected as evidence loss.
- Repeat all 150 jobs. Rejected as unnecessary and outside this request.
- Assume absence of a Skill defect proves infrastructure causality. Rejected
  because a successful later run does not establish the original cause.

## Consequences

One additional provider call is permitted only after the frozen run closes and
the diagnostic inputs, constraints and explicit user authority are recorded.
Report its usage separately. Do not publish, install, commit, push, tag or release.

## Confirmation

Confirm unchanged original evidence, separate diagnostic directory and receipt,
one call at most, exact tool/input bindings or declared path differences,
LF-valid captured events and usage, presence or absence of a terminal response,
observed Skill defects if any, and the bounded acceptance conclusion.

## Revisit when

The clone would modify original files, comparable inputs cannot be retained,
the diagnostic needs another call, or its result is used to erase other failures.
