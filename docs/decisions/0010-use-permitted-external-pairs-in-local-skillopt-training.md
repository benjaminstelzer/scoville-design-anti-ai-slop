---
format_version: 1
id: ADR-0010
status: accepted
created: 2026-09-01
accepted: 2026-09-01
scope: qualification/external-material
---

# Use permitted external pairs in local SkillOpt training

## Decision

Permit useful third-party before/after, preferred/rejected, and localized
critique pairs in the local SkillOpt `train` split when an external-material
receipt verifies access, model-input, optimization, storage, logging, and
output-handling permission for that exact use. Use only source-authored or
human-authored direction, rating, critique, or preference labels as Gold.
Do not let the proposing or grading model invent its own aesthetic label.

External training artifacts remain under
`Z:\Projekts\AI\scoville-design-eval-local\external-pairs`; no source bytes or
reconstructive output enter either repository or public evidence. Group by
source and task so exact or near-duplicate content cannot enter
`valid_unseen`, the independent holdout, or a comparator lane later counted as
qualification evidence. Ambiguous permission defaults to method/reference
only.

## Problem

The research found valuable labeled comparisons, but the initial evaluation
contract restricted them to external validation. This leaves useful
human/source judgment out of SkillOpt even when local optimization use is
permitted. Conversely, counting a trained pair again as independent evidence
would create leakage.

## Drivers

- The user explicitly requested that the found comparison pairs also inform
  SkillOpt training while staying out of the public GitHub repository.
- Source and professional-human labels are stronger training targets than a
  VLM grading its own aesthetic output.
- Training examples and independent qualification evidence must remain
  disjoint.
- Model input, optimization, and logging can have different permission terms
  from merely viewing a public page.

## Considered alternatives

- Keep every external pair outside SkillOpt. This preserves maximal separation
  but discards useful labeled craft and critique examples.
- Use every locally viewable pair without a receipt. This confuses local
  storage with permission and risks source leakage into logs or public output.
- Use external pairs in Train and Validation. This inflates evidence through
  direct contamination.
- Let a VLM assign aesthetic Gold. This optimizes toward the judge's taste and
  violates the accepted evidence boundary.

## Consequences

- W3C BAD may train only its documented functional repair dimensions; it is not
  a general aesthetic label.
- A. Dawn Journal may train the source's stated alignment/hierarchy lesson,
  not universal beauty.
- TASTE, UICrit, Vibe Design Arena, Apple RLDF, and similar datasets require
  item/source-specific receipts and output controls before use.
- Commercial books and previews remain human learning references unless an
  exact fixture permission exists.
- SkillOpt reports separate original versus external training rows and never
  promotes a candidate solely on memorized source examples.

## Confirmation

Every external Train row resolves to a receipt, source label, local-only path,
and source-group ID. Automated disjointness and perceptual/semantic
near-duplicate checks find no external Train artifact in `valid_unseen`, sealed
holdout, or qualification comparators. Logs and public reports contain no
source bytes or reconstructive output. Ablation results show whether external
pairs changed promotion without being reused as evidence.

## Revisit when

A source changes its terms, optimizer logging cannot be redacted, source labels
prove too subjective or inconsistent, or external examples dominate promotion
without improving original unseen cases.
