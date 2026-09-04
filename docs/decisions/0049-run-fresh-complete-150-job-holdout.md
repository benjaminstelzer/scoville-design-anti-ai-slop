---
format_version: 1
id: ADR-0049
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/full-holdout
supersedes: ADR-0047
---

# Run a fresh complete 150-job holdout

## Decision

The user explicitly requests the complete 150-job holdout after previously
choosing targeted verification. Supersede ADR-0047 for future qualification and
run a fresh arm-blind suite against the final ADR-0048 package.

Create qualification-v9 rather than resume v7 or the retired partial v8 build.
Bind exact `gpt-5.6-terra` with reasoning `high`, the pinned local Windows CLI,
the final Design executable manifest, the retained UI manifest, frozen prompts,
source-cleared cases, authenticated expert-read scoring, terminal alignment,
parent rendering where preregistered, and per-job receipts. Use 30 fresh sealed
cases and 150 registered arm-balanced jobs; reuse no exposed v7 case or outcome.

Execute every registered job. A classified product failure remains visible but
does not stop later distinct jobs. Stop only when authorization, custody,
integrity, runner, provider-before-response, or benchmark-validity failure could
invalidate later evidence. No job receives an outcome retry after any model
response, and no package or Gold contract changes inside the frozen suite.

## Problem

ADR-0047 deliberately replaced full qualification with one targeted public
boundary replay. That replay repaired the demonstrated defect but cannot supply
complete holdout coverage. The user now wants the full matrix executed.

The partly exposed v7 suite is tied to a pre-ADR-0048 package and defective Gold;
continuing its remaining jobs would not produce a complete qualification of the
final package. The partial v8 build was retired before execution and is not an
executable substitute.

## Drivers

- Execute the user's newly expanded qualification scope.
- Preserve unseen-case and arm-blind integrity.
- Test the exact final package rather than a superseded snapshot.
- Finish all 150 jobs even when individual product outcomes fail.
- Preserve exact failures, usage, routes, renders, and reviewer limits.
- Keep publication and installation outside this authorization.

## Considered alternatives

- Continue v7 at its fourth job. Rejected because v7 binds a superseded package,
  exposed canaries, and a defective Gold relation.
- Reactivate the partial v8 build. Rejected because it was retired as incomplete
  and non-executable before any custody or runtime proof.
- Treat the ADR-0048 public replay as full qualification. Rejected because one
  source-cleared case proves only the repaired boundary.
- Stop the new suite on the first classified product failure. Rejected because
  the user requested complete 150-job execution; integrity failures still stop.
- Edit the package or Gold after observing outcomes. Rejected because that
  would invalidate the frozen comparison.

## Consequences

- Qualification-v9 requires fresh custody artifacts and a zero-call readiness
  gate before provider execution.
- The run may use more than 150 provider calls when a preregistered job permits
  parent-rendered repair calls; progress is reported separately by jobs and
  calls.
- Individual failures limit claims but do not prevent completion of unrelated
  jobs.
- A material harness, custody, authorization, or benchmark-integrity defect
  pauses execution and remains visible until independently resolved.
- No publication, installation, commit, push, tag, or release is authorized.

## Confirmation

Confirm a fresh suite identity, exact package and tool hashes, 30 source-cleared
sealed cases, 150 registered jobs, arm-balanced schedule, independent custody,
zero-call validation, per-job receipts, no outcome retries, all jobs executed,
and a final ledger that separates product results from route, render, benchmark,
reviewer, and infrastructure evidence.

## Revisit when

The final package changes before the first job, an integrity defect invalidates
future execution, the user changes the complete-run instruction, or a result
would require publication or installation.
