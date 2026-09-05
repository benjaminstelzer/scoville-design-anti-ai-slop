# W-020 rendered-repair admission

Date: 2026-09-03  
Decision: [ADR-0028](../decisions/0028-admit-parent-rendered-repair-before-broad-qualification.md)  
Candidate manifest: `81530628273139A1518B9D44A309CF10ED6FE41585E35A0D6C54C236F547D6DF`

## Scope and controls

This gate reused the three immutable v3 outputs recorded in
[w005-bounded-v3-regression.md](w005-bounded-v3-regression.md). All nine
Call-A source, report and parent-render hashes matched that record before any
provider call. The executable package manifest was current and no package file
changed.

Each case used one isolated `gpt-5.6-terra` Medium call with its exact Call-A
source, report and parent render. Calls ran sequentially through pinned
`codex-cli 0.147.0-alpha.1.2`; the child had workspace-write access, no network,
no approval path and one image input. The parent rendered each resulting SVG
exactly once through pinned Edge `152.0.4191.53`. There was no retry, third call,
reserve, SkillOpt proposal, package edit or sealed call.

Descriptor SHA-256:

- PK2-A: `3E763C23E1EB53A91C30D8FBBBD4C33BA9DC357B7A5D317559751A3B0E45830D`
- Wayfinding: `B1B56B59512CD1EB4F1138E8FB33B15450146E1912EA9342449DCF87011A632B`
- Mark: `0787B21F1590C839C12B7787D7736FE6D97FF5A8297C230DF1557DB36C34B595`

## Results

| Case | Exact selected route | Source and evidence | Parent render | Result |
| --- | --- | --- | --- | --- |
| PK2-A | `packaging-graphics-and-sku-systems` + `typography-and-typesetting` | Only the barcode guide label changed; XML, dimensions, palette, IDs, protected-zone coordinates, exact wording and all other source were preserved. SVG `0355598B4BA399567A4C0DAB6BAECB3A6BD888E9A0B09CDE98F796328ED17D3D`; report `35FF2F742C53501741E3FBF448B14EB8656EC8D016F7D4891DCAB03FC1FCC0F4`. | `D55CA1171B58DD6230F18DE1EE465A6CFB2ECD6159EB5CF4F82D5B894BCDE5E1` shows both guide lines inside the protected box without crossing the back/glue fold. | Pass |
| Wayfinding | `physical-wayfinding-and-signage-systems` + `cartography-and-spatial-data` | XML, dimensions, palette, topology, route/sign/node IDs, north-up label, schedule and recovery trace passed; edits were limited to display geometry and evidence text. SVG `18C69389865233FEE5A13B4D6E58B47CF21E4C6199F8AF94B1621EAD63D26BC1`; report `AF636A15389F2479D446B0F7B5A5E1D99F27F936F68A9E28B2C99B48AC162148`. | `27CA902010DFD79661710CECA5286CDE041546C8129DE3F08F91F42DC4260BDE` removes the title and centre collisions, but `S-ENT-01` still obscures part of `NODE GAL-B` and `Gallery B`. | Fail; no retry |
| Mark | `logo-and-identity-mark-design` only | A and B were byte-preserved; only C geometry and its matching report paragraph changed. XML, dimensions, labels, colours, forbidden elements and all four C contexts passed. SVG `50687AF9B594CE898C624FC511B5D80C5E0B10DC3D02F83FA54326533883F178`; report `75023D96822A0F17D30589F26DDF4E35A6F21EF798BB3966F790892709576987`. | `E9692988D019A26F6A29B0B56AE75AA859DC6681C654936A74D358DDE33BB702` shows three disconnected folded rails around visible ground at 96 px, 24 px, reversed 24 px and 20 px. | Pass |

Child-side attempts to invoke unavailable `python` or `git` failed inside the
restricted PATH in PK2-A and Mark, and an initial exact-fragment replacement
failed in Wayfinding. These diagnostics remain in the raw events. Each call
then completed its source checks with available PowerShell. The parent reran
the decisive XML, source-diff, route, hash and render checks independently; the
failed child helper attempts do not supply positive evidence.

## Receipts and usage

| Case | Terminal state | Raw-events SHA-256 | Input | Cached input | Output | Provider total | Uncached input + output |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| PK2-A | completed in 112.945 s | `829E242E127E057606A3BB5F3F63BEEE122F6DF4B131C012D3B68925833CB2E8` | 132156 | 103680 | 5051 | 137207 | 33527 |
| Wayfinding | completed in 241.833 s | `1FFE5CC9D409C37A8C7730B5D72AE4970B531015AB10DC3EA5CED8577C242D81` | 214863 | 161408 | 11975 | 226838 | 65430 |
| Mark | completed in 140.551 s | `7B928544A5096D26326DE2DA627C111A5553A8CC94212116553DE651F8232020` | 200100 | 163968 | 6333 | 206433 | 42465 |
| **Total** | three calls | — | **547119** | **429056** | **23359** | **570478** | **141422** |

## Unchanged deterministic gates

- package validator: valid with 28 modules and the same twelve soft token-target warnings;
- package unit tests: 17/17 passed;
- direct route contract: 44/44 fixtures valid across 41 signals;
- successor v2 route contract: 10/10 cases valid;
- generated module index: current;
- Design/UI boundary: active Design retains strict UI and UI-only retains Greenfield fallback;
- Skill Creator quick validation: valid;
- executable package manifest: current at the candidate hash above;
- local Markdown links: 182 checked, zero missing;
- native Plan validator: 30 files, 20 Work Items, 28 Decisions, zero errors and warnings.

## Admission verdict and claim limit

The bounded parent-render mechanism repaired PK2-A and Mark, and all three Call
B routes remained exact. Wayfinding still failed visible professional quality
after its sole permitted repair. Therefore the three-of-three ADR-0028
admission gate fails and W-005 must remain paused. This evidence authorizes no
retry, package change, broad qualification, publication, installation, commit,
push, tag or release. It proves only the stated runs, sources, checks and parent
renders; it does not establish general visual competence or causal superiority.
