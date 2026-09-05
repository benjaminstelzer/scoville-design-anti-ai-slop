# Pre-implementation review reconciliation

Date: 2026-09-01  
Combined outcome: complete; both requested advisers returned independent answers  
Role: internal Plan evidence, not product approval or qualification evidence

## Provider records

| Adviser | Requested configuration | Context/session | Result |
| --- | --- | --- | --- |
| Fable | `claude-fable-5-1`, high | persistent session `bf22e960-f533-4f37-aead-07ae1e5810a8`; customizations disabled; the adapter returned no separate `reported_model` metadata | Revise before implementation |
| SOL | `gpt-5.6-sol`, xhigh | fresh target `/root/plan_review_sol`; no parent turns | Revise before implementation |

The earlier `claude-fable-5` run is treated as a preliminary review because the
user explicitly required the updated Fable 5.1 alias. It is not the Fable
review of record.

## Verified convergence

Both reviewers independently identified the following material defects in the
pre-review contract. Repository inspection confirmed each one:

1. The final holdout was scheduled after implementation while W-005 called it
   implementation-unseen.
2. SkillOpt did not explicitly prohibit optimizing a model/VLM aesthetic score.
3. The Design/UI split lacked an observable activation/applicability signal, a
   rank in UI's owner ladder, and a compact cross-Skill decision handoff.
4. The exception protocol allowed intent to be invented after critique.
5. The reference topology had no numeric context budget or frozen route matrix.
6. Accessibility and evidence floors could disappear behind a missed route.
7. Several mapped professional domains lacked sufficient learning sources for
   specialist claims.
8. Human pairwise review lacked frozen reviewer, blinding, margin,
   disagreement, and claim rules.
9. “Local-only” storage did not itself establish permission for model input,
   evaluation, logging, modification, or evidence publication.
10. The installed package needed attribution independent of the repository
    README.

## Applied reconciliation

- ADR-0003 was revised while still proposed to add external-material use
  classes, default-deny behavior, authoring separation, receipts, a sibling
  local workspace, and bundled attribution.
- ADR-0006 proposes an operational successor to ADR-0001 with concern-level
  ownership, activation/applicability, precedence, handoff, constraint loop,
  and Design-only evidence limits.
- ADR-0007 proposes an operational successor to ADR-0002 with declared versus
  inferred intent, preference and tradeoff semantics, experiment state, numeric
  authority, and comparison triggers.
- ADR-0008 proposes an operational successor to ADR-0004 with a reduced route
  topology, route matrix, three-reference ordinary limit, and `o200k_base`
  ceilings.
- ADR-0009 proposes a pre-implementation independent qualification contract and
  prohibits aesthetic SkillOpt objectives.
- W-007 was inserted before implementation. W-002 now depends on W-007.
- The domain-maturity ledger separates mapped, source-grounded,
  behavior-tested, production-tested, and human-validated capability.
- Targeted sources were added for branding, data visualization, scripts,
  motion, editorial/multi-page work, photography, wayfinding, packaging, and
  colour technology. Thin specialist domains remain bounded rather than filled
  with invented rules.
- `docs/evaluation/preimplementation-contract.md` captures the route, context,
  pair-registration, holdout, grader, human-review, comparator, defect, and
  claim contracts without exposing holdout content.

## Calibrated differences

- A fixed reference count is not an outcome. The proposed topology retains
  twelve task references plus one maintenance-only attribution source because
  colour reproduction versus imagery direction, and critique versus production,
  have distinct triggers. Routing tests may still merge a route that fails to
  change decisions.
- Three human reviewers are required only for a cross-person comparative claim.
  A one-reviewer run may still complete but must be reported solely as that
  person's preference.
- Design handoff in this Skill means artifact intent, production, and
  implementation constraints. It does not duplicate Scoville Handoff's session
  transfer concern.
- SkillOpt may optimize textual generation-process compliance and functional
  semantics, but never use an automated aesthetic outcome as its objective.

## Unresolved gates

1. The user must explicitly accept, reject, or revise ADR-0003 and ADR-0006
   through ADR-0009.
2. An independent holdout custodian must be assigned before W-002.

## Follow-up result

After the final corrections, the same Fable 5.1 session and SOL target each
returned `READY FOR USER DECISION` with no remaining Blocker or High finding.
Native profile validation again returned `valid: true`, 0 errors, and 0
warnings. This closes the review-reconciliation check only; it does not dispose
the proposals, assign custody, qualify the product, or authorize implementation.

Until both unresolved gates close, implementation remains blocked.
