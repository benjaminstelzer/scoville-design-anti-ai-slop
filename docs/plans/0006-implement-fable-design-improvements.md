---
format_version: 1
id: PLAN-0006
status: active
created: 2026-09-04
updated: 2026-09-04
current_item: W-006
---

# Implement Fable design improvements

## Goal

Deliver the Fable-proposed design successor with concrete subject-specific
craft guidance and simpler proportionate operation, preserving authority and
evidence integrity. The complete scope, owner mapping, adaptations and tests
are specified in docs/evaluation/fable-implementation-contract.md; the unaltered
proposal is docs/evaluation/fable-design-improvement-proposal.md. Fable accepted
the plan in session 7d03e896-c898-42a4-abee-b39d759bde77. The user's subsequent
"Setzte den Plan so um" authorises execution beginning with W-001.

The subsequent explicit publication request adds W-006 for Design and UI under
ADR-0058. W-004's remaining evaluation lanes are not release pass claims.

## Non-goals

No implementation during plan preparation; no implicit activation, installation,
commit, push, tag, release or publication; no new full 150-job holdout; no edits
to frozen packages, ledgers, results, evaluator gold or historical Decisions;
no fixed token, context or expert-count limit; no blanket pattern bans or
automatic human-approval claims. Do not treat plan approval as empirical proof.

## Work items

### W-001 Deliver the coherent compact runtime and new modules

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0055, ADR-0032]
Outcome: The compact three-operation Core and two complete new modules work through a coherent successor-v2 registry and tooling while the existing craft modules retain their established guidance.
Acceptance: G01-G02 and R01-R09 have implemented or adapted-with-reason dispositions; no required item is deferred; the 30-module registry and generated direct index agree; solo and partner handoffs retain their records; source headers and evidence semantics are defined before validation; new-schema tests and historical-schema non-regression pass; the installed derivative differs only by the documented comment transform; no fixed resource gate or lost domain constraint is introduced.
Steps:
1. Capture the current source manifest and approved plan; inventory active consumers of modes and status and module IDs; preserve all unrelated user work and historical schemas.
2. Define source-header conventions and local-synthesis attribution plus evidence-field semantics; provision the required source-index entries before any new module is submitted to package validation.
3. Implement the complete dated Generic Signatures module and Coordination module plus the concise Core; preserve the minimal solo phase record and conditionally expanded communication fields in their named owners.
4. Coordinate draft status and successor-v2 registry with schema-dispatched validators and tests; preserve old vocabulary and counts in historical schema paths instead of relaxing them globally.
5. Update the index generator and installable-package build path; retain authoring markers and exact source hash plus a deterministic comment-stripped derivative hash.
6. Establish the intermediate milestone with positive and negative and mixed route checks for both new modules before applying broad craft-content additions.
7. Apply scoped metadata and language hygiene and shared-proof deduplication; update current documentation and load examples without renumbering retained IDs or rewriting evidence history.
8. Run package and index and route and Design/UI boundary and Skill Creator checks plus affected unit tests; inspect the complete source-to-runtime diff and resolve introduced failures.
Evidence: [docs/evaluation/plan-0006-implementation.md W-001 dispositions and proof-floor inventory, 27 unit tests and 59 route fixtures passed, docs/evaluation/plan-0006-w001-build.json source and 34-file runtime verified]

### W-002 Deliver the subject-specific craft additions

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0055]
Outcome: The twelve existing craft owners receive the concrete positive guidance and diagnostics G03-G14 without duplicating Generic ownership or forcing redesign of valid work.
Acceptance: Every G03-G14 entry is implemented or adapted-with-reason with exact owner and source/synthesis attribution; no required addition is deferred; the complete signature/cause/legitimate-case/counter-move mechanism survives; declared handoff and protected geometry and task scope remain intact; affected package and route checks pass.
Steps:
1. Resolve each proposal locator against current headings and map each craft addition to the source-header convention established in W-001.
2. Implement G03-G14 in their craft owners using Fable's insertion texts as the basis; retain legitimate defaults and subject-bound causal alternatives.
3. Check every changed craft owner for duplicated shared catalog content and lost scope or authority floors; verify direct routing and source-ID resolution.
4. Record each disposition and run the affected deterministic checks without claiming visual improvement before W-004.
Evidence: [docs/evaluation/plan-0006-implementation.md W-002 complete G03-G14 dispositions, Current 30-module package and 60 interpreted route fixtures passed]

### W-003 Verify the changed provenance and disputed dates

Status: done
Depends on: [W-001, W-002]
Blocked by: []
Decisions: [ADR-0055]
Outcome: New and changed guidance has accurate provenance and the specific disputed source dates are resolved or explicitly bounded without invented inspections.
Acceptance: R10 and G01-G14 attribution are verified against available receipts; new source IDs or local-synthesis records support their bounded claims; material unresolved currentness is checked with primary sources or withheld; historical freeze dates remain historical; affected source and package checks pass.
Steps:
1. Audit the initial source map and local-synthesis entries established before W-001 validation, including the signature catalog date and recheck trigger.
2. Compare the disputed standard and paper dates with named historical research receipts; obtain primary-source verification where truth or currentness remains material.
3. Record exact version and inspection depth; qualify or remove unsupported attribution rather than inventing passage support or approval.
4. Correct only source-dependent current claims and rerun affected checks; preserve unresolved external acceptance requirements as explicit limits.
Evidence: [docs/evaluation/plan-0006-source-audit.md primary dates and inspection limits, Source-header and registry and rule-map validation passed]

### W-004 Demonstrate focused behavior and hand off the local candidate

Status: paused
Depends on: [W-001, W-002, W-003]
Blocked by: []
Decisions: [ADR-0055, ADR-0032]
Outcome: The final local candidate has observed evidence for the changed design and routing behavior with failures and limits retained, without repeating the full holdout or claiming general superiority.
Acceptance: All seven targeted case families and host activation checks execute with real artifacts and applicable renders; read-only critique and named-style routing pass; content and authorization invariants hold; genuine design improvements and legitimate conventional cases are separately judged; no mandatory implementation is deferred; Fable reviews the final package and evidence; observed case references are recorded without overstating pass status; a hash-verified local candidate and exact limits are handed off without installing or publishing.
Steps:
1. Freeze the focused case inputs and comparison criteria before outcomes; use the retained pre-change package and final candidate as distinct arms with equal model and tool conditions.
2. Execute small repair and generic named-style design and quiet utility and motion/data and mixed-domain and unavailable-proof and read-only generic critique cases; retain prompts and actual reads and source artifacts and renders and failure records.
3. Exercise genuine host activation separately from interpreted-signal fixtures; if unavailable, mark host activation unverified rather than simulating a pass or silently changing invocation policy.
4. Ask Fable to judge the candidate against its proposals and observed case evidence; separate an architectural review from blind artifact comparison and preserve disagreement.
5. Resolve introduced in-scope failures and repeat only affected cases; do not retry an unfavorable valid outcome until it passes or turn a runtime budget into acceptance criteria.
6. Populate module evidence lists only with actually executed case receipts; retain tested artifact hashes and all outcomes, and verify any subsequent metadata-only annotation separately.
7. Validate final source and derivative manifests and current aggregate checks once; disclose every deferral or unverified host lane and do not mark required acceptance done while it remains unobserved; retain historical hashes and deliver only a local completion record and candidate path.
Evidence: [docs/evaluation/plan-0006-focused-freeze.json inputs and tested manifests, docs/evaluation/plan-0006-sol-interim-reviews.md independent runtime and blind artifact reviews, ADR-0056 records the user-selected interim reviewer contingency, ADR-0057 records the explicit matched SOL execution choice, docs/evaluation/plan-0006-execution-progress.md all families and justified extensions executed and independently reviewed, docs/evaluation/plan-0006-case-receipts.json twenty executed sessions with original defects and correction stages retained, docs/evaluation/plan-0006-record-scope-build.json five R02 clarification clauses with independent fidelity review and two targeted retests, docs/evaluation/plan-0006-final-local-build.json hash-verified 34-file local derivative with evidence-only annotation, docs/evaluation/plan-0006-final-checks.json final local deterministic checks, docs/evaluation/plan-0006-final-audit.json SOL metadata and claim audit with capture defect resolved]
Next action: Resume the still-unverified genuine host H1-H5 checks and the original proposal-session final package/evidence review when selected. W-005 does not substitute for either lane; separately authorised publication is owned by W-006.

### W-005 Resolve the independent installed-package review findings

Status: done
Depends on: [W-001, W-002, W-003]
Blocked by: []
Decisions: [ADR-0055, ADR-0032]
Outcome: The installed-form package resolves the substantiated findings from Fable session 06c61365-6b5d-4862-8be7-5e0ffc346b62 and receives a same-session follow-up review with disagreements and limits retained.
Acceptance: Each of the seven finding categories has an implemented or evidence-backed adapted disposition; external receipts and metadata are not runtime dependencies; automatic discovery stays enabled with precise scope; no resource cap or unsupported efficacy claim is introduced; affected package and routing and boundary checks pass; actual token measurements qualify the estimated budget concern; a new hash-verified installed-form package is reviewed read-only in the same Fable session without project history; the original package and review remain unchanged; no installation or publication occurs.
Steps:
1. Preserve the five affected source files and the original review; verify each finding against its canonical owner and measured token counts.
2. Clarify external receipt references and the non-routed metadata role; identify the generated index and existing repository drift check without making authoring tools runtime dependencies.
3. Define optional partner names by responsibility and remove the out-of-context Greenfield statement; retain standalone operation and ownership constraints.
4. Mark the generic-signature catalogue explicitly as reviewer heuristics and correct the source-class conjunction and absent developer-record wording and Cartography route label.
5. Narrow discovery to requested or unresolved visual judgment while preserving automatic selection; retain advisory resource estimates and document measurement semantics rather than inventing hard limits.
6. Run only affected deterministic checks and token measurement; build a new isolated installed-form package and preserve both manifests and exact changes.
7. Resume Fable session 06c61365-6b5d-4862-8be7-5e0ffc346b62 for a read-only result review; resolve only substantiated in-scope residual findings and retain the final report and actual read coverage before returning selection to paused W-004.
Evidence: [docs/evaluation/plan-0006-installed-review-fixes.md seven finding dispositions and complete same-session review outcome, Package and index and 60 route fixtures and Design/UI boundary and Skill Creator checks passed, Four focused boundary guard tests passed including three negative mutations, Final affected package checks passed with fifteen advisory target-only notices, Final 34-file runtime B8874386F46DA1319FA75502887152D247318BEE1B50D4F64C9E5D84B9986F9C hash-verified, Fable accepted the two residual corrections with no remaining actionable problems, Actual reads and unchanged-file hashes verified without installation or publication]

### W-006 Publish the Design and UI packages

Status: in_progress
Depends on: [W-001, W-002, W-003, W-005]
Blocked by: []
Decisions: [ADR-0058]
Outcome: Design is installed for Codex and Claude and both Design and UI have verified GitHub releases with consistent public documentation and family membership.
Acceptance: The reviewed Design runtime matches both local installations and the distributed package; current structural and affected boundary checks pass; both README and changelog files follow the release Skill; each release has one annotated version tag and one stable GitHub Release on its verified commit; family and profile audits pass; unverified host and empirical lanes remain explicit.
Steps:
1. Verify exact source and remote state and preserve the profile WordPress entry by the authorised fast-forward.
2. Correct publication copy and canonical family membership; package the reviewed runtime without development files.
3. Run release checks and inspect the intended public files and claims before committing.
4. Publish the two releases and narrow family updates; verify GitHub state before retiring the previous UI release and tag.
5. Record observed publication evidence without changing historical evaluation outcomes.
Evidence: [Both local Design installations contain exactly 34 byte-identical reviewed runtime files, Profile fast-forward ad21b3322fc66ad247158c75d582826c10fe6c34 preserved the WordPress entry, docs/release-validation.md records 32 unit tests and 60 interpreted routing cases and package checks, Eight-member family and exact staged package bytes and local README links verified]
Next action: Commit the prepared candidates and publish both releases with exact remote and family audits before retiring the previous UI release.
