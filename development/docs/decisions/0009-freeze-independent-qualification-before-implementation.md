---
format_version: 1
id: ADR-0009
status: accepted
created: 2026-09-01
accepted: 2026-09-01
scope: qualification/evidence
transition_batch: 2f8f411b120257971bedf6a858d451262a7857491826e9b29e4833c7ad439380
transition_batch_members: [ADR-0003, ADR-0006, ADR-0007, ADR-0008, ADR-0009]
---

# Freeze independent qualification before implementation

## Decision

Freeze the final holdout construction contract, opaque split manifest and
hash, route Gold, original-pair preregistration schema, human-review protocol,
comparator parity, thresholds, and claim templates before any Skill package
file is authored. The final holdout content remains unavailable to Skill
authors and SkillOpt; only opaque IDs, hashes, split membership, rubric version,
and custodian enter repository evidence.

SkillOpt may optimize routing, ownership, functional constraints,
source/content fidelity, exception/evidence honesty, and deterministic
production checks. It must not optimize a model- or VLM-scored aesthetic
objective. Visual generation, critique, and repair outcomes are qualified later
through blinded human comparison at intended size and context. Automated visual
checks remain supporting evidence only.

## Problem

The active Plan freezes holdout cases after implementation while later claiming
they were unused by implementation. It also does not prevent SkillOpt from
optimizing against an unreliable aesthetic judge.

## Drivers

- A holdout written after the Skill is implementation-informed even if SkillOpt
  has not seen it.
- Design research documents professional disagreement on visual preference.
- Functional and routing Gold can be deterministic; aesthetic quality cannot.
- Market leadership is a personal ambition, not an acceptance criterion or
  public factual claim.

## Considered alternatives

- Freeze only before SkillOpt. This leaves implementation leakage.
- Use a VLM aesthetic judge during optimization. This can reward judge quirks
  and contradicts the evidence boundary.
- Use one unblinded maintainer opinion. This supports only a stated personal
  preference, not a general improvement claim.
- Publish third-party comparison material as the holdout. This violates the
  local-only and source-clearance requirements.

## Consequences

- An independent custodian must seal the holdout before W-002; implementers and
  SkillOpt cannot inspect or predict its content.
- Original pair Gold records mutation class, expected direction, preregistered
  evidence, validation votes, and date before candidate runs.
- Human review records reviewer count and qualifications, blinding, order
  randomization, repeated-run policy, per-dimension ratings, vote margin,
  disagreement, rationale, and no-decisive-winner handling.
- Comparator Skills run only within their declared scope under equal model,
  host, tool, prompt, context/time budget, and repeat conditions.
- Benchmark defects are quarantined across all arms, independently adjudicated,
  never edited in place after outcomes, and rerun only under a new suite version.

## Confirmation

A dated hash, holdout-internal duplicate check, and custodian receipt precede
the first package file. Cross-split disjointness and near-duplicate checks pass
after Train and `valid_unseen` exist but before optimization. The SkillOpt
grader specification contains no aesthetic objective. A preflight pilot with
at least three blinded independent reviewers covers a functional pair, craft
pair, deliberate exception, and true tradeoff, preserves disagreement, and
validates the report schema before qualification runs. If only one reviewer is
available, the pilot may validate the schema but supports only that named
reviewer's preference claim.

## Revisit when

Independent custody is infeasible, human-review resources support only narrower claims, or a validated
design-quality instrument becomes available.
