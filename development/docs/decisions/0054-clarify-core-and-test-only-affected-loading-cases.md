---
format_version: 1
id: ADR-0054
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: skill/core-discovery
---

# Clarify Core and test only affected loading cases

## Decision

The user explicitly selected a narrow clarification: identify `SKILL.md` as
the Core and require additional package reads to use existing exact links.
Apply this after PLAN-0002's frozen execution and separate adjudication close.
Preserve the original v9 snapshots and measurements as historical evidence.

Validate the changed loading behavior only, using the affected missing-Core
cases as a targeted development regression. Include the seventh same-mechanism
failed read alongside the six out-of-index cases. Keep original task inputs,
model settings and unrelated instructions where feasible; disclose differences.
Do not repeat the complete holdout, change design rules or Gold, or claim this
targeted regression is a new independent qualification.

## Problem

Seven captured executions read `SKILL.md` and then attempted a nonexistent
Core reference. Neither `core.md` nor `design-core.md` is linked by the package.
The package and test prompts use Core without explicitly mapping it to the
entrypoint. This is an observed naming ambiguity and a plausible contributor,
not proof of the sole cause of those failures.

## Drivers

- Implement the user's explicitly approved clarification.
- Test the evidenced loading defect without repeating unaffected work.
- Preserve frozen evidence and distinguish successor behavior.
- Avoid converting unrelated routing or artifact failures into passes.

## Considered alternatives

- Leave the naming ambiguity unchanged. Does not implement the user's choice.
- Add a new Core file. Creates unnecessary structure and duplicate ownership.
- Rewrite the Skill broadly or run another full holdout. Outside this request.
- Clarify only the test prompt. Does not fix the ambiguity in the reusable Skill.

## Consequences

The successor Skill differs from the frozen v9 package by a small entrypoint
clarification. Previously earned evidence remains scoped to its exact package.
Only relevant structural checks and bounded affected-case loading tests run.
No installation, publication, commit, push, tag or release is authorized.

## Confirmation

Inspect the focused entrypoint diff and all referenced paths. Run the Skill
validator and relevant package checks, then inspect the affected-case traces
for actual successful entrypoint/expert reads and absence of invented paths.
Report all failures and limits; do not retry until an arbitrary pass or treat
loading success as proof of the complete design result.

## Revisit when

The same failure persists, the correction requires wider instruction changes,
the targeted check cannot preserve meaningful conditions, or another full
holdout is proposed.
