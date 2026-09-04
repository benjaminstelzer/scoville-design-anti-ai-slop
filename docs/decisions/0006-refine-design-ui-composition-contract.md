---
format_version: 1
id: ADR-0006
status: accepted
created: 2026-09-01
accepted: 2026-09-01
scope: family/ownership
supersedes: ADR-0001
transition_batch: 2f8f411b120257971bedf6a858d451262a7857491826e9b29e4833c7ad439380
transition_batch_members: [ADR-0003, ADR-0006, ADR-0007, ADR-0008, ADR-0009]
---

# Refine the Design and UI composition contract

## Decision

Replace the broad accepted ownership statement with an operational
concern-level contract. A sibling Skill is **active** only when its instructions
are present in the current task context; discovery or installation is not
activation. It is **applicable** only to the concrete concern at hand. Neither
Skill searches for, loads, or simulates the other to determine this.

Use this precedence for composed UI work: system, safety, and legally binding
accessibility; explicit user direction; repository instructions; incumbent product design system; an active
Design decision for the concern; framework or platform defaults; local
convention; then Skill defaults. Design may diagnose an incumbent system and
propose an owner-level change, but neither Skill silently overrides it.

For consequential composed decisions, Design hands UI a compact record with:
concern, decision, intended effect, authority/source, preserved constraints,
allowed variation, deliberate exception and compensation if any, validation
target, and current evidence status. UI consumes that record without
re-deciding the settled design concern.

Concern ownership is:

| Concern | Design | UI when active |
| --- | --- | --- |
| Hierarchy, density, workflow, adaptive composition | Intended relationship and transformation | Framework-valid responsive implementation and behavior proof |
| States and feedback | Intended presentation, priority, and recovery experience | Component states, semantics, focus/input behavior, announcements, transitions, and proof |
| Accessibility | Inclusive communication and equivalent meaning as a design input | Semantic, interactive, platform, scaling, and rendered-mechanics implementation |
| Typography, colour, spacing, imagery | Direction, roles, relationships, and critique | Tokens/components faithfully implement the accepted direction |
| Rendered interface | Interpret visual quality and design consequence | Capture and verify states, viewports, interaction, and framework behavior |

If UI reports a real implementation constraint, Design revises the affected
decision and UI re-implements it. UI does not silently redesign; Design does
not prescribe framework internals. With UI excluded, Design may direct and
inspect the primary rendered state through the available artifact tool, but it
must name unverified responsive, state, semantic, framework, and accessibility
mechanics. With Design excluded, UI uses only its bounded standalone fallback.

## Problem

The accepted split names broad owners but leaves activation, applicability,
precedence, responsive decisions, state presentation, accessibility, rendered
interpretation, and mid-task handoff ambiguous. The current UI owner ladder has
no rank for an active Design decision.

## Drivers

- Standalone Skills cannot introspect sibling installation reliably.
- An incumbent product system must remain above both Skills.
- Greenfield Design direction must outrank a framework's aesthetic defaults.
- Responsive behavior and accessibility contain both design and implementation
  concerns.
- Composed runs must not spend context re-litigating ownership.

## Considered alternatives

- Keep the accepted high-level split without an operational signal. This leaves
  normal activation and overlap cases ambiguous.
- Give Design unconditional precedence. This would let it override incumbent
  systems and implementation constraints.
- Give UI all responsive, state, and accessibility decisions. This would remove
  central design judgment from Design.
- Duplicate critique in both Skills. This creates double-owner loops.

## Consequences

- UI's owner ladder and each routed UI-quality section need concern tags.
- The cross-Skill decision record is used only when another owner consumes it,
  not for every local spacing choice.
- Tests need exactly one decision owner and one implementation/proof owner per
  concern in solo, composed, incumbent, and opt-out cases.
- Design-only UI evidence is useful but explicitly bounded.

## Confirmation

Table-driven traces cover installed-but-not-active, Design-only, UI-only,
composed Greenfield, incumbent system, each opt-out, and neither active. Each
trace names one design-decision owner and one implementation/proof owner for
hierarchy, responsive transformation, state presentation, accessibility,
tokens, and interaction semantics. UI consumes a Design record without
re-deciding it, and the constraint loop changes only the affected decision.

## Revisit when

The host exposes a reliable typed composition protocol, the decision record is
more costly than the drift it prevents, or a separate interaction/service
design owner is introduced.
