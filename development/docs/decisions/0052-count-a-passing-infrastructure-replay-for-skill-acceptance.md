---
format_version: 1
id: ADR-0052
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/missing-response-diagnostic
supersedes: ADR-0051
---

# Count a passing infrastructure replay for Skill acceptance

## Decision

The user explicitly wants one repetition of the incomplete execution, followed
by substantive assessment, and wants a fitting result to count as valid rather
than penalizing the Skill for the earlier execution interruption. Replace
ADR-0051's no-credit acceptance rule with this user-adjudicated result rule.

After the frozen holdout closes, execute one separately authorized replay of
J-6F04714F845A's slot-2 task. Keep the original prompt, schema, prior artifact,
repair request, package snapshots, exact model and pinned host tools. Use an
isolated clone; declare any necessary path differences before the call. Bind
the inputs and tools in a narrow diagnostic authorization. Allow exactly one
provider attempt, no retry and no additional model repair.

Assess the resulting response and artifact against the unchanged case
requirements and Gold, then render and independently inspect the result. If
the result fits and no Skill defect is identified, count this case as passed
in the user-adjudicated Skill acceptance ledger. Do not count the original
missing-message execution as a negative Skill result. If a substantive Skill
defect is found, retain it honestly instead of waiving it as infrastructure.

Preserve transport 171 and every original frozen event, score and state. Keep
preregistered measurements and the later user-adjudicated replacement in
separate fields with an explicit link. Do not describe the replacement as an
uninterrupted original pass or as proof of the original interruption's cause.
The overall acceptance conclusion still evaluates other relevant Skill
outcomes independently; this decision does not erase unrelated failures.

## Problem

The original execution has valid events and usage but no final agent message.
Its cause is unknown and it is not evidence of a Skill defect. The user does
not want that technical incompleteness to lower Skill acceptance when a single
substantively checked repetition yields a valid result.

## Drivers

- Follow the user's explicit updated acceptance rule.
- Judge the Skill on a complete and substantively checked result.
- Preserve original evidence and distinguish later adjudication.
- Avoid repeating the full holdout or concealing genuine Skill failures.

## Considered alternatives

- Keep ADR-0051's diagnostic-only no-credit rule. Rejected by the user's update.
- Delete or overwrite the original failure. Rejected; preserve audit history.
- Automatically pass on receipt of any final message. Rejected; substantive
  requirements, artifact correctness and visual review must also pass.
- Repeat all 150 jobs. Rejected as unnecessary and outside the request.

## Consequences

The final report may say this case passed after one execution-failure replay,
with the initial interruption separately disclosed. This is an explicitly
post-incident acceptance decision, not the original frozen statistical result.
Only one additional provider attempt is allowed. Publication, installation,
commit, push, tag and release remain prohibited.

## Confirmation

Confirm separate authorization, exact comparable inputs, preserved originals,
one captured attempt and usage, unchanged-Gold substantive assessment, rendered
review, and an explicit mapping from the original unresolved result to the
user-adjudicated pass or observed Skill failure.

## Revisit when

Comparable inputs cannot be preserved, substantive checks identify a Skill
defect, another call is needed, or adjudication would hide unrelated failures.
