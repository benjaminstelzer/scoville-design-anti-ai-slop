# Practical guidance review fixes

Date: 2026-09-05. Local implementation of the user's request to remove size
guidelines completely and fix the confirmed Astra/Fable findings from
[review 0024](../reviews/0024-practical-guidance-implementation-review.md).

## Result and scope

All requested follow-up fixes are complete. The current package has no Core,
index, leaf, common-load or leaf-count size guidelines. Typography's missing
coupled-setting operation has separate paired evidence; Cartography now
distinguishes line and area labeling as well as point labeling; the Motion
derivative has consistent status text. Original Plan 7 outcomes remain intact.
No installation, commit or publication occurred.

## Removed size policy

ADR-0059 records the explicit user choice. Removed the registry budget block,
all 30 module targets/ceilings and all common-load ceilings. Core routes by
actual decisions and expertise. The package validator no longer computes
token sizes or applies length/leaf-count gates under any supported schema.
Structural builds work without `tiktoken`; its only remaining use is optional
descriptive measurement. Source, route, evidence, index, module identity and
metadata-format checks remain. Old numeric policies in frozen evaluation
records are explicitly historical in `development/README.md`, not current
admission rules. Provider and explicit user limits remain applicable.

Removed ten obsolete size-policy tests and added two regression tests for
large content/all-module acceptance and malformed common loads. The remaining
suite has **26 passing tests**. Missing/duplicate module IDs, source failures,
status/header drift and generated-index drift still fail. The default Python
environment reports `tiktoken: None`; both current-package validation and the
runtime-build preservation/no-overwrite test pass there.

Astra's bounded follow-up review (`/root/astra_implementation_0007_review`)
returned **Pass**, with no actionable size-policy defect. Its own structural
check returned zero errors/warnings and 30 modules with token measurement
blocked. It did not repeat the unit suite or review the then-running W-002
artifacts. Fable's earlier findings are resolved below; no new Fable verdict
is claimed for this follow-up.

## Separate supplementary evidence

`evaluation/plan-0008/freeze-receipt.json` identifies the new immutable task
freeze under `Z:/Projekts/AI/output/design-plan8-supplements/`. PG-02S is paired
and baseline precedes candidate; PG-08S is candidate-only with a legitimate
non-map control. These explicitly fill missing subquestions, not retries of
the original tasks. The original runner is imported unchanged and checks its
original protocol; the supplement verifies its own frozen runner hash.
Original Core/runtime is used for baseline; current Core/owner text is used
for candidates. Requested model/effort is `gpt-6-astra` / `high` for all three
fresh isolated CLI calls, with the same inherited isolation settings and no
executor tool calls. This is manual owner selection and inline exposure,
not proof of automatic host routing. Different Core text and a single pair
also prevent attributing differences to Typography alone.

| Case | Observed result | Limit |
| --- | --- | --- |
| PG-02S baseline and candidate | Each shows three specimens containing exactly two identical protected paragraphs. Actual platform font is Georgia, regular 18px. Original 648px/29px produces four lines per paragraph; narrower 432px/29px produces five; selected 432px/27px keeps five and reduces paragraph height from 145px to 135px. Both explain the leading decision, retain the original comparison and supply the legitimate unchanged wide control. All four HTML renders inspected. | The operation is now exercised. Both arms choose the same settings; no beneficial model difference or audience readability advantage is demonstrated. Specimen values are task fixtures, not package-size or universal typography guidelines. |
| PG-08S candidate | Identical supplied line/polygon/point geometry at 600px and 300px with the full 0–100 extent. Willow Brook uses a separate offset label curve at 600px and a horizontal name with a leader at 300px; the leader ends at the curve's midpoint (45.625,25). Orchard stays labeled inside its area. Long Meadow uses its long axis at 600px and an exterior callout to its top edge at 300px. Depot's center stays (80,78). All names are legible and associated in both inspected views; source geometry and the accessible table reconcile exactly. The lookup control answers a different name/type question. | Fictional drawing geometry, no CRS/jurisdiction. No audience, GIS certification or broader cartographic correctness claim. |
| PG-11 coordinator derivative | Original subtitle replaced only with “Status of the current step.” Six browser observations verify initial Ready, Waiting, settled Ready, interrupted Ready, reduced-motion Waiting and reduced-motion Ready. Title, data-state and subtitle agree; reduced final state has no active animation. Waiting and reduced Ready screenshots visually inspected. | This corrects the coordinator derivative of the model artifact. Original HTML and answer retain the reviewed failure. No Motion runtime defect or additional model call is inferred. |

Cartography's new line/area guidance is original synthesis grounded in inspected
Esri [line-label](https://doc.esri.com/en/arcgis-pro/latest/help/mapping/text/labels-for-line-features.html)
and [polygon-label](https://doc.esri.com/en/arcgis-pro/latest/help/mapping/text/labels-for-polygon-features.html)
placement options. Source ledger PG-S04 and the runtime source index bound this
to method/reference use; no third-party settings or artwork are imported.

Chrome 152.0.7977.76 rendered six supplementary artifacts with remote requests
blocked. `output/playwright/design-plan8/supplements-receipt.json` records
computed specimens, actual CDP font usage, geometry, text and screenshots;
`motion-receipt.json` records the six state checks and derivative/source hashes.
The unused `pageErrors` field in the supplement render receipt is a placeholder,
not a browser-console audit. Claims here rely on the actual assertions and
inspected source/renders, not that field.

## Other review dispositions

- PG-06 still reports candidate reasoning output 0 versus baseline 773, with
  both requesting `high`. This is reported usage asymmetry, not proof of a
  configured effort change, absent reasoning or the cause of its original
  render defect. No unchanged-task rerun occurred.
- The original three leaf and 17 common-load ceiling exceedances remain dated
  measurements against the then-existing policy. Current policy removes those
  guidelines instead of increasing them or explaining away warnings.
- No beneficial model difference attributable to the practical additions is
  established. Fable's Adobe-fetch limitation remains a reviewer coverage
  limit; Astra's source verification is not attributed to Fable. A revision
  quota and retroactive acceptance weakening remain rejected.

## Verification and preservation

`plan-0008-receipts.json` consolidates the three new sessions and raw usage,
source hashes, render receipts and preservation checks. All original **28**
Plan 7 trial receipts, answers and prompts, and **54** HTML artifacts match
their recorded hashes. Original baseline runtime, source snapshot, protocol
and runner are unchanged. PLAN-0006 W-004 matches HEAD exactly; its unfinished
work is not counted here.

Package validation: **zero warnings, 30 modules**. Generated index current;
**60 route cases / 44 signals** pass; Design/UI boundary passes; Skill metadata
passes. Native profile validation passes with **8 plans, 49 work items,
59 decisions, zero errors/warnings**. `git diff --check` passes.

Final runtime build: **35 files**, source/runtime bytes verified against the
build receipt, manifest
`236BB694B0DF74294E758D0AA560754C79B6BD96CB0DA0C0B4347DF08637BD69`.
See `plan-0008-final-build.json`; optional descriptive counts are in
`plan-0008-measurements.json`. These checks establish local structure and the
reported artifact behavior, not release, host, audience or model qualification.
