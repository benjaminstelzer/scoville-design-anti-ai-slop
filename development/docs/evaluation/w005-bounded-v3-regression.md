# W-005 bounded v3 regression

Date: 2026-09-03  
Status: failed visual/evidence gate; exact routing passed 3/3  
Decision: ADR-0027

## Frozen candidate and execution

- Package manifest: `81530628273139A1518B9D44A309CF10ED6FE41585E35A0D6C54C236F547D6DF`
  over 32 executable files.
- Manifest file SHA-256:
  `249FFD69974258C2D375DFC7F0A8E5D3D4CCD3CD7080267350BA8B886B2D332F`.
- All three workspaces were prepared before the first provider call from the
  same candidate manifest.
- Every call used exact `gpt-5.6-terra` with reasoning `medium`, pinned
  `codex-cli 0.147.0-alpha.1.2`, workspace-write sandbox, no network, no retry,
  no repair call and no reserve.
- The parent-only renderer remained helper
  `B2AE196765E9D94A3CD4DA6E21E0BBD3D048110E354C1C05C5BDC9A34079CB9A`,
  config `0F33D14F0A69A5CAA5178F7ED180233B2BA83BD7271A8636A611A701AA1513BD`
  and Edge `BF9CB9E184D1719E2EBB7CE66B1FAD2EFACA215BD86796ED474D0A025B6882AB`
  version `152.0.4191.53`.

Before provider work, package validation passed with 28 modules, 1,465 Core
tokens, 1,187 generated-index tokens and maximum phase load 11,675 tokens.
Package tests passed 17/17; route fixtures passed 44/44; successor route v2
passed 10/10; generated-index, Design/UI boundary, Skill Creator, local links,
manifest and native Plan checks passed. The package validator retained twelve
warning-only expert-target overruns below their ceilings.

## Results

| Case | Exact route | Structural result | Parent-rendered result | Verdict |
| --- | --- | --- | --- | --- |
| PK2-A | `packaging-graphics-and-sku-systems` + `typography-and-typesetting` | SVG dimensions, IDs, fold/barcode coordinates, palette, exact content, Arial and forbidden-feature checks passed | The barcode-zone guide text crosses its protected box and the back/glue boundary at full size and is unreadable at thumbnail size | Route repair passed; visual gate failed |
| Wayfinding | `physical-wayfinding-and-signage-systems` + `cartography-and-spatial-data` | SVG dimensions, route/sign IDs, stable node labels and north-up label passed | Arrival panels cover the title and Gallery B information; recovery, node and route labels collide in the centre | Route repair passed; visual gate failed |
| Mark | `logo-and-identity-mark-design` only | SVG dimensions, all twelve pressure-context groups, palette and forbidden-feature checks passed | A and B are visibly distinct, but C renders as detached rectilinear blocks rather than the reported three folded rails; the report/source/render mechanism claim is not aligned | Route repair passed; visual and evidence gates failed |

The three raw-event SHA-256 values are:

- PK2-A: `80D527A5FD009784D5261279A612CBD6FE30AF1D191673CD2262449703DF22F6`
- Wayfinding: `A1A5933A83D8798B1947424CCA7B7C54DB8E041ABB7767731E71459F0A660C0B`
- Mark: `26781E5A43E45258F104AA4BEE79CEC8523C7DFFE4D78033994DF54D31F3847E`

Artifact and render SHA-256 values:

- PK2-A SVG `31A19163255B34A46E24FD9A73C96DFDB24EEEF73EA1792236E53938FAD7BA73`,
  full render `173AFA6A73972C4F8CFD142035DE3D3B498725F0F251122449DCFAE40B4CF8BD`,
  thumbnail `2B7974FE5EFE784249D6855659DCDF678A560A26B1E083178D054CF02C67A894`.
- Wayfinding SVG `2D5F02399D2219B8A8FE8C9FB42BAF53F22D302C1172C839868C9DA307BD84E3`,
  render `34CF2121DD66FB5627CBA463E0658A0CCADD40CF6CC908F874EA5C5ED73E0ED6`.
- Mark SVG `2C4A5CBDEDBD09362979A1C7BF6CC6AD287E9DAB459283C7EF738F4A253712B7`,
  render `2E0CEA7B85EFB4CDE88EF7916F42F0C7428FADA7F88BC3ED1805EB1D14A1EB63`.

## Usage and conclusion

The three terminal responses used 365,473 input tokens, including 265,088
cached input tokens, and 22,895 output tokens. Provider-total usage was 388,368;
uncached input plus output was 123,280.

ADR-0027's route causes are repaired for these exact cases, but its requirement
that all three also pass rendered visual and evidence dimensions in one call is
not met. No result is retried, repaired or reclassified. No sealed holdout,
SkillOpt, publication, installation, commit, push, tag or release occurred.
Broad W-005 qualification cannot start under the accepted ADR-0027 gate.
