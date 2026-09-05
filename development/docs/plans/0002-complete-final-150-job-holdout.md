---
format_version: 1
id: PLAN-0002
status: completed
created: 2026-09-03
updated: 2026-09-04
---

# Complete the final 150-job holdout

## Goal

Execute a fresh arm-blind 150-job holdout against the exact final ADR-0048
Scoville Design package and retained Scoville UI package, then record bounded
qualification evidence for every registered job. After the frozen run closes,
perform the user's one separate diagnostic repetition of the missing-response
case without replacing its original holdout result.

## Non-goals

Do not reuse exposed v7 cases, revive partial v8, edit frozen Gold or package
content after outcomes, outcome-retry a frozen holdout job, hide failed jobs,
or publish, install, commit, push, tag, or release either Skill.

## Work items

### W-001 Freeze and validate the fresh full-holdout suite

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0037, ADR-0043, ADR-0044, ADR-0048, ADR-0049]
Outcome: Qualification-v9 is a fresh executable zero-call suite bound to the final package and ready for separately authenticated arm-blind execution.
Acceptance: Exact final Design manifest F6A076D5C2272F4FAD23FB6C236523287D19E0C7EACF8484D5AD7993E0EAAD6F and UI manifest FD255A274E2D92C6DDA14CAD2A85FF0E7702960CEE6B2D3B9F20E04A78A78875 are copied and verified; 30 fresh source-cleared cases create exactly 150 registered jobs with frozen Gold prompts fixtures arm-balanced schedule canaries call slots rendering rules and authenticated-read scoring; encrypted custody archives opaque manifests and case-private staging expose no sealed plaintext to the parent; runner authorization integrity resume terminal-response no-outcome-retry and complete-run semantics pass adversarial model-free tests; exact Terra High pinned CLI host sandbox and network conditions are recorded; provider calls runtime jobs and operational unseals remain zero until a signed execution receipt binds the complete readiness state.
Steps:
1. Derive qualification-v9 only from validated v7 infrastructure and the final ADR-0048 package while excluding all prior private cases and outcomes.
2. Have the existing independent custodian author and seal 30 fresh source-cleared cases with frozen Gold and an arm-balanced 150-job schedule.
3. Bind exact package tool prompt renderer scorer schedule custody and authorization hashes in the public runner manifest.
4. Run the complete zero-call unit adversarial security resume and readiness gates and record their receipts.
5. Create one signed execution authorization that permits the complete 150-job run but no publication or package mutation.
Evidence: [custody receipt A74C37CDF7BE761235B8812E995ACD594C368AC032273597B28A60112965152D, exact Design file F6A076D5C2272F4FAD23FB6C236523287D19E0C7EACF8484D5AD7993E0EAAD6F and UI package FD255A274E2D92C6DDA14CAD2A85FF0E7702960CEE6B2D3B9F20E04A78A78875 verified in snapshot-set-v9, 50 of 50 zero-call tests bind runner 786C9D63CD8993B57D8BF46B3382D93BB7C8899B8843F26A5CEB42315D1AEAC4 and policy 55786B59DB36571BBD6E61A90177BD809E843C9881D3750BDAA1F9C58EAEC028, signed authorization receipt 449B5709595145CE0F9DB921E0DE60BA8EB8D5A22BF11CBFC5EA3658B7302E21 verifies nine current bindings]

### W-002 Execute all 150 jobs and record bounded qualification

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0037, ADR-0043, ADR-0044, ADR-0048, ADR-0049]
Outcome: Every qualification-v9 job reaches a preserved terminal execution result and the final ledger reports exact package behavior without inflating failures or reviewer evidence.
Acceptance: All 150 registered jobs execute once in the frozen arm-blind order under exact Terra High and the bound host tools; every model response is terminal for its call slot and no job is outcome-retried; classified product failures do not stop later distinct jobs while authorization custody integrity benchmark or pre-response infrastructure failures fail closed; each job preserves exact arm case repeat route reads terminal alignment artifact source render scorer usage timing and receipt hashes; the final report reconciles registered started terminal passed failed quarantined and unexecuted counts to 150 plus provider calls retries and cumulative usage; representative visual comparisons use only preregistered reviewer evidence and report disagreement or missing review honestly; claims name exact model host package cases reviewer basis and limitations and never convert incomplete or failed lanes into qualification credit; final package route index Design UI Skill Creator native Plan and workspace checks pass without package mutation; no publication installation commit push tag or release occurs.
Steps:
1. Execute the preregistered canary jobs in arm-balanced order and inspect integrity plus receipts before opening the remaining schedule.
2. Continue one immutable shard at a time until every registered job has a terminal result or a material integrity failure requires a durable pause.
3. Reconcile job call render route artifact reviewer and usage ledgers against the frozen schedule after each shard.
4. Produce the final full-holdout ledger and run unchanged-package deterministic validation.
Evidence: [final ledger C389ADE647EC48A72AAC7FC48628727A2CA7CE8A632F9EA085B83720A9091C26 reconciles 150 jobs with 149 regular terminal results and one unresolved execution failure, 189 attempts include 150 initial and 39 repair attempts with zero transport retries and no open jobs or locks, final validation 0E72774A48EE1C85145384C361E52EA5DBEF00B9F0BA5860288A6DD671625E60 verifies 54 frozen bindings and 150 chains plus 111 render chains and 9 passing accounting tests, unchanged-package checks passed in receipt 676FCA7228809949A5A45699040EEF7B8DAEF37F46FA9FFA5B839D8FAF7CBB85 without frozen package mutation, audit 245C1D52D46F788133F2F0BF70841BDD495F79593BF3750C7B8E4A3BA4FA5B94 preserves 98 automatic passes plus 33 failures and 19 unavailable results without full qualification credit, ADR-0050 continuation preserved all original evidence and original transport 171 remains unresolved for separate ADR-0052 adjudication]

### W-003 Adjudicate execution and parser failures separately

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0052, ADR-0053]
Outcome: One separate execution replay and model-free recovery of proven parser failures supply substantively assessed user-adjudicated Skill results without rewriting original measurements.
Acceptance: Original transport 171 and all frozen evidence remain unchanged; one authorized replay call at most uses pinned tools and comparable cloned inputs with exact hashes and declared path differences; proven Unicode-parser failures alone are recovered from existing complete responses with zero model calls using a tested value-preserving LF adapter; unchanged-Gold substantive checks and independent rendered review establish fitting results; those results count as valid passes in separate user-adjudicated acceptance fields without treating original technical failures as negative Skill results; genuine Skill failures remain visible; no retry or repair loop and no publication or installation occurs.
Steps:
1. Freeze a separate narrow diagnostic authorization and input manifest after the original holdout closes.
2. Run the single diagnostic call in an isolated cloned workspace and preserve complete output and usage.
3. Recover only proven parser failures from existing responses with the tested diagnostic LF adapter and no model calls.
4. Assess requirements and rendered artifacts and record user-adjudicated results separately from preserved original measurements.
Evidence: [adjudication ledger 4FA3F33F932F9BD5260F408DBB89EE73703EA50A1B62E4BC2C9ADC8E7679E33D records one all-dimension pass and eleven failures or unresolved outcomes without overwriting originals, validation 547E92CBF5933F882B7B554CE2E990D565E36C822A70D03EB02805A7A7F27496 verifies twelve assessment and review chains plus frozen bindings and original job chains, one separate provider attempt completed with zero retries or repairs and eleven existing responses were recovered with zero model calls, twelve renders received independent Root review with five visual passes and seven failures while private substantive review retained three indeterminate source-fidelity outcomes, root report docs/evaluation/qualification-v9-final-report.md records original and adjudicated results plus unchanged-package checks and explicit qualification limits, authorization A33CC011375C72EEB090BBDD8E6A8A1E7D22E7A0C289E8465CC51C354EF1BB62 and root release 3A19FAB4D630337FD6A5B3E22063646D8649FF6BE292957D1AA7EED751366528 bound the separate execution]
