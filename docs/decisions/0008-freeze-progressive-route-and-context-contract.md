---
format_version: 1
id: ADR-0008
status: accepted
created: 2026-09-01
accepted: 2026-09-01
scope: skill/context
supersedes: ADR-0004
transition_batch: 2f8f411b120257971bedf6a858d451262a7857491826e9b29e4833c7ad439380
transition_batch_members: [ADR-0003, ADR-0006, ADR-0007, ADR-0008, ADR-0009]
---

# Freeze the progressive route and context contract

## Decision

Retain progressive multi-route disclosure with a smaller decision-oriented
reference topology. Core owns activation, applicability, precedence, brief
invariants, the generative/critique/revision loop, rule types, the accessibility
floor, exception timing, provenance/evidence gates, and the route matrix.

Use these routed references in version one:

1. `brief-and-concept.md`
2. `composition-and-layout.md`
3. `typography-and-writing-systems.md`
4. `colour-and-reproduction.md`
5. `imagery-and-art-direction.md`
6. `information-and-data.md`
7. `brand-and-visual-systems.md`
8. `ui-and-interaction-design.md`
9. `motion-and-sequence.md`
10. `media-production-and-handoff.md`
11. `critique-and-validation.md`
12. `culture-ethics-and-provenance.md`
13. `sources-and-attribution.md`, maintenance-only

No task loads `sources-and-attribution.md` unless attribution, provenance,
licensing, or source maintenance is itself relevant. A route is retained only
if it has a distinct trigger and can change a decision. Several references may
load, but no ordinary route loads more than three without a task-specific
reason.

Measure UTF-8 Skill files with `o200k_base`, matching the current Scoville UI
benchmark. The version-one ceilings are: Core at most 1,500 tokens; ordinary
single-domain Core plus routed context at most 3,800; ordinary mixed Core plus
up to three references at most 7,000. Crossing a ceiling fails qualification
unless a new Decision changes the budget with measured evidence.

## Problem

The accepted progressive-disclosure decision has no route matrix, reference
budget, or stable topology. The audit's chapter-like reference list duplicates
foundations, critique, accessibility, collaboration, and production concerns.

## Drivers

- Context cost must be falsifiable and measured.
- Accessibility, ownership, evidence, and exception rules cannot disappear
  because a route was missed.
- Colour reproduction and imagery direction have different triggers.
- A broad Skill needs mixed routes without an encyclopedic Core.

## Considered alternatives

- Keep the original fifteen-file list. This preserves chapter labels but not
  distinct routing ownership.
- Put all cross-cutting knowledge in one foundations reference. This becomes a
  second hidden Core.
- Limit every task to one reference. This fails real mixed design work.
- Remove budgets until implementation. This makes compactness unfalsifiable.

## Consequences

- A frozen route matrix declares required and forbidden reads for single and
  mixed tasks.
- Each reference maps to verified sources or is an explicitly bounded,
  unqualified routing stub.
- More than three routes is an exceptional task decision, not a normal mode.
- Context measurement joins routing correctness; it never replaces outcome
  quality.

## Confirmation

Single- and mixed-domain routing cases hit the predeclared minimum set, avoid
forbidden reads, and stay within token ceilings. Each retained route changes at
least one decision on its positive cases and stays unloaded on its negative
cases. The Core alone still enforces ownership, functional accessibility,
exception, provenance, and evidence floors.

## Revisit when

Observed tasks consistently require the same route bundle, a ceiling weakens
behavior, a route lacks discriminating triggers, or measured runtime context
does not match the declared accounting method.
