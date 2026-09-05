# Stage-2 GitHub Skill comparison: imagery and art direction

**Capture:** 2026-09-02T13:19:30Z  
**Decision served:** identify the three most-starred current, qualifying exact-domain Skills whose repositories contain at least E1 evidence; compare their demonstrated mechanisms with [the current executable](../../../../scoville-design-anti-ai-slop/references/imagery-and-art-direction.md) and [the expert-depth audit](../reference-audits/imagery-and-art-direction.md).  
**Ranking rule:** stars determine order only after exact-scope and E1 qualification. Evidence quality, visual quality, rights, and adoption value remain separate.  
**Adoption lens:** [adoption-priority.md](../adoption-priority.md), with visible type quality, relationship-based spacing, negative space, hierarchy, subject-specific composition, responsive preservation, and image integrity weighted above prompt length or provider count.

## Result

Three qualifying repositories were found and ranked. All three are E1. None has reproducible Skill-specific visual evaluation or independent E3 evidence.

| Rank by current stars | Repository and exact Skill | Stars at capture | Evidence level | What the evidence actually establishes |
|---:|---|---:|---|---|
| 1 | [jau123/MeiGen-AI-Design-MCP — OpenClaw image/video Skill](https://github.com/jau123/MeiGen-AI-Design-MCP/blob/9f51ef065a68ffcc16701b2769726b8fe820095e/openclaw/SKILL.md) and [product-photoshoot workflow](https://github.com/jau123/MeiGen-AI-Design-MCP/blob/9f51ef065a68ffcc16701b2769726b8fe820095e/plugin/skills/product-photoshoot/SKILL.md) | 1,737 | **E1** | Committed sample images, a working provider/tool contract, and manual smoke scenarios show a generation-routing workflow. The scenarios are not automated and the Skill explicitly forbids inspecting/describing generated results. |
| 2 | [liyue-aigc/female-portrait-director — SKILL.md](https://github.com/liyue-aigc/female-portrait-director/blob/8cddecd6786d187688e8e89a1f606540186a962f/SKILL.md) | 1,451 | **E1** | Multiple committed portrait outputs and prompt examples demonstrate a narrow portrait-direction system. No automated outcome tests, source-to-output preservation fixtures, or independent review were found. |
| 3 | [joeseesun/qiaomu-mondo-poster-design — SKILL.md](https://github.com/joeseesun/qiaomu-mondo-poster-design/blob/e82e411c403ca5a0327a85682c658ad155cd9cbb/SKILL.md) | 1,155 | **E1** | Many committed poster/cover images visibly demonstrate symbolic metaphor, figure-ground, screen-print treatment, and type hierarchy. No tests, rights receipts, or prompt-to-output provenance were found. |

The popularity order is not the adoption order. MeiGen has the strongest provider workflow and the weakest inspection contract. Female Portrait Director has the deepest narrow photographic parameter propagation and a heavily gendered style corpus. Qiaomu shows the strongest visible metaphor/negative-space/type composition and the most severe imitation, trademark, quotation, and provenance problems. The current Scoville reference is less visually evidenced but materially stronger on selection, sequence, crop meaning, documentary modes, prohibited inventions, access, rights, and proof ceilings.

## Search and qualification boundary

### Search funnel

The current pass used authenticated GitHub code and repository search with variants around **imagery, photography, illustration, art direction, image generation, portrait, product photography, image sequence, picture editing, responsive crop, hero image, reference preservation, visual integrity, Skill.md**, plus the candidates from the per-reference audit. Repository metadata, exact Skill files, trees, examples, tests/evals, workflows, licence files, asset notices, and representative images were inspected at pinned snapshots.

Search was public-GitHub-first, in English and repository-native Chinese where surfaced, through 2026-09-02. Code-search ranking and indexed public files cannot prove global exhaustiveness. Broad UI/website Skills, video-only direction, model wrappers without art-direction behavior, mirrors, and Skills without E1 evidence were not substituted.

### Admission test

A repository qualified only when:

1. a concrete Skill or directly usable agent instruction materially owned still-image generation, photography, illustration, or art direction;
2. the exact mechanism was inspectable at a pinned commit;
3. at least one committed example/output or relevant reproducible artifact existed;
4. the output was inspected, not accepted from a README adjective;
5. licence, asset, provider, and evidence limitations could be reported.

Static output can qualify at E1 even when it demonstrates a bad mechanism. Qualification means “inspectable,” not “safe” or “better.”

### High-star near-misses and lower qualifiers

| Repository | Stars at capture | Disposition |
|---|---:|---|
| [YouMind-OpenLab/nano-banana-pro-prompts-recommend-skill](https://github.com/YouMind-OpenLab/nano-banana-pro-prompts-recommend-skill/blob/3b584cb414ed89f9738dc7c5101221f71d460273/SKILL.md) | 1,843 | Higher than every ranked repository but excluded: only README and Skill files were present; no example, test, eval, output, asset, or licence file. E0. |
| [op7418/guizang-material-illustration](https://github.com/op7418/guizang-material-illustration/blob/cf26e194ce075cd205329abab29cc71fda3e78b2/SKILL.md) | 1,097 | Exact illustration prompt workflow, but only the Skill, README, and a prompt template were present. No output/test and no detected licence. E0. |
| [GiMi-Xiaomi/gimi-illustration-skill](https://github.com/GiMi-Xiaomi/gimi-illustration-skill/blob/0f602eaf5c50c8b0c7a4619ce53095cfc9e30622/SKILL.md) | 651 | Qualifying E1 with many three-style examples and a reference-lock workflow, but below the third-ranked repository by stars. Gimi character/reference/calibration assets have a separate restrictive IP notice. |
| [op7418/Document-illustrator-skill](https://github.com/op7418/Document-illustrator-skill/blob/8344815d407cc25cc04c327557f36ed839f0aaef/SKILL.md) | 588 | Excluded. The examples directory explicitly says its images are placeholders; the scripts/styles claimed in README were absent from the inspected tree. A remote cover alone does not prove the exact workflow. E0. |
| [vibeeval/vibecosystem — art-director](https://github.com/vibeeval/vibecosystem/blob/3b763b1fb288f57bfa3cce76ef18184b96461a78/skills/art-director/SKILL.md) | 530 | Exact label but no art-director-specific examples, tests, or outputs. Repository GIFs demonstrate the broader orchestration product, not this Skill’s image outcomes. E0. |
| [jiahuiqu17/paper-signal](https://github.com/jiahuiqu17/paper-signal/tree/7567ff05f93fe525bf886b3a0dce36903ab8c43b/skills) | 108 | Lower-star qualifying candidate with unusually strong artifact records, subject routes, series outputs, preservation manifests, visible QA, and deterministic artifact/eval-contract tests. Visual outcome remains maintainer-reviewed E1; its tests do not score images. |
| [kangarooking/design-image-studio](https://github.com/kangarooking/design-image-studio/blob/dc43ec482fd0e2452b9feb75d82344467690e0dd/SKILL.md) | 98 | Lower-star qualifying E1 with committed poster/product/infographic outputs and a design-brief compiler. Several outputs contain garbled text, generic layouts, and unreceipted brands/assets; no outcome tests were found. |

## Rank 1 — jau123/MeiGen-AI-Design-MCP

### Snapshot, maintenance, licence, and dependencies

- **Current snapshot and latest relevant Skill change:** [9f51ef065a68ffcc16701b2769726b8fe820095e](https://github.com/jau123/MeiGen-AI-Design-MCP/tree/9f51ef065a68ffcc16701b2769726b8fe820095e), 2026-08-05T12:09:44Z.
- **State:** active; GitHub archived flag false.
- **Exact paths:** [openclaw/SKILL.md](https://github.com/jau123/MeiGen-AI-Design-MCP/blob/9f51ef065a68ffcc16701b2769726b8fe820095e/openclaw/SKILL.md), [product-photoshoot/SKILL.md](https://github.com/jau123/MeiGen-AI-Design-MCP/blob/9f51ef065a68ffcc16701b2769726b8fe820095e/plugin/skills/product-photoshoot/SKILL.md), plus visual-creative and social-thumbnail sibling Skills.
- **Repository licence:** MIT.
- **Visual assets:** no separate asset licence or provenance ledger was found for the committed samples.
- **Remote data and services:** the claimed 1,446 prompt entries, thumbnails, provider models, MeiGen cloud, and npm package behavior are remote dependencies with their own uninspected/current terms. Root MIT does not establish reuse rights in server-side prompts, model outputs, trademarks, or depicted likenesses.
- **Observed asset risk:** inspected samples reproduce the CHANEL name/product trade dress and a likely recognizable celebrity-like portrait. No source, consent, trademark, likeness, or output-rights receipt accompanied them.

### Claimed scope and actual mechanism

The top-level Skill is a multi-provider image/video tool router:

1. search a curated prompt gallery or enhance a short brief;
2. choose single, multi-direction, multi-step, edit/reference, or provider-workflow mode;
3. require confirmation before batches and videos;
4. route to MeiGen cloud, local ComfyUI, or OpenAI-compatible providers;
5. preserve local reference-image paths through internal compression/upload;
6. track generation IDs and avoid duplicate paid retries;
7. return exact URLs/paths from tool output.

The product-photoshoot sub-Skill requires a product reference and proposes four distinct directions: lifestyle, macro, scale/context, and marketing layout. It then asks which paid calls to execute.

The critical actual constraint is explicit: the agent is told it **cannot see generated images** and must never describe them. There is no mandatory view/inspection step after generation. This is a functional delivery policy, not art-direction validation.

The repository’s eval scenarios are a manual checklist for calls, confirmations, reference paths, retries, provider errors, and language. They are not automated and do not assess image fidelity or visual quality.

### Visible evidence under the adoption lens

The inspected minimal, botanical, model, and luxury examples show:

- clean commercial lighting and material rendering;
- a strong copy zone in the minimal product shot;
- recognizable product-label typography in some samples;
- varied foreground/context density across product-only, botanical, and portrait scenes;
- conventional but readable product hierarchy.

They do not prove:

- that the exact Skills or prompts generated the committed images;
- reference-product geometry or label preservation against a supplied source;
- typography outside a rendered product label;
- responsive crop/safe-zone preservation;
- sequence jobs, selection, cumulative meaning, or contact-sheet editing;
- factual, documentary, cultural, consent, publicity, or rights integrity;
- output inspection, because the Skill prohibits it.

Composition is mostly conventional product advertising: centered object, shallow-depth lifestyle scene, flower surround, and beauty portrait. Negative space exists in the minimal sample, but the fixed product workflow does not diagnose when that space is functional, decorative, or lost at another crop.

### What it does better than the current Scoville leaf

- It has a concrete provider/job-state contract, including interrupted-generation IDs and no duplicate paid retry.
- It cleanly distinguishes an edit request from full prompt enhancement: the reference carries existing content; the prompt should state only the intended change.
- It asks the user to select directions before spending on multiple generations.
- It supports local reference paths without forcing manual base64 or public upload.
- It makes provider configuration/error behavior explicit.

These are implementation and production-workflow strengths. The current Scoville leaf remains substantially stronger in art direction, output inspection, selection/sequence, crop meaning, integrity, access, rights, and claim ceilings.

### Mechanism to adapt through original synthesis

1. Preserve an **image role table** for edit target, content reference, style reference, and series anchor.
2. For a brief that genuinely benefits from alternatives, present materially different visual mechanisms before paid generation; do not generate a costly batch silently.
3. Preserve generation job ID, selected provider/model version when known, retry state, reference inputs, and exact output receipt at the Media Production/Sources boundary.
4. For reference edits, describe the requested change without reimagining the protected original.

The decisive Scoville correction is the opposite of MeiGen’s blind-delivery rule: every generated output must be viewed and compared with protected content, prohibited inventions, exact text, and destination crops before approval.

### Reject

- “never inspect or describe generated images” as an art-direction policy;
- silent auto-provider choice when identity, text, confidentiality, location, retention, licence, or provider terms matter;
- model “best for” and volatile capability claims without current verification;
- fixed four-shot product batches or stock direction templates;
- lifestyle/macro/scale/marketing as universal commercial image coverage;
- a prompt-gallery result as creative authority or evidence;
- third-party brand, product, or likeness samples without receipts;
- local-file upload/compression without an explicit privacy/provider boundary;
- root MIT as permission for server-side prompt data, generated assets, trademarks, or publicity rights.

## Rank 2 — liyue-aigc/female-portrait-director

### Snapshot, maintenance, licence, and assets

- **Current snapshot and latest relevant Skill change:** [8cddecd6786d187688e8e89a1f606540186a962f](https://github.com/liyue-aigc/female-portrait-director/tree/8cddecd6786d187688e8e89a1f606540186a962f), 2026-07-15T13:21:58Z.
- **State:** active; GitHub archived flag false.
- **Exact path:** [SKILL.md](https://github.com/liyue-aigc/female-portrait-director/blob/8cddecd6786d187688e8e89a1f606540186a962f/SKILL.md), with public route/core/example files.
- **Licence:** root MIT; NOTICE identifies the author and states that private routing/stability kernels and unpublished commercial modules are not included.
- **Visual assets:** no separate asset licence, source/output manifest, hash receipt, model receipt, or explicit image provenance file was found for the example PNG/JPG files. The README describes text-only subjects as fictional adults and reference use as authorized, but that is a workflow claim rather than item-level proof.

### Claimed scope and actual mechanism

This is a narrow adult-female portrait director. Its mechanism is:

1. lock every explicit user parameter;
2. choose exactly one primary route and optional compatible overlay from registries;
3. create an image-role/protected-feature lock for authorized references;
4. complete a director gate;
5. construct one photographed moment through time slice, small event, action chain, gaze target, clothing/material, scene layers, camera, composition, light, colour, and finish;
6. propagate all explicit fields into a five-paragraph final prompt plus negative constraints;
7. invoke generation only when explicitly requested.

The repository includes many committed outputs for lifestyle, urban fashion, fantasy/costume, e-commerce, retro-Hong-Kong, French, and curve-focused routes, plus prompt examples. No automated tests or source-to-result preservation cases were found.

### Visible evidence under the adoption lens

The inspected lifestyle, urban fashion, gufeng/xianxia, and e-commerce outputs visibly demonstrate:

- coherent camera distance, pose, gaze, lighting, background depth, clothing, and finish within each route;
- technically polished subject rendering;
- route-specific environment and material detail;
- readable conventional portrait hierarchy.

They do not demonstrate:

- typography or typesetting;
- active spacing/negative-space logic beyond portrait framing;
- unusual or subject-derived composition; most examples use centered or familiar commercial/fashion framing;
- responsive crop systems, contact sheets, sequence editing, or campaign progression;
- reference-identity preservation against an inspectable input;
- consent, release, publicity, cultural authority, or asset provenance.

The corpus is visually narrow: young, conventionally attractive, polished women dominate. Route labels and examples such as “pure-desire curves,” French effortless, retro Hong Kong, and gufeng/xianxia turn gender, culture, era, and desirability into style fingerprints. Technical polish is not evidence of representative adequacy.

### What it does better than the current Scoville leaf

- It gives portrait work a much more detailed **parameter-propagation audit**.
- It distinguishes explicit locks from inferred supplements.
- It converts a portrait brief into a photographed moment rather than a static list of traits.
- Time slice, small event, action chain, gaze target, selective environment details, depth layers, and lighting placement form a useful causal photography vocabulary.
- It prevents image generation when the user requested only a prompt.

Scoville remains stronger in general photography/illustration coverage, communication thesis, sequence, crop meaning, commissioning, documentary modes, prohibited inventions, representation, access, rights, and proof.

### Mechanism to adapt through original synthesis

Adapt a medium-specific **protected-variable table**:

- supplied fact or explicit requirement;
- visual variable it controls;
- permitted variation;
- protected relation;
- observable failure;
- smallest repair;
- output evidence.

For portrait photography, add time slice, action chain, gaze target, body/wardrobe material, camera relation, background function, light direction/quality, and destination crop. This should be available without a gendered style catalogue or mandatory five-paragraph prompt.

### Reject

- gender as a route family and attraction/curve intensity as a default design axis;
- style names that reduce culture, place, era, or femininity to a visual costume;
- narrow youth/beauty outputs as portrait quality or representation proof;
- fixed exactly-five-paragraph output;
- hidden/private kernels as unverifiable authority;
- 20-style menus and route fingerprints as general portrait expertise;
- a “fictional adult” prompt statement as proof of age, non-likeness, consent, or publicity clearance;
- direct generation before inspecting references and final output;
- sample images or prompt expression without item-level provenance and applicable rights.

## Rank 3 — joeseesun/qiaomu-mondo-poster-design

### Snapshot, maintenance, licence, and assets

- **Current snapshot:** [e82e411c403ca5a0327a85682c658ad155cd9cbb](https://github.com/joeseesun/qiaomu-mondo-poster-design/tree/e82e411c403ca5a0327a85682c658ad155cd9cbb), 2026-03-16T14:23:23Z.
- **Latest relevant Skill change:** bcff688ff3b19a7c2505f7e22ef42fa8195dd96e, 2026-03-08T09:59:26Z.
- **State:** active; GitHub archived flag false.
- **Exact path:** [SKILL.md](https://github.com/joeseesun/qiaomu-mondo-poster-design/blob/e82e411c403ca5a0327a85682c658ad155cd9cbb/SKILL.md).
- **Licence:** root MIT; no separate example-asset licence or source/output receipt.
- **Underlying rights risk:** inspected outputs visibly contain Mondo and Olly Moss names/marks, film titles, character/story imagery, credited filmmaker/actor names, a copyrighted film quotation, “limited edition” wording, and signature-like marks. Root MIT cannot grant rights in those third-party elements.

### Claimed scope and actual mechanism

The Skill turns a subject into posters, book/album covers, social images, and article illustrations through:

1. choose one symbolic element;
2. select a composition pattern such as figure-ground inversion, scale contrast, or single-shape storytelling;
3. choose a limited palette and screen-print texture;
4. select one of many named historical/living designer styles;
5. generate one or compare three style variants;
6. optionally transform an existing image.

The repository contains many committed images, including IMDB-film posters, book/album covers, and a negative-space example. It has no tests or evals, and no prompt/output/rights manifest.

### Visible evidence under the adoption lens

The inspected **Flirting Scholar**, **Shawshank Redemption**, and **Pulp Fiction** examples show the strongest adoption-priority visual evidence among the ranked imagery candidates:

- clear figure-ground and object-metaphor mechanisms;
- focal hierarchy readable at thumbnail size;
- active negative space rather than generic emptiness;
- strong display/support typography and controlled line breaks;
- subject-specific imagery rather than generic atmosphere;
- different spatial structures across the three subjects.

The same examples expose severe failures:

- generated Mondo/artist attribution and edition marks create false provenance;
- artist-name routing encourages direct imitation;
- film titles, quotes, character imagery, and marks lack rights records;
- fixed type/graphic percentages and aspect ratios are presented as “master” patterns;
- there is no source comparison, documentary/fiction mode, responsive crop, accessibility, or final-output integrity record.

### What it does better than the current Scoville leaf

- It visibly demonstrates that one subject-derived metaphor can outperform literal scene accumulation.
- It exposes several materially different composition mechanisms rather than only camera variables.
- Its strongest examples use figure-ground, scale contrast, and iconic-object compression to create a memorable thesis.
- It shows negative space, type, and image working as one hierarchy.

The current Scoville leaf already has the safer underlying principles—image thesis, observable content, subject-specific reason, and rejection of style-first generation—but lacks rendered examples that prove it can achieve this conceptual compression.

### Mechanism to adapt through original synthesis

Adapt only a rights-clean **symbolic mechanism comparison**:

1. derive the exact subject/message relation;
2. generate several mechanisms such as literal evidence, object metaphor, figure-ground relation, scale contrast, or contextual portrait;
3. state what each preserves and risks;
4. select by subject truth, originality, legibility, access, production, and rights;
5. render and inspect without named-artist imitation.

Figure-ground is a compositional mechanism, not an Olly Moss style. Screen-print limitation is a production/aesthetic option, not a Mondo entitlement. No prose, prompt, image, fixed ratio, designer mapping, or branded example should be copied.

### Reject

- “master-level” or “legendary designer” claims;
- living or named artist/style imitation;
- Mondo branding, signatures, fake edition marks, or fabricated credits;
- film/book/album IP, quotations, titles, actors, and marks without clearance;
- 9:16 as a poster default;
- 2–5 colours, 70% negative space, or 30/30/40 image/type/space as universal rules;
- centered symmetry, one focal point, retro palettes, or a named decade as automatic quality;
- genre-to-style mappings and prompt formulae;
- prompt compliance as output proof;
- MIT as clearance of third-party copyright, trademark, publicity, or generated-output terms.

## Comparative capability matrix

| Decision-relevant capability | Current Scoville reference + audit | MeiGen | Female Portrait Director | Qiaomu Mondo |
|---|---|---|---|---|
| Communication thesis | One image thesis tied to subject/message | Brief enhancement; product directions are channel/sales roles | One photographed moment; no general communication thesis | Strong subject-symbol compression, often style-first |
| Photography variables | Planned camera position/distance/angle, focus/motion, light, gesture, context | Fixed product shot directions and prompt descriptors | Deepest portrait-specific camera/pose/gaze/light propagation | Mostly illustration/poster variables |
| Illustration variables | Planned literal–abstract, silhouette, line/value, texture, perspective, detail/space | Generic prompt style fields | Not applicable | Strong metaphor/figure-ground; limited screen-print family |
| Selection and sequence | Distinct image jobs, redundancy, transition, pacing, cumulative meaning | Batch directions; no picture-editing sequence | None | Comparison variants; no narrative sequence |
| Responsive crop/text zone | Protected action/identity/evidence/copy zones and final crop inspection planned | Aspect ratio parameter, no demonstrated cross-crop preservation | Prompt ratio lock only | Fixed format recipes, no responsive preservation |
| Reference preservation | Preserve/change/prohibited invention and source comparison planned | Reference path and short edit prompt; no output inspection | Explicit parameter and authorized-reference lock, no preservation fixture | Image-to-image exists; no protected-feature record |
| Output inspection | Mandatory master/crop/full/thumbnail/strip review planned | Explicitly prohibited | No demonstrated inspect/compare loop in top-level evidence | No inspectable QA contract |
| Documentary/rights/provenance | Mode gate, original/source, prohibited edits, consent/rights/C2PA ceiling | Missing; branded/likeness samples unreceipted | Fictional-adult/authorized-reference policy, no item evidence | Serious imitation/false-provenance/third-party IP failures |
| Type/spacing/negative space | Text-zone and live-type rules; Composition/Typography own deeper system | Minimal sample has copy space; no type system | No type evidence; conventional portrait spacing | Strong visible type hierarchy and active negative space, but fixed recipes |
| Subject-specific composition | Required and causally diagnosed | Conventional product/photo directions | Route-specific portrait moments | Strongest visible symbolic subject-specific work |
| Evidence | Current SOL baseline only; no specialist outcome suite | E1 samples + manual behavior scenarios | E1 samples | E1 samples |

## Adoption decision

### Adopt or adapt

1. **Protected-variable propagation.** From Female Portrait Director, turn explicit requirements and reference features into a lock table before expanding photographic variables.
2. **One photographed moment.** For portrait/people work, use time slice, small event, action chain, gaze, selective context, camera relation, and light behavior rather than a trait pile.
3. **Symbolic mechanism comparison.** From Qiaomu, compare literal evidence, object metaphor, figure-ground, scale contrast, and contextual portrait as materially different concepts; strip named artists, brands, formulas, and derivative examples.
4. **Provider/job receipt.** From MeiGen, retain reference roles, provider/model/version when known, generation ID, retry state, output paths, and paid-batch confirmation at the appropriate production boundary.
5. **Minimal reference-edit prompt.** State only the allowed change while the reference supplies protected content; then inspect the result against the lock table.
6. **Visible evidence gate.** Render at final size, every required crop, thumbnail, and strip/contact sheet. The public landscape shows why prompt detail and repository examples are insufficient.

### Do not adopt

- blind delivery after generation;
- fixed four-shot product sets, fixed style menus, fixed paragraphs, fixed aspect ratios, or topic-to-aesthetic mappings;
- living/named artist imitation or style transfer presented as professional art direction;
- gendered attraction routes, cultural costume categories, anonymous beauty ideals, or “fictional adult” as consent/age proof;
- polished output as proof of identity, product accuracy, documentary truth, accessibility, or rights;
- trademarked products, celebrity-like faces, film IP, quotations, signatures, and edition marks without an asset receipt;
- model/provider claims or remote prompt datasets without current terms;
- hidden kernels, inaccessible remote dependencies, or root licences treated as clearance for third-party content.

### Architecture impact

The Stage-2 evidence does **not** overturn the existing recommendation to retain one imagery-and-art-direction leaf. The public landscape is fragmented:

- provider routing without inspection;
- narrow portrait prompting;
- narrow poster-style imitation;
- lower-star illustration and zine products with their own fixed aesthetics.

No candidate shows that photography, illustration, selection, sequence, crop, generation, integrity, access, rights, and output proof work better as separate directly routed curricula. The strongest transferable mechanisms still share the image thesis, protected variables, controlled variation, causal repair, and inspection contract. A split would duplicate those load-bearing relations.

The public examples do strengthen one implementation priority: Scoville’s future open tests must contain real rendered photography, illustration, metaphor, sequence, and crop artifacts. Rules alone cannot establish subject-specific composition or professional image judgment.

## Evidence and claim limits

- Stars are a capture-time popularity metric, not evidence of quality, originality, safety, maintenance, or professional adoption.
- All three rankings are maintainer-authored E1. No independent evaluator, reproducible visual benchmark, blinded comparison, or external-adoption result was found for the exact Skills.
- The committed images do not establish which prompt, model, reference, seed, edit, or review produced them unless the repository supplied a receipt; the top three did not.
- Visual inspection covered representative committed files, not every example.
- Static images cannot prove campaign continuity, crop resilience, identity preservation, factual integrity, consent, rights, accessibility, reproduction, or repeatability.
- Root MIT does not clear trademarks, copyrighted works, quotations, likenesses, generated-output terms, remote prompt datasets, or private inputs.
- No external Skill demonstrates professional picture editing, commissioning, documentary verification, contextual accessibility, or current rights clearance at the breadth required by the audit.
- This comparison authorizes mechanism-level original synthesis only. It does not authorize copying external Skill prose, prompts, examples, style names, assets, or proprietary/private kernels.

**Stage-2 conclusion:** MeiGen is the most popular qualifying generation workflow, Female Portrait Director is the deepest qualifying narrow photography prompt system, and Qiaomu Mondo is the strongest qualifying visible conceptual-composition example. Their best mechanisms are reference locking, photographed-moment direction, paid-generation/job receipts, and symbolic mechanism comparison. Their blind inspection, fixed recipes, gender/culture/style stereotypes, imitation, and rights failures must be rejected.
