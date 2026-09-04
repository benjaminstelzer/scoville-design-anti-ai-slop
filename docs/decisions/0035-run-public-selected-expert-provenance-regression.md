---
format_version: 1
id: ADR-0035
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/provenance-regression
---

# Run a public selected-expert provenance regression

## Decision

Accepted automatically under the user's standing instruction to accept project
decisions: preserve the Canary-5 fail-stop and run exactly one public Terra High
regression under the same frozen `design_plus_revised_ui` candidate contract.
The regression compares authenticated Design expert reads in raw execution
events with the terminal response's `selected_experts` field.

Use a source-cleared public fixture whose exact Design route already passed as
C06-R3. Stage the frozen qualification-v5 Design and UI snapshots, require the
same structured response field and one text-only model-response slot, and make
no package, parser, scorer, Gold or sealed-runtime change before observing the
result.

If the applicable expert reads occur and the terminal list is again empty or
incorrect, treat the mechanism as publicly reproduced and revise the owning
package or response contract only in a new executable and sealed-suite
generation. If the terminal list matches the reads, retain the sealed failure
as indeterminate and make a separate evidence-policy decision; do not retry the
sealed outcome. Route drift, infrastructure failure or unverifiable raw events
make the regression inconclusive and stop this lane.

## Problem

Canary 5 failed only `route / selected_expert_provenance`: an applicable Design
expert was read but the terminal response recorded an empty list. The sealed
evidence does not establish whether this is a repeatable package/response-
contract weakness or a single model-output adherence failure. Continuing the
sealed suite or changing the package from one private outcome would compromise
the qualification boundary.

## Drivers

- Preserve the terminal sealed failure without outcome retry.
- Distinguish repeatable public behavior from a private one-off omission.
- Keep the test source-cleared, reproducible and independently inspectable.
- Bind claimed selected experts to authenticated reads rather than prose alone.
- Avoid changing product or scoring controls before the failure mechanism is
  reproduced publicly.

## Considered alternatives

- Retry Canary 5. Rejected because the terminal model response cannot be
  retried for outcome.
- Continue with Canary 6 or the remaining holdout. Rejected because the canary
  batch has failed.
- Patch `selected_experts` from observed reads after the response. Rejected
  because it rewrites model evidence and weakens the explicit contract.
- Change the package immediately. Rejected because one sealed omission does not
  isolate an owning product defect.
- Waive provenance reporting now. Rejected because route/read traceability is a
  frozen W-005 dimension and requires a separate evidence-policy decision.

## Consequences

- Exactly one additional public provider call is authorized for diagnosis.
- Canary 5, Canary 6 and all non-canary holdout execution remain closed.
- A reproduced omission requires new package and suite generations; existing
  sealed results remain historical evidence only.
- A non-reproduction does not convert Canary 5 to pass and does not authorize a
  retry.
- W-005 was already in progress, so its immutable `Decisions` list cannot add
  ADR-0035; mutable Evidence and Next action record the result.

## Confirmation

Confirm a zero-call preflight bound to the frozen Design/UI manifests, public
fixture, prompt, schema, pinned CLI and sandbox; one terminal Terra High call;
raw-event hashes; exact expert-reference read extraction; exact comparison to
`selected_experts`; artifact and schema validity; and a receipt proving no
sealed or subsequent provider call occurred.

## Revisit when

The public regression reproduces the omission, route reads differ from the
expected public route, raw events cannot authenticate reads, infrastructure
fails, or the project proposes weakening the frozen provenance gate.
