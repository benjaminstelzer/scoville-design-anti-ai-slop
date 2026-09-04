---
format_version: 1
id: PLAN-0004
status: completed
created: 2026-09-04
updated: 2026-09-04
---

# Align advisory resource budgets

## Goal

Apply ADR-0032 to the current Skill package and validator so resource estimates
guide work without excluding required experts or automatically failing quality.
Resolve verified package-clarity issues from the user's independent Fable review.

## Non-goals

Do not alter frozen snapshots or results; weaken authorization or structural
checks; change design rules; rerun model evaluations; install or publish.

## Work items

### W-001 Make resource and expert-count estimates advisory

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0032]
Outcome: Current runtime instructions and package checks agree that resource and expert-count estimates are guidance rather than hard gates.
Acceptance: Core and README no longer impose fixed resource or four-expert caps; registry policy explicitly covers all resource estimates; focused tests prove advisory overruns retain metrics without errors while structural errors and historical hard modes remain intact; current package validation passes; frozen evidence and prior review copy remain unchanged.
Steps:
1. Inspect the existing budget consumers and preserve the prior source for comparison.
2. Align runtime guidance and registry policy with the accepted decision.
3. Update the validator and focused tests without weakening non-budget checks.
4. Verify the current package and record the scope and evidence limits.
Evidence: [21 package tests passed including advisory overruns and more than four experts with historical hard modes preserved, Current package VALID with 17 advisory warnings and unchanged structural checks, Core and README remove fixed resource and expert-count caps; modules.yaml explicitly selects advisory policy, Frozen Core and both final ledgers retain their recorded hashes; prior Fable input matches the before-change copy]

### W-002 Resolve verified independent package-review findings

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: The standalone package explains its optional owners and metadata and exposes unambiguous routing and evidence boundaries without adding fixed resource caps.
Acceptance: Each Fable finding has a source-checked disposition; verified issues receive the smallest correction; expert ownership and distinct evidence meanings remain preserved; package and affected checks pass; unsupported estimates are not adopted as facts; historical evidence remains unchanged and no model-quality improvement is claimed without a behavioral test.
Steps:
1. Verify findings against the current package and its consumers.
2. Clarify only the supported runtime and metadata ambiguities.
3. Run affected deterministic checks and inspect the complete scoped diff.
Evidence: [docs/evaluation/fable-package-review-corrections.md records all review findings and source-checked dispositions, Final package VALID with 33 advisory warnings; index and 50 route fixtures and Design/UI boundary and Skill Creator passed, Runtime diff changes only SKILL.md and modules.yaml and source-index.md; all 28 expert bodies remain unchanged, Complete scoped source and test diff inspected; no model-quality claim or new model run or installation or publication]
