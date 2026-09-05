---
format_version: 1
id: ADR-0019
status: accepted
created: 2026-09-02
accepted: 2026-09-02
scope: content/source-runtime-contract
---

# Use local rules with offline source provenance

## Decision

Put every operative rule, exception, causal repair, and proof requirement in
the owning runtime reference. Keep install-time definitions in non-routed
`references/source-index.md`. Use source IDs only to resolve provenance,
scope, evidence strength, license, bias, currency, and recheck triggers in a
non-routed rule-to-source map and research ledger.

A live source URL is never required to apply an admitted runtime rule. A broken
or outdated link blocks new source-dependent or release-sensitive claims until
the authority is refreshed; it does not silently remove the local rule.

Every consequential rule is classified as a binding constraint,
evidence-bounded rule, contextual convention, heuristic, attributed preference,
or deliberate exception. Numeric guidance also records source scope,
population, language/script, medium, task, and override evidence.

## Problem

Opaque identifiers such as `L-01` or `E-10` do not teach behavior by themselves,
and runtime dependence on external books or webpages would be fragile. Copying
protected source expression into the package would create licensing risk. The
agent instead needs the independently worded applied rule locally plus an
inspectable provenance path for audit and current verification.

## Drivers

- The Skill must work offline after installation.
- Public access is not the same as an open adaptation license.
- Standard books can ground original synthesis without being shipped.
- Current standards, browsers, provider terms, licenses, and supplier
  specifications require later re-verification.
- Source mapping must explain why a rule exists and where its limits begin.

## Considered alternatives

- Fetch every source at runtime. This is slow, fragile, and often legally or
  technically impossible.
- Ship books, screenshots, or source excerpts. Most canonical material is
  copyright-protected or contains third-party assets.
- Remove source IDs and trust the model. This loses traceability and makes
  scope corrections harder.
- Put full bibliographies in every leaf. This wastes context without improving
  applied behavior.

## Consequences

- Each reference header lists only source IDs used by consequential rule
  clusters.
- Static validation rejects unresolved IDs and rule clusters with no source or
  explicit bounded empirical rationale.
- The public repository contains original instructions and bibliographic
  records, not source scans or restricted comparison material.
- Local-only licensed comparison pairs live outside the repository with hashes
  and receipts; public evidence contains descriptions and results only.

## Confirmation

Package validation must pass with network disabled. A source-resolution test
must map every header ID and consequential cluster. A deliberately unavailable
URL must not change runtime output except that current verification is marked
blocked where the task requires it.

## Revisit when

A source license permits useful adaptation or a machine-readable standard can
be vendored safely and materially improves behavior without expanding ordinary
context.
