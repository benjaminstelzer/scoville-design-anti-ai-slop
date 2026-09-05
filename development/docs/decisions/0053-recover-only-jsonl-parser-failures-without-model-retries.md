---
format_version: 1
id: ADR-0053
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/harness-recovery
---

# Recover only JSONL parser failures without model retries

## Decision

In the separate ADR-0052 diagnostic assessment, decode JSONL using LF record
boundaries rather than Python's broader `splitlines()` behavior. Require valid
JSON records and preserve every decoded value and event order. If the unchanged
scorer interface requires text input, an in-memory JSON reserialization may
escape Unicode separators while preserving the exact parsed data. Record the
original input hash and adapter identity; never rewrite original captures.

After the frozen run closes, apply this append-only model-free assessment only
to the proven Unicode-parser failures whose complete original responses are
already captured. Use unchanged Gold and substantive scoring rules. Render
their captured artifacts and obtain independent parent review where the frozen
job required it. Make no model call or additional repair for these cases, and
do not rescore already assessed unaffected jobs.

A recovered result that substantively and visually passes may count as valid
in the user-adjudicated Skill acceptance ledger under the user's instruction
not to penalize the Skill for pure test failures. Preserve all original harness
errors and preregistered results separately. Any genuine route, artifact or
visual failure remains a failure; correct parsing alone is not a pass.

## Problem

Literal Unicode separators inside valid JSON strings caused the frozen parser
to reject several complete responses. The preserved responses can be assessed
without paying for new model attempts or pretending their original evaluation
succeeded. The same defect could also obstruct the separately requested replay.

## Drivers

- Evaluate existing substantive evidence instead of repeating model work.
- Keep pure harness defects out of negative Skill performance counts.
- Preserve raw evidence, Gold, original results and explicit adjudication.
- Apply only the demonstrated parsing correction, not broader scorer changes.

## Considered alternatives

- Repeat the affected model jobs. Rejected because complete responses exist.
- Modify the frozen parser or overwrite original scores. Rejected.
- Credit a case solely because its JSON parses. Rejected; all substantive and
  required visual checks still apply.
- Rescore every unaffected job. Rejected as unnecessary and outside scope.

## Consequences

The diagnostic adapter and focused tests are separate from the frozen runner.
This authorizes zero additional provider calls beyond ADR-0052's sole attempt.
Current and recovered results remain independently traceable. Publication,
installation, commit, push, tag and release remain prohibited.

## Confirmation

Confirm focused LF, CRLF, Unicode, malformed-JSON and parsed-value-preservation
tests; unchanged original hashes and Gold; exactly the proven affected case
set; zero recovery model calls; substantive and rendered outcomes; and explicit
mapping between original harness errors and user-adjudicated results.

## Revisit when

The input is genuinely malformed, decoded values change, the defect has a
different cause, Gold would change, or another model attempt is required.
