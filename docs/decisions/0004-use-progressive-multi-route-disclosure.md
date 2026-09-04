---
format_version: 1
id: ADR-0004
status: superseded
created: 2026-09-01
accepted: 2026-09-01
scope: skill/context
superseded_by: ADR-0008
---

# Use progressive multi-route disclosure

## Decision

Keep `SKILL.md` limited to shared ownership, mode, authority, exception,
evidence, and routing rules. Put substantial domain knowledge in focused,
one-level references and load only the references that can change the current
task. A task may load several applicable references, but there is no routine
load-all path, no deep reference chain, and no implicit sibling-Skill load.
Source and license records remain available for maintenance and attribution but
do not enter ordinary task context unless provenance or licensing is relevant.

## Problem

An allround design Skill needs broad knowledge, but loading typography, colour,
composition, branding, UI, motion, print, accessibility, production, critique,
and provenance on every request would waste context and make relevant rules
harder to follow.

## Drivers

- The user's explicit requirement to avoid unnecessary token use and allow
  several relevant knowledge areas in the same task.
- Agent Skills progressive-disclosure conventions.
- Independent standalone operation without hidden dependencies.
- SkillOpt and routing tests must be able to observe missing and unnecessary
  reads separately.

## Considered alternatives

- Put all knowledge in one Core. This is simple but expensive and noisy.
- Create one Skill per design subdomain. This increases discovery collisions,
  cross-Skill coupling, and repeated shared rules.
- Load exactly one domain reference. This fails genuinely mixed work such as
  typography plus composition plus print validation.

## Consequences

- The Core needs a precise multi-select reference router.
- Shared principles remain in one canonical owner and are not duplicated among
  references.
- Evaluation records observed reference reads and treats both missing required
  knowledge and unrelated loading as failures.
- Reference granularity must be justified by distinct triggers, not by chapter
  aesthetics.
- Runtime context cost is measured, not inferred from file count alone.

## Confirmation

Representative single- and multi-domain tasks load the predeclared minimum
reference set, produce complete decisions, and avoid unrelated references.
No-Skill, solo, and composed traces show no hidden Design-to-UI or UI-to-Design
dependency. SkillOpt proposals do not improve token cost by weakening content
or routing correctness.

## Revisit when

Observed tasks consistently require the same reference combination, route
selection is less reliable than a smaller Core, or measured context savings do
not justify the routing complexity.
