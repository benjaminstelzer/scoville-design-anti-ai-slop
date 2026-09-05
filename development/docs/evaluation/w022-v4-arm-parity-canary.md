# W-022 v4 Terra High arm-parity canary

Date: 2026-09-03  
Decision: [ADR-0030](../decisions/0030-create-a-v4-suite-with-three-call-arm-parity.md)  
Status: admission failed on the frozen route dimension  
Design manifest: `81530628273139A1518B9D44A309CF10ED6FE41585E35A0D6C54C236F547D6DF`  
UI manifest: `FD255A274E2D92C6DDA14CAD2A85FF0E7702960CEE6B2D3B9F20E04A78A78875`

## Model-free suite result

Qualification-v3 and its three failed holdout attempts remained unchanged.
The new local `qualification-v4` suite makes the old implicit matrix boundary
explicit: 156 registered executions, six quarantined executions for
`HD-14B8E6D9`, and 150 runnable case-arm-repeat jobs. Repair call slots and
pre-response transport attempts are different state dimensions.

The v4 harness passed 25 of 25 unit tests with zero model calls. Covered
contracts include the three-slot renderable path, one-slot text path,
arm-equal policy, parent render before repair, terminal response semantics,
allowlisted pre-response retry, fixed backoff, idempotent resume, one active
shard, append-only receipts, hash-chain verification, duplicate terminal
rejection, matrix-count validation and incomplete-suite scoring blocks.

The two package snapshots revalidated against their manifests. The public
canary descriptor SHA-256 was
`4E222ABDF0D7B5F688B75EA313EFB846CB0C7742CC327911A449C7297B042C3E`.
Its preflight verified seven control hashes, both source inputs, the empty
No-Skill package path, the exact Design package copy, exact Terra High, zero
provider calls and no holdout unseal. The final controlled-suite manifest is
`E0CD1CB6F5CD4B7C4321B8FCF048E8390C1D89AE32F27584B43A501825BAF541`.

## Arm-parity execution

Both arms received the same public Wayfinding input, exact
`gpt-5.6-terra` High, pinned CLI, sandbox, 900-second per-call limit, parent
renderer, image path, localized-defect rule and maximum Call A/B/C sequence.
Calls ran one at a time. Every response terminated its call. No transport
retry, reserve, parallel call, package edit or holdout access occurred.

| Arm and call | Selected experts | Provider total | Uncached input + output | Parent render |
| --- | --- | ---: | ---: | --- |
| No-Skill A | none | 150,783 | 39,935 | `9A75D5E4...6E463E` |
| No-Skill B | none | 91,918 | 29,966 | `11060641...4051A` |
| No-Skill C | none | 198,329 | 38,073 | `2D3DD1F3...ECAFE` |
| Design A | Wayfinding + Cartography | 203,064 | 45,624 | `61A85AD6...C0103` |
| Design B | Cartography | 340,003 | 44,579 | `DCDF5767...3F387` |
| Design C | Cartography + Wayfinding + Composition | 231,497 | 65,353 | `B016FA62...57B85E` |

Across all six calls, input was 1,161,629 tokens including 952,064 cached;
output was 53,965; provider total was 1,215,594; and uncached input plus output
was 263,530.

## Visual and source progression

No-Skill Call A created every required node, route, sign, arrival, north-up
label and recovery meaning, but its recovery arrows and explanation collided
with the central route and J1/J2 labels. Call B moved and wrapped only the
recovery group but left the explanation behind `S-J1-01`. Call C moved only
that explanation. Final SVG SHA-256
`41B439DB0AAD2EE08F21640D4D4369B63DEE6CE13366D089CDE0710F8570E780`
and final render SHA-256
`2D3DD1F386FDD1C8667ED19E5FE56541FEEDD8E334CDAD7966F1DDB80D9ECAFE`
passed the named collision checks.

Design Call A selected the exact frozen primary route: Wayfinding plus
Cartography. It created every required source and evidence element. Its J1/J2
labels collided and `R-J2-B` lacked contrast on the diagonal route. Call B
changed only those three labels; the J1 anchor then collided with ENT. Call C
changed exactly the J1 label y-position. Final SVG SHA-256
`28E717E3BDA7E7594CBF7AE48D6DF8E96290A82315B17F15BF8557872F87D932`
and final render SHA-256
`B016FA62B1E04F5D94E30D9C2680B9C79E9B9F97321BD565C1C06B99DA57B85E`
passed the named visible defects with all protected source dimensions intact.

The final visual passes are one evaluator's inspection of this public case,
not preference, cross-person or general competence evidence.

## Admission verdict

V4 admission fails. Call C loaded `composition-and-layout` in addition to
Wayfinding and Cartography for a single specialist-map node-label placement.
The frozen descriptor expected the Wayfinding plus Cartography route and the
gate requires route and visual dimensions to pass separately. The clean final
render cannot retroactively erase the over-read.

No v4 sealed canary or holdout call is admitted. The result isolates a current
Terra High routing defect: local label collision repair inside an already
selected specialist system can pull in Composition even when overall
hierarchy, reading order, grid, semantic spacing and content fit are settled.
Any correction requires a new package manifest and a new suite identity; these
six calls cannot be retried or promoted as qualification evidence.
