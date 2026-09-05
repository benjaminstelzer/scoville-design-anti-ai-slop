---
format_version: 1
id: ADR-0036
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/route-evidence
---

# Score route provenance from authenticated expert reads

## Decision

Accepted automatically under the user's standing instruction to accept project
decisions: close qualification-v5 as a failed historical generation without
retry, continuation or retrospective rescoring. Build a fresh qualification-v6
executable and independently sealed holdout generation on the unchanged Design
and UI package manifests.

In v6, derive the scored loaded-expert set from authenticated completed command
events that read exact staged expert-reference paths. Compare that normalized
set with the preregistered Gold route. Fail closed when events are missing,
unparseable, ambiguous, outside the staged snapshots, or contain a forbidden or
unexpected expert read. Baseline arms that must not load Design pass only with
an empty authenticated Design-read set.

Keep the terminal `selected_experts` field in the response schema and compare it
with authenticated reads as a separate `reported_route_alignment` diagnostic.
A mismatch remains visible as response-telemetry nonconformance but does not
replace or override the authenticated loaded-expert evidence and is not itself
a Design package route failure. Never synthesize or patch the model response.

Before any v6 sealed call, prove this policy with public synthetic fixtures and
negative tests, freeze all parser, scorer, runner, prompt, schema, schedule,
package and holdout hashes, and preregister a fresh six-shard armblind canary
batch. No qualification-v5 result enters the v6 score.

## Problem

Qualification-v5 Canary 5 read the applicable Design expert but returned an
empty `selected_experts` list and therefore failed its frozen self-report-based
route check. The ADR-0035 public regression then read both expected experts and
reported both correctly in one terminal response, so the omission did not
reproduce. This neither establishes a package defect nor permits v5 to pass.

The v5 route check used an agent-authored summary as the scored proxy for what
the runtime actually loaded, although hashed raw execution events contain the
stronger direct evidence. A fresh generation can correct that evidence-policy
defect without changing a known outcome or weakening the actual route gate.

## Drivers

- Preserve all v5 outcomes and its fail-stop exactly as observed.
- Score the behavior W-005 names: the expert files actually loaded.
- Use evidence independent of the model's terminal self-description.
- Keep self-report disagreement visible rather than silently repairing it.
- Fail closed on missing, ambiguous or out-of-snapshot provenance.
- Prevent outcome-aware mutation by requiring a fresh sealed generation.

## Considered alternatives

- Retry or rescore Canary 5. Rejected because its terminal outcome and frozen
  scorer are immutable.
- Continue v5 after a failed canary. Rejected because ADR-0033 requires every
  sealed canary to pass before remaining holdout execution.
- Keep self-report as the v6 route authority. Rejected because it is indirect
  evidence and can disagree with authenticated file reads.
- Remove `selected_experts`. Rejected because response-report alignment remains
  useful diagnostic evidence.
- Treat any self-report mismatch as a v6 product failure. Rejected because it
  would again substitute reporting adherence for the loaded-expert behavior
  being qualified.
- Change the Design package. Rejected because neither the private failure nor
  the non-reproducing public regression establishes a package defect.

## Consequences

- Qualification-v5 remains failed and contributes bounded historical evidence
  only: four passed canary shards and one terminal failed candidate job.
- Qualification-v6 needs fresh custody, schedule, canaries and complete frozen
  controls; no prior response is reused as a v6 score.
- Route score, response-report alignment and artifact/evidence checks are
  reported separately.
- W-005 was already in progress, so its immutable `Decisions` list cannot add
  ADR-0036; mutable Evidence and Next action record it.
- This decision does not authorize publication, installation, commit, push,
  tag or release.

## Confirmation

Confirm synthetic positive and negative cases for exact reads, missing reads,
forbidden reads, self-report-only claims, omitted self-report after valid reads,
baseline empty reads, malformed events and paths outside staged snapshots.
Confirm immutable v6 manifests, a fresh encrypted holdout and opaque manifests,
zero-call staging, six armblind canaries, terminal job receipts, scorer/report
separation, and no reuse or mutation of v5 outcomes.

## Revisit when

Raw events cannot authenticate exact staged paths, the runtime command-event
contract changes, public negative tests admit a false read, a v6 canary exposes
an integrity or infrastructure defect, or the project proposes combining route
score and self-report alignment again.
