---
format_version: 1
id: ADR-0007
status: accepted
created: 2026-09-01
accepted: 2026-09-01
scope: design/judgment
supersedes: ADR-0002
transition_batch: 2f8f411b120257971bedf6a858d451262a7857491826e9b29e4833c7ad439380
transition_batch_members: [ADR-0003, ADR-0006, ADR-0007, ADR-0008, ADR-0009]
---

# Refine rule and exception epistemics

## Decision

Retain binding constraint, functional floor, evidence-backed default, craft
heuristic, and convention as authority types. Treat **experiment** as a
declared workflow state applied to a heuristic or convention, not as an
authority class. Treat **tradeoff** as an evaluation outcome. Treat
**preference/taste** as attributed non-defect evidence whose owner, audience,
and scope must be named. An untyped numeric prescription is no stronger than a
craft heuristic.

For generated work, declare the intended effect, bent principle, protected
functions, expected gain, accepted cost, and falsifier before rendering. For
existing work, distinguish documented intent, inferred intent, and unknown
intent. Intent first invented during critique cannot convert a candidate defect
into a successful exception; it must survive a conventional rendered control.
Always state gain and cost. Require a rendered comparison when an exception was
undeclared, is challenged, touches a functional floor, or has a material and
uncertain gain.

Use one critique verdict set: defect, tradeoff, attributed preference,
intentional exception, or unverifiable.

## Problem

The accepted rule taxonomy correctly permits design exceptions, but it lets a
model invent intent after seeing criticism. It also mixes experiment as a rule
type with tradeoff and preference as critique labels.

## Drivers

- Successful rule-breaking needs evidence without turning design into a rigid
  checklist.
- Existing artifacts often lack a documented rationale.
- Preference is real input but not objective defect evidence.
- Numeric folklore must not gain authority by repetition.

## Considered alternatives

- Preserve the existing exception language. This allows post-hoc stories.
- Require every exception to be documented before any design exists. This is
  impossible for audits of existing work and too ceremonial for exploration.
- Reject inferred intent entirely. This would erase legitimate readings of
  historical or supplied work.

## Consequences

- Design mode records consequential experiments before render; critique mode
  calibrates confidence when intent is inferred or unknown.
- Successful exceptions and accidental imitations need paired cases.
- Reference entries state source scope and applicability for evidence-backed
  defaults.
- Minor local choices do not require a ledger unless contested or consequential.

## Confirmation

Blind cases contain the same visible deviation once with compensating
structure and once as accidental failure. The Skill distinguishes them from
artifact evidence, then updates confidence appropriately when documented
intent is revealed. An undeclared “intentional” defense remains a candidate
defect until the control comparison supports it.

## Revisit when

Predeclaration suppresses productive improvisation, the control comparison is
too expensive for the decisions it changes, or reviewers still use preference
as defect evidence.
