---
format_version: 1
id: ADR-0001
status: superseded
created: 2026-09-01
accepted: 2026-09-01
scope: family/ownership
superseded_by: ADR-0006
---

# Split design judgment from UI implementation with a standalone fallback

## Decision

Scoville Design owns design definition and judgment when it is active and
applicable. This includes design systems, art direction, visual concept,
information hierarchy, UI design and workflow arrangement, typography, colour,
spacing, imagery, and critique. Scoville UI owns strict implementation through
the chosen framework, incumbent design system, components, tokens, platform
conventions, responsive behavior, interaction states, accessibility mechanics,
and rendered interface proof. If Design is absent, inactive, inapplicable, or
explicitly excluded, UI retains its bounded standalone Greenfield rules.
Neither Skill depends on, installs, requires, simulates, or reimplements the
other.

## Problem

The current UI Skill owns both visual/design decisions and their framework
implementation. The requested Design Skill would compete with it unless
ownership changes by concern. Removing UI's Greenfield capability entirely
would violate the requirement that every Scoville Skill remain independently
useful.

## Drivers

- The user's explicit distinction between design definition and strict
  framework/design-system implementation.
- Independent operation for every Skill.
- A canonical design system must outrank both Skills when one already exists.
- Design must be able to improve hierarchy and workflow without gratuitously
  replacing a framework's visual language.
- UI must retain accessibility, state, responsive, and rendered-evidence
  protections.

## Considered alternatives

- Keep all UI-design judgment in Scoville UI. This leaves Design unable to own
  Greenfield UI design and creates duplicate typography, hierarchy, and spacing
  authorities.
- Move all Greenfield behavior to Design and make UI implementation-only in
  every environment. This creates a practical dependency and weakens UI when
  Design is unavailable or excluded.
- Let both Skills decide independently. This creates conflicting visual owners
  and makes composed behavior unpredictable.

## Consequences

- UI's Core and references need conditional ownership wording and new routing
  tests.
- Design needs complete standalone UI-design knowledge but must yield
  framework implementation and proof concerns when UI is active.
- UI retains Greenfield rules as a fallback, not as a competing owner when
  Design is active and applicable.
- Existing design systems and explicit user/project direction remain above both
  Skills.
- Qualification must test solo, composed, incumbent-system, and opt-out cases.

## Confirmation

Controlled routing traces show one design-decision owner per concern. UI-only
Greenfield cases remain behavior-complete. Composed cases show Design making
the decision and UI implementing it without duplicated or contradictory
guidance. Existing UI regressions for framework fidelity, accessibility,
states, responsiveness, and rendered proof still pass.

## Revisit when

A target host cannot expose active/applicable Skill context reliably, UI-only
fallback materially diverges from composed Design behavior, or a third Skill
needs to own interaction or service design separately.
