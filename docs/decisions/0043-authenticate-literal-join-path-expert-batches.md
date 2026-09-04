---
format_version: 1
id: ADR-0043
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/route-provenance
---

# Authenticate literal Join-Path expert batches

## Decision

Accepted automatically under the user's standing instruction to accept project
decisions: do not classify ADR-0042 public stress Case 1 until the canonical
route extractor can authenticate one strict PowerShell batch-read form already
present in its immutable raw events.

Recognize a batch only when the completed zero-exit command declares a literal
`$files` array of distinct known expert basenames, iterates that array, calls
`Get-Content -Raw` through `Join-Path` against the exact staged Design references
directory, contains no wildcard, traversal, UNC or outside-workspace root, and
the authenticated command output contains both a unique filename header and the
complete normalized staged file content for every declared expert. Anything
dynamic, unknown, duplicated, missing or ambiguous fails closed.

Keep explicit-path authentication unchanged. Add adversarial tests for a valid
literal batch and for dynamic arrays, unknown or duplicate files, wildcard,
traversal, UNC/outside roots, missing headers, truncated content and failed
commands. Replay immutable Case 1 only after all tests pass. Make no additional
provider call and preserve the ADR-0042 sequential stop until replay is terminal.

## Problem

Case 1 successfully read the three expected staged experts by looping over a
literal filename array and joining each filename to the staged references
directory. The existing extractor searched only for a complete expert path in
the command text, so it returned zero authenticated reads despite successful
commands and full file bodies in the captured output.

## Drivers

- Authenticate what the command and captured output actually prove.
- Reject arbitrary dynamic path construction or self-report-only claims.
- Preserve staged containment and exact known-expert authority.
- Avoid another model call when immutable evidence is sufficient.
- Keep future sealed runners fail-closed and manifest-bound.

## Considered alternatives

- Count terminal `selected_experts`. Rejected because self-report is diagnostic
  only.
- Treat every `Join-Path` command as a read. Rejected because variables and roots
  may be dynamic or outside the snapshot.
- Rewrite raw events into explicit paths. Rejected because evidence is immutable.
- Run Case 1 again with a prescribed read command. Rejected because outcome
  retries are prohibited and unnecessary.
- Keep the zero-read score. Rejected because it is an extractor false negative,
  not the observed command behavior.

## Consequences

- Case 1 is rescored from immutable raw events after model-free validation.
- The route-provenance code and future runner manifest change again; v6 remains
  immutable failed historical evidence.
- If Case 1 passes replay, ADR-0042 may continue to Case 2; otherwise the public
  suite remains stopped.
- No Design package file changes from this infrastructure repair.
- Publication, installation, commit, push, tag and release remain unauthorized.
- W-005 was already in progress, so its immutable `Decisions` list cannot add
  ADR-0043; mutable Evidence records the repair and replay.

## Confirmation

Confirm the immutable Case-1 raw hash, exact literal list, known files, staged
root, completed command, headers and full normalized bodies; all adversarial
rejections; unchanged package and Gold; zero new provider or sealed calls; and
the sequential fail-stop before any later case.

## Revisit when

Another shell or batch form is proposed, command-output capture changes, file
content becomes too large for authenticated capture, or future sealed suite
generation incorporates the repaired extractor.
