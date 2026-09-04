# W-004 SkillOpt optimization report

Date: 2026-09-02  
Target and optimizer: `gpt-5.6-sol`, `xhigh`  
SkillOpt commit: `ba820b500f9da96685cf2780c7dc85ed4eb6563e`  
Network: disabled; isolated Codex home; no Fable or Opus behavior calls

## Frozen inputs

- Pre-optimization Design `SKILL.md`:
  `DEA073D4FB341BFEBCA0E1A14CAC78A758F3E07ECDED226CEF54A7BD9AF808D1`
- Pre-optimization UI `SKILL.md`:
  `5E4005BCC9EBC4476E3B2AB14CD4A4D5CEA7837A15EA17A3C39563E9E3575C48`
- Design v1 benchmark lock:
  `29B327AC234FD274C216D539561D79725EB1B695B0A2C645875B47D438F972EF`
- UI v1 benchmark lock:
  `72186916F165E54426BF23FBF501296F1728F4E312F4D86769D66E7FB1C7D1FE`

The independent holdout custodian checked 36 W-004 rows against each other and
all 30 opaque qualification cases: 36/36 IDs unique, 630 benchmark-to-
benchmark comparisons, 1,080 benchmark-to-holdout comparisons, zero exact
duplicates, and zero material near-duplicate collisions. Criteria were NFKC
normalization, SHA-256, five-token shingle Jaccard 0.18, TF-IDF cosine 0.65,
numeric fingerprints, and manual mechanism comparison. No holdout content was
exposed.

## Primary SkillOpt result

| Run | Selection | Train | Optimizer outcome | Tokens |
| --- | ---: | ---: | --- | ---: |
| `design-w4-train-r1` | 8/8 Hard | 10/10 Hard | one byte-identical/non-improving proposal rejected; initial Skill retained | 927,930 |
| `ui-w4-train-r1` | 3/3 Hard | 7/7 Hard | no usable patch in either batch; initial Skill retained | 532,280 |

No generated candidate was promoted. The initial W-004 Test gate nevertheless
found routing weaknesses: Design 2/4 raw Hard and UI 3/4 raw Hard. These rows
were consumed at that point and were never re-labelled as unseen.

## Repairs and benchmark adjudication

Three minimal source corrections followed the consumed Test diagnosis:

- Design's generated index now recognizes editorial layout separately from a
  brand system and treats period/genre/vernacular language as style direction.
- UI's COMPOSED router now requires Quality when implementation must reason
  about states, semantics, accessibility structure, focus/input,
  announcements, or responsive mechanics.

Independent SOL adjudication found three frozen-Gold problems:

1. `route-val-culture` legitimately requires imagery/art direction, cultural
   ethics/provenance, and sources/attribution; v1 required culture only.
2. `ui-comp-test-bounded-design-with-system` legitimately requires UI Quality
   for responsive/state mechanics; v1 forbade it.
3. `route-test-annual-report-system` legitimately requires colour/reproduction
   for print plus screen; its wording is also ambiguous about whether already-
   verified charts require Sources.

The original locked suites and failed rows remain unchanged. Adjudicated v2
regression locks are:

- Design: `CED1ABD56DD3E877390B78B94DE8EB37006236970327194946D99054A678D6A4`
- UI: `D10D6AFEE2CE221634E7FA5A6BD472CC15B81F9F1E14231FCC9C15F89049A33C`

Results on the repaired source:

- Design v2 open Validation: 8/8 Hard.
- Design v2 consumed Test regression: 3/4 raw Hard; the sole row is the
  independently adjudicated Annual Report Gold defect above.
- UI v2 open Validation: 3/3 Hard.
- UI v2 consumed Test regression: 4/4 Hard.

These are regression results, not renewed unseen evidence. W-005 must use the
independent qualification holdout.

## Local external-pair ablation

The external lane remains outside both repositories under
`Z:\Projekts\AI\scoville-design-eval-local\external-train-v1`.

- OpenOregon Figure 36 / A. Dawn Journal was downloaded from the CC-BY book,
  rendered from PDF page 180, visually inspected, and supplied as a binary PNG
  attached to the initial SOL request. The figure credits Ahmed Dawn under
  CC BY 2.0.
- The official W3C BAD archive supplied unchanged before/after Home HTML for a
  documented accessibility-repair comparison, not visual-taste Gold.
- External material occurred only in Train. Validation and Test were original
  synthetic regression cases.

SkillOpt Studio gained validated `binary_files` plus `attached_images` support
so an image is materialized from scorer-hidden Base64 and passed through the
native Codex CLI `--image` argument. Five focused unit tests passed. Earlier
Base64 and weak-visual-proof smokes remain failed evidence rather than being
overwritten.

Final ablation inputs both passed 2/2 Train Hard:

- external lock:
  `8EAEC3DC1F8E53BF668127AC2B8856390168F0B1708B1D87D56AC88782A08E97`
- synthetic control lock:
  `A94122919A553AF17CBA475DD37CFEA7098D27A0A1ADFB70E283011134616AAE`

Runs `design-external-v8-train-r1` and
`design-external-control-v3-train-r1` each proposed a compact comparison-claim
scope sentence. The wording differed slightly but the mechanism was the same;
both candidates lost the soft gate and were rejected. The external material
therefore did not change promotion and is not qualification evidence.

## Retained candidates

- Design `SKILL.md`:
  `671B6BAC24569360D23AC0300BEFEC0B478FE035EC9EF79B19E144239369AEF8`
- Design `modules.yaml`:
  `302FB0999EAA2C514162D1BF58733282637C0D5CF52D3252C3D9B7A10BB60C8E`
- UI `SKILL.md`:
  `217F298D4B98808012FE41C024D5B92B01B6F06929245DCC3C8206CE288F462C`
- Design package validator: 14 modules, Core 1,120 tokens, generated index 450,
  largest expert 1,762, Core plus three largest experts 4,074.

W-004 proves conservative routing optimization and rejection behavior. It does
not prove professional visual-quality gains, cross-person taste agreement, or
general graphic-design competence.

