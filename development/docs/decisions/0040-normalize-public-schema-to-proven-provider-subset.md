---
format_version: 1
id: ADR-0040
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/public-regression-transport
---

# Normalize the public schema to a proven provider subset

## Decision

Accepted automatically under the user's standing instruction to accept project
decisions: preserve ADR-0039 attempt 2 as a second terminal pre-response
infrastructure failure. The provider rejected `uniqueItems` on
`selected_experts` before inference, so attempt 2 contains no model response,
output, usage, authenticated read or behavioral route evidence.

The ADR-0039 type-only validator was too narrow. Replace it with a recursive
provider-subset validator whose permitted shapes are derived from the exact
qualification-v6 response schema already accepted by the same pinned CLI and
provider. Normalize only the five public result properties to those proven
shapes:

- `case_id`: typed string with the public case constant;
- `mode`: typed string with a one-value enum;
- `selected_experts`: array of non-empty strings with the proven maximum;
- `artifact_paths`: array of non-empty strings;
- `unknowns`: non-empty array of non-empty strings.

Validate exact case, mode, artifact path and duplicate-free route values after
the response rather than through unsupported schema keywords. Bind the
previously accepted qualification-v6 schema and its hash as the dialect
reference. Preserve the public brief, Gold, prompt, model, effort, Design
manifest, staged package and authenticated-read authority unchanged.

After attempt 1 and attempt 2 are separately frozen and the expanded
model-free tests pass, permit exactly one attempt-3 transport opportunity with
separate overwrite-refusing paths. It remains a replacement for a missing
behavioral result, not an outcome retry. Any attempt-3 failure is terminal and
no fourth attempt is authorized.

## Problem

Attempt 2 added the explicit types requested by the first provider error but
retained `uniqueItems`, which the response-format dialect rejects. The local
validator encoded only the first observed rule and therefore gave false
confidence instead of checking the complete permitted subset already present
in the working qualification harness.

## Drivers

- Preserve both failed transport attempts and their exact evidence.
- Stop learning provider-schema rules one error at a time.
- Reuse schema shapes already accepted by the same execution path.
- Keep exact behavioral values enforced after structured response parsing.
- Change no brief, Gold, prompt, package, model or route authority.
- Allow one final bounded transport opportunity and no fourth attempt.

## Considered alternatives

- Remove only `uniqueItems` and call again. Rejected because the incomplete
  validator could still miss another dialect restriction.
- Use unrestricted JSON output. Rejected because it weakens deterministic
  terminal parsing.
- Copy the complete v6 output contract. Rejected because the public regression
  needs only five fields and should not add unrelated behavioral obligations.
- Count attempts 1 and 2 as failed route outcomes. Rejected because neither
  reached inference or produced an authenticated read.
- Continue retrying schema errors until accepted. Rejected; attempt 3 is the
  final transport opportunity under this decision.

## Consequences

- Attempts 1 and 2 remain terminal infrastructure evidence with zero product
  evidence.
- Exact duplicate and artifact-path checks move to deterministic post-response
  validation, not model judgment.
- Attempt 3 uses a schema composed only from shapes proven in the accepted v6
  schema and separate raw-event and stderr paths.
- A terminal attempt-3 model response is the sole behavioral result admitted
  for ADR-0038.
- Qualification-v6 remains failed and all sealed shards remain stopped.
- Publication, installation, commit, push, tag and release remain unauthorized.
- W-005 was already in progress, so its immutable `Decisions` list cannot add
  ADR-0040; mutable Evidence records the decision and result.

## Confirmation

Confirm both prior raw-event hashes and exact provider errors, zero behavioral
evidence in both attempts, the unchanged behavioral inputs and package digest,
the bound accepted v6 schema, recursive keyword-and-shape rejection including
`uniqueItems`, exact post-response checks, separate attempt-3 paths, one final
transport opportunity, no outcome retry, zero sealed calls and preserved v6
fail-stop.

## Revisit when

Attempt 3 becomes terminal, the proven reference schema is no longer accepted,
any behavioral input changes, or a fourth transport opportunity is proposed.
