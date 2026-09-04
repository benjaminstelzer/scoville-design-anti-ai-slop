---
format_version: 1
id: ADR-0058
status: accepted
created: 2026-09-04
accepted: 2026-09-04
scope: project/publication
---

# Publish Design and UI

## Decision

Record the user's explicit request to install Design for Codex and Claude and
publish both Design and the related UI changes using benjaminstelzer-github.
The user also authorises the profile README fast-forward. This is publication
authority, not a declaration that unobserved evaluation lanes passed.

## Problem

Design has no public repository yet. UI's optional Design composition is local
and unpublished. Publishing only family links would not deliver that behavior.

## Drivers

- Explicit user requests for both releases and Design installation.
- Preserve the reviewed runtime, source provenance and historical evidence.
- Retain unrelated repository work and the profile's WordPress entry.
- Apply the GitHub Skill's common copy and one-current-release rules.

## Considered alternatives

- Publish only Design and sibling links. The user selected both releases.
- Wait for every historical evaluation lane. Publication was explicitly
  requested with known limits, which remain visible and are not marked passed.
- Publish both with bounded claims and exact package verification. Selected.

## Consequences

Design and UI receive separate versioned releases. Brainstorm, Research, Code,
Scribe, Plan, Handoff and the Scoville system prompt receive only family README
updates. The private GitHub Skill source receives its membership snapshot and
manifest update without a release. The public profile receives the Design entry.
No new complete holdout or provider run is authorised by this Decision.
W-004 remains paused with its original acceptance intact.

## Confirmation

Verify the two exact branch commits, annotated tags, stable releases, package
inventories, public copy, profile and family membership from GitHub. Verify the
two local Design installations against the reviewed 34-file runtime. Remove
the previous UI release and tag only after its successor is verified.

## Revisit when

A package or release check fails, remote work changes concurrently, publication
would expose private material, or the user changes scope.
