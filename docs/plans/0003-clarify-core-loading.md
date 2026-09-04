---
format_version: 1
id: PLAN-0003
status: completed
created: 2026-09-03
updated: 2026-09-04
---

# Clarify Core loading

## Goal

After PLAN-0002 closes, make the narrowly authorized Core clarification in the
successor Skill and verify only the affected loading behavior.

## Non-goals

Do not mutate frozen v9 snapshots or original results, change design rules or
Gold, repeat the full holdout, waive unrelated failures, or publish, install,
commit, push, tag or release.

## Work items

### W-001 Clarify the entrypoint and verify affected loading cases

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0054]
Outcome: The successor Skill identifies SKILL.md as its Core and the targeted regression establishes whether invented Core reads recur.
Acceptance: PLAN-0002 and its original evidence are preserved before the successor edit; the diff only clarifies Core identity and exact linked package reads; relevant structural checks pass; the seven same-mechanism affected loading cases are assessed with original traces retained and test differences declared; successful and failed loading outcomes are reported without a new full-holdout or universal-quality claim; no publication installation commit push tag or release occurs.
Steps:
1. Complete the frozen execution and separate technical adjudication in PLAN-0002.
2. Add the narrow entrypoint clarification without changing design rules or reference contents.
3. Run focused structural checks and the bounded affected-case loading regression.
4. Record the successor diff and observed results with their limits.
Evidence: [PLAN-0002 completed with original and adjudicated ledgers retained before successor work, original SKILL.md remains in snapshot-set-v9/design with SHA256 76CD2F7F86B0FF5494F090EA1C1911EED158D4AB5B7109F7BDD121D95B71B206, successor SKILL.md A341CFDF23529180D72A92D9CD98144ECC44C4686866EB82E1174D2D3E67189C changes only the existing post-index loading sentence, Skill Creator and pinned package validators pass with Core 1468 tokens and unchanged advisory warnings after replacing the initial over-budget paragraph, docs/evaluation/adr0054-core-loading-regression.md records seven reviewed loading passes across five distinct prompts with zero retries and unchanged original results, Four automatic flags were verified as valid UI reads with full-body evidence; original observer flags remain retained, Final preservation receipt verifies 302 original files and seven capture chains with no active provider process, No new overall qualification claim or publication installation commit push tag or release]
