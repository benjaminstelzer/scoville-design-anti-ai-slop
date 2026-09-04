---
format_version: 1
id: ADR-0002
status: superseded
created: 2026-09-01
accepted: 2026-09-01
scope: design/judgment
superseded_by: ADR-0007
---

# Type design rules and permit evidenced exceptions

## Decision

Scoville Design classifies guidance as binding constraint, functional floor,
evidence-backed default, craft heuristic, convention, or experiment. Only the
first two categories are non-negotiable without changing the underlying
authority or function. Other rules may be broken when the intended effect is
named, required communication and accessibility remain intact, compensating
structure is present, the real artifact is inspected in context, and the whole
design is stronger despite the stated cost.

## Problem

Rigid checklists make technically orderly but lifeless work and erase valid
experimental design. Unbounded exceptions allow arbitrary inconsistency to be
rationalized after the fact. The Skill needs to know both the value and the
scope of a rule.

## Drivers

- The user's explicit requirement that design rules are grounded but remain
  breakable when the design benefits.
- Accessibility, required content, licenses, and explicit constraints cannot
  be waived by taste.
- Grids, alignment, contrast, typographic scales, spacing rhythms, and genre
  conventions are tools rather than universal laws.
- Visual quality claims require the rendered artifact and its intended context.

## Considered alternatives

- Treat every rule as a hard gate. This suppresses experimentation and mistakes
  convention for function.
- Treat rules as optional taste. This removes useful defaults and makes critique
  non-reproducible.
- Use one confidence score for all guidance. This hides the difference between
  legal authority, empirical evidence, craft practice, and subjective
  preference.

## Consequences

- References must state purpose, default, context variables, failure modes,
  valid exceptions, and disconfirming evidence rather than only commands.
- Critique must distinguish defect, tradeoff, preference, and intentional
  exception.
- Tests need deliberate good rule breaks and accidental violations.
- Exceptions remain local unless explicitly promoted into a design system.

## Confirmation

Evaluation cases containing a successful broken grid, deliberate ambiguity,
unusual typography, and intentional density are preserved when their function
and compensating structure survive. Parallel accidental failures are detected
and prioritized. Binding accessibility, content, and license constraints are
never waived as aesthetic exceptions.

## Revisit when

The exception protocol consistently rationalizes defects, adds more ceremony
than judgment, or suppresses expert recognition that cannot be usefully
formalized.
