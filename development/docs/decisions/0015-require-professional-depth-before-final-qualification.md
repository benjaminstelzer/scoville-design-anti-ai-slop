---
format_version: 1
id: ADR-0015
status: accepted
created: 2026-09-02
accepted: 2026-09-02
scope: content/expert-depth
---

# Require professional expert depth before final qualification

## Decision

Do not continue sealed qualification from RC7 until every routed expert module
has passed a professional-depth audit. Topic coverage is insufficient: each
material concern must contain enough task-local instruction to generate,
discriminate, critique, repair, permit justified exceptions, and verify the
work without requiring a live source fetch.

Begin with typography and writing systems. Decide from the audit whether a
domain remains one bounded expert or is split into directly routed flat leaves.
The existing 1,800-token figure is a cost target, not a hard ceiling; sufficient
professional depth takes precedence. Keep progressive disclosure: deeper
knowledge loads only when its concern can change the result.

## Problem

The current typography module names several correct axes but compresses some
criteria into broad phrases. For example, `measure`, `leading`, `tracking`, and
`fallback` do not by themselves teach the agent how to diagnose character
confusability, paragraph rhythm, justification, punctuation, page-break
quality, fallback metric drift, or context-specific numeric heuristics. Similar
compression may exist in other expert modules.

## Drivers

- The Skill should act like a capable all-round graphic designer, not a topic
  checklist.
- Rules must be applicable and source-bounded rather than remembered slogans.
- Rules remain breakable when intent, functional floors, compensating
  structure, and whole-result quality justify the exception.
- Frontier-model prior knowledge should not be recopied unless the Skill needs
  to focus, correct, teach, or externally verify it.
- Added depth must not make unrelated tasks load the whole curriculum.
- Exact professional coverage and correctness outrank token savings; selective
  routing then limits cost, and compression is optimized only after both pass.

## Considered alternatives

- Keep RC7 because Terra handled one typography critique well. One successful
  critique does not prove comprehensive generation or repair guidance.
- Add every textbook rule to one long module. This wastes context and turns
  conventions into universal laws.
- Depend on live books and links. This makes runtime behavior fragile and
  creates licensing and availability risk.
- Add fixed recipes such as 45–75 characters or two fonts everywhere. These
  can be useful starting hypotheses only in their actual language, medium, and
  reading context.

## Consequences

- W-011 audits depth and source mapping before package prose changes.
- W-012 produces a new candidate and new manifests; RC7 evidence remains
  historical and is not silently transferred.
- A leaf may exceed 1,800 tokens when the concern is not cleanly separable and
  the added payload is necessary; the exception records measured context cost
  and non-inferiority evidence.
- Consequential rules are typed as binding constraint, evidence-bounded rule,
  contextual convention, heuristic, preference, or deliberate exception.
- Numeric guidance states population, script, medium, task, source, and what
  observation should override it.
- Sealed holdout work stays paused until changed paths pass one-at-a-time open
  Terra High tests.

## Confirmation

The audit must show for every shipped expert: inputs, formal variables,
failure signatures, causal diagnosis, generation moves, smallest repairs,
exceptions, verification views, source IDs, and claim limits. Package
validation, token budgets, selective-read tests, applied open cases, and render
inspection must pass on the successor candidate.

## Revisit when

A module's routed use becomes rare enough to withhold, or direct evidence shows
that a smaller focus prompt performs non-inferiorly across its professional
coverage.
