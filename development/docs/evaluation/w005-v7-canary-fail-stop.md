# W-005 qualification-v7 Canary fail-stop

Date: 2026-09-03  
Status: qualification-v7 failed and stopped at Canary 2  
Decision: ADR-0045

## Result

The fresh signed v7 authorization admitted exactly six sequential preregistered
arm-balanced Canary shards and the remaining 138 jobs only after all six passed.
Canary 1 passed both jobs and all 18 scorer checks. Canary 2 stopped after its
candidate returned a terminal response and failed only the exact route-set gate.

- Canary shards passed: 1 of 6
- Canary shards started: 2 of 6
- Terminal jobs: 3 of 150
- Provider calls: 3
- Terminal model responses: 3
- Retries: 0
- Renders: 0
- Holdout jobs started: 0
- Remaining private plaintext files: 0

Canary 2 recorded three authenticated Design expert reads against two Gold
experts. Its terminal `selected_experts` aligned with all three authenticated
reads. The baseline job was not started, Canaries 3 through 6 were neither
registered nor started, and no holdout job began.

## Evidence hashes

- signed execution authorization:
  `A1D1E43A43636E36C88E1EC9C545D9078E0A34CE8D61DE0ECDC287BA99A57C65`
- Canary-1 result:
  `367240450663034CD12CC042A8CC961B2DF1684E1B1185DA29B223D62860FF6C`
- Canary-1 validation:
  `E89F4F20F3770FB0D6F9FADC01A3105C70B4C349E26C16CEC76F6D70AD6C3CAE`
- Canary-1 sealed archive:
  `48508F49CAD964147AAFC71E6D50146BCDF4075DD5A33C5B4B913C4F6E19AAC2`
- v7 fail-stop:
  `FBE8E02E268118115EC0F801E3825C6358D3ED11F9ABDBA72FBD80173429299B`
- fail-stop validation:
  `B4C6F0CC22856629EB72F41AA34FA2F7953B6E661CEBF64C001A1E36671CEDD3`
- sealed failure archive:
  `FBE43A53F636F0071E47A8E75461BF490E2F08419F3A6A84CFA2DDA94CA0C24A`
- append-only score-hash correction:
  `89F9C0A99D943BBD7E851FEC3792BE421D48E8A482B745F05AE4418BE16AD797`
- correction validation:
  `89FF14CD1242DC254AF64938841ED1C5FEE6ACA9C3584045DB65C992D1921317`
- first arm-blind adjudication:
  `DCC484EDC4B3392097927DE892B057E807F67350B5FE6BB54971ABA0F0F6DC5F`

The append-only correction adds the score hash captured before plaintext
cleanup; it changes no original evidence and made no call.

## Classification and next gate

The current classification is
`indeterminate_package_or_benchmark_boundary`. Qualification-v7 is failed, not
partially qualified, and cannot resume. ADR-0045 permits only a model-free
independent arm-blind contract review of the already sealed evidence. No package
or Gold change is justified yet. Publication, installation, commit, push, tag
and release remain unauthorized.
