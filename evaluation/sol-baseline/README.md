# SOL application baseline

This open benchmark profiles the frozen `gpt-5.6-sol` `xhigh` target before
expert-module authoring. It is not the sealed holdout and provides no public
qualification by itself.

Arms:

- `no-skill`: minimal neutral control;
- `core-only`: application-first Core without specialists;
- `generic-checklist`: conventional token-comparison control.

Run each open split under a unique run ID for each repetition. Never use the
benchmark's open `test` row as `valid_unseen` or claim it was implementation-
unseen. Visual artifact fields require extraction, rendering, blind identity,
and qualified human review outside the deterministic scorer.

Deterministic scoring covers only output shape, known seeded defects,
preservation decisions, and evidence honesty. It does not score beauty,
professional polish, originality, or style quality.
