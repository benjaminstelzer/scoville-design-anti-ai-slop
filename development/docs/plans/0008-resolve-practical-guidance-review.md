---
format_version: 1
id: PLAN-0008
status: completed
created: 2026-09-05
updated: 2026-09-05
---

# Resolve practical guidance implementation review

## Goal

Implement the user's 2026-09-05 request to remove size guidelines completely and fix the other confirmed findings in review 0024. Preserve the original Plan 7 evaluation while adding the missing typography comparison, line/area cartography assistance and corrected Motion derivative. The instruction authorizes this follow-up plan and direct execution.

## Non-goals

No installation, commit, publication, historical outcome replacement, unchanged-task outcome retries or model-superiority claim. PLAN-0006 remains paused in its draft plan. Historical Plan 7 records remain evidence of the reviewed implementation.

## Work items

### W-001 Remove operative package size guidelines

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0059]
Outcome: Runtime metadata and current authoring tools and guidance impose no package or module size guideline.
Acceptance: Remove targets, ceilings, leaf-count allowances and size warnings; retain useful descriptive measurement and structural failures; adapted tests, package, index, route and boundary checks pass; historical records are preserved.
Steps:
1. Inspect operative policy consumers and current documentation.
2. Remove size policy fields and validation branches, adjusting meaningful regression tests.
3. Verify structural controls and historical preservation and record the result.
Evidence: [26 unit tests passed including large-content and all-module acceptance with structural negative cases, package validator zero warnings, generated index current, 60 route cases and Design UI boundary passed, current README distinguishes historical protocols from current policy, tokenization removed from structural validation]

### W-002 Complete the missing practical guidance evidence

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0059]
Outcome: Coupled typography settings and point, line and area label distinctions have bounded practical evidence; the Motion derivative has consistent status text.
Acceptance: Freeze separate PG-02S paired baseline/candidate and PG-08S candidate/control tasks before execution; preserve original trials; inspect exact content, controlled typography size/measure/leading comparisons and authoritative line/area geometry at two sizes; cite inspected primary cartographic sources; render and verify corrected Waiting, Ready, interruption and reduced-motion states; report PG-06 usage as an observed asymmetry without inferring configured effort; validate and build the final local package and report actual limitations.
Steps:
1. Freeze new supplementary tasks and source exposure without modifying the original protocol.
2. Complete source-backed cartography instructions and produce the separate Motion derivative.
3. Execute the new tasks, inspect artifacts and runtime states, then record bounded findings and final checks.
Evidence: [docs/evaluation/plan-0008-implementation.md observed findings and limits, docs/evaluation/plan-0008-receipts.json three new calls and six inspected supplementary artifacts with exact content geometry and actual Georgia, six consistent Motion state checks on a separate coordinator derivative, original 28 trials and 54 artifacts unchanged, source-backed line and area guidance, docs/evaluation/plan-0008-final-build.json verified 35-file runtime, original PLAN-0006 W-004 preserved]
