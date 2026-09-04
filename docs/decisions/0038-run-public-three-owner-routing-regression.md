---
format_version: 1
id: ADR-0038
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: qualification/route-adjudication
---

# Run a public three-owner routing regression before changing the package

## Decision

Accepted automatically under the user's standing instruction to accept project
decisions: preserve the qualification-v6 Canary 1 fail-stop as failed historical
evidence and do not retry it or continue to another sealed shard.

Run exactly one source-cleared public Terra High behavioral regression that
requires the same three Design owner IDs as the failed candidate route. The
public brief and independent Gold route must be newly authored without private
case facts, wording, artifacts, scores or signatures. Freeze the current Design
package manifest
`3D19CE209E52AFCE91B888D6FB489E29EA9846A1442896129563D4B94ADC01C2`,
authenticate exact staged expert reads as route authority, retain the terminal
route report only as an alignment diagnostic, make one terminal provider call
and perform no retry.

If the public regression reads fewer than all three Gold owners, the routing
defect is publicly reproduced. Make only the narrowest package or Core routing
change supported by that result, rerun the public regression, and generate a
fresh sealed qualification suite with new package and runner manifests.

If the regression reads all three owners, the private failure is not publicly
reproduced. Do not change the package from sealed evidence alone; record the
cause as unconfirmed and require a separate accepted decision for any broader
diagnostic or package change. In both branches qualification-v6 remains failed
and cannot be reused as a passing result.

## Problem

Canary 1 failed because the candidate produced one authenticated expert read
against three preregistered expected owners. The parser, scorer, runner,
transport and frozen expert-file presence checks passed, but the existing
public fixtures prove only the authenticated-read scoring mechanism, not the
same three-owner behavioral routing pressure. The private case cannot safely be
used as public implementation guidance.

## Drivers

- Preserve arm-blind secrecy and the v6 fail-stop.
- Separate a package defect from a private-case or Gold-specific anomaly.
- Obtain public, inspectable evidence before changing canonical routing.
- Keep the diagnostic to one bounded call with no retry.
- Prevent a failed sealed result from being relabeled as passing evidence.
- Require fresh manifests and a fresh sealed suite after any package change.

## Considered alternatives

- Patch Core directly from the sealed adjudication. Rejected because the exact
  private routing pressure has no public behavioral reproduction.
- Retry Canary 1 or run Canary 2. Rejected because the preregistered fail-stop
  makes qualification-v6 terminal after the first failed shard.
- Publish the private brief or Gold route for debugging. Rejected because it
  breaks arm-blind custody and contaminates future evaluation.
- Treat the one-versus-three mismatch as a scorer defect. Rejected because the
  authenticated extractor, raw event class, expected snapshot files and
  terminal alignment checks passed.
- Generate several public variants immediately. Rejected because one exact
  bounded falsifier is sufficient to decide whether a package change is
  currently supported.

## Consequences

- The Custodian may derive only the three public owner IDs from private Gold and
  must certify that no other private fact enters the public fixture.
- The public fixture, Gold route, descriptor, prompt and result may be inspected
  in the local evaluation workspace.
- No sealed call, shard, retry or unseal follows from this decision.
- A reproduced failure permits only a narrow evidence-backed routing repair;
  it does not authorize publication, installation, commit, push, tag or release.
- Any package change invalidates the current executable Design and runner
  manifests for future sealed qualification.
- W-005 was already in progress, so its immutable `Decisions` list cannot add
  ADR-0038; mutable Evidence records the decision and outcome.

## Confirmation

Confirm a source-cleared fixture certification, independent public Gold route,
the unchanged Design manifest, exact staged package hashes, one terminal Terra
High call, zero retries, authenticated read extraction, terminal-report
alignment, zero sealed calls and no private case material in public artifacts.
Record either public reproduction or non-reproduction without weakening the v6
failure.

## Revisit when

The public regression completes, its Gold route is disputed by source review,
authenticated extraction diverges from raw events, the frozen package changes,
or a broader diagnostic is proposed after non-reproduction.
