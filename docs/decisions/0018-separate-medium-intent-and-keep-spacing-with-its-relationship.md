---
format_version: 1
id: ADR-0018
status: accepted
created: 2026-09-02
accepted: 2026-09-02
scope: architecture/medium-and-spacing-ownership
---

# Separate medium intent and keep spacing with its relationship

## Decision

Add direct `web-and-responsive-design` and
`editorial-and-fixed-media-design` leaves while keeping shared visual craft in
its owning domain leaves.

Do not add a standalone spacing module:

- Composition owns semantic grouping, macro rhythm, density, margins, grid
  intervals, negative space, optical balance, and spatial tension.
- Typography owns glyph, word, line, paragraph, baseline, column, and break
  spacing.
- Design owns design-system spacing roles and intended relationships. Scoville
  UI owns strict framework and token implementation when active.
- Responsive and fixed-media leaves own transformation, medium-specific proof
  requirements, and the Design record without redefining the base rules. UI or
  Media Production executes and owns the applicable runtime, provider, or
  physical proof.

Design owns intended responsive transformation. Scoville UI owns framework
breakpoints and queries, component behavior, semantics, focus and input,
announcements, and rendered interaction proof. Design owns fixed/editorial
sequence, pacing, page/spread/fold/face relationships, viewing context, and
physical constraints as design inputs. Media Production owns preflight, export,
receiver requirements, and provider or physical proof.

## Problem

The current package names responsive recomposition and print constraints but
does not give either medium a complete applied decision contract. Repeating
web/print branches in Typography, Composition, Colour, Imagery, and UI would
duplicate rules. A separate spacing curriculum would likewise detach each gap
from the relationship it communicates.

## Drivers

- Responsive web work changes structure under content pressure.
- Fixed and editorial work exploits final dimensions, sequence, spread, viewing
  distance, folds, and physical constraints.
- Spacing quality depends on grouping, hierarchy, typography, medium, and
  deliberate tension rather than one scale or amount.
- The Design/UI and design/production boundaries must remain testable.

## Considered alternatives

- Keep medium branches inside every craft leaf. This repeats transformation
  logic and makes ownership inconsistent.
- Add web, print, editorial, packaging, and wayfinding leaves. This exceeds the
  current specialist evidence and creates overlapping generalist modules.
- Put responsive design in Scoville UI. That makes implementation own design
  intent and prevents Design-only use.
- Add an independent spacing expert. It would routinely co-load and encourage a
  detached token/raster recipe.

## Consequences

- Responsive editorial/marketing work can load shared craft plus the web leaf
  without a full application workflow curriculum.
- Native application workflow can load interaction design without web-specific
  material.
- Multi-page and fixed outputs can load fixed-media intent while production
  proof remains separately routed.
- Packaging faces and signs may use the fixed-medium floor, but structural,
  materials, regulatory, installation, and environmental-safety questions
  escalate to specialists.
- Abstraction remains relational: “more whitespace” and “use the 8-point grid”
  are rejected unless the actual system and relationship justify them.

## Confirmation

Open Terra High cases must include responsive recomposition, fixed editorial
sequence, print-intent handoff, spacing parent-cause repair, Design-only, UI-only
fallback, and composed Design/UI ownership. The routes fail if they duplicate
base typography/composition rules or let Design claim UI/production proof.

## Revisit when

Repeated routed evidence shows that editorial, packaging, or wayfinding has a
stable independent signal and specialist outcome gain, or that one medium leaf
cannot remain coherent without duplicating a domain curriculum.
