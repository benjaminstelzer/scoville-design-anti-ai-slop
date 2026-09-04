# W-004 Design routing benchmark provenance

Frozen: 2026-09-02 before SkillOpt candidate generation.

- Scope: deterministic module selection, direct reads, read order, forbidden
  reads, shell-call ceiling, and exact response shape.
- Target and optimizer: `gpt-5.6-sol`, `xhigh`.
- Train: ten self-authored single-domain routing probes.
- Validation: eight self-authored specialist and mixed-domain probes, not used
  as item-specific optimizer examples.
- Test / `valid_unseen`: four self-authored cross-domain artifact problems,
  sealed before training and unavailable to the open-split loader until the
  final SkillOpt test stage.
- Source groups: prompts were authored for this benchmark and contain no copied
  third-party wording or comparison assets. Single-domain Train, mixed open
  Validation, and cross-medium Test families are disjoint by scenario and ID.
- External comparison pairs: none. They remain eligible only for a separately
  receipted local Train ablation and are not needed for this routing objective.
- Excluded objectives: aesthetic quality, visual preference, general design
  competence, and source authority are not machine-scored here.
- Independent check: the sealed-holdout custodian must confirm exact and
  conceptual near-duplicate absence without revealing holdout content before
  optimizer proposals begin.

