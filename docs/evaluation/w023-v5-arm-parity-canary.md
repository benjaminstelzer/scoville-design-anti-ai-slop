# W-023 v5 Terra High owner-local routing canary

Date: 2026-09-03  
Decisions: [ADR-0031](../decisions/0031-exclude-owner-local-specialist-repair-from-composition.md), [ADR-0032](../decisions/0032-treat-resource-budgets-as-guidance.md)  
Status: public admission passed; sealed execution remains unauthorized  
Design manifest: `3D19CE209E52AFCE91B888D6FB489E29EA9846A1442896129563D4B94ADC01C2`  
UI manifest: `FD255A274E2D92C6DDA14CAD2A85FF0E7702960CEE6B2D3B9F20E04A78A78875`

## Isolated package repair

W-022 failed because Design Call C loaded Composition for one local specialist
map-label collision after general composition was settled. The W-023 package
changes only the Core selection boundary needed by that evidence: owner-local
specialist label repair no longer selects Composition. Equivalent wording
tightening kept Core at 1469 `o200k_base` tokens. No expert reference,
`modules.yaml`, generated index, source contract or UI package changed.

Direct route fixture RF45 requires Wayfinding plus Cartography and forbids
Composition, Diagrams, Instructional and UI for an owner-local wayfinding-map
label repair. The complete direct contract passed 45 of 45 cases; the blind
successor-v2 contract remained 10 of 10. The new 32-file executable package
manifest is `3D19CE209E52AFCE91B888D6FB489E29EA9846A1442896129563D4B94ADC01C2`.

## V5 suite and preflight

Qualification-v3 and v4 remained unchanged. Qualification-v5 binds the new
Design snapshot and unchanged UI snapshot under a new suite identity. Its
inherited call-slot contract passed 25 of 25 unit tests with zero model calls
and retains 156 registered executions, six quarantined executions and 150
runnable jobs. The controlled-suite manifest is
`23E9527D7739CB5B7014E4A00DFCC606AC655A6427F940A672503FE41DF425F2`.

The distinct original public case uses Riverside Learning Campus rather than
the v4 fixture. It has seven nodes, six physical edges, three decision signs,
four arrival confirmations and one non-invented missed-turn recovery trace.
Descriptor SHA-256 is
`E21CD8CE6BFBCECD39681982A797E436319C449515C7C3D589D924E46CE9CCA7`.
Zero-call preflight verified seven controls, both inputs, the empty No-Skill
package path, the exact Design copy, Terra High and no holdout access. A
preflight import-path invocation defect was corrected before any model call;
the controlled suite was rebuilt afterward.

## Arm-parity execution

Both arms received exact `gpt-5.6-terra` High, the pinned CLI, the same
parent renderer, the same maximum Call-A/B/C opportunity and the same local
repair stop rule. Calls ran one at a time. Each response terminated its call.
Both arms passed after Call B, so each left Call C unused. There were four
model responses, zero transport retries and no sealed access.

| Arm and call | Selected experts | Provider total | Uncached input + output | Parent render |
| --- | --- | ---: | ---: | --- |
| No-Skill A | none | 115846 | 51590 | `411ECFB1...3333D` |
| No-Skill B | none | 206964 | 43636 | `B80F39E2...1F465` |
| Design A | Wayfinding + Cartography | 318728 | 59400 | `671DB39C...6DB62` |
| Design B | Wayfinding | 167465 | 40745 | `076C795A...F36F8` |

Across all four calls input was 764363 tokens including 613632 cached; output
was 44640; provider total was 809003; and uncached input plus output was
195371. These measurements are reported rather than used as an automatic
quality gate under ADR-0032.

## Route and visual result

No-Skill Call A used no experts and created every required source and evidence
element. Its render showed multiple node-label collisions and an overflowing
S-JA-01 line. Call B changed only local label positions and that panel-local
text fit. Final source SHA-256 is
`A825F8DA95116025AD0C4E0B232EB92E0B890C6F9C1B4AA9B8E29CB6817ECBF7`;
final render SHA-256 is
`B80F39E2341FA3A70709A59C4A43239FF7D70AFD8520E039EAAB46448CF1F465`.

Design Call A selected the exact primary route: Physical Wayfinding plus
Cartography. It preserved all facts and produced a legible route system, with
one remaining intersection between `N-JB · Library junction` and the red
recovery arrowhead. Call B received only the immutable source, report, render
and that local defect brief. It selected Physical Wayfinding alone because
the map encoding was already settled, changed one SVG label position and did
not load Composition. Final source SHA-256 is
`6246D6197153A8A89542075380A470F21B1FF55412D2F2D0C5BD201E91F4E131`;
final render SHA-256 is
`076C795ADDB2A3305C9D71AD32943DDF7D84123DB9F3E2FD222976649E3F36F8`.

Both final renders pass the named visible defects with protected topology,
IDs, text, signs, arrivals, recovery meaning and authority limits intact. The
visual verdict is one evaluator's inspection of this public synthetic case.

## Deterministic gates and verdict

- package unit tests: 17 of 17;
- package schema: valid with 28 modules and Core 1469 tokens;
- direct route contract: 45 of 45;
- successor-v2 route contract: 10 of 10;
- generated module index: current;
- Design/UI boundary: active Design strict UI and UI-only Greenfield fallback;
- Skill Creator validation: valid;
- executable package and controlled-suite manifests: current;
- native Plan: zero errors and zero warnings before lifecycle close.

W-023 passes. The demonstrated Terra High Composition over-read did not recur
on a distinct public case, both arms received equal repair opportunity and
both final renders passed. This admits the mechanism and changed package for
continuation into W-005. It is not sealed qualification and does not authorize
unsealing, a real sealed call, installation, publication, commit, push, tag or
release.
