# Practical guidance plan review

Date: 2026-09-05. Scope: PLAN-0007 and its evaluation contract. Both reviewers received identical self-contained prompts independently; neither received the other's answer. This is plan review, not design or implementation proof.

## Reviewed revisions and reviewers

| Revision | Plan SHA-256 | Contract SHA-256 |
| --- | --- | --- |
| R1 | 9785CBD23617A23782DD75AB86A5B07811D833C3E0B7A3835BFBB23602B1A7C4 | BF59BCFD478F76E1489A7C6941E62D1870D44E64659AF602693F67290EC597CE |
| R2 | 7DC4FB2DFC13BEB8BE5092A6E37B26E2533D26F677893CEA72584EFCC8C22381 | D1B52C3A6C3C5D175B457BF96E5B96A6B0D3376E5B13F316EF62F44F754267AA |

Audit archive SHA-256: CE3ED0B627768DEBE59F69CAB98AB11896878B39D46E52B1BDAC12874224A5B6. Exact R1/R2 snapshots and common prompts are retained in the workspace `output/scoville-design-plan-0007-*` files outside this repository. The original audit commit remains b5a824b; coordinator and Astra verified that the subsequent daca889 diff affects only README and CHANGELOG.

- Astra: fresh host agent `/root/astra_plan_0007_review`, requested `gpt-6-astra`, effort `xhigh`; R2 used the same agent. R1: **ready with minor changes**. R2: **ready**, no implementation blocker. Astra verified R2 hashes. No design cases or holdouts executed.
- Fable: requested `claude-fable-5-1`, effort `high`, customizations disabled; persistent session `8d8fe08b-de4e-4066-aa75-2031633e82dc`, resumed for R2. Provider wrapper `reported_model` is null, so requested identity is not presented as independently verified backend identity. R1 and R2: **ready with minor changes**. No permission denials. R1 cost $4.4071905, R2 $1.390564; these are review costs only. Original adapter replies are `output/scoville-design-plan-0007-fable-r1.json` and `-r2.json`. Fable compared snapshots textually and could not hash or inspect git; those checks were performed by the coordinator.

## Findings and disposition

| Finding | Source | Disposition |
| --- | --- | --- |
| Freeze was split between W-001 and later items | Astra R1, Fable R1 | Accepted. All evaluation inputs, subquestions, manifests, countercases and final transfer inputs freeze in W-001. Later teaching content is separate. |
| Pattern construction lacked a concrete acceptance clause | Astra R1 | Accepted. W-002 requires an actual repeated surface, density/edge behavior, invariants and legitimate irregular/crop countercases. |
| C01–C16 collides with existing common-load identifiers | Fable R1 | Accepted. New families use PG-01–PG-16; existing metadata IDs remain unchanged. |
| Source admission needs explicit use classes and lineage | Fable R1 | Accepted with correction. ADR-0003/0019 and the live source index permit inspecting and citing reference-only material. They prohibit packaging/adapting its protected expression/assets. An external number must not be relabelled local synthesis. Fable R2 accepted this correction to its earlier suggestion. |
| Application could be mistaken for mentioning a technique | Fable R1 | Accepted. Require a locatable artifact relation, protected floors and operation-specific evidence; critique stays read-only and justified no-change controls can pass. |
| Evaluate artifacts before rationale | Both R1 | Accepted. Neutral identifiers, evaluator declared at freeze, arm masking where practical, self-assessment limits explicit. No automatic extra provider lane. |
| Full comparisons for every illustrative P2 example are disproportionate | Fable R1 | Accepted. P1 and proposed Core behavior use matched comparisons; P2 may establish bounded candidate sufficiency or documented existing-source sufficiency without a comparative claim. |
| Seven unchanged leaves should not become a new full qualification project | Astra R1 | Accepted. Target only touched boundaries, preserve unaffected evidence. |
| Critique example was owner-local | Fable R1 | Accepted. Use a cross-domain finding/challenge and an owner-local no-load control. |
| Token growth and Core duplication | Fable R1 | Accepted. Existing measurement tool covers changed leaves/Core/common loads; Core changes require an actual baseline gap and useful candidate difference. No hard token gate. |
| More concrete composition, hierarchy and alternate-theme operations | Fable R1 | Accepted within current owners and applicable contexts. No mandatory new theme/state surface. |
| Separate freeze Work Item | Fable R1/R2 | Not adopted. W-001 explicitly owns this prerequisite; a second item adds no independent deliverable. |
| Preserve unresolved PLAN-0006 lanes and exact old runtime | Both rounds | Accepted. User subsequently authorized direct implementation. Transition returns PLAN-0006 to draft with paused W-004 unchanged, documents why, and selects PLAN-0007 W-001. Native Plan lifecycle explicitly supports active-to-draft; draft here is retained inactive work, not a claim that completed items are unwritten. |
| P2 comparison becomes necessary after candidate-only observation | Astra R2 | Add to W-001 freeze: retain the original observation; freeze a new explicitly justified comparison revision with baseline before candidate. Never fish for a better valid result. |
| Contract still describes PLAN-0006 as active without transition qualifier | Fable R2 | Accepted as final wording correction before activation. Add the dated lifecycle explanation to PLAN-0006, preserving W-004 and Next action exactly. No further review requested for this nonmaterial correction. |

## Conclusion and limits

The reviewed plan covers Core, all 23 proposed additions and seven preservation rows in ten Work Items. Astra's final verdict is ready; Fable's final verdict is ready with the two small lifecycle wording clarifications above. Both are resolved in the activation change. Review agreement does not establish model improvement, source-use permission or working artifacts.

The execution model/settings, concrete fixtures, renderers, source admission and observation records are W-001 execution work. The user's instruction to implement once ready authorizes that work; it does not authorize installation or publication, and it does not finish PLAN-0006's DH5 or original Fable lane.
