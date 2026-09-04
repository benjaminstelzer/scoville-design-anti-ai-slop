---
format_version: 1
id: ADR-0057
status: accepted
created: 2026-09-04
accepted: 2026-09-04
scope: design/execution-model-contingency
---

# Use SOL for remaining paired execution

## Decision

The user explicitly authorised SOL to generate the remaining test artifacts,
using the same model for both comparison arms. Run the incomplete C4 pair and
the not-yet-executed C5A, C5B, C6 and C7 pairs with gpt-5.6-sol, high effort,
fresh isolated sessions, matched read-only file/image tools and unchanged raw
case inputs. Retain the completed and interrupted Fable attempts separately.

## Problem

Fable's session limit prevented completion of paired tests. ADR-0056 authorised
review substitution only. The user has now answered yes to the separate
execution-model choice. A SOL candidate cannot be compared against the existing
Fable C4 baseline as if execution conditions were matched.

## Drivers

- Continue the accepted implementation and focused proof without a full holdout.
- Match model, settings, tools and prompts within every actual comparison pair.
- Preserve original outcomes, provider failures and reviewer independence.
- Keep installation and all publication operations separately unauthorised.

## Considered alternatives

- Wait for Fable for all remaining generation: no longer follows the newly
  selected execution direction.
- Generate only missing candidates with SOL: saves one C4 baseline call but
  confounds model and package effects.
- Selected: use SOL for both arms of every remaining pair; do not repeat the
  already completed C1-C3 Fable pairs. Extend only for a concrete uncovered
  changed mechanism, not to obtain a favourable score.

## Consequences

SOL and Fable strata are reported separately, never pooled into a model-invariant
improvement claim. Runtime package hashes remain distinct from model-generated
artifact hashes. Read-only generation returns proposed source for authorised
host materialisation and rendering; critique cannot mutate its inputs.
Use the official supported Codex non-interactive isolation flags and retain
actual events. No global Skill installation or user configuration edit occurs.
Genuine SOL host activation may be tested separately under isolated discovery;
it is not inferred from interpreted route fixtures.

This supplements ADR-0056 after its revisit condition was met. It does not
rewrite that historical review-only choice or waive unfinished acceptance.
W-004's authored Decisions list is immutable under format-version-1; record
this supplemental choice in execution evidence without editing that list.

## Confirmation

Before outputs, freeze the SOL run settings and case/pair manifest. Capture
actual tool/read events, returned source, applicable real renders, errors and
unfavourable outcomes. Use a separate fresh blinded reviewer for pair judgment.
Correct only evidenced defects and recheck only affected cases. Final package
and acceptance claims remain bounded by the observations actually completed.

## Revisit when

The SOL harness cannot provide comparable real execution, an additional changed
mechanism remains uncovered, Fable returns for its retained-session final
review, or the user changes the accepted scope.
