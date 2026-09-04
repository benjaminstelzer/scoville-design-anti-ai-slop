# Stage-two Skill comparison: Editorial and fixed-media design

Date: 2026-09-02  
Capture: 2026-09-02T14:33:33Z  
Target: proposed `editorial-and-fixed-media-design` medium leaf  
Method: `reference-audit-method.md`, Stage two

Local baselines: [composition and layout](../../../references/composition-and-layout.md),
[typography and typesetting](../../../references/typography-and-typesetting.md),
[media production and handoff](../../../references/media-production-and-handoff.md),
[composition audit](../reference-audits/composition-and-layout.md), and
[production audit](../reference-audits/media-production-and-handoff.md).

This is a current, bounded GitHub and public-Skill comparison for editorial,
multi-page, print, presentation, poster, and other fixed-media design. It ranks
repositories by captured GitHub stars only after an exact Skill or directly
usable agent instruction and an E1 or higher evidence artifact were found.
Stars belong to repositories, not to the exact Skill. Rank 3 is a historical
mirror of an earlier version of rank 2's upstream family, so the three ranks do
not represent three independent mechanisms.

Public discovery used GitHub repository, contents, tree, commit, and code-search
APIs plus web search. Exact paths, evidence artifacts, history, and licenses were
inspected at the pins below. Tests were inspected but not executed. Search can
miss renamed, private, new, non-English, registry-only, or poorly indexed
Skills; the result is not globally exhaustive.

## Decision

The three qualifying repositories are `nexu-io/open-design`,
`K-Dense-AI/scientific-agent-skills`, and
`davila7/claude-code-templates`. OpenDesign supplies the clearest inspectable
multi-page pacing scaffold, but it is a locked magazine-deck template rather
than general editorial competence. K-Dense supplies the strongest fixed-output
requirements, provenance, final-size, technical validation, and honest proof
boundary; its current generator explicitly does not compose the poster. The
Davila package preserves an older K-Dense LaTeX-poster recipe with concrete
templates, but it is stale, heavily hardcoded, and adds
almost no independent evidence.

None of the three proves professional editorial design across books,
magazines, brochures, posters, signage, decks, and print. None provides a
credible book or magazine spread system, binding/fold behavior, typographic
colour and page fragmentation, or independent visual-quality evaluation.
No candidate has E3 evidence.

The proposed Scoville leaf should therefore not be built from any candidate's
templates or numbers. It should synthesize three mechanisms only:

1. an explicit content and sequence plan before isolated pages;
2. a medium record that binds dimensions, final viewing conditions, page,
   spread, panel, fold, binding, and protected zones to their actual authority;
3. a proof ladder that separates design intent, rendered fit, production
   preflight, and provider or physical approval.

Shared Composition and Typography remain the owners of general spatial and
type reasoning. The new medium leaf should own how those decisions transform
across pages, spreads, panels, fixed canvases, and final viewing contexts.
Media Production should continue to own export, preflight, packaging, provider
handoff, and proof status.

## Qualification and star ranking

Evidence levels follow the audit method. E1 means an inspectable example or
output artifact. E2 means a reproducible test, evaluation, or deterministic
check. E3 requires independent evaluation or external adoption evidence that
supports capability. A template or synthetic fixture can prove that a
mechanism exists; it does not prove good design.

| Rank | Repository and exact Skill path | Stars at capture | Pin, activity and latest relevant update | Exact license and asset status | Evidence level and what it proves |
| --- | --- | ---: | --- | --- | --- |
| 1 | [`nexu-io/open-design`, `design-templates/guizang-ppt/SKILL.md`](https://github.com/nexu-io/open-design/blob/ff2cc80f336f94786128113eddbbb9e3719fecc8/design-templates/guizang-ppt/SKILL.md) | 93,552 | Active, not archived. Repository pin `ff2cc80f336f94786128113eddbbb9e3719fecc8`; pushed 2026-09-02. Exact Skill last changed in [`ebcba704efbc29e8384388deadd888504b83cf3f`](https://github.com/nexu-io/open-design/commit/ebcba704efbc29e8384388deadd888504b83cf3f) on 2026-07-31; the example last changed in [`f1a0b60c6cd1c9f5c735ae5645e47244b468e71c`](https://github.com/nexu-io/open-design/commit/f1a0b60c6cd1c9f5c735ae5645e47244b468e71c) on 2026-08-18. | Root is Apache-2.0, but the exact template directory has a more specific [MIT license](https://github.com/nexu-io/open-design/blob/ff2cc80f336f94786128113eddbbb9e3719fecc8/design-templates/guizang-ppt/LICENSE), copyright op7418. The HTML calls Google Fonts and unpkg Lucide; those services, font files, icons, user images, publication names, and style anchors retain separate rights and availability boundaries. | **E1.** A complete runnable HTML template, ten paste-ready layout skeletons, and a [nine-slide content example](https://github.com/nexu-io/open-design/blob/ff2cc80f336f94786128113eddbbb9e3719fecc8/design-templates/guizang-ppt/assets/example-slides.html) are inspectable. They prove one fixed-viewport deck mechanism and example completeness. No exact-path render test, accessibility test, projector/print test, independent review, or comparative visual-quality evaluation was found. |
| 2 | [`K-Dense-AI/scientific-agent-skills`, `skills/pptx-posters/SKILL.md`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/1dd0fccf46fc3c9855c4a0c313a0c57fe4319883/skills/pptx-posters/SKILL.md) | 42,007 | Active, not archived. The former `claude-scientific-skills` URL redirects to the canonical repository name. Pin `1dd0fccf46fc3c9855c4a0c313a0c57fe4319883`; pushed 2026-08-31. Exact Skill and tests last changed in [`2f2022de186dbf73f4c3b6e37b9856fa5cb66db4`](https://github.com/K-Dense-AI/scientific-agent-skills/commit/2f2022de186dbf73f4c3b6e37b9856fa5cb66db4) on 2026-07-26. | Root and Skill declare [MIT](https://github.com/K-Dense-AI/scientific-agent-skills/blob/1dd0fccf46fc3c9855c4a0c313a0c57fe4319883/LICENSE.md). No separate notice was found for the documentation screenshot. The Skill does not grant rights to author content, fonts, conference material, figures, QR targets, or printer profiles; its manifest requires separate provenance and permission for supplied assets. Dependencies retain their own licenses. | **E2.** Deterministic manifest, generation, package-security, bounds, overlap, reading-order, DPI, palette, and export-plan checks have source tests, including a [synthetic generation smoke test](https://github.com/K-Dense-AI/scientific-agent-skills/blob/1dd0fccf46fc3c9855c4a0c313a0c57fe4319883/tests/pptx-posters/test_generation_smoke.py). A documentation screenshot is inspectable. These artifacts prove technical generation and named checks, not hierarchy, whitespace, typography, communication success, or professional visual quality. Tests were inspected, not run here. |
| 3 | [`davila7/claude-code-templates`, imported `cli-tool/components/skills/scientific/latex-posters/SKILL.md`](https://github.com/davila7/claude-code-templates/blob/8a3613d31efb825adc0371cefa0b6798f15e43fd/cli-tool/components/skills/scientific/latex-posters/SKILL.md) | 30,505 | Active, not archived. Repository pin `8a3613d31efb825adc0371cefa0b6798f15e43fd`; pushed 2026-09-02. Exact files were imported once in [`2fe0cfa568ebeafa363f39db7567d0d6a99aee85`](https://github.com/davila7/claude-code-templates/commit/2fe0cfa568ebeafa363f39db7567d0d6a99aee85) on 2025-12-20 and have no later exact-path update. | Root is [MIT](https://github.com/davila7/claude-code-templates/blob/8a3613d31efb825adc0371cefa0b6798f15e43fd/LICENSE). The import commit and README attribute the scientific collection to K-Dense under MIT; the exact path has no separate notice. The repository license does not clear user figures, logos, fonts, conference material, AI-provider outputs, or printer profiles. | **E1.** Three concrete LaTeX templates, including the [`beamerposter` scaffold](https://github.com/davila7/claude-code-templates/blob/8a3613d31efb825adc0371cefa0b6798f15e43fd/cli-tool/components/skills/scientific/latex-posters/assets/beamerposter_template.tex), code examples, a review script, and a checklist are inspectable. They prove that an old scaffold exists, not that it compiles, satisfies current provider rules, or yields good design. No exact-path tests, rendered comparison set, or independent evaluation was found. |

## Candidate 1: OpenDesign `magazine-web-ppt`

### Claimed scope and observed mechanism

The Skill produces a single-file, horizontally paged HTML deck on a fixed
`100vw` by `100vh` canvas. It infers one of five named magazine directions,
locks one preset palette, creates a project record, aligns a narrative arc,
page count, and theme-rhythm table, then fills ten predefined slide skeletons.
It requires a class-name preflight, a browser preview, and a final checklist.
The example contains nine real-content slides and declares its sequence as a
light/dark/hero rhythm.

The useful mechanism is the order of decisions: audience and decision goal,
then narrative arc and page roles, then sequence rhythm, then page
construction, then strip/index inspection. The candidate is strongest as a
worked deck scaffold, not as a general design method.

### What it does better than the current medium proposal

- It makes sequence planning explicit before page-by-page styling.
- It provides page-role vocabulary: cover, divider, data moment, image-text
  spread, comparison, process, quote, and close.
- It forces a whole-deck rhythm record instead of validating isolated hero
  slides only.
- The overview/index mechanism supplies a compact thumbnail-strip view.
- The runnable example exposes actual class, viewport, typography, image-slot,
  navigation, and content behavior rather than stopping at a prose claim.
- Its preflight finds one common implementation cause: a visually broken page
  can originate in a missing shared class rather than in the page's local
  composition.

### Weighted design assessment

**Typography.** The template defines display, body, metadata, and numeral
roles, but then hardcodes specific serif/sans/mono families and category-based
jobs. This demonstrates role mapping only. It does not prove that the families
fit the supplied language, subject, projection conditions, fallback, or
license. It contains no serious typesetting, paragraph, microtype, or
fragmentation evaluation.

**Semantic spacing and negative space.** The Skill understands that hero,
body, image, and data pages need different density. However, most intervals
are fixed `vh`/`vw` values, and advice such as sixty percent empty space is a
style recipe. It does not distinguish within-group, between-group, section,
edge, caption, gutter, pause, reveal, and transition space as separate causes.

**Hierarchy.** Page roles, type roles, theme changes, and content-specific
layouts produce a visible hierarchy scaffold. The fixed role mapping does not
prove that the most consequential content becomes primary or that a complex
page remains intelligible at projection distance.

**Pacing and spreads.** Sequence planning is the candidate's best transferable
idea. It nevertheless treats pacing as a mandatory light/dark/hero alternation
and a repeated hero interval. A deck's actual argument, emotion, evidence, and
audience attention may require another cadence. The canvas is a sequence of
single viewports, not facing editorial spreads.

**Final size, viewing context, and folds.** The template adapts to browser
viewport units and has a narrow-screen media query, but it does not define
projector size, room distance, lighting, PDF export, print page, physical
proof, binding, fold, panel, gutter loss, trim, bleed, or safe zones. Network
font and icon dependencies can also change an offline presentation.

**Design versus production.** Visual direction, content structure, CSS
implementation, navigation, external dependencies, and preview are bundled in
one Skill. There is no explicit distinction between a design decision, a
render check, a technical pass, and audience or venue approval.

### Reject or re-verify

- Reject the five permitted style directions, named-publication mimicry,
  default Monocle choice, and refusal to accept another palette.
- Reject fixed slide counts, theme alternation, hero-page cadence, layout
  catalog, ratios, font stack, image heights, title lengths, and percentage
  whitespace as general editorial rules.
- Do not import the statement that a preset has the “lowest failure
  probability”; no evaluation supporting that probability was found.
- Do not treat a runnable browser example as projection, print, access,
  editorial, or subject-specific quality proof.
- Do not depend on live font or icon CDNs for an offline or archival artifact
  without a licensed, tested fallback and packaging decision.
- Publication names can be research references, not a license to reproduce
  their distinctive trade dress or to make a five-style taxonomy canonical.

## Candidate 2: K-Dense `pptx-posters`

### Claimed scope and observed mechanism

The current Skill creates and audits a one-slide, editable, macro-free
PowerPoint research poster from an author-approved local manifest. It records
physical trim, bleed, safe margin, PowerPoint canvas, scale, conference and
printer requirements, final-output type and raster thresholds, fonts,
provenance, licenses, reading order, alt text, QR fallbacks, and approval bound
to a content hash. It then runs deterministic manifest, asset, palette,
package, layout, and export-plan checks before manual PowerPoint, access, PDF,
printer, and physical-proof gates.

The most important boundary is explicit: the generator renders exact approved
manifest content and **does not compose, summarize, research, or correct it**.
That makes this a strong production and proof comparator and only a partial
design comparator.

### What it does better than the current medium proposal

- It distinguishes physical output from authoring canvas and makes scaling
  explicit rather than assuming canvas points equal final print points.
- Every numeric threshold must be labelled heuristic, source-specific,
  conference-required, or printer-required.
- It refuses print-readiness when the actual conference, printer, color mode,
  font, asset, approval, or output plan is unresolved.
- It separates source/package checks from rendered PowerPoint, accessibility,
  PDF, printer, author, and physical proof.
- Effective DPI is derived from placed final inches rather than metadata DPI.
- Font availability, embedding permission, substitution, glyphs, and PDF
  records are separate questions.
- Synthetic tests prove fail-closed technical behavior without pretending the
  fixture is a successful design.

### Weighted design assessment

**Typography.** This is the strongest candidate on final-size scaling, font
availability, substitution, licensing, and proof. Its design guidance still
uses only a small role set and does not evaluate typeface compatibility,
typographic colour, line endings, paragraph rhythm, editorial justification,
folios, or page fragmentation.

**Semantic spacing and negative space.** The reference says to group related
evidence and use spacing before decoration. The generator validates declared
rectangles, bounds, overlaps, and safe zones. Geometry cannot determine whether
a gap expresses grouping, pacing, emphasis, tension, or accidental emptiness.

**Hierarchy.** Research question, key result, and interpretation are named
targets, and source order is explicit. A manifest cannot prove that the visual
hierarchy communicates those priorities or that every block is not equally
loud.

**Pacing and spreads.** The strict profile is exactly one slide. It has no
page-to-page pacing, facing spreads, folios, recurring anchors, master/parent
variation, text threading, section transitions, or binding logic.

**Final size, viewing context, and folds.** Final physical size, scale, viewing
distance, lighting, substrate, printer, and reduced/full-size proof are strong.
The scope is a flat poster; folds, panels, binding, imposition, crossover
images, inside/outside margins, creep, and gutter loss remain absent.

**Design versus production.** This is the best boundary of the three. Design
must first decide and obtain approval for content, reading order, rectangles,
roles, and visual intent. The tooling owns deterministic production and names
what still requires PowerPoint, author, accessibility, printer, and physical
review. Scoville should preserve this separation while keeping its Design leaf
capable of actual composition.

### Reject or re-verify

- Do not import the one-slide PPTX profile, manifest schema, dependency pins,
  security rules, approved shape types, or local-only workflow into a general
  design leaf.
- Do not convert WCAG screen contrast mathematics into universal print
  conformance; the candidate correctly treats it only as a declared target.
- Do not convert its heuristic font or raster thresholds into defaults.
- Bounds, overlap, DPI, package safety, and manifest approval are not visual
  quality scores.
- A reduced-scale proof is useful only when its scale, viewing distance,
  output process, and limitations are recorded. It does not replace the final
  substrate/provider proof.
- The current Skill intentionally withholds composition. Scoville must adopt
  the proof boundary, not the inability to design.

## Candidate 3: imported historical K-Dense poster Skill

### Claimed scope and observed mechanism

The imported instruction describes professional LaTeX research posters using
`beamerposter`, `tikzposter`, and `baposter`. It includes standard section
lists, column and block layouts, font and image numbers, palette suggestions,
LaTeX snippets, a large checklist, reduced-scale print review, peer tests, and
three placeholder LaTeX templates. The import commit attributes it to K-Dense
and no exact-path update has followed
since 2025-12-20.

### What it contributes

- It keeps final poster size and view-from-distance review visible.
- It recommends both automated PDF inspection and human visual inspection.
- Reduced-scale print, short exposure, and peer explanation tests are concrete
  communication checks when their context is recorded.
- The LaTeX examples expose actual authoring scaffolds rather than
  only describing them.

These mechanisms are already represented more carefully in the current
K-Dense candidate. Rank 3 therefore adds evidence of propagation and an older
failure surface, not an independent state-of-the-art approach.

### Weighted design assessment

**Typography, spacing, hierarchy, and negative space.** The Skill names each
concern but immediately replaces judgment with fixed sizes, family counts,
line measures, whitespace percentages, column counts, and “professional”
templates. The examples use generic blocks, columns, placeholder text, and
fixed numerical dimensions. They prove a scaffold, not an effective
subject-specific design.

**Pacing, spreads, final context, and folds.** Final poster size and distance
checks are present. The scope remains one large page. There is no meaningful
multi-page sequence, spread, fold, panel, binding, or imposition method.

**Design versus production.** Concept, content, generated figures, template,
layout, PDF checks, accessibility claims, printing, and provider steps are
mixed together. A mandatory call for two or three AI-generated figures makes a
provider and content choice before the brief proves that figures are needed.

### Reject or re-verify

- Reject mandatory AI figures, mandatory visual-area percentages, fixed word
  counts, fixed family counts, fixed font sizes, universal DPI, column counts,
  margins, spacing, bleed, QR size, contrast targets, and reading distances.
- Reject claims that sans serif, one named grid, Z-pattern, equal distribution,
  or a template is inherently professional or naturally followed by the eye.
- Reject the generic LaTeX scaffolds as Scoville templates and do not inherit
  their placeholder content or styles.
- Do not import commands for PDF/X, font embedding, CMYK conversion, or
  provider delivery without verifying the current tool, file, printer, and
  profile contract.
- The stale import requires re-verification before any operational reuse.
  Repository activity does not mean this exact Skill is maintained.

## Weighted adoption comparison

| Required concern | OpenDesign deck | K-Dense current poster | Davila historical import | Scoville decision |
| --- | --- | --- | --- | --- |
| Typography | Clear display/body/metadata roles in one runnable stack; fixed faces and viewport units | Strong final-size scaling, font availability, rights, substitution, and proof; shallow editorial typesetting | Hardcoded sans, family-count, point-size, and line-length recipes | Typography expert owns face choice, compatibility, typesetting, and microtype. Medium leaf adds final context, fragmentation, page/spread roles, and proof targets. |
| Semantic spacing | Different page roles and densities, but spacing is mostly fixed `vh`/`vw` | Declared rectangles and safe zones; geometry cannot infer relationships | Repeats fixed gaps, margins, percentages, and “consistent spacing” | Name within-group, between-group, section, edge, gutter, caption, sequence, pause, reveal, and tension functions. No universal scale or ratio. |
| Negative space | Treats open hero pages as pacing, but imposes style percentages | Names whitespace and grouping, with no causal evaluation | Prescribes even distribution and fixed percentages | Preserve separation, pacing, framing, direction, emphasis, tension, and recovery. Diagnose trapped, competing, decorative, or accidental emptiness before changing amount. |
| Hierarchy | Page roles, theme contrast, and type roles give one usable scaffold | Content priorities and reading order are explicit; manifest cannot prove perceptual order | Standard poster sections and generic card hierarchy | Start from consequence, task, narrative, and reading order. Use the fewest sufficient visual signals and verify actual scan/read behavior. |
| Pacing and spreads | Best sequence record and thumbnail/index view; cadence is hardcoded; no facing spreads | One-slide scope | One-page scope | Add flat plan, page roles, thumbnail strip, facing-spread inspection, recurring anchors, parents, folios/navigation, density curve, section transitions, and controlled variation. |
| Final size and viewing | Fixed browser viewport; no room, projector, print, or offline dependency proof | Strongest physical size, authoring scale, distance, substrate, printer, PDF, and proof boundary | Useful reduced-scale and distance checks, but universal numbers | Record actual final dimensions, scale, distance, lighting/device/substrate, orientation, interaction, and authority. Test exact output or clearly bounded proxy. |
| Folds, binding and panels | None | None | None | P1 gap: add fold map, panel order, crossover risk, protected zones, inside/outside margins, gutter/binding loss, creep/imposition questions, and provider authority without inventing numbers. |
| Subject-specific composition | Five named styles and layouts can make output coherent but also generic | Exact content approval prevents invention but generator does not compose | Generic academic template and mandatory generated figures | Derive spatial thesis and page system from brief, content, subject, audience, and medium. A template is only an implementation aid after the design decision. |
| Design/production ownership | Conflated | Strongest separation; deterministic production with manual/provider gates | Conflated and provider-assumptive | Design owns medium concept, sequence, page/spread/panel behavior, typography/spacing intent, exceptions, and validation target. Production owns export, preflight, packaging, supplier execution, and proof status. |
| Evidence | E1 runnable source and example; no visual evaluation | E2 technical tests and synthetic fixture; no design-quality evaluation | E1 scaffold only; stale mirror | Use artifacts as mechanism evidence only. Require Scoville renders, exact-content checks, final-context inspection, and qualified visual/provider review for stronger claims. |

## Direct implications for `editorial-and-fixed-media-design`

### Proposed ownership

The leaf should own design transformations caused by a fixed or sequential
medium:

- physical or fixed-canvas dimensions, orientation, ratio, final viewing
  distance, device/projection context, lighting, substrate, and expected use;
- content map, flat plan, page/spread/panel roles, density and pacing curve,
  section transitions, recurring anchors, folios/navigation, master/parent
  logic, and controlled variation;
- page, facing spread, fold, gatefold, panel, binding/gutter, trim, bleed,
  live/safe area, protected crop, and crossover intent as design constraints;
- how general hierarchy, type, spacing, colour, and imagery are expressed at
  final size across the sequence;
- the exact render, thumbnail strip, spread, fold dummy, projection, distance,
  or physical proof needed to judge the design;
- deliberate exceptions and compensating counterstructure across the system.

The leaf should not repeat a full composition, typography, colour, imagery,
brand, style, or production curriculum. It records medium transformations and
calls the already routed experts for deep domain decisions.

### Minimum professional decision record

Before designing, capture:

1. purpose, audience, consequence, content inventory, required order, and
   immutable items;
2. artifact class: single fixed canvas, paged sequence, facing-page
   publication, folded piece, presentation, signage, packaging face, or other
   named format;
3. final dimensions, orientation, scale, viewing distance, lighting/device or
   substrate, handling, duration, and venue/provider authority;
4. page, spread, panel, fold, binding, trim, bleed, safe/live area, protected
   subject, and imposition context where applicable;
5. sequence thesis: entry, development, evidence, pauses, transitions,
   climax, recovery, and close;
6. recurring anchors and permitted variation across page or panel roles;
7. typography, imagery, colour, and spacing decisions that change because of
   the medium;
8. intended evidence and current status: source-valid, rendered, visually
   inspected, production-checked, provider-confirmed, physically proofed.

Unknown provider, fold, binding, colour, font, or final-size facts remain
unknown. A provisional design may proceed with labelled assumptions when safe,
but it cannot be called production-proofed.

### Sequence and spread method

Use a content-derived flat plan rather than a library of page templates:

- assign a communicative job to every page, spread, panel, or slide;
- map hierarchy and reading order before selecting grids or page furniture;
- establish the least complex recurring anchor system that preserves
  orientation and permits subject-specific variation;
- mark dense, open, transition, evidence, image-led, reading-led, and recovery
  moments as observations, not mandatory categories;
- inspect single pages, facing spreads, fold/panel order, and the whole
  thumbnail strip;
- compare intended order with source, navigation, and accessible reading order;
- repair the shared parent, page role, content allocation, type measure, crop,
  or grid before adding local nudges.

Pacing is a consequence of content, audience, duration, page turns, and visual
change. Do not require alternating colours, a hero at a fixed interval, equal
spread density, or a fixed number of templates.

### Semantic spacing and negative-space method

Classify a relevant interval before changing it:

- **within** an item or semantic unit;
- **between** peer items or groups;
- **section** transition;
- **edge** or live-area relation;
- **gutter/fold/binding** relation;
- **caption/source/annotation** attachment;
- **sequence** pause or page-turn reveal;
- **framing/direction** around a focal subject;
- **tension/counterstructure** in deliberate asymmetry or overlap.

Then identify the parent cause. “More whitespace” is not a repair when the
actual problem is excessive content, false grouping, weak hierarchy, wrong
measure, an arbitrary card, a trapped gap, a fold conflict, or an unbalanced
sequence. Optical relationships may override geometric equality when the
intent, protected constraints, and compensation remain clear.

### Final-context proof ladder

1. **Source-valid:** required content, order, assets, rights, and authority are
   recorded.
2. **Artifact-valid:** editable source and export parse; page count, dimensions,
   links/assets, fonts, and required content are present.
3. **Rendered:** all pages, spreads, panels, and relevant states render at the
   named targets.
4. **Visually inspected:** hierarchy, grouping, type, spacing, negative space,
   crops, sequence, and exceptions were judged in single, spread, strip, and
   final-context views.
5. **Production-checked:** actual export/preflight checks pass for the named
   format and provider contract.
6. **Provider/physical proofed:** the actual venue, printer, publisher,
   fabricator, device, projection, fold dummy, or physical proof passed.

Do not collapse these states into “done.” A valid PDF is not a good layout; a
good screen render is not print approval; a passed overlap checker is not
semantic grouping; an approved printer proof is not evidence that readers
understand the hierarchy.

## Route boundaries

### Load `editorial-and-fixed-media-design`

Load it when fixed-medium reasoning can change the result:

- book, magazine, report, catalogue, zine, brochure, leaflet, or other paged
  editorial design;
- facing spreads, section pacing, folios, recurring anchors, parent/master
  pages, threading, or sequence critique;
- poster, signage, exhibition panel, fixed social/ad canvas, deck, or other
  final-size/viewing-distance design;
- folds, panels, gatefolds, binding, gutters, crossovers, trim/bleed/live areas,
  or fixed-format adaptation;
- critique or repair whose likely cause is page/spread/panel allocation,
  sequence, final size, viewing context, or fixed-medium constraint.

### Do not load it merely because the deliverable is a file

- An approved design needing only export, preflight, packaging, or supplier
  delivery routes to Media Production and Handoff.
- A single composition with a supplied ratio and no consequential final-medium
  question may need only Composition, Typography, Colour, or Imagery.
- Responsive web recomposition belongs to the proposed web/responsive medium
  leaf; framework mechanics and interactive proof belong to Scoville UI.
- A style request routes to Style Direction; subject imagery routes to Imagery
  and Art Direction; brand governance routes to Brand and Visual Systems.

### Composition and Typography boundary

Composition owns general hierarchy, grouping, grid selection, density,
relationships, negative-space diagnosis, and deliberate spatial exception.
Typography owns roles, face choice and compatibility, glyph distinction,
measure, leading, kerning/tracking/word spacing, alignment, hyphenation,
microtype, numerals, fallback, and font proof. The medium leaf owns how those
decisions behave across page roles, spreads, folds, panels, final dimensions,
viewing distance, and sequence.

### Design and Production boundary

Design owns the medium concept and record: content allocation, page/spread/
panel system, hierarchy and order, typography and spacing intent, folds and
protected zones, image behavior, exceptions, and the validation target.
Media Production owns implementation and evidence for page boxes, preflight,
font embedding/subsetting, image resolution, colour conversion/profile,
overprint/trapping, imposition, export, packaging, provider delivery, and
physical/provider proof. Actual printer, publisher, venue, platform, and
fabricator specifications outrank both Skills.

## Failure to cause to smallest repair and proof

| Failure signature | Likely parent cause | Smallest design repair | Required proof |
| --- | --- | --- | --- |
| Every page is competent but the publication feels monotonous | One page template, density, type scale, or image ratio repeated without a sequence thesis | Reassign communicative page/spread roles and vary density, entry, image/text relation, or scale while preserving recurring anchors | Single pages, facing spreads, and thumbnail strip compared at the same scale; content/read order retained |
| Sequence feels random or the reader gets lost | No flat plan, weak section transitions, inconsistent anchors, folios, navigation, or parent ownership | Define section/page roles and restore the smallest recurring orientation system; change local pages only where their job differs | Page/spread strip, page-turn walkthrough, navigation and accessible order check |
| Layout is crowded despite small type and tight gaps | Content allocation or page count is wrong; local spacing is compensating for overload | Edit, redistribute, add a page/panel, or change the information architecture before shrinking type or gaps | Exact-content comparison; intended-size render; sequence and page-count check |
| Layout feels empty but adding elements makes it worse | Empty area has no declared framing, pacing, direction, emphasis, or tension job; focal hierarchy is weak | Strengthen the primary relation, crop, anchor, or page role; remove decorative filler | Intended-size and thumbnail views; focal/reading path described; preserved content |
| Related items look separate or unrelated items merge | Within/between/group/section spacing or shared-edge ownership is wrong | Repair the parent group and semantic interval before adding boxes, rules, or isolated nudges | Alignment/grouping overlay plus visual review with decoration reduced |
| All roles compete | Too many hierarchy signals are simultaneously loud or page roles lack priority | Re-rank consequence and use fewer coordinated signals; quiet support roles instead of adding another accent | Squint/blur/greyscale or decoration-reduced diagnostic plus intended-size reading review |
| A facing spread works as two pages but not as a spread, or vice versa | Gutter, crossover, inside/outside margin, focal balance, or page-turn intent was ignored | Recompose the spread around protected content and binding context; keep independent-page survival where required | Facing-spread render, separated-page render, binding/gutter simulation or physical dummy |
| Content disappears, duplicates, or reads in the wrong order after a fold | Panel map, front/back orientation, fold sequence, imposition, or accessible/source order is unresolved | Correct the fold/panel architecture and protected zones before cosmetic changes | Numbered fold dummy, front/back panel map, unfolded/folded review, provider/imposition confirmation |
| Type is legible on the authoring canvas but fails in use | Final scaling, viewing distance, lighting, projection, font substitution, or substrate was not tested | Adjust role/face/size/measure/contrast at the final context; do not apply a universal point size | Final-size or bounded reduced proof under named distance/device/light; font/render receipt |
| Image, title, or annotation is clipped at trim, gutter, fold, or safe area | Wrong or assumed production geometry, or protected subject not declared | Obtain the actual authority; move or art-direct the protected element; preserve deliberate bleed only where supported | Page-box/fold/binding overlay, export render, provider preflight and physical proof as applicable |
| A template looks polished but unrelated to the subject | Style/layout chosen before content, concept, audience, and medium thesis | Return to brief evidence; derive subject-specific spatial, type, imagery, and sequence decisions; keep template only as a scaffold if still useful | Alternative rationale, subject/content trace, rendered comparison; no claim from template popularity |
| Deterministic checks pass but the result still feels weak | Bounds, overlap, DPI, and package checks were mistaken for composition judgment | Run causal visual critique; locate hierarchy, grouping, rhythm, crop, type, or subject mismatch; repair the smallest owner | Same-scale before/after renders plus qualified human/design review; technical checks remain separate |
| Deliberate overlap, asymmetry, crop, or page break is auto-normalized | Aesthetic signal or exception was mistaken for a defect | Record intent, stable counterstructure, affected contexts, required floors, and compensation; repair only the actual failure | Exact-context render, content/order/access/production checks, and preserved-strength record |

## Mechanisms to synthesize and claims to withhold

### Adopt or test through original Scoville wording

1. Require a sequence/content plan before isolated page construction.
2. Inspect fixed and paged work at four scales: detail, page/panel, facing
   spread or fold, and complete strip/sequence.
3. Record final physical or display context separately from the authoring
   canvas; label every number by authority or heuristic status.
4. Carry page, spread, panel, fold, binding, protected-zone, and final-viewing
   intent into the canonical Design record.
5. Separate deterministic artifact and production checks from semantic visual
   judgment, provider proof, and audience understanding.
6. Diagnose spacing by semantic relationship and sequence job, not by a fixed
   scale or a request for more whitespace.
7. Repair the smallest shared owner: content allocation, page role, parent,
   group, type measure, grid, crop, or medium geometry before local decoration.
8. Keep a fail-closed `Not verified` state for unresolved supplier, font,
   asset, fold, binding, colour, or physical-output claims.

### Reject from the executable package

- locked style atlases, named-publication mimicry, template catalogs, and
  provider-specific defaults presented as general design knowledge;
- universal grid, column, margin, spacing, whitespace, family-count, font-size,
  word-count, slide-count, hero-cadence, image-ratio, DPI, bleed, fold, safe-area,
  or viewing-distance numbers;
- mandatory generated imagery, generic academic poster sections, or one
  platform's authoring primitives as design requirements;
- eye-pattern, balance, harmony, professionalism, accessibility, or print-ready
  claims inferred from a checklist, geometry, or one example;
- any assumption that a repository license clears external fonts, icons,
  publication style, supplied assets, generated outputs, printer profiles, or
  provider terms;
- tests of parsing, bounds, overlap, hashes, package safety, or DPI presented as
  evidence of visual quality or reader comprehension.

## Search exclusions, independence, and limits

- [`anthropics/skills`](https://github.com/anthropics/skills/tree/53048666b05b4799081517d00e09e0a2dd688678/skills/canvas-design) had 173,178 stars. Its exact `canvas-design` directory contains the instruction and bundled font files but no inspectable output, render, test, or evaluation artifact. Font assets do not evidence the Skill's design-quality claims, so it is E0 for this comparison.
- [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills/tree/be2a406907dbc61b73e6827ded415c96139d13a2/canvas-design) had 74,289 stars and mirrors the same canvas instruction and font bundle without an exact-path design artifact. It is E0 here and does not add independent evidence.
- [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills/blob/7eb694978762421c30855d80de73d1a909a8c335/skills/design-it/editorial-design/SKILL.md) had 45,855 stars. The exact editorial directory contains only `SKILL.md`; no example, output, test, or evaluation was found. It is E0 despite exact terminology.
- Higher-star general agent collections without an exact editorial, print, multi-page, poster, or fixed-media Skill and evidence artifact were not substituted.
- Rank 3 is a stale mirror of K-Dense prior art. Its repository stars measure the whole template collection, not adoption of that poster Skill. The three ranked rows therefore contain only two independent source families.
- As a lower-star independent visual comparator, [`yanliudesign/mono-color-skill`](https://github.com/yanliudesign/mono-color-skill/tree/de607fedfff647eaf5400e0aa43085787d7d1fca) had 1,982 stars and includes multiple poster outputs, design-system data, eval cases, and validators. It was not promoted over a higher-star qualifying repository because the contract ranks by repository stars. Its useful content/space decision flow belongs primarily to Style and Composition comparison, and its fixed percentages and layout families remain recipes.
- No qualifying candidate showed professional book typography, long-document fragmentation, native multi-page source, binding/fold dummy, publisher/printer proof, or blinded comparative review across several subjects.
- E1 and E2 here support mechanism existence and technical behavior only. They do not establish that any ranked candidate “is a professional designer” or outperforms the current Scoville package.

## Proposed tests and claim ceiling

The smallest open Terra High tests for the proposed leaf should be run one at a
time after implementation:

1. **Editorial generation:** create a six-to-eight-page reading artifact from
   supplied exact copy, images, and font rights. Require a flat plan, distinct
   page/spread roles, recurring anchors, deliberate density variation, final
   dimensions, and one justified exception. Fail on template repetition,
   dropped text, generic magazine mimicry, weak type, or unexplained gaps.
2. **Brochure/fold critique:** inspect supplied flat and folded renders with one
   seeded panel-order error, crossover loss, trapped gap, valid full-bleed
   exception, and unknown printer geometry. Fail if the critic invents bleed,
   fixes the valid exception, or misses the architectural cause.
3. **Poster repair:** repair a fixed-size poster with strong concept but weak
   grouping, all-loud hierarchy, final-distance type failure, and an unsafe
   edge. Preserve concept; obtain actual dimensions/provider rules; re-render
   at final size and bounded reduced scale.
4. **Production-boundary case:** given a visually approved design and a failed
   preflight, route export/profile/font/image/provider work to Media Production
   without redesigning the artifact or claiming physical proof.

Deterministic checks can prove exact content, page/panel count, dimensions,
source links, bounds, overlaps, page boxes, font records, asset resolution,
and manifest/evidence labels. Renders can support fit and visual inspection.
A qualified designer, editor, accessibility specialist, native reader, printer,
publisher, venue, or fabricator remains necessary where their authority changes
the claim.

Even a passing set cannot prove universal taste, market preference, all media,
all scripts, legal clearance, printer/publisher acceptance, or superiority over
professional human designers. The warranted claim would be narrower: on the
tested editorial and fixed-media tasks, the Skill applied a source-bounded
medium method, produced or diagnosed the artifact, preserved deliberate
strengths, localized causal failures, made targeted repairs, and reported the
actual evidence ceiling.
