# W-019 targeted v2 pilot

Date: 2026-09-03  
Status: completed with no accepted Skill change  
Parent package: `CD3931B3E56E0EA86CF2C355E5243C77BFC2F0DA47899545BC870B8E57D03A28`

## Frozen execution

All three baselines were prepared before the first provider call. Every model
call used exact `gpt-5.6-terra` with reasoning `medium`, ran alone through the
pinned `codex-cli 0.147.0-alpha.1.2`, had network disabled, and used the same
32-file parent package. The parent-only Edge renderer remained
`B2AE196765E9D94A3CD4DA6E21E0BBD3D048110E354C1C05C5BDC9A34079CB9A`
with configuration
`0F33D14F0A69A5CAA5178F7ED180233B2BA83BD7271A8636A611A701AA1513BD`.

The five completed baseline calls used `1,061,247` provider-total tokens and
`215,679` uncached-input-plus-output tokens. One additional SkillOpt optimizer
call completed but its harness rejected the response before retaining output or
usage; its possible billing is unknown and excluded from those totals.

| Call | Raw events | Provider total | Uncached + output | Route | Final result |
| --- | --- | ---: | ---: | --- | --- |
| PK2-A baseline | `A2D12FB722587CCF449AE2BD91EABA01C8FB12F6BA6AB5A7CBCC483189A2FD02` | 354,323 | 55,955 | Packaging + Typography + Composition | exact recurring route failure; visual pass without repair |
| Wayfinding baseline | `AE313AE0D2A2C96D271FAD5D0E490752B83AF2EE13AB090BC404C77C8CC25F57` | 159,143 | 38,055 | Wayfinding only | new route signature; visible recovery and compass defects |
| Wayfinding repair | `A06618FDCBD44E896322B8863DB2CCDEDD8D8FEB4B66315B5E54FE33FEA03F5C` | 185,737 | 38,025 | Wayfinding only | visual repair passed; Cartography still omitted |
| Mark baseline | `F14CB2BFECD376EC4188D277C5A1B8E13E83868A0D60C58C0917A796A4CDEC01` | 109,833 | 35,337 | Mark only | exact recurring generic near-variant collapse |
| Mark repair | `FC0BD30BE59C488CE0CAE08341C9019AD48535082D36F994D3E09954B59364D3` | 252,211 | 48,307 | Mark + Concept | new route signature and rendered evidence contradiction |

## Case verdicts

### PK2-A

The baseline selected Packaging, Typography and forbidden Composition. This is
the exact preregistered W-017 signature. The source preserved the 1040 by 600
geometry, panel/fold/barcode IDs, exact content, palette and claim limits.

- SVG: `6020DFACF6A146C20ADCA8D1145CFA20C974B9FC10112345170A796BEE1585F4`
- report: `4E36EFB620A860CE345C99D08D31406724BCDCD9DA474894A7CCF61BE6F0B137`
- full parent render: `12360E2A9D6BA0A5C2F951A70E1DAB7EF9600935231FCF41C623C867CD9CCA07`
- scaled thumbnail from that render: `E38D81394454AAA785CA7755970DF41A1B90BFA8CB527C248037D0CB56C0C8D8`

The smoke band no longer dominates, side copy remains inside its panel, and
storage copy clears the barcode zone. No model repair call was needed. Route
failed; visual, ownership, source and evidence boundaries passed.

### Wayfinding

The first call selected Wayfinding only. It omitted required Cartography but
did not substitute Diagrams or Instructional as W-017 did. That different
signature closed the optimization lane. Parent render
`6EAEFF853B80D22D4A438FF7099485BECF7B5FA975C2B8856960A309F7A3A451`
showed the header compass label outside its carrier and recovery geometry
crowding J1/J2.

The single permitted image-feedback repair kept the route/content contract,
produced SVG
`7C8EE9730FCFF4AAAACDC28A7EA259DD8010C0C78CBB89CA3537C49C2132D554`,
and passed parent render
`57DD60F0D1AFD43655325BAE600D14E6D48DE5103F6FD7FC0BDEF8F94C198C52`.
The final visual and ownership result passed. Exact route still failed because
Cartography remained absent.

### Mark

The first call routed exactly to Mark but A and B shared the same three-route
path geometry with positive/negative treatment; C remained another fork-like
three-piece form. Parent render
`55F377ADC85D5AC4E23405E337EBD9B647E6E297E47F7CFC9F494F5CD098E06C`
confirmed the exact preregistered generic near-variant collapse.

The single image-feedback repair produced visibly more different candidates in
SVG `A7ED98ED8BE321E43F7598BB199E6B463EE5D3DE999C6233EB205E2F186E7F2A`
and render
`FA82CAF3A8B558923EFA502C63825403232E19D2E4316FA6FFD64D2B4DB8AD8C`.
It also selected forbidden Concept. The report says B is one connected receiver
field, while the render shows four disconnected corner blocks. That new route
and evidence signature closed the optimization lane. The repaired output does
not pass all required dimensions.

## SkillOpt result

Only Packaging was eligible. One isolated optimizer call used the frozen Core,
Packaging, Typography and incorrectly selected Composition sources with exact
Terra Medium. Input manifest
`DDAC6BD9A2D8337F54169B0E35A36FDBA806B9E0825BEE9271A869577223657D`
bound all allowed source hashes. The response used a non-unique `old_text`
selector in `SKILL.md`; the harness rejected it before retention or application.
Local failure receipt
`00DD4AC10EB5F456318151E2ED97B9877AD9EDE77CFF799B81274857862DE62B`
records the exact failure and unknown-usage boundary. No retry is permitted.

No proposal was accepted, no paired rerun was eligible, and no integrated
regression was triggered. The parent package remains byte-identical to the
accepted manifest.

## Deterministic gates

- package and token/context validator: valid; 28 modules; Core 1,472; index
  1,163; largest expert 2,340; Core plus index plus four largest 11,634; twelve
  target-only warnings and zero errors;
- package validator tests: 17 of 17 passed;
- generated direct index: current;
- successor v2 route contract: 10 cases valid;
- deterministic route fixtures: 39 cases valid;
- Design/UI boundary: active Design means strict UI and UI-only retains its
  Greenfield fallback;
- Skill Creator quick validation: valid;
- local Markdown links: zero missing;
- package manifest check: current at `CD3931...03A28`.

## Conclusion

W-019 completed its targeted diagnosis but did not clear W-005. Packaging still
over-reads Composition, Wayfinding omits Cartography, and Mark does not yet
produce a route-clean and evidence-consistent mechanism set in one call. The
results are open development evidence only. They do not qualify the Skill and
do not authorize sealed evaluation, publication, installation or release.

