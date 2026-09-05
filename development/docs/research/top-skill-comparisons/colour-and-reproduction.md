# Stage-2 GitHub Skill comparison: colour and reproduction

**Capture:** 2026-09-02T13:19:30Z  
**Decision served:** identify the three most-starred current, qualifying exact-domain Skills whose repositories contain at least E1 evidence; compare their demonstrated mechanisms with [the current executable](../../../../scoville-design-anti-ai-slop/references/colour-and-reproduction.md) and [the expert-depth audit](../reference-audits/colour-and-reproduction.md).  
**Ranking rule:** stars determine rank only after scope and evidence qualification. Evidence quality, visual quality, licence safety, and adoption value remain separate judgments.  
**Adoption lens:** [adoption-priority.md](../adoption-priority.md), with visible type quality, spacing/rhythm, negative space, hierarchy, subject-specific composition, responsive translation, role-based colour, and reproduction proof weighted above feature count.

## Result

Three qualifying repositories were found in the bounded current search.

| Rank by current stars | Repository and exact Skill | Stars at capture | Evidence level | What the evidence actually establishes |
|---:|---|---:|---|---|
| 1 | [yanliudesign/mono-color-skill — SKILL.md](https://github.com/yanliudesign/mono-color-skill/blob/de607fedfff647eaf5400e0aa43085787d7d1fca/SKILL.md) | 1,978 | **E2 contract / E1 visual** | Machine-readable design catalogs and deterministic schema/catalog checks exist; many inspectable poster outputs show the visual system. CI does not execute or score image generation, and examples are not proven eval outputs. |
| 2 | [nevertoday/zhongguo-traditional-colors — xxd colour Skill suite](https://github.com/nevertoday/zhongguo-traditional-colors/tree/4747ba361cb1ddcf3c95c3fe5e124e26585ab7f7/skills) | 1,179 | **E2 functional / E1 visual** | A working static colour workspace, screenshots, datasets, and many deterministic browser/data/contrast/responsive checks exist. No inspected run proves that an agent using the Skills produces the shown site or professionally correct print output. |
| 3 | [louisedesadeleer/color-correct — SKILL.md](https://github.com/louisedesadeleer/color-correct/blob/4c38e5cff615eef58ec3b3197a02b8df472a5f50/SKILL.md) | 23 | **E1** | Inspectable look contact sheets, LUTs, measurement scripts, and a concrete ffmpeg workflow demonstrate a before/after comparison mechanism. No automated test, independent review, or declared licence was found. |

Popularity and evidence do not point in the same direction. Rank 1 has the strongest visible editorial craft but is a narrow style system. Rank 2 has the strongest functional colour-tool and routing evidence but unresolved licence/provenance documentation. Rank 3 has the smallest audience but the most explicit measurement-to-preview correction loop. None covers colour appearance, semantic roles/states, accessible data encoding, ICC transforms, spot/overprint/material behaviour, and contract/physical proof together.

## Search and qualification boundary

### Search funnel

The current pass used authenticated GitHub code and repository search with variants around **colour/color, palette, accessibility, WCAG, data colour, CMYK, ICC profile, proof, print production, grading, HDR, BT.2020, Skill.md**, plus the candidates already identified in the per-reference audit. Repository metadata, exact Skill files, current tree contents, examples, tests/evals, workflows, licence files, and representative visual artifacts were inspected at pinned snapshots. Search was conducted in English and repository-native Chinese where surfaced.

The search is bounded to public GitHub and publicly linked materials reachable on 2026-09-02. GitHub code search is ranking-sensitive and cannot prove global exhaustiveness. Fork/mirror duplicates, broad UI/graphic-design Skills, pure converter commands, and Skills without exact colour/reproduction ownership were not substituted for missing candidates.

### Admission test

A repository qualified only when:

1. it contained a concrete Skill or directly usable agent instruction for colour judgment, colour application, or reproduction;
2. the exact mechanism was inspectable at a pinned commit;
3. the repository contained an inspectable output, example, functional fixture, or reproducible deterministic check relevant to that mechanism;
4. the evidence was not only a README claim;
5. licence and dependency limits could be stated rather than guessed.

### High-star near-misses

| Repository | Stars at capture | Why it was not ranked |
|---|---:|---|
| [clshortfuse/renodx — BT.2020 PNG generation Skill](https://github.com/clshortfuse/renodx/blob/1bf69897d646b6c558e334e5b34e2f3aa28b2032/.agents/skills/bt2020-png-generation/SKILL.md) | 1,917 | Exact and technically useful, with a concrete RGB16/PQ/cICP Python template, but no committed generated sample or Skill-scoped test. The Skill also points to absent repository paths such as AVIF/HDR findings and analysis helpers. Its implementation source is stronger than prose, but it does not satisfy this Stage-2 E1 output/eval gate. |
| [meodai/skill.color-expert](https://github.com/meodai/skill.color-expert/blob/6514810aaab15cdd0e4202af52a6afed27ed314d/SKILL.md) | 567 | A substantial sourced colour reference and trigger-eval corpus, but no rendered examples, output artifacts, or outcome tests. The trigger files test activation expectations, not visual or reproduction quality. E0 for this comparison. |
| [omer-metin/skills-for-antigravity — packaging-print-production](https://github.com/omer-metin/skills-for-antigravity/blob/e8dcf4e8737921a10088bd5c9eb65e81f74c051f/skills/packaging-print-production/SKILL.md) | 138 | Exact print concerns are named, but no Skill-specific output or production/eval artifact was found. Its generic CMYK, rich-black, bleed, type-size, and ink-limit recipes are not provider/process proof. E0. |
| [clawic/skills — colour Skill](https://github.com/clawic/skills/blob/f825206afbf1c697202533a9187be68c7b697e0e/skills/color/SKILL.md) | 17 | Broad colour routing and recipes, but no exact Skill output or test. E0. |
| [ilikescience/design-tokens-skill](https://github.com/ilikescience/design-tokens-skill/blob/787f9724ecc171715d132cdde2215a7ab88d8b0d/SKILL.md) | 15 | Structured light/dark token fixtures provide bounded E1 implementation evidence, but the repository had fewer stars than the three admitted candidates and no visual/reproduction proof. |

## Rank 1 — yanliudesign/mono-color-skill

### Snapshot, maintenance, and licence

- **Current snapshot:** [de607fedfff647eaf5400e0aa43085787d7d1fca](https://github.com/yanliudesign/mono-color-skill/tree/de607fedfff647eaf5400e0aa43085787d7d1fca), 2026-08-31T21:22:12Z.
- **Latest relevant Skill change:** 1ce7be1545b9dd92ff4862fe0bfd45260eab0a1f, 2026-08-30T19:09:10Z.
- **State:** active; GitHub archived flag false.
- **Skill/code licence:** root MIT.
- **Visual assets:** [ASSET-LICENSE.md](https://github.com/yanliudesign/mono-color-skill/blob/de607fedfff647eaf5400e0aa43085787d7d1fca/ASSET-LICENSE.md) excludes the examples directory from MIT and reserves all rights; the visual examples may be viewed and linked but not copied, modified, redistributed, sublicensed, sold, or used commercially without permission.
- **Data/assets:** JSON design catalogs and scripts are covered by MIT; the example PNGs are not. No example image may be imported into Scoville.

### Claimed scope and observed mechanism

The Skill claims one- or two-ink editorial image generation from a theme, phrase, object, or reference image. The actual mechanism is unusually concrete:

1. resolve subject, intent, exact wording, reference role, and faithful-versus-abstract representation;
2. compile a recipe manifest from machine-readable colour, typography, composition, carrier, rhythm, and imperfection catalogs;
3. assign each ink plate a content role;
4. choose one composition family and one focal event;
5. generate a raster prompt and image;
6. inspect full size and thumbnail;
7. retry once for named failures such as extra ink, weak plate roles, lost subject, bad text, cloned composition, or dispersed emphasis.

The repository contains 16 declared eval cases, a JSON schema, design-system validators, CI, a generated design-system board, and many visual examples. CI validates the eval contract and catalogs; it does not run an image model or compare generated images with Gold.

### Visible evidence under the adoption lens

The inspected design board, **Night Market**, and **Radio** examples visibly support:

- strong display/support type contrast and generally clean line breaking;
- subject/type collision rather than detached safe-zone composition;
- asymmetric focal hierarchy and controlled two-colour roles;
- quiet space that frames and intensifies the focal event;
- distinct subject-specific compositions rather than one card grid;
- coherent mechanical-print texture across subject, type, and colour.

They do not establish:

- correct typesetting in arbitrary language/script or long copy;
- accessible contrast, non-colour redundancy, or semantic state coverage;
- physical one-/two-ink separations, trapping, overprint, substrate response, spot-ink measurement, or press proof;
- cross-medium reproduction;
- reliable subject preservation or legal clearance;
- non-inferiority beyond this narrow style family.

The visible examples are polished, but the Skill’s own fixed percentages and palette aliases explain part of that consistency. Example quality cannot turn those settings into general colour law.

### What it does better than the current Scoville leaf

- It makes the role-before-swatch principle executable through an explicit **plate-role manifest**.
- It links colour area, focal event, release zone, image treatment, and type behavior in one inspectable artifact.
- It has real examples that demonstrate hierarchy, active negative space, and subject-specific limited-colour composition.
- It gives a bounded inspect-and-retry loop rather than stopping at prompt formulation.

Scoville remains stronger in accessibility scope, semantic role × state × theme × destination modeling, data-colour truth, ICC/profile ownership, screen/print nonidentity, provider proof, and exception governance.

### Mechanism to adapt through original synthesis

Adapt only this causal form:

> named colour/ink role + affected content + intended area/hierarchy + protected semantic meaning + representative render views + one targeted repair

For limited-colour work, a plate-role record can complement the planned Scoville role/state/theme/destination matrix. Full-size and thumbnail inspection can detect competing accents and lost hierarchy. The actual swatches, style language, catalogs, percentages, composition families, text, and examples must not be copied.

### Reject

- fixed 3:4 default as a quality rule;
- controlled two-ink as the general default;
- 70–85% dominant and 15–30% accent as a universal colour distribution;
- 25–55% empty paper, 5–9% margins, 45–80% object area, or 5–12× type jumps as general laws;
- topic-to-hue aliases and fixed palette pairings;
- serif/grotesk/mono recipes as proof of typesetting;
- simulated print texture or hex values as physical reproduction evidence;
- automatic English text for non-English tasks;
- hard style bans outside this intentionally narrow visual product.

## Rank 2 — nevertoday/zhongguo-traditional-colors

### Snapshot, maintenance, and licence

- **Current snapshot:** [4747ba361cb1ddcf3c95c3fe5e124e26585ab7f7](https://github.com/nevertoday/zhongguo-traditional-colors/tree/4747ba361cb1ddcf3c95c3fe5e124e26585ab7f7), 2026-08-31T03:51:10Z.
- **Latest relevant Skill-suite change inspected:** 22ded7bc1e8c6e4dea0fbf55791a295b1082fcb2, 2026-06-09T15:46:03Z.
- **State:** active; GitHub archived flag false.
- **Exact paths:** [colour brief](https://github.com/nevertoday/zhongguo-traditional-colors/blob/4747ba361cb1ddcf3c95c3fe5e124e26585ab7f7/skills/xxd-color-brief/SKILL.md), [accessible colour](https://github.com/nevertoday/zhongguo-traditional-colors/blob/4747ba361cb1ddcf3c95c3fe5e124e26585ab7f7/skills/xxd-accessible-color/SKILL.md), [data visualization](https://github.com/nevertoday/zhongguo-traditional-colors/blob/4747ba361cb1ddcf3c95c3fe5e124e26585ab7f7/skills/xxd-data-viz/SKILL.md), [existing-design audit](https://github.com/nevertoday/zhongguo-traditional-colors/blob/4747ba361cb1ddcf3c95c3fe5e124e26585ab7f7/skills/xxd-existing-design-audit/SKILL.md), and [print/packaging](https://github.com/nevertoday/zhongguo-traditional-colors/blob/4747ba361cb1ddcf3c95c3fe5e124e26585ab7f7/skills/xxd-print-packaging/SKILL.md).
- **Repository licence conflict:** the current root LICENSE is GPL-3.0 and GitHub detects GPL-3.0, while current English/Chinese README text still says MIT. The licence file is controlling evidence for this audit; the documentation contradiction blocks copying until the maintainer resolves it.
- **Fonts:** bundled Noto Serif SC subset carries SIL OFL 1.1.
- **Data and card imagery:** no separate, complete provenance/licence receipt was found for the 742 colour records, 8,904 harmony sets, or colour-card images. Contributor guidance asks for sources where possible but does not establish them. Do not import the data or images.

### Claimed scope and observed mechanism

This is a directly routed colour suite rather than one monolithic prompt:

- translate vague direction into temperature/lightness/saturation/cultural-signal/risk constraints;
- build palettes from a bounded named-colour set;
- apply roles to layouts;
- calculate accessible foreground/background pairs and add non-colour cues;
- select categorical, sequential, diverging, highlight, or semantic chart logic;
- audit existing colours through keep/merge/replace/remove/reserve;
- plan print/packaging roles and require printer profiles or physical proofs when production values are unavailable.

The repository includes a working static site, 742 image cards, 8,904 palette relationships, screenshots, and many deterministic scripts for contrast, page generation, manifests, responsive structure, accessibility dialogs, role models, and mobile layout. These tests establish data/site behavior. They do not test an LLM run against the Skill outputs or validate press colour.

### Visible evidence under the adoption lens

The inspected gallery, palette explorer, and scene-testing screenshots show:

- competent Chinese heading/body hierarchy and generally controlled navigation density;
- clear separation of browse, compare, scene-test, and role-preview tasks;
- colour in actual web/cover/layout mockups instead of isolated swatches only;
- explicit role previews for background, heading, body, button, and visual blocks;
- responsive and contrast tooling backed by deterministic scripts.

Limits visible in the same artifacts:

- most spatial systems are fixed UI/card templates rather than subject-specific composition;
- many colour-card examples use recurring decorative motifs and low-density display layouts rather than varied real content;
- harmony browsing shows palette relationships but not perceptual, CVD, semantic, or destination correctness;
- the screenshots do not prove actual agent-generated output;
- CMYK values printed on cards are not production transforms or proof.

### What it does better than the current Scoville leaf

- It demonstrates **selective routing** among brief, palette construction, application, accessibility, data, audit, tokens, brand, and print.
- It gives an existing-design audit explicit keep/merge/replace/remove/reserve actions.
- It exposes a useful repair order: inventory current roles, locate duplicate/orphan roles, select conservative/balanced/full repair, then validate the repaired role system.
- It tests real UI structures and colour roles rather than presenting palette prose only.
- Its print Skill correctly refuses to promise exact output from HEX when production specifications are missing.

Scoville remains stronger in generality, source/destination/profile assignment-versus-conversion, viewing conditions, CVD simulation limits, continuous/diverging/cyclic semantics, gradients, dark/forced modes, WCG/HDR, spot/process/overprint/material causality, and soft-versus-contract/physical proof.

### Mechanism to adapt through original synthesis

Adapt the **role inventory → defect class → bounded repair level → destination verification** sequence. The route split itself is useful prior art, but Scoville’s colour concerns do not yet have independent signal evidence sufficient to split the current leaf. A compact internal branch is preferable:

- ordinary colour judgment;
- accessible/semantic/data checks when material;
- external reproduction verification when physical output is material.

Do not copy the 742-colour dataset, harmony tables, names, decorative cards, or Skill prose. Do not attach a generic “traditional” or national cultural meaning to colours without current authority and context.

### Reject

- the fixed 742-colour universe as a general colour system;
- harmony-category membership as proof of visual fit;
- vague cultural-signal words as audience evidence;
- “maximize hue and lightness separation” without perceptual/output testing;
- a 12-category recommendation as a universal chart limit;
- WCAG ratios as a complete accessibility verdict;
- generated/synthetic CMYK values as print readiness;
- generic packaging ratios, shelf recipes, or material predictions;
- any reuse while the GPL-versus-MIT documentation conflict and dataset/image provenance remain unresolved.

## Rank 3 — louisedesadeleer/color-correct

### Snapshot, maintenance, and licence

- **Current snapshot and latest relevant change:** [4c38e5cff615eef58ec3b3197a02b8df472a5f50](https://github.com/louisedesadeleer/color-correct/tree/4c38e5cff615eef58ec3b3197a02b8df472a5f50), 2026-07-09T14:20:07Z.
- **State:** active; GitHub archived flag false.
- **Exact path:** [SKILL.md](https://github.com/louisedesadeleer/color-correct/blob/4c38e5cff615eef58ec3b3197a02b8df472a5f50/SKILL.md).
- **Licence:** no repository licence file or detected SPDX licence. The Skill, scripts, LUTs, GIF/video, screenshots, and look names must be treated as all-rights-reserved unless the owner states otherwise. Reference and independent synthesis only; no copying.
- **Dependencies:** ffmpeg, Python, Pillow, NumPy, optional yt-dlp, and the playback/encoding environment.

### Claimed scope and observed mechanism

The Skill colour-corrects and grades video through a closed loop:

1. probe codec/bit depth/colour metadata and sample 4–6 frames;
2. inspect frames and measure luma percentiles, per-tonal-band RGB casts, and saturation;
3. correct white balance, tint, exposure/contrast, saturation, and curves in a named order;
4. render nine look variants on one or preferably two representative frames;
5. let the user select;
6. preview side-by-side on multiple frames;
7. re-measure the result and run a bounded skin-shift gate;
8. render non-destructively and verify frames again.

Committed evidence includes two visible look contact sheets, a demo, 18 LUT files, and measurement/consensus/skin-check/LUT-generation scripts. There are no automated tests. The README’s claims that LUTs match within about 1/255 and that creator looks derive from median/IQR analysis were not backed by committed raw samples or a reproducible report in the inspected tree.

### Visible evidence under the adoption lens

The two inspected contact sheets show subtle, distinguishable changes across the same portrait and street scene. They support the key mechanism: a look that seems acceptable on skin can affect sky, foliage, walls, or screen-like neutrals differently, so one representative frame is weak evidence.

Typography, spacing, and composition evidence is deliberately minimal: large labels sit over a comparison grid. This candidate provides no typesetting, negative-space, layout, or subject-specific composition advantage. It is relevant because it demonstrates colour comparison and correction, not design composition.

### What it does better than the current Scoville leaf

- It operationalizes the audit’s missing **representative-sample loop**.
- It separates neutral correction from creative grading.
- It requires the agent to name the defect before changing filters.
- It combines visual judgment with measurements and asks whether the metric moved in the predicted direction.
- It makes user comparison a gate before a costly full render.
- It preserves the source by producing a new file and keeps debug artifacts.

Scoville remains broader and safer on semantic roles, accessibility, data colour, source/destination profiles, physical print, WCG/HDR, theme/state systems, and evidence labels.

### Mechanism to adapt through original synthesis

Adapt this general loop:

> sample representative states/frames/destinations → name the role/context failure → measure what can be measured → make one bounded correction → render before/after → inspect visually → re-measure predicted variables → approve or revise

For static design, “frames” become representative states, backgrounds, crops, themes, data cases, print simulations, and physical proofs. The mechanism is stronger than isolated swatch approval and transfers without copying the LUTs, look names, thresholds, or ffmpeg chains.

### Reject

- mandatory nine-look menu;
- named creator-derived looks without permission/provenance detail;
- fixed filter order as universal across all pipelines;
- 6,500 K as a neutral baseline and hard brightness/curve limits as general colour law;
- “skin is the referee” as a universal hierarchy or correctness test;
- YCbCr skin-box thresholds as proof across skin tones, lighting, camera pipelines, and makeup;
- hard-coded content-to-look mapping;
- “log needs a LUT first” without camera/transform/working-space detail;
- bt709-tag preservation or one player as cross-platform colour proof;
- undocumented licence and any scripts/LUTs/assets from the repository.

## Comparative capability matrix

| Decision-relevant capability | Current Scoville reference + audit | Mono Color | Chinese Traditional Colors | Color Correct |
|---|---|---|---|---|
| Role before swatch | Strong, general semantic roles; planned role × state × theme × destination matrix | Strong plate-role manifest, visible examples | Strong routed role model and migration actions | Not the concern; correction parameters rather than semantic roles |
| Accessibility/non-colour meaning | Scoped WCAG, redundant cues, CVD stress and simulation limits | Not demonstrated | Ratios and non-colour cues named; working contrast tools, but no user/CVD proof | Not demonstrated |
| Data semantics | Planned sequential/diverging/cyclic/categorical/threshold distinctions | None | Sequential/diverging/categorical/highlight branching, but generic distance logic | None |
| Screen/print ownership | Named source → transform → destination → proof; profile assignment/conversion distinction | Simulated one-/two-ink aesthetic only | Correctly asks for provider profile/proof when unavailable; otherwise shallow | Actual digital video transform; no print |
| Representative evidence | Required actual-size/state/theme/destination views; still unimplemented | Full-size + thumbnail and many examples | Site screenshots and deterministic functional checks | Strongest representative-frame before/after loop |
| Physical proof | Provider profiles, separations, ink/substrate, contract/production proof | None | Checklist and warning, no measured print artifact | None |
| Typography/typesetting evidence | Colour owns legibility relation, not type curriculum | Strong display hierarchy in a narrow style, fixed recipes | Competent Chinese UI/card hierarchy, template-bound | Comparison labels only |
| Spacing/negative space | Colour should preserve hierarchy; Composition owns spatial system | Visible active paper and focal/release contrast, but fixed percentages | Functional UI spacing; little subject-specific composition | Not applicable |
| Exception/claim ceiling | Explicit rule/scope/risk/compensation/owner/proof | Style-specific hard rules dominate | Some conditional states; no full exception record | User choice, but fixed workflow and thresholds |
| Independent outcome evidence | None yet; open tests planned | None | None | None |

## Adoption decision

### Adopt or adapt

1. **Representative comparison set.** From Color Correct, sample several states/frames/backgrounds/destinations before approval. Render the correction before full output and verify that measured changes match the causal hypothesis.
2. **Explicit role manifest.** From Mono Color, state which content a colour or plate owns and how much visual authority it should have, but avoid numeric area recipes.
3. **Repair levels.** From Chinese Traditional Colors, preserve working roles and choose conservative, balanced, or systemic repair by actual defect rather than rebuilding reflexively.
4. **Machine-readable handoff.** Record source/destination spaces, semantic roles, state/theme/destination variants, evidence and unresolved fields in a compact artifact that can be deterministically checked.
5. **Visible proof under the adoption lens.** Colour changes must be inspected with the actual type, spacing, negative space, hierarchy, image, data, state, and medium. A colour-only tool cannot claim those relationships without the rendered artifact.

### Do not adopt

- fixed swatches, harmony wheels, topic-to-hue meanings, palette counts, area percentages, or text-scale recipes;
- national/traditional colour lists without item-level provenance and audience authority;
- style catalogues or creator-derived “looks” as general colour expertise;
- simulated paper/ink texture as physical reproduction;
- HEX/CMYK labels as profile transforms;
- isolated contrast, CVD simulation, one frame, one monitor, or one screenshot as final proof;
- external prose, examples, datasets, LUTs, or assets whose licence is absent, conflicting, restricted, or does not clear underlying rights.

### Architecture impact

The Stage-2 evidence does **not** overturn the existing audit recommendation to retain one colour-and-reproduction leaf. The public candidates are either narrow style systems, a culturally bounded colour workspace, or a video-grade loop. None demonstrates a superior general split between colour judgment and reproduction, and none supplies the cross-boundary causal reasoning the current audit requires.

The cheapest decision-changing test remains the audit’s open set: role/state/theme generation, CVD/non-colour repair, data-scale discrimination, source/profile/destination conversion, spot/overprint/substrate critique, gradient/dark/HDR cases, and cross-media physical proof. Compare the current and proposed Scoville payload against the transferable mechanisms above, not against their recipes or visual assets.

## Evidence and claim limits

- Stars are a popularity snapshot, not capability, safety, openness, or visual-quality evidence.
- All three ranked repositories are maintainer-authored. No E3 independent evaluation or external adoption evidence was found for the exact Skills.
- Static images prove that an output exists. They do not prove prompt causality, repeatability, rights, accessibility, colour accuracy, print fidelity, or expert judgment.
- CI/schema checks prove only the assertions they execute. Mono Color’s CI does not render; Chinese Traditional Colors’ tests primarily validate the product site/data; Color Correct has no committed automated tests.
- Visual inspection was limited to representative committed images, not every artifact.
- No physical print, calibrated display, ICC transform, spectrophotometric measurement, HDR reference path, or human accessibility/user study was executed in this research pass.
- The comparison supports mechanism adoption through original synthesis only. It does not authorize copying protected expression, examples, datasets, LUTs, style names, or third-party visual material.

**Stage-2 conclusion:** Mono Color is the most popular qualifying craft example, Chinese Traditional Colors is the strongest qualifying routed functional colour system, and Color Correct contributes the strongest closed correction/preview loop. Scoville should adapt their evidence mechanisms while rejecting their fixed style recipes, unresolved rights/licences, and false reproduction shortcuts.
