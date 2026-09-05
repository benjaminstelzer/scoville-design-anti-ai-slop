---
format_version: 1
id: ADR-0011
status: accepted
created: 2026-09-01
accepted: 2026-09-01
scope: product/knowledge/evaluation
---

# Prioritize applied design and measure only SOL

## Decision

Order the Skill's product priorities as:

1. generate an original, professional design from brief, content, and medium;
2. distinguish effective, mediocre, defective, clichéd, and AI-slop design;
3. improve an artifact through localized causes, targeted changes, rendering,
   and renewed judgment;
4. apply recognizable style DNA professionally without assembling a cliché
   checklist;
5. load theory and history only when they improve a decision, style execution,
   critique, or repair.

Treat strong-model prior knowledge as the baseline. Package only the smallest
tested intervention class: `focus`, `correction`, `teaching`, or
`external-verification`. Measure, optimize with SkillOpt, and qualify behavior
only on the exact frozen GPT-5.6 SOL configuration. Fable 5.1 may perform the
explicitly requested read-only Plan/gap review, but it is not a behavior-test
arm. Opus 5 is not invoked. Do not claim Fable or Opus parity from assumption.

## Problem

A study-sized design corpus can consume context without improving design. A
strong base model already contains broad design vocabulary and history, while
its actual weaknesses appear in application, discrimination, generic output,
repair, and evidence-calibrated judgment. Multi-model qualification would add
substantial cost that the user explicitly rejected.

## Drivers

- The user explicitly confirmed the five application-first priorities.
- The user explicitly directed measurement only for SOL.
- Token cost must track observable behavioral benefit, not curriculum length.
- Design history is useful support but not the primary product outcome.
- Model training knowledge is opaque and cannot be assumed current or reliable
  merely because the model can discuss a topic.

## Considered alternatives

- Ship a compressed graphic-design textbook. This duplicates model knowledge
  and risks better recitation without better artifacts.
- Measure SOL, Fable, and Opus. This would support broader claims but exceeds
  the authorized evaluation cost.
- Omit sources because the model already knows the field. This would make
  corrections, volatile facts, production rules, and attribution unauditable.
- Optimize only routing and prose. This would miss the visual application and
  repair goal.

## Consequences

- A module is admitted because it changes SOL behavior or supplies a required
  source/current-fact boundary, not because the topic belongs in a degree.
- No-Skill, Core-only, generic-checklist, selected-module, full-bundle,
  wrong-expert, and ablation controls are required.
- Visual generation and repair remain human-reviewed at intended context;
  SkillOpt does not become an aesthetic oracle.
- Fable's Plan critique is reported separately from product evidence.
- Public qualification names SOL, its effort/configuration, host, hashes,
  cases, and reviewer basis. Other models remain untested.

## Confirmation

Every shipped module item resolves to a source or observed SOL failure and one
of the four intervention classes. Removing or shortening it is tested. The
qualification suite measures generation, discrimination, repair, style
execution, routing, and evidence separately. No public statement implies that
Fable 5.1 or Opus 5 was tested.

## Revisit when

The supported SOL version changes materially, a user authorizes multi-model
qualification, or repeated evidence shows that a different intervention class
or broader knowledge payload improves unseen design outcomes.
