---
format_version: 1
id: ADR-0039
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/public-regression-transport
---

# Replace the pre-response schema rejection without retrying an outcome

## Decision

Accepted automatically under the user's standing instruction to accept project
decisions: retain ADR-0038 public attempt 1 as a terminal infrastructure failure
with no model response and no behavioral evidence. Its response schema used
`const` without an explicit `type` for three properties, and the provider
rejected the request as `invalid_json_schema` before inference.

Preserve the raw events, empty stderr and all attempt-1 descriptor, schema,
runner and preflight hashes. Correct only the response-schema dialect defect by
adding the missing explicit types. Add a model-free adversarial validator that
rejects every object property lacking a provider-required type and confirms the
exact fixed schema. Freeze the same public brief, Gold route, prompt, model,
effort, Design manifest, staged package and route authority.

After the corrected post-failure preflight passes, permit exactly one replacement
transport attempt. This is not an outcome retry because attempt 1 produced no
model response, output, usage or route evidence. The replacement still permits
one terminal response, no outcome retry and zero sealed calls. Any further
pre-response or post-response failure stops and requires a new decision.

## Problem

The public fixture passed its local contract tests, but they checked JSON
Schema validity rather than the narrower provider response-format dialect. The
API requires a `type` key even when `const` already determines a value's type.
The runner therefore created one transport attempt and received HTTP 400 before
the model could run.

## Drivers

- Preserve the failed transport attempt rather than erasing or relabeling it.
- Distinguish transport opportunity from behavioral outcome retry.
- Repair only the demonstrated lowest-layer schema defect.
- Add a regression that would have rejected the original schema locally.
- Keep the package, public Gold, model and sealed boundary unchanged.
- Stop after one corrected replacement attempt regardless of outcome.

## Considered alternatives

- Treat attempt 1 as the ADR-0038 route result. Rejected because no model
  response or authenticated expert read exists.
- Edit the existing raw events and rerun under the same attempt identity.
  Rejected because it would destroy the terminal failure evidence.
- Remove structured output. Rejected because it broadens the harness change and
  weakens deterministic terminal parsing.
- Add types and loop until the provider accepts. Rejected because unbounded
  transport retries would conceal harness quality and spend.
- Stop all diagnosis permanently. Rejected because one narrow, locally testable
  transport replacement can still answer the accepted public falsifier.

## Consequences

- Attempt 1 remains failed infrastructure evidence and contributes zero route
  evidence.
- Attempt 2 uses separate raw-event and stderr paths and cannot overwrite or
  retry either attempt.
- The attempt-2 descriptor binds ADR-0038, ADR-0039, the preserved failure
  receipt, corrected schema and unchanged behavioral inputs.
- A terminal attempt-2 response is the only behavioral result admitted by the
  public regression.
- Qualification-v6 remains failed and sealed execution remains stopped.
- Publication, installation, commit, push, tag and release remain unauthorized.
- W-005 was already in progress, so its immutable `Decisions` list cannot add
  ADR-0039; mutable Evidence records the decision and transport outcome.

## Confirmation

Confirm the attempt-1 raw-event hash and exact provider error, zero model output
and usage, explicit types on every schema property, adversarial rejection of the
old schema, unchanged public brief Gold prompt package manifest and staged
digest, separate attempt-2 paths, one allowed replacement attempt, no outcome
retry, zero sealed calls and preserved v6 fail-stop.

## Revisit when

Attempt 2 becomes terminal, the provider response-format dialect changes, a
different schema defect appears, any behavioral input changes, or another
transport opportunity is proposed.
