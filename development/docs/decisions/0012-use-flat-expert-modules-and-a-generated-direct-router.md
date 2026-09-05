---
format_version: 1
id: ADR-0012
status: accepted
created: 2026-09-01
accepted: 2026-09-01
scope: architecture/progressive-disclosure
---

# Use flat expert modules and a generated direct router

## Decision

Ship one standalone Scoville Design Skill with:

- a compact Core that owns the application loop, modes, synthesis, ownership,
  rule strength, exceptions, provenance, and evidence limits;
- a canonical authoring-time `modules.yaml` registry;
- a compact direct module index generated into `SKILL.md` from that registry;
- flat, package-local expert modules selected as a set rather than by a
  first-match route;
- no expert-to-expert reference chains and no runtime Skill dependency;
- validators that fail on duplicate ownership, cycles, orphan files, missing
  sources, budget violations, or generated-index drift.

The direct generated index preserves one-level Skill-to-reference navigation
while keeping `modules.yaml` the only hand-edited routing source. Extensions
add namespaced leaf modules through the same build-time contract; they do not
mutate the Core, override ownership silently, or auto-discover another
installed Skill.

## Problem

One monolithic Skill wastes context, but dozens of top-level Skills or nested
reference chains create discovery, dependency, routing, and maintenance
failure. A separate runtime manifest is compact but would add another
reference hop and can drift from direct Skill links.

## Drivers

- Agent Skills supports progressive loading of a Core and on-demand resources.
- Current authoring guidance recommends direct, shallow references.
- A design task often needs multiple expert concerns at once.
- Every Scoville Skill must remain independently usable.
- The package must be expandable without making all future knowledge active.
- Selective-loading claims require observable file-read traces and outcome
  ablations, not self-report.

## Considered alternatives

- Put all knowledge in `SKILL.md`. This is simple but violates the token and
  relevance goals.
- Make every expert a separate installed Skill. This expands the top-level
  catalog and makes common design work depend on coordinated activation.
- Route from one reference into another. This creates hidden transitive reads
  and incomplete-load risk.
- Read `modules.yaml` at runtime and then follow its paths. This keeps one
  source but adds a nested navigation hop. The generated direct index avoids
  that tradeoff.

## Consequences

- Operation modes (`generate`, `critique`, `repair`, `style-direction`) stay
  orthogonal to expert domains rather than multiplying route combinations.
- Every expert module must contain inputs/diagnostics, generation actions,
  critique checks, repair moves, style-direction effects where applicable,
  rule strength/exceptions, verification, and source IDs.
- Style knowledge begins as an application compiler plus SOL-proven patches;
  broad history/atlas content remains optional until tests justify loading it.
- The runtime package remains one Skill. Authoring extensions are package
  contributions, not runtime dependencies.
- A smaller selected payload is reportable; total token, money, or latency
  savings are not claimed without end-to-end evidence.

## Confirmation

Static validation proves registry/index agreement, one-level direct paths,
unique ownership, acyclic depth-one dependencies, source resolution, and token
budgets. Instrumented cases prove all required expert files and no forbidden
expert files were read before output. Selected-module behavior is non-inferior
to the full bundle on qualified tasks, and expected-module ablation measurably
weakens its target dimension.

## Revisit when

Host-native module or Skill dependency standards become portable, read traces
show the generated index is unnecessary, or extension volume makes a single
package registry unmaintainable.
