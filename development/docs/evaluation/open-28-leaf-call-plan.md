# W-017 open Terra Medium call plan

Date: 2026-09-02  
Status: terminal; all named cases attempted with no qualified pass  
Machine contract: [`successor-28-open-matrix.yaml`](successor-28-open-matrix.yaml)

## Remaining allocation

| Lane | Remaining | Retry reserve | Maximum |
| --- | ---: | ---: | ---: |
| Named capability and boundary cases | 0 | 0 | 0 |
| Conditional SkillOpt pairs | 0 | 0 | 0 |
| **W-017 remaining total** | **0** | **0** | **0** |

The nine W-012 terminal calls remain in
[`successor-open-evidence.md`](successor-open-evidence.md) against their exact
23-leaf snapshots. They consume historical budget and show prior behavior, but
grant no pass to the 28-leaf snapshot. One W-015 High call was interrupted
before raw events, status or usage existed; possible billing is unknown and it
grants zero evidence. W-017 performs no sealed call.

## Binding configuration

- Model: exact `gpt-5.6-terra`
- Reasoning: exact `medium`
- Execution: one terminal call at a time; never batch or auto-continue
- After each call: inspect route, trace, artifact, actual render/image-view
  events, score receipt and usage before deciding whether another call is safe
- Provider-total, uncached-input-plus-output and monetary cost stops: none under
  the user's explicit instruction to ignore the cost stop
- Usage remains recorded and reported after every call
- Core ceiling: `1,500`; generated index ceiling: `1,200`; target three and
  maximum four leaves; Core plus index plus selected leaves: `15,000`

No public Terra tariff is available. Token ceilings are the binding cost proxy.
Capture a provider-displayed credit estimate if available. Purchasing credit or
exceeding a user-specified monetary allowance requires fresh authority.

## Preconditions before call 1

1. Package, source union, rule map, read graph, generated index, route fixtures,
   token, local-link, Skill Creator, Plan, UI ownership and manifest checks pass.
2. Every named case has immutable prompt, input assets, hashes, Gold ownership,
   selected/forbidden routes, artifact contract and scoring assertions.
3. Local-only fonts, comparison pairs, screenshots and renders remain outside
   the public repository and are referenced by hash only.
4. The wrapper rejects paths outside the case workspace and records every
   initial image path/hash in preflight and run status. `render-inspected`
   additionally requires content-specific observations from every supplied
   render that source inspection alone cannot establish. The CLI event stream
   does not echo initial image messages as separate view events.
5. D28-EH1 and D28-CI1 remain frozen zero-credit failures. No retry or reserve
   is available without new user authority.

## Named call order

Run in the machine-contract order. The first case is an end-to-end harness and
evidence-honesty canary. Subsequent cases stop independently at their authority
boundary. A failure remains visible; do not edit Gold after seeing output.

SkillOpt may touch only leaves and Core fields credited by its paired passed
case. Re-run the paired case and the affected route negatives after each
proposal. Reject any proposal that weakens source scope, parent-cause repair,
incumbent authority, proof honesty or standalone operation even if it is
shorter.

## Exit

W-017 may hand its evidence to the next Work Item when all ten named cases have
honest receipts or visible bounded failures, no unclassified infrastructure
defect remains, every used reserve is justified, usage is recorded under the
explicit no-cost-stop decision, the final exact hashes validate, and claims
describe the observed model/configuration only.

Terminal state: ten Medium calls completed and one additional call timed out
without terminal usage. D28-EH1 used its former coverage
reserve and remains a bounded benchmark/routing failure. D28-CI1 exceeded the
superseded W-016 per-call ceiling. D28-CI2 produced a correct, visibly coherent
CI repair, but the frozen route Gold omitted the materially required fixed-media
leaf; it therefore remains a zero-credit bounded benchmark failure and makes
D28-SO1 ineligible. D28-CI3 correctly preserved an unresolved CI-authority
conflict but over-read Brief and Production relative to frozen Gold, so it is a
zero-credit bounded routing-overlap result. D28-MK1 routed exactly to Mark but
failed professional visual-mechanism quality in the evaluator render. D28-IN1
routed exactly and preserved source semantics, but its connector crossed the
warning text in the evaluator render. D28-AD1 routed exactly but allowed its
campaign route to cover mandatory qualifier/CTA content in two evaluator
renders, making D28-SO2 ineligible. D28-PK1 timed out after producing partial
artifacts, read an extra Composition leaf, receives zero credit and makes
D28-SO3 ineligible; confirmed usage excludes its unknown possible billing.
ADR-0024 records the user's instruction to ignore the cost stop. D28-WF1 then
substituted Diagrams plus Instructional for frozen Cartography and received zero
credit. D28-BO1 routed exactly and preserved the Design/UI/Scribe split, but
its evaluator render exposed misleading failure arrows and clipped actions. No
named case passed every dimension, so no conditional SkillOpt call became
eligible.
