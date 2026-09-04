# RC7 final audit and routing report

Date: 2026-09-02  
Model scope: GPT-5.6 SOL, xhigh reasoning  
Status: executable package GO, clean sealed qualification running

## Result

Independent SOL returned **GO** with no P1 or P2 finding for the exact RC7
package. Package validation, generated-index validation, full package identity,
and 36 repeated open routing cases passed.

This is an executable-package and selective-loading result. It is not visual-
quality consensus or expert-equivalence evidence.

## Closed findings

The final package closes every audit finding encountered during RC2 through
RC7:

- `critique` is read-only and cannot silently become generation or repair
- phase transfer and Design-to-UI handoff use one canonical record
- general imagery plus generated and documentary imagery route to Art Direction
- privacy, sustainability, synthetic evidence, IP, consent, and standalone
  jurisdiction concerns route to Culture and Provenance
- source audits and explicit license/attribution work route to Sources without
  treating every consent or rights concern as source verification
- recurring template systems route to Brand while spatial template decisions
  route Composition only when they remain material
- design exceptions route by their affected domain without forcing Composition
- generic words such as `design`, `audit`, and `review` cannot invent an expert
  concern

## Routing evidence

The final open suite is
`evaluation/routing/benchmark-v9`. It contains six Train and six Validation
cases and was executed three times per split.

| Run | Split | Hard | Soft |
| --- | --- | ---: | ---: |
| `design-rc7-routing-train-r1` | Train | 6/6 | 0.95261 |
| `design-rc7-routing-train-r2` | Train | 6/6 | 0.95261 |
| `design-rc7-routing-train-r3` | Train | 6/6 | 0.95261 |
| `design-rc7-routing-val-r1` | Validation | 6/6 | 0.94670 |
| `design-rc7-routing-val-r2` | Validation | 6/6 | 0.94670 |
| `design-rc7-routing-val-r3` | Validation | 6/6 | 0.94670 |

Aggregate: 18/18 Train and 18/18 Validation. Every row recorded
`agent_ok=1`, `behavior_hard=1`, `efficiency_hard=1`, complete token data, and
no failed invariant.

Earlier v3 through v8 failures and Gold adjudications remain unchanged. They
show why a single favorable routing run was insufficient and why ambiguous
template-governance wording remains an efficiency limit rather than proof of a
semantic owner failure.

## Executable identity

The RC7 package contains exactly 17 executable files. The canonical package
manifest hashes sorted UTF-8 records of
`path\0byte_count\0file_sha256\n`.

- package manifest SHA-256:
  `623AF68CE12F8E8934DF3DACC7BD8A67CCCB37D0FD16EFFD3D0C1FBE8D74FE85`
- `SKILL.md` SHA-256:
  `D9BB604B9CBE1E212AEDD13D1D2220E22C49AB46741332E60515DCBA24B6E3DF`
- `modules.yaml` SHA-256:
  `7AB89C91E27C7216A1DE7BCB10F28EFE533F3FC4B48473375E495918EC9AC5EE`
- manifest file:
  [rc7-executable-package-manifest.json](rc7-executable-package-manifest.json)

`scripts/build_package_manifest.py --check` verifies the live package against
this manifest. The immutable Studio snapshot is
`frozen-controls/scoville-design-rc7-final`.

## Holdout boundary

No clean holdout case ran under the superseded RC4 package. The final sealed
qualification is authorized only for custody-owned immutable snapshots of RC7,
the current five-file UI package, and pinned Taste Skill v2 at commit
`ccbc15639c97057cbfcf32ecebc38ef716e4bb37`.

The earlier live-source attempt remains quarantined with zero accepted product
evidence. Its local infrastructure-receipt SHA-256 is
`8118a88721970a4e08b9d33c191bfad374764701edd55d73a2681632e34f9642`.

## Claim boundary

RC7 is the final executable candidate for the clean holdout. The open evidence
supports routing stability, package identity, authorization boundaries, and
progressive disclosure on the named cases. Visual outcome claims remain gated
by the clean sealed aggregate and the frozen independent human-review protocol.
