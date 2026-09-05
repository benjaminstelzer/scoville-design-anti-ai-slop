# W-021 second rendered-repair pass

Date: 2026-09-03  
Decision: [ADR-0029](../decisions/0029-admit-one-second-rendered-repair-pass.md)  
Predecessor evidence: [W-020 rendered-repair admission](w020-rendered-repair-admission.md)  
Candidate manifest: `81530628273139A1518B9D44A309CF10ED6FE41585E35A0D6C54C236F547D6DF`

## Frozen input and controls

The Wayfinding Call-B source, report and parent-render hashes matched the W-020
record before Call C:

- SVG: `18C69389865233FEE5A13B4D6E58B47CF21E4C6199F8AF94B1621EAD63D26BC1`
- report: `AF636A15389F2479D446B0F7B5A5E1D99F27F936F68A9E28B2C99B48AC162148`
- render: `27CA902010DFD79661710CECA5286CDE041546C8129DE3F08F91F42DC4260BDE`

The executable package manifest was current. Descriptor
`B3233B155F93DA6D274A63075C04F57033E94E80536C9B59D68C16228A6563D1`
passed package-copy, single-image and pinned-CLI dry-run preflight. One isolated
`gpt-5.6-terra` Medium call ran through pinned
`codex-cli 0.147.0-alpha.1.2` with workspace-write, no network and no approval
path. There was no retry, fourth call, reserve, SkillOpt proposal or package
edit.

## Call-C result

- terminal state: completed in 108.459 seconds;
- exact selected route: `physical-wayfinding-and-signage-systems` plus
  `cartography-and-spatial-data`;
- raw-events SHA-256:
  `4BBDF4C0DFBB797CF922F2B0B5A3A7B5D45028205C7F32F19E6A043CCCECCDA7`;
- output SVG SHA-256:
  `6FA37AC7CA00F16F41DEF97149699A4E61356A32F67CEEFDACFE1FD5CD50A63E`;
- output report SHA-256:
  `378B72F75355930323D1E86ADDC46855ADE716B988175086AB8C3218B933206E`;
- final parent-render SHA-256:
  `5A764C4C4B4D303B13ED2F16AC1BE648485DEC768D2B86251A18ADAB78596F8E`.

The SVG diff changes exactly the two Gallery B text elements: both move from
`x="1138"` to `x="1080"` and add `text-anchor="end"`; their text and y
coordinates remain unchanged. Every other SVG byte is preserved. The report
adds only the supplied-render observation, exact local repair and unrendered
child-output boundary. The child attempted unavailable `python` and `git`
helpers inside the restricted PATH; those failures remain in the raw events and
supply no positive evidence. Its available PowerShell checks completed, and the
parent independently verified XML and the complete source diff.

The parent rendered the final SVG exactly once through pinned Edge
`152.0.4191.53`. `NODE GAL-B` and `Gallery B` are fully visible to the left of
their node and do not touch the route, node, border, north-up block, arrival
panel or `S-ENT-01`. No other collision, clipping or misleading route geometry
is visible in the intended 1800 by 1200 render.

## Usage

| Input | Cached input | Output | Provider total | Uncached input + output |
| ---: | ---: | ---: | ---: | ---: |
| 206439 | 169344 | 4640 | 211079 | 41735 |

Combined W-020 plus W-021 use is 781557 provider-total tokens and 183157
uncached-input-plus-output tokens across four calls. The failed W-020
Wayfinding result remains visible and receives no retroactive pass.

## Final gates

- package validator: valid with 28 modules and the same twelve soft token-target warnings;
- package unit tests: 17/17 passed;
- direct route contract: 44/44 fixtures valid across 41 signals;
- successor v2 route contract: 10/10 cases valid;
- generated module index: current;
- Design/UI boundary: active Design retains strict UI and UI-only retains Greenfield fallback;
- Skill Creator quick validation: valid;
- executable package manifest: current at the candidate hash above;
- native Plan validator before lifecycle completion: 31 files, 21 Work Items,
  29 Decisions, zero errors and warnings.

## Admission verdict and claim limit

W-021 passes. The admitted bounded final set is PK2-A Call B, Wayfinding Call C
and Mark Call B. All retain exact routes, source structure and evidence
boundaries, and all final parent renders pass the named visible defects. This
admits the maximum-two-repair-pass mechanism for the next W-005 qualification
stage only when every comparator arm receives identical maximum call count,
renderer, image access, stop rules and budget, with first-call and final results
reported separately.

This does not erase W-020, prove general visual competence or establish causal
superiority. It authorizes no publication, installation, commit, push, tag or
release.
