# Stage-2 GitHub Skill comparison: media production and handoff

**Capture:** 2026-09-02T13:47:00Z  
**Decision served:** identify the three most-starred current, qualifying exact-domain Skills with E1+ evidence for editable artifact generation, rendering, preflight, export, and handoff; compare them with [the current executable](../../../references/media-production-and-handoff.md) and [the expert-depth audit](../reference-audits/media-production-and-handoff.md).  
**Ranking rule:** stars rank repositories only after exact-domain and evidence qualification. Popularity, evidence strength, visible craft, production correctness, and licence safety remain separate.  
**Adoption lens:** [adoption-priority.md](../adoption-priority.md), with visible type, spacing/rhythm, negative space, hierarchy, subject-specific composition, and medium-correct proof weighted above feature count.

## Result

Three qualifying repositories were found in the bounded current search.

| Rank by current stars | Repository and exact Skill | Stars at capture | Evidence level | What the evidence actually establishes |
|---:|---|---:|---|---|
| 1 | [anthropics/skills — `skills/pptx/SKILL.md`](https://github.com/anthropics/skills/blob/53048666b05b4799081517d00e09e0a2dd688678/skills/pptx/SKILL.md) | 173,167 | **E2 functional / E0 visual** | Inspectable OOXML validation, rendering, thumbnail, cleanup, overflow, and font-substitution utilities form a reproducible deck QA path. No committed generated deck, test result, or visual benchmark proves the Skill's design advice. |
| 2 | [K-Dense-AI/scientific-agent-skills — `skills/pptx-posters/SKILL.md`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/1dd0fccf46fc3c9855c4a0c313a0c57fe4319883/skills/pptx-posters/SKILL.md) | 41,996 | **E2 functional / E1 visual** | A strict artifact manifest, local generator, package/layout/palette/asset/export validators, extensive executable tests, and inspectable poster/workflow imagery exist. The evidence supports this one-slide PPTX pipeline, not general print readiness or visual excellence. |
| 3 | [JetBrains/skills — `slides/SKILL.md`](https://github.com/JetBrains/skills/blob/e0f258b5cfed145015cb3e48da9a97947f7c4ed7/slides/SKILL.md) | 334 | **E2 functional / E0 visual** | Rebuildable PptxGenJS source, raster rendering, montage, overflow detection, and font-resolution inspection are directly usable deterministic checks. The repository contains no Skill-scoped example deck or visual outcome comparison. |

The star order is not the capability order. K-Dense has the strongest traceable artifact-and-preflight contract. Anthropic has the broadest PPTX authoring failure corpus but a restrictive proprietary licence and unsupported visual recipes. JetBrains has the smallest clear source-render-check-deliver loop. None demonstrates a complete cross-media contract spanning SVG, raster, accessible PDF, PDF/X/provider proof, editable documents, decks, motion, physical print, and authority-bound handoff.

## Search and qualification boundary

Authenticated GitHub code, repository, and tree search covered combinations of `SKILL.md`, artifact, editable, render, export, preflight, PDF, PDF/X, SVG, print, PPTX, DOCX, slide, poster, overflow, handoff, proof, manifest, and receipt. Candidate Skill files, current repository state, exact-path history, licences, scripts, tests, examples, and representative committed imagery were inspected at pinned commits.

A repository qualified only when it contained a concrete Skill or directly usable agent instruction that owned artifact production/handoff rather than generic file manipulation, plus an inspectable output/example or a reproducible deterministic check tied to that mechanism. A converter recipe, README feature claim, UI screenshot, or unrelated repository test was E0. GitHub search ranking and indexing prevent a claim of global exhaustiveness.

### High-star and close near-misses

| Repository | Stars at capture | Why it was not ranked |
|---|---:|---|
| [claude-office-skills/skills](https://github.com/claude-office-skills/skills/tree/9c4c7d5cd2813a8936bf2c9fdb174ea883b85a11) | 433 | Contains many converter/manipulation Skills and one test PDF, but no inspected Skill-scoped output or production test establishes its broad visual-preservation claims. Generic file tooling was explicitly out of scope. |
| [aws-samples/sample-spec-driven-presentation-maker](https://github.com/aws-samples/sample-spec-driven-presentation-maker/tree/main/sdpm) | 128 | Qualifying lower-star alternative with PPTX fixtures and extensive functional tests. It did not outrank JetBrains by stars; its cloud/application architecture and style-library ownership are larger dependencies than a leaf mechanism requires. |
| [Noi1r/powerpoint-skill](https://github.com/Noi1r/powerpoint-skill/tree/main/powerpoint-slides) | 117 | Qualifying lower-star deck Skill with a committed source/deck example, but narrower test and preflight evidence than the ranked repositories. |
| [omer-metin/skills-for-antigravity — packaging print production](https://github.com/omer-metin/skills-for-antigravity/blob/e8dcf4e8737921a10088bd5c9eb65e81f74c051f/skills/packaging-print-production/SKILL.md) | 138 | Exact print vocabulary but E0: no Skill-scoped production artifact or proof. Universal CMYK, bleed, rich-black, ink-limit, type-size, and box-clearance recipes cannot substitute for the actual provider/process. |
| [metedata/pdf-proof](https://github.com/metedata/pdf-proof/blob/8ba4cf66645958d2b25eec874afe0a0442287b9e/SKILL.md) | 76 | Strong E1 localized PDF evidence output, but it verifies specific text values rather than generating, preflighting, or handing off production artifacts. Its localization mechanism is more relevant to Critique/Validation. |

## Rank 1 — anthropics/skills PPTX

### Snapshot, state, licence, and dependencies

- **Current snapshot:** [`53048666b05b4799081517d00e09e0a2dd688678`](https://github.com/anthropics/skills/tree/53048666b05b4799081517d00e09e0a2dd688678), committed 2026-09-01T18:30:38Z.
- **Latest exact-Skill change:** `fa0fa64bdc967915dc8399e803be67759e1e62b8`, 2026-07-17T02:47:37Z.
- **State:** active; GitHub archived flag false.
- **Exact Skill/code/assets licence:** [`skills/pptx/LICENSE.txt`](https://github.com/anthropics/skills/blob/53048666b05b4799081517d00e09e0a2dd688678/skills/pptx/LICENSE.txt) is proprietary. It prohibits extraction/retention outside the service, reproduction, derivatives, and distribution except as the applicable Anthropic agreement permits. No expression, scripts, palette tables, or assets may be imported into Scoville.
- **Dependencies:** PptxGenJS, Node, Python, markitdown, Pillow, defusedxml, lxml, LibreOffice, and Poppler; optional React icon/sharp tooling. Their independent licences and installed versions remain separate from the proprietary Skill terms.

### Scope, actual mechanism, and proof

The Skill owns creation, editing, reading, and QA of PPTX/POTX. Its strongest mechanism is not its style advice but its source-and-receipt loop:

1. keep editable PptxGenJS or OOXML authority source;
2. establish layout before content and preserve native charts/objects where possible;
3. validate relationships, content types, schema, slides, and chart structures;
4. extract exact content and reject placeholders;
5. rasterize every slide, inspect the full set, repair source, regenerate PDF/PNGs, and recheck;
6. deliver editable deck plus required rebuild assets.

The repository includes deterministic validators and render helpers, so E2 functional qualification is warranted. It contains no committed Skill output or before/after deck benchmark. Claims about impressive, topic-specific, or professional visual design therefore remain E0.

### Adoption-priority visual lens

No committed deck supports typography, spacing, negative-space, hierarchy, or composition claims. The prose does identify useful failure signatures—font substitution, text overflow, box padding, collision, unequal gaps, alignment, and placeholder residue—but then mixes them with fixed font-size tables, margin/gap numbers, palette recipes, mandatory visual elements, layout menus, and house-style bans. Those values may be tool-context starting points; they are not general design evidence.

### Better mechanism and original synthesis

Adopt the **dual validation lane**: deterministic package/content validation plus fresh rendered inspection, each producing a distinct receipt. Preserve editable chart/text ownership and fix the authoring source rather than the packed derivative. Carry renderer/font-engine identity into the receipt so a LibreOffice render is not mistaken for PowerPoint proof.

Reject proprietary expression, fixed typography/spacing recipes, mandatory imagery, style bans, palette catalogs, one-pass limits as quality laws, and any inference that a successful LibreOffice render proves Office interoperability, accessibility, projection, printing, or provider acceptance.

## Rank 2 — K-Dense PPTX posters

### Snapshot, state, licence, and dependencies

- **Current snapshot:** [`1dd0fccf46fc3c9855c4a0c313a0c57fe4319883`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/1dd0fccf46fc3c9855c4a0c313a0c57fe4319883), committed 2026-08-31T17:14:01Z.
- **Latest exact-Skill change:** `2f2022de186dbf73f4c3b6e37b9856fa5cb66db4`, 2026-07-26T16:54:14Z.
- **State:** active; GitHub archived flag false.
- **Licence:** exact `pptx-posters` frontmatter and root [`LICENSE.md`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/1dd0fccf46fc3c9855c4a0c313a0c57fe4319883/LICENSE.md) say MIT. Templates, tests, and repository-authored documentation have no separate restriction detected. Supplied author assets and fonts remain governed by their own provenance/licences; the Skill explicitly requires those records.
- **Dependencies:** exact generation pins `python-pptx==1.0.2`, `Pillow==12.3.0`, and `lxml==6.1.1`; PowerPoint, accessibility inspection, PDF export, printer proof, and author approval remain manual/external.

### Scope, actual mechanism, and proof

This Skill produces one editable, macro-free scientific poster from a strict local JSON manifest. It binds exact content, every element and asset, provenance/licence, hashes, reading order, geometry, physical/output requirements, author approval, and export plan before generation. Scripts then validate the manifest, inventory bounded images, audit declared palette pairs, plan export, generate without overwrite, inspect ZIP/XML security, and check bounds/overlap/reading order/font size. The test suite exercises approval invalidation, unsafe relationships, macro/embedded payloads, asset signatures, path traversal, effective DPI, palette findings, physical scaling, layout, and output non-overwrite.

This is the strongest E2 evidence in the ranking. Committed workflow/poster imagery provides E1 visual evidence, but it is documentation and example output rather than an independent judged result. Manual PowerPoint, accessibility, author, PDF, colour-conversion, printer, and physical-proof gates are explicitly outside automation.

### Adoption-priority visual lens

The visible workflow poster is readable and ordered, with clear heading levels and grouped process stages. It is also a conventional boxed three-column academic system with dense microcopy and little subject-specific composition. It does not prove sophisticated typesetting or output at viewing distance. The safer `pptx-posters` Skill avoids the older `latex-posters` Skill's blanket AI-imagery percentages and hard whitespace/content limits; those older recipes must not leak into the shared production contract.

### Better mechanism and original synthesis

Adopt the **hash-bound authority graph and receipt chain**:

`approved manifest/input hashes -> non-destructive editable generation -> package/layout/asset/export receipts -> actual application/access review -> exported-PDF receipt -> provider/physical proof`

This sharpens the current Scoville audit's artifact contract. Also adapt fail-closed unresolved-rights/provider fields, approval invalidation after any content change, local-only asset resolution, separate design-versus-physical dimensions, and explicit automation ceilings.

Reject the single-slide/PPTX security profile as a universal format architecture, exact dependency pins in the conceptual leaf, one manifest schema as canonical ownership, WCAG sRGB contrast as print proof, declared DPI/font thresholds as universal rules, and any suggestion that package safety or bounds checks establish typography, accessibility, scientific correctness, colour conversion, or print readiness.

## Rank 3 — JetBrains Slides

### Snapshot, state, licence, and dependencies

- **Current snapshot:** [`e0f258b5cfed145015cb3e48da9a97947f7c4ed7`](https://github.com/JetBrains/skills/tree/e0f258b5cfed145015cb3e48da9a97947f7c4ed7), committed 2026-06-29T16:39:58Z.
- **Latest exact-Skill change:** `985a353f81a79d5c6c2823fe80caf8bb06e96263`, 2026-04-28T15:14:51Z.
- **State:** active; GitHub archived flag false.
- **Licence:** exact [`slides/LICENSE.txt`](https://github.com/JetBrains/skills/blob/e0f258b5cfed145015cb3e48da9a97947f7c4ed7/slides/LICENSE.txt) is Apache-2.0. No separate licence was found for the small Skill icon assets; do not import them because they add no mechanism value.
- **Dependencies:** PptxGenJS, Python, python-pptx, NumPy, Pillow, LibreOffice, and renderer/font tooling; their runtimes and licences are external.

### Scope, actual mechanism, and proof

The Skill creates or edits PPTX while preserving rebuildable JavaScript, native text/charts when practical, intentional crop/contain behavior, and final `.pptx` plus assets. Its deterministic utilities render slides, create a montage, detect overflow by enlarging the slide canvas and examining the padded render, and report font substitution. These checks qualify as E2 functional evidence, but no Skill-scoped deck, test run, or before/after artifact establishes output quality.

### Adoption-priority visual lens

The Skill correctly requires explicit theme fonts, deliberate text boxes, stable spacing, source/reference aspect-ratio matching, and render review. No visible evidence supports its typesetting or composition, and “stable spacing” is not a diagnostic system. It does not inspect paragraph rhythm, trapped gaps, hierarchy, density, series pacing, or projection/print behavior.

### Better mechanism and original synthesis

Adapt its compact **editable source + target render + montage + focused overflow/font diagnostics + rebuildable delivery** pattern as the minimum deck branch inside the larger artifact contract. The padded-canvas overflow test is a useful narrow receipt when its renderer/version and tolerance are recorded.

Reject 16:9 as a default outside an unspecified deck context, implicit reliance on one renderer, copied implementation scripts when an equivalent original check suffices, and any promotion of overflow/font checks to visual, accessibility, Office, or production proof.

## Comparative capability matrix

| Capability | Current Scoville reference + audit | Anthropic PPTX | K-Dense PPTX posters | JetBrains Slides |
|---|---|---|---|---|
| Authority source | Plans editable master; audit requires authority graph and hashes | Editable JS/OOXML, but no manifest/hash contract | Strong manifest, hashes, approvals, no-overwrite | Editable JS plus deck/assets |
| Syntax/package proof | Planned per-format validators | Strong OOXML/schema/relationship/chart checks | Strong bounded ZIP/XML/security checks and tests | Focused overflow/render/font checks; weaker package proof |
| Render loop | Intended + diagnostic context; source repair | Every slide, content dump, fix/rerender | Manual app/PDF/physical gates after deterministic checks | Render every slide + montage + focused rerun |
| PDF/print proof | PDF/X/provider/profile/separation/physical proof are conditional | Export/render only; no provider or physical proof | Explicitly blocks CMYK/print claims pending provider proof | Not established |
| SVG/raster/motion/doc coverage | Planned branches with one shared causal spine | PPTX only | One-slide PPTX poster only | PPTX only |
| Accessibility | Delivered-format semantics/manual/AT proof planned | Visual/content QA; no complete delivered-format proof | Explicit manual reading-order/AT/alt-text gate | Not established |
| Type/spacing/composition evidence | Required visible proof under subject and medium | E0 visual; fixed recipes in prose | E1 conventional academic poster; strong fit checks, limited craft range | E0 visual |
| Licence/adoption safety | Original synthesis only | Proprietary; no copying/derivatives | MIT, with third-party assets still separately owned | Apache-2.0 |

## Adoption decision

### Adopt or adapt

1. **Hash-bound artifact contract.** Adapt K-Dense's manifest/approval invalidation into a format-neutral authority graph: purpose, source inputs, derivatives, versions/hashes, receiver, rights, geometry, colour, accessibility, owners, and unresolved risk.
2. **Layered receipts.** Keep source-created, syntax/package-validated, render-inspected, semantic/access-tested, export-verified, and provider/physical-proofed distinct. Each receipt names the exact target hash, tool/version, conditions, date, result, and authority.
3. **Source-first repair.** From all three, fix the editable authority, rebuild, regenerate the exact target, and invalidate earlier render/proof receipts after material input changes.
4. **Target plus diagnostic renders.** Use full-resolution target output, montage/thumbnail/distance view, and detail views selected by medium. Inspect type, spacing, negative space, hierarchy, crop, sequence, and content extremes—not only bounds.
5. **Format adapters behind one spine.** Keep SVG/raster, PDF/print, document/deck, motion, and UI handoff as internal gates until independent routing data supports flat leaves. Do not impose a PPTX manifest on every artifact.

### Reject

- proprietary Anthropic expression, scripts, assets, or derivative wording;
- fixed font sizes, margins, gap scales, palette percentages, visual counts, poster word counts, and whitespace quotas as universal production rules;
- PDF/X, tagged PDF, valid XML/OOXML, embedded fonts, green contrast checks, or a clean render as “production ready”;
- one renderer, monitor, viewer, or soft proof as application interoperability, accessibility, supplier, or physical proof;
- toolchain-specific file trees, cloud services, exact dependency pins, or security profiles as canonical Scoville ownership;
- destructive outlining, flattening, rasterization, or derivative patching without a preserved authority source and named reason.

## Evidence and claim limits

- Stars are a current popularity snapshot, not evidence of output quality, safety, openness, or production acceptance.
- No ranked Skill has E3 independent evaluation or demonstrated cross-media professional coverage.
- Anthropic and JetBrains qualify through reproducible deterministic checks but provide no Skill-scoped visible outcome. Their typography, spacing, and composition claims remain unsupported.
- K-Dense's tests strongly establish schema, package, layout, security, and artifact-contract behavior; they cannot establish visual quality, content truth, accessibility, colour match, printer acceptance, or physical output.
- Representative committed imagery was inspected, not every asset or generated artifact. No local deck generation, PowerPoint round trip, PDF/X validation, assistive-technology test, calibrated proof, or physical print was run in this pass.
- Mechanisms may inform original synthesis only. Exact proprietary text is prohibited; permissively licensed code still carries notice obligations and third-party dependency/asset rights.

**Stage-2 conclusion:** the strongest adoption target is K-Dense's hash-bound, fail-closed artifact/receipt chain, combined with the source-render-repair discipline shared by all three. Scoville should keep its broader format-neutral ownership and proof boundaries, and reject visual recipes or tool success as production evidence.
