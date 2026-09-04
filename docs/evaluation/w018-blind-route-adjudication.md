# W-018 blind route adjudication

Date: 2026-09-02  
Status: completed; development contract only  
Contract: [`successor-route-contract-v2.yaml`](successor-route-contract-v2.yaml)

## Blind method

Phase 1 gave a fresh Terra Medium adjudicator ten anonymized task contracts,
Core/direct index and mechanically generated compact ownership summaries for
all 28 leaves. It received no W-017 IDs, routes, Gold, receipts, statuses,
verdicts, failure summaries or common-load sets. It selected 20 candidate leaves.

Phase 2 received only those candidates' full current reference files and the
frozen Phase-1 result. It could remove but not add leaves. Both phase inputs and
outputs were hashed before the read-only alias map was unblinded. No broad
allowed sets or alternate exact sets were produced.

## Unblinded comparison

| Case | Blind v2 finding | W-017 interpretation |
| --- | --- | --- |
| D28-EH1 | add Critique; forbid Composition | corrected run matched v2; old Gold was too narrow |
| D28-CI1 | Brand + Composition + Typography + Font Technology | observed route matched v2; old Gold was too narrow |
| D28-CI2 | add Typography + Fixed Media | old Gold was too narrow; observed route still omitted Typography |
| D28-CI3 | add Brief + Production | observed route matched v2; old Gold was too narrow |
| D28-MK1 | Mark only | unchanged; observed exact |
| D28-IN1 | Instructional + Diagrams | unchanged; observed exact |
| D28-AD1 | Advertising + Imagery + Brand | unchanged; observed exact |
| D28-PK1 | Packaging + Typography; forbid Composition | unchanged; observed Composition was a genuine over-read before timeout |
| D28-WF1 | Wayfinding + Cartography; forbid Diagrams/UI | unchanged; observed Diagrams + Instructional was a genuine misroute |
| D28-BO1 | UI Workflow + Web | unchanged; observed exact |

## Consequence

W-017 receipts and Gold remain immutable. The v2 contract corrects four
under-specified Gold sets without retroactively granting W-017 qualification.
It also preserves two real routing defects: Packaging over-read Composition and
Wayfinding substituted non-canonical relational/instructional owners for
Cartography. Current Skill ownership prose already supported the blind v2
result; the primary required change is versioned evaluation metadata and
negative fixtures, not broader runtime loading.

## Evidence and claim boundary

- Phase 1 output: `9D7999B84BFACBFEA63A74B62B22FD9C54352F039C030A4DB6DD618BF6D86838`
- Phase 2 output: `7F3422AF2F2651CDCBA9C0B8FBE481A0C5526FCCE538627B48847E644FE09F73`
- Alias map: `4AB7E15A379B8319E875420AA362A46737F0E8BAF77969170B91404284B77AB1`
- Provider usage: Phase 1 `61,255`; Phase 2 `180,620` total tokens.
- Two invalid-schema requests failed before model response and have separate
  zero-credit receipts; neither supplies route evidence.

This adjudication validates ownership interpretation for these exact task
contracts only. It is not Skill qualification, route-performance evidence for
another model, or permission to change W-017 results.
