# Fable 5.1 Plan review and reconciliation

Date: 2026-09-02  
Reviewed independent bundle: `66ED3E2BC8676AD53D6F121C787B8C77DA9ED58399CE44C4730F942196368408`

## Provider record

- Model: `claude-fable-5-1`
- Effort: `high`
- Full-read session: `c876c964-28e0-496d-a1aa-efe6f40dd333`
- Adapter terminal state: budget exhausted before it returned the answer
- Recovered local persistent assistant record: `VERDICT: REVISE`
- Findings: no Blocker, six High, six Medium, three Low
- Hash limitation: Fable had no hashing tool; the calling agent independently
  verified all 65 file hashes and aggregate with zero mismatch

Two later provider attempts failed before a usable final answer because of the
same large-session budget and then the five-hour session limit. The user then
explicitly directed the work to continue without further Fable calls. No more
Fable cost or approval is required for W-013.

## High findings and corrections

| Finding | Correction |
| --- | --- |
| Credited leaves lacked separate case/leaf/dimension assertions | Added 138 explicit falsifiable assertions to `leaf-contract-matrix.yaml`; validator rejects missing, vague, extra, unselected, or uncredited assertions |
| C08/C19 exceeded Core's phase rule and no pre-authoring load ceiling existed | Repacked both to three leaves; froze ordinary three, maximum four and 15,000-token Core-plus-leaves gate; tasks above it use separate calls, not headings |
| `rule_exception` could not distinguish C01 from C04 | Predeclared single-domain exceptions stay in the owner; challenged, undeclared, cross-domain or conventional-control exceptions load Critique; explicit fixtures added |
| Icon, pictogram and symbol systems had no owner or case | Brand owns cross-touchpoint family grammar and lifecycle; UI owns semantic/state/name intent; Information owns glyph semantics; Culture owns authority; C13 adds optical/semantic family stress |
| Presentations, documents and templates were absent | Fixed Media signals/owns now include presentations, decks, documents and reusable templates; C18 adds a tagged document/deck reading-order assertion |
| Audit-local source IDs were not scheduled for merge | W-012 step 1 now merges every admitted audit/curriculum ID with license/scope/bias/currency/recheck fields, regenerates the rule-source map and source index before Wave A |

## Medium and Low disposition

- Typography retains a compact fallback/render floor; Font Technology loads
  only for materially open repertoire, shaping, metrics, features, deployment,
  embedding or license.
- Composition owns within-page spatial relations; Fixed Media owns cross-page
  sequence, anchors, pacing and template/fold relations.
- SkillOpt proposals may change only leaves credited by their paired frozen
  case; unpaired leaves remain unoptimized.
- C18 includes a packaging/wayfinding specialist escalation assertion.
- W-012 explicitly adds responsive transformation intent to the UI active-
  Design owner list.
- C03 explicitly tests the font-technology decision before repair.
- Campaign-format, no-person synthetic-integrity, and still-image-versus-
  temporal-sequence boundary wording was added.

## Status

Every Fable finding is incorporated. Per the user's explicit instruction, no
Fable follow-up will be attempted. A final SOL rereview of the corrected exact
bundle is the remaining W-013 review action. Reviewer findings and approval are
process evidence only.

