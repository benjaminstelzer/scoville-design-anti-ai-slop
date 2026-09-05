---
format_version: 1
id: ADR-0041
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/route-provenance
---

# Canonicalize repeated Windows path separators in route provenance

## Decision

Accepted automatically under the user's standing instruction to accept project
decisions: retain the successful ADR-0040 attempt-3 raw events and perform no
additional provider call. Repair only the canonical route-provenance path check
so repeated Windows separators in a relative staged path normalize to one
separator before containment comparison.

The authenticated-read gate still requires a completed zero-exit command, an
explicit `Get-Content` read, a known exact expert filename, non-empty command
output, no wildcard, exactly one terminal agent message and either a relative
path under the staged Design package or an absolute path under the exact
workspace. Canonicalization must not turn an absolute outside-workspace path,
parent traversal, UNC path, wildcard or unknown expert into an accepted read.

Add regressions for repeated relative and staged-absolute separators plus
outside-workspace, parent-traversal, UNC, wildcard and ambiguous-path rejection.
Replay the immutable attempt-3 raw events after the tests pass. Apply the same
repair to future suite generation and rebuild every affected runner manifest;
do not mutate qualification-v6's historical failed result.

## Problem

Attempt 3 produced one valid terminal model response and one successful
PowerShell command reading the exact three public Gold experts. PowerShell
accepted doubled separators in those relative paths, but `_path_is_staged`
compared them against a single-separator literal and failed closed. The extractor
recognized all three exact filenames and authenticated the command completion
and output, so only lexical separator canonicalization blocked adjudication.

## Drivers

- Score real staged reads rather than a shell's harmless separator spelling.
- Preserve all security and fail-closed boundaries around path authority.
- Avoid another provider call when immutable raw events are sufficient.
- Add adversarial proof before replaying the result.
- Keep qualification-v6 historical evidence unchanged.
- Require fresh manifests for any future sealed suite using the repaired code.

## Considered alternatives

- Treat attempt 3 as a route failure. Rejected because the gate failed before
  route comparison on lexical spelling despite authenticated successful reads.
- Accept every path matched by the filename regex. Rejected because an outside
  absolute path could then receive route credit.
- Rewrite the raw command strings. Rejected because execution evidence must
  remain immutable.
- Run another model call with single separators. Rejected because no additional
  behavioral evidence is needed and ADR-0040 prohibits a fourth attempt.
- Normalize full filesystem paths with unchecked resolution. Rejected because
  the extractor must classify recorded command text without creating a path or
  weakening traversal and UNC rejection.

## Consequences

- Attempt 3 remains the sole terminal behavioral result for ADR-0038.
- The public adjudication may proceed by replay after the repaired extractor and
  adversarial tests pass.
- qualification-v6 remains failed on its original immutable scorer result; the
  repair cannot retroactively turn it into a pass.
- The repaired extractor changes a future runner manifest and therefore
  requires a fresh sealed suite if qualification resumes.
- No Design package file changes solely from this infrastructure repair.
- Publication, installation, commit, push, tag and release remain unauthorized.
- W-005 was already in progress, so its immutable `Decisions` list cannot add
  ADR-0041; mutable Evidence records the repair and replay result.

## Confirmation

Confirm the immutable attempt-3 raw hash, expected three regex matches, command
success and output, separator-only normalization, repeated relative and absolute
acceptance, all adversarial rejections, unchanged package and public Gold,
authenticated replay, terminal-report alignment, zero additional provider and
sealed calls, and unchanged v6 historical receipts.

## Revisit when

The runner changes shells or path syntax, relative-workspace semantics change,
UNC paths become required, a new traversal form appears, or future sealed suite
generation incorporates the repaired extractor.
