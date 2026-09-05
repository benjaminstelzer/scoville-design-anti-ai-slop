# Reference audit: media production and handoff

Date: 2026-09-02  
Status: W-011 research audit; executable package unchanged  
Scope: `references/media-production-and-handoff.md` and its direct Core/module contract

## 1. Current contract

### Route, ownership, evidence, and size

- **Activation:** the Direct Index selects this leaf for `artifact`, `export`,
  `preflight`, `render`, or `handoff`; `modules.yaml` maps those terms to
  `production` and `handoff`.
- **Status / intervention:** `retained-floor` / `external-verification`.
- **Owned concerns:** `artifact_contract`, `render_contract`,
  `production_preflight`, and `handoff_record`.
- **Declared sources:** L-01, L-17, L-27, L-38, P-01. Only L-01/L-27 are
  production foundations; L-17 adds cross-format access questions; L-38 is a
  volatile image-provider source; P-01 concerns Skill packaging, not artifact
  quality. The current source set does not support the full claimed PDF, print,
  SVG, document, presentation, motion, and supplier-handoff range.
- **Evaluation:** SOL-B03, SOL-B09, and SOL-B11 found malformed SVG, clipped
  social output, and presentation overlap/clipping. The R2/R3 repetition gate
  did not establish a persistent SOL-specific weakness. It does establish a
  model-independent completion floor: source validity, target rendering,
  content-fit regression, and honest evidence labels.
- **Measured size:** 331 whitespace-delimited words, 2,611 bytes, approximately
  480 tokens by the project audit's word-based proxy. This is far below the
  1,800-token cost target, but size alone is not an admission argument.

### Explicit behavior now supplied

| Mode | Current rule | Audit judgment |
| --- | --- | --- |
| Generation | Keep an authoritative editable master; record dimensions, units, colour/profile, fonts/licenses, assets, variants, access equivalents, export settings, owners, supplier facts, and approvals. | Correct frame, but no decidable artifact schema or medium-specific acceptance gates. |
| Critique | Validate syntax/resources, then inspect clipping, overflow, substitution, links, assets, transparency, resolution, data, colour, states, and crops at intended plus diagnostic context. | Strong sequence, but the list conflates static-artifact preflight with UI interaction/accessibility ownership and omits several format-critical checks. |
| Repair | Change the source, rerender, compare protected dimensions, and stop after two passes unless continuation is requested. | Good causal loop; should explicitly prohibit patching only a derivative and require source/derivative hashes and rebuild evidence. |
| Exception | Core permits a declared exception when communication/accessibility survive and compensating structure improves the whole; vendor/platform specifications outrank memory. | Useful general rule. The leaf lacks domain exceptions for outlined type, flattening, missing bleed, low-resolution intentional effects, separate print/access outputs, or provider-specific black/overprint settings. |
| Verification | Distinguish `source-created`, `syntax-validated`, `render-inspected`, `interaction-tested`, and `production-proofed`. | Essential boundary, but each label needs a scoped receipt. `production-proofed` is unsafe without proof type, process, target, date, result, and approver. |

## 2. What is already strong

1. **Source and rendition are distinguished.** The module correctly rejects the
   common category error that an editable/source file is already a render, or
   that a render is already a physical/provider proof. This is its strongest
   professional safeguard.
2. **Inspection follows construction.** Syntax/resource validation before
   visual judgment prevents a polished screenshot from hiding malformed XML,
   missing links, substituted fonts, or an unrebuildable artifact.
3. **Intended and diagnostic contexts are both required.** A production check
   at final size plus a thumbnail, crop, projection, alternate viewport, or
   proof reveals defects that a single authoring view misses.
4. **The handoff inventory is cross-medium.** Dimensions, units, colour,
   profiles, fonts, assets, variants, safe/crop areas, access equivalents,
   current provider facts, ownership, and approvals are the right classes of
   information.
5. **Repair is bounded and regression-aware.** Repairing the smallest coherent
   cause, rerendering, and comparing protected dimensions is better than
   cosmetic patching or open-ended churn.
6. **Volatile facts remain external.** The instruction that current supplier
   and platform requirements outrank memory is correct and source-bounded.
7. **The leaf is routed only by explicit production concerns.** It is not a
   default design checklist, so deeper content can remain selectively loaded.

## 3. Missing professional capability

### Contract and traceability

- Define an **artifact contract**, not merely a list of questions. At minimum:
  artifact ID and purpose; authoritative source or build graph; required source
  and rendition formats; geometry/units; target medium/process/platform;
  editable/native versus placed/flattened elements; fonts and permitted
  embedding/packaging; linked assets with hashes, rights, and versions; crop,
  safe, trim, bleed, dieline, and finishing geometry where relevant; colour
  spaces/profiles/output intent; accessibility equivalents and reading order;
  export preset/tool/version; validator/render/proof receipts; owners,
  approvals, and unresolved risk.
- Treat “one master” as **one authority graph**, not necessarily one file. A
  generated SVG, deck, or motion project may require source code, data, assets,
  fonts, and a lockfile. The contract must say what rebuilds what.
- Fingerprint source inputs and renditions. A handoff without hashes or stable
  version IDs cannot prove that the inspected file is the delivered file.

### Format-specific production depth

- **SVG:** preserve live text and semantics when the output must stay searchable,
  selectable, localizable, or accessible; control font availability; produce an
  outline-only supplier derivative only when required; preserve the live-text
  master and accessible equivalent. Check namespaces, viewBox/dimensions,
  external references, embedded rasters, filters, clipping, scripts/event
  handlers, IDs, and rendering in the actual embedding context.
- **Raster variants:** distinguish highest-authority master from target
  renditions. Record pixel dimensions, intended displayed/printed size,
  effective resolution, crop/focal intent, alpha, compression, colour profile,
  sharpening/resampling, and variant hash. Upsampling does not create captured
  detail.
- **Print/PDF:** select the receiver's PDF/X part/profile instead of saying
  “print-ready.” Verify output intent, embedded fonts, page boxes, separations,
  spot names/alternates, overprint, total ink/black rules supplied by the
  process, transparency/blending space, effective image resolution, dieline and
  finishing layers, and current supplier preflight. PDF/X itself does not set a
  universal image-resolution threshold or bleed amount.
- **Fonts:** distinguish visual presence, PDF embedding, editable-document
  embedding, and permission to package raw font files. Preserve exact font
  versions and fallback behavior; do not infer license from successful export.
- **Documents and presentations:** preserve native styles, objects, charts,
  tables, source data, notes, and rebuild source where practical. Validate
  pagination/slide geometry, overset/overflow, font substitution, reading order,
  alt text, headings/tables/language, projection and print context, and the
  actual exported PDF rather than assuming authoring semantics survive export.
- **Motion:** record composition size, frame rate, duration/timebase, codec and
  container, alpha and colour handling, audio/caption tracks, safe areas,
  platform limits, loop/final-hold behavior, poster frame, and reduced/static
  equivalent. Inspect timed playback and representative frames; a storyboard is
  not an encoded-delivery proof.

### Production judgment and escalation

- Replace symptom lists with **failure → cause → repair → proof**. Examples:
  clipped copy may come from font substitution or the wrong aspect ratio, not
  merely a small box; muddy brand colour may come from the wrong output intent
  or substrate, not from “bad CMYK”; missing white art may come from accidental
  overprint; inaccessible reading order may come from source object order, not
  visible geometry.
- Distinguish parser/build success, render fit, semantic/access inspection,
  soft proof, validation print, contract proof, physical sample, press check,
  and supplier approval. Each answers a different question.
- Packaging and wayfinding remain **risk/owner stubs**. The leaf may verify file
  disposition, dieline/layer separation, sign/display PDF requirements, and
  evidence transfer; it must escalate structural packaging, materials,
  tolerances, finishes, legal copy, tactile/Braille, installation, human-factors,
  safety, and jurisdictional duties to qualified owners.
- Clarify **Design versus UI ownership**. Design/Media owns visual intent,
  artifact/export contracts, static assets, and evidence transfer. The incumbent
  UI owner implements DOM/native semantics, components, responsiveness, states,
  input behavior, and interaction tests. Media may carry an `interaction-tested`
  receipt; it must not invent or self-certify one.

## 4. Rule-quality audit

| Class | Rules that belong | Necessary correction or exception |
| --- | --- | --- |
| Binding constraints | Required content and dimensions survive; files parse/build; linked resources resolve; output matches the named receiver contract; rights/access/production unknowns stay explicit; evidence labels describe only completed checks. | A visually attractive output never overrides these floors. Fail closed when the required receiver profile, font permission, or proof authority is unknown. |
| Evidence-bounded rules | PDF/X requires the selected conformance behavior, self-contained printable content, embedded fonts, and an output intent; PDF/UA/WTPDF and WCAG PDF techniques govern tagged-PDF semantics in their stated scopes; SVG live text preserves text data; ICC profiles communicate colour conditions. | Cite the exact part/version and receiver. Do not turn one PDF/X, PDF/UA, SVG, or ICC rule into a universal cross-format command. |
| Contextual conventions | Native editable objects, linked assets, PDF/X-4, process-black text, live transparency, safe areas, package folders, and separate renditions are often useful. | They are defaults only when the target toolchain, process, receiver, and rights allow them. |
| Numeric starting points | 300 ppi, 3 mm bleed, 24/30/60 fps, social pixel presets, rich-black recipes, and type/safe margins may seed a provider discussion. | None is universal. Effective resolution depends on final size and process; bleed/black/codec/frame rate/safe area come from the actual receiver and production method. |
| Preferences | File naming style, folder depth, archive layout, whether source is code or a native application file, and whether one or several delivery renditions are preferred. | Make these project conventions unless they affect reproducibility or receiver acceptance. |
| Justified exceptions | Outlined-text derivative, flattened transparency for a legacy RIP, deliberately coarse raster treatment, zero bleed for content with no edge bleed, raster-only final, or separate print/access PDFs. | Preserve an editable/semantic authority source, declare the reason, compensate with an accessible/text equivalent where needed, and prove the actual receiver output. |
| Reject as slogans or cargo cult | “CMYK from the start,” “always 300 DPI,” “3 mm bleed is mandatory,” one fixed rich black, “PDF/X means press-ready,” “tagged means accessible,” “outlined means safe,” “all SVGs need title and desc,” “screen proof equals print,” or “export succeeded means done.” | Each collapses a conditional production decision into a false universal and can cause rework, access loss, or expensive output failure. |

The current leaf contains no overt numeric cargo cult. Its risk is the opposite:
its broad checklist is too underspecified to decide acceptance, exceptions, or
the proof needed for each medium.

## 5. Specialist Skill prior art

The GitHub search covered `preflight`, `PDF/X`, print production, SVG export,
tagged PDF/reading order, editable document/deck, render validation, motion
export, and production handoff. No inspected Skill credibly spans the complete
cross-media professional contract; the useful mechanisms are distributed.

| Skill | Pinned inspection | License | Mechanism worth learning from | Do not copy or generalize |
| --- | --- | --- | --- | --- |
| [`packaging-print-production`](https://github.com/omer-metin/skills-for-antigravity/blob/e8dcf4e8737921a10088bd5c9eb65e81f74c051f/skills/packaging-print-production/SKILL.md) | `e8dcf4e8737921a10088bd5c9eb65e81f74c051f`, 2026-01-22 | Apache-2.0 | Separates creation patterns, sharp edges, and validation; makes manufacturing constraints visible. | Invented “veteran” authority and universal CMYK, bleed, type-size, box-clearance, rich-black, stock, and finishing recipes. Supplier/process evidence must replace persona certainty. |
| [`svg`](https://github.com/mgifford/accessibility-skills/blob/f2cbb99c5a45a02f47002923f020f5098b552bb0/skills/svg/SKILL.md) | `f2cbb99c5a45a02f47002923f020f5098b552bb0`, 2026-07-31 | AGPL-3.0 | Chooses semantics by SVG purpose/embedding context and includes sanitization and final-context testing. | The metadata's blanket title/description mandate conflicts with the body and must not become a universal rule; AGPL text is not reusable in an MIT payload without a license decision. |
| [`presentation-skill`](https://github.com/siril9/presentation-skill/blob/311e29920c7c7ab37a93c12676bab7baecc0f4a6/SKILL.md) | `311e29920c7c7ab37a93c12676bab7baecc0f4a6`, 2026-08-24 | MIT | Source-first rebuilds, stable object IDs, editable native objects, artifact manifests, render QA, and receipts. | Its toolchain, coordinate-free IR, grammar system, and deck-specific thresholds are implementation choices, not general handoff law. |
| [`docx`](https://github.com/Last-emo-boy/oai-skills/blob/361d1aa63eb2df497f268568feeb562a96182a8c/docx/SKILL.md) | `361d1aa63eb2df497f268568feeb562a96182a8c`, 2026-05-26 | No repository license detected; reference-only | Render every page, repair source, rerender, and use format-specific audits/diffs rather than trusting OOXML or text extraction. | No permission to reuse expression; “flawless” is an overclaim, and a raster render cannot prove reading order, alt quality, or Office interoperability. |
| [`motion-design-agent` export](https://github.com/soilmass/motion-design-agent/blob/132c9d59231cf0fd91964ee433ba9e7e0b3bbf6d/skills/export/SKILL.md) | `132c9d59231cf0fd91964ee433ba9e7e0b3bbf6d`, 2026-01-24 | MIT | Flat export route and explicit format/resolution/frame-rate/quality dimensions. | Platform presets and frame-rate/codec recipes are neither current receiver contracts nor proof; its standards claims are broader than the inspected evidence. |
| [`latex-posters`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/1dd0fccf46fc3c9855c4a0c313a0c57fe4319883/skills/latex-posters/SKILL.md) | `1dd0fccf46fc3c9855c4a0c313a0c57fe4319883`, 2026-08-31 | MIT | Compile, inspect edges, and treat overflow as a delivery error. | Fixed visual percentages, word/element limits, font sizes, and mandatory AI imagery are cargo-cult constraints; mentioning PDF/X does not establish correct prepress. |
| [`PDF Converter`](https://github.com/claude-office-skills/skills/blob/9c4c7d5cd2813a8936bf2c9fdb174ea883b85a11/pdf-converter/SKILL.md) | `9c4c7d5cd2813a8936bf2c9fdb174ea883b85a11`, 2026-01-31 | MIT | Makes conversion direction and post-conversion checking explicit. | Star ratings, universal DPI tables, “perfect” conversion claims, and generic “preserve exact formatting” language lack production, accessibility, or receiver proof. |

Prior art therefore supports a source-first, render-and-repair, receipt-bearing
architecture. It does not justify importing universal production numbers or
claiming specialist prepress, accessibility, packaging, or motion authority.

## 6. Authoritative research and learning sources

Audit-local IDs below are proposed additions or refinements for the ledger; they
do not modify the executable source map.

| ID | Source, version/date, status | Claim supported | Limit and reuse status |
| --- | --- | --- | --- |
| MP-01 | PDF Association, [*PDF/X in a Nutshell 2.0*](https://pdfa.org/wp-content/uploads/2017/05/PDFX-in-a-Nutshell.pdf), 2017 public technical guide | PDF/X files are complete/printable under the selected part; fonts are embedded; output intent identifies printing conditions; TrimBox/BleedBox relationships matter. PDF/X does **not** set universal minimum image resolution or bleed amount. | Secondary guide to ISO 15930, not the standard itself; reuse license not verified, so reference and synthesize only. |
| MP-02 | Ghent Workgroup [technical specifications](https://gwg.org/technical-specifications/), 2022/2015 families; [digital print](https://gwg.org/technical-specifications/digitalprintspecification/), [packaging](https://gwg.org/technical-specifications/gwg-2015-packaging-specification/), [sign/display](https://gwg.org/technical-specifications/sign-display-specification/), and [job tickets](https://gwg.org/job-tickets/), living pages inspected 2026-09-02 | PDF/X-Plus preflight is market-specific; digital print, packaging, and sign/display differ; white overprint and transparency blending are failure surfaces; job tickets carry intent/approval/viewing-condition metadata. | Exact receiver and latest profile still govern. No reuse license established; reference-only. |
| MP-03 | International Color Consortium, [ICC.1:2022-05 and ICC.2:2019](https://www.color.org/specifications/), current list inspected 2026-09-02 | Profiles and registered characterization data communicate device/document colour conditions and enable managed conversions/proofing. | Colour management does not predict ink/substrate/finish without the actual process and proof. ICC specifications are copyrighted; reference-only. |
| MP-04 | ISO/TC 130, [*Guidelines for using print production standards*, v1.0](https://committee.iso.org/files/live/sites/tc130/files/Resources/Guidelines%20for%20using%20print%20production%20standards%20v1.0%202019.pdf), 2019 | Separates soft proof (ISO 14861/12646), contract proof (ISO 12647-7), validation print (ISO 12647-8), viewing conditions (ISO 3664), PDF/X delivery, and process-dependent requirements. | Overview, not conformance proof; individual standards and current provider implementation remain authoritative. No adaptation license assumed. |
| MP-05 | W3C, [SVG 2 Text](https://www.w3.org/TR/SVG2/text.html), [SVG 2 structure/accessibility](https://www.w3.org/TR/SVG/struct.html), living Recommendation/draft set inspected 2026-09-02 | SVG text remains character data, supporting search, selection, localization, and accessibility; rendering depends on font resources; essential SVG needs correct final-context semantics. | Browser/AT/tool support varies; SVG text or `<title>` alone is not an accessible equivalent. W3C document terms permit reference; any adaptation must follow those terms. |
| MP-06 | Microsoft, [OpenType 1.9.1 OS/2 `fsType`](https://learn.microsoft.com/en-us/typography/opentype/spec/os2), inspected 2026-09-02; Adobe Fonts, [font-file packaging](https://helpx.adobe.com/fonts/web/getting-and-using-fonts/package-font-files.html), updated 2025-11-12 | Embedding permissions distinguish restricted, print/preview, editable, no-subsetting, and bitmap-only use; packaging raw fonts is a separate license question. | Metadata cannot replace the EULA or jurisdiction-specific review. Public proprietary documentation; reference-only. |
| MP-07 | Adobe InDesign, [preflight](https://helpx.adobe.com/uk/indesign/desktop/print/preflight/configure-and-use-the-preflight-panel.html), [effective PPI](https://helpx.adobe.com/indesign/desktop/troubleshoot/file-and-output-issues/pixelated-graphics.html), and [overprint/black](https://helpx.adobe.com/indesign/desktop/print/color-output-and-separations/about-overprinting.html), updated 2026 | Preflight checks missing fonts/links, overset text, and resolution; effective PPI depends on final scaling; overprint/black behavior must be previewed and provider-specific rich-black values requested. | Product behavior and examples are not universal production standards; “300 ppi” is a common example, not a cross-process law. Adobe terms; reference-only. |
| MP-08 | ISO, [ISO 14289-2:2024 (PDF/UA-2)](https://www.iso.org/standard/82278.html); PDF Association, [Well-Tagged PDF 1.0](https://pdfa.org/wp-content/uploads/2024/02/Well-Tagged-PDF-WTPDF-1.0.pdf), 2024 | Defines accessible/reusable Tagged PDF 2.0 structure and the current PDF/UA-2 technical boundary. | PDF/UA does not prove content quality, colour/contrast, cognitive access, or the conversion process. ISO text is copyrighted; WTPDF 1.0 is CC BY 4.0 and may inform attributed original synthesis. |
| MP-09 | W3C WAI, [PDF1 alt text](https://www.w3.org/WAI/WCAG22/Techniques/pdf/PDF1.html) and [PDF3 reading/tab order](https://www.w3.org/WAI/WCAG21/Techniques/pdf/PDF3), updated 2025 | Tags, alternatives, logical reading order, and tab order must be checked in the delivered PDF; authoring structure can fail during conversion; manual/AT inspection remains necessary. | WCAG techniques are sufficient examples, not mandatory methods or complete PDF/UA evaluation. W3C document terms apply. |
| MP-10 | Microsoft, [PowerPoint accessibility guidance](https://support.microsoft.com/en-us/accessibility/powerpoint/make-your-powerpoint-presentations-accessible-to-people-with-disabilities), current page inspected 2026-09-02 | Reading order, alt text, object grouping, built-in structure, Accessibility Checker, screen-reader review, and tagged-PDF export are distinct checks. | Product-specific and not evidence that an exported PDF preserved every semantic relationship. Microsoft site terms; reference-only. |
| MP-11 | W3C, [responsive-image use cases](https://www.w3.org/TR/respimg-usecases/) and [Images Tutorial](https://www.w3.org/WAI/tutorials/images/); Adobe, [JPEG/PNG export options](https://helpx.adobe.com/indesign/desktop/save-export-and-publish/save-and-export/jpeg-and-png-export-options.html), inspected 2026-09-02 | Crops/variants follow use context; alternatives follow image purpose; pixel size, resolution, profile, alpha/compression, and overprint simulation are explicit rendition choices. | Web source selection and static export are different production contexts. W3C terms/Adobe terms apply; synthesize, do not copy proprietary prose. |
| MP-12 | Accessibility Standards Canada, [CAN-ASC-2.4 overview](https://accessible.canada.ca/standards-and-technical-guides/standards-and-technical-guides-database/overview-draft-standard-can-asc-24-wayfinding-and-signage), 2026 **draft**; U.S. Access Board, [ADA signs guide](https://www.access-board.gov/ada/guides/chapter-7-signs/), current U.S. guidance | Wayfinding is a multisensory environmental system; sign character, tactile, placement, contrast, and installation duties are jurisdiction- and sign-type-specific. | Canadian source is draft and expected to change; U.S. rules are not global. Use only to enforce escalation and current-jurisdiction checks, not to teach universal wayfinding dimensions. |

The contradiction check resolves the most consequential apparent conflicts:
live text improves editability/semantics but may require a controlled outlined
supplier derivative; PDF/X controls exchange but not every process tolerance;
Tagged PDF is necessary structure but not sufficient access proof; and a soft
proof is useful prediction but not a contract proof, physical sample, or press
approval.

## 7. Applied Dos and Don’ts

### Intake, masters, and derivatives

- **Do** freeze the receiver contract before export: target, dimensions/units,
  process/platform, required standards, editable/native requirements, assets,
  fonts, colour, access equivalents, variants, owner, deadline, and proof/approval
  authority. **Do not** accept “high-res,” “print-ready,” “editable,” or
  “accessible PDF” as complete specifications. [MP-01–MP-04, MP-08–MP-10]
- **Do** identify the authority graph and rebuild command/tool versions; hash
  every declared source input and released rendition. **Do not** patch only a
  PDF/PNG/PPTX derivative when a source of truth exists. A mismatched hash means
  the prior render or proof no longer covers delivery. [SOL-B03/B09/B11;
  bounded reproducibility rationale]
- **Do** keep destructive conversions as named derivatives. **Do not** replace
  live text, layers, linked data, native charts, or editable motion with flattened
  output unless the receiver requires it and the authority source remains.

### SVG and raster output

- **Do** keep SVG text as text when search, copy, localization, accessibility,
  or editing matters; package/serve licensed font resources or choose a verified
  fallback. **Do not** outline silently. If a receiver requires outlines, create
  `supplier-outlined` beside `master-live-text`, preserve exact text elsewhere,
  and compare both renders. [MP-05, MP-06]
- **Do** parse SVG/XML, verify viewBox and declared geometry, resolve or reject
  undeclared external resources, inspect embedded rasters/filters/clips, and
  sanitize untrusted or generated SVG before rendering. **Do not** infer safety
  or accessibility from valid XML. Test the actual `<img>`, inline, object, print,
  or slide embedding context. [MP-05; specialist-Skill mechanism from section 5]
- **Do** record each raster rendition's pixel dimensions, target size, effective
  resolution, crop/focal intent, resampling/sharpening, alpha, compression,
  profile, and hash. **Do not** call an upsampled file a higher-detail master or
  reuse one crop across incompatible aspect ratios. [MP-07, MP-11]

### PDF and print

- **Do** obtain the supplier's current PDF/X part/profile and finishing/dieline
  instructions; then preflight file integrity, output intent, font embedding,
  page boxes, separations, spot alternates/names, overprint, white objects,
  transparency/blending space, effective resolution, trim/bleed geometry, and
  protected copy. **Do not** label a generic PDF preset “press-ready.” [MP-01–MP-04,
  MP-07]
- **Do** derive minimum effective resolution and bleed/safe requirements from
  final size, image content, screening/output process, finishing tolerance, and
  receiver profile. **Do not** enforce 300 ppi or 3 mm as universal laws. A
  deliberately coarse image or zero-bleed page may pass if the declared intent
  and actual process proof pass. [MP-01, MP-02, MP-04, MP-07]
- **Do** inspect separations and overprint with the appropriate tool and proof.
  **Do not** apply one rich-black formula, use registration colour for ordinary
  black, or assume screen appearance predicts ink interaction. Accidental white
  overprint can remove content; wrong blending space can shift colour; wrong
  black construction can cause show-through, registration, drying, or ink-limit
  problems. Repair the source colour/overprint state and rerun the receiver
  preflight. [MP-02, MP-03, MP-07]
- **Do** keep live transparency when the selected standard/RIP supports it and
  flatten only for a documented legacy contract. **Do not** flatten early merely
  from habit; flattening can rasterize type, create stitching, or change blends.
  Compare separation/render output after any conversion. [MP-01, MP-02]

### Fonts, documents, presentations, and motion

- **Do** inventory font file/version, glyph coverage, source use, PDF embedding,
  editable-document embedding, and raw-file packaging permission separately.
  **Do not** infer that “embedded in PDF” permits sending the font file or editing
  a shared template. Repair with a licensed embed, receiver-owned font, verified
  fallback, or controlled outline derivative—not a silent substitution. [MP-01,
  MP-06]
- **Do** keep native document/deck styles and objects when they must be edited;
  preserve chart/table data and rebuild source; render every page/slide and test
  dense/corner cases, notes, projection, and print. **Do not** treat a clean
  contact sheet as semantic proof. Inspect reading order, language, headings,
  tables, links, alternatives, and the exported PDF itself. [MP-08–MP-10]
- **Do** record motion timebase/frame rate, duration, size, codec/container,
  alpha/colour, audio/captions, loop and final hold, safe areas, target platform,
  poster frame, and reduced/static output. **Do not** substitute a storyboard or
  source preview for final encode/playback inspection. Fix the authority source,
  re-encode, inspect timed playback plus representative frames, and verify the
  reduced/static equivalent. [Receiver specification; bounded media rationale]

### Accessibility, supplier proof, and ownership

- **Do** treat authoring semantics, exported tags, automated conformance, manual
  reading order, screen-reader/keyboard use, and alternative quality as separate
  evidence. **Do not** claim accessibility because a file is tagged or an
  automated checker is green. [MP-08–MP-10]
- **Do** name proof type and scope: calibrated soft proof, validation print,
  contract proof, physical prototype, press check, platform upload, or supplier
  acceptance. Record target hash, tool/device/process/profile, conditions, date,
  result, reviewer/approver, and open deviations. **Do not** promote a monitor
  preview or internal render to `production-proofed`. [MP-02–MP-04]
- **Do** let packaging/wayfinding production pass validate file layers,
  geometry disposition, receiver format, and evidence transfer. **Do not**
  approve dieline engineering, tolerances/materials/finishes, mandatory copy,
  Braille/tactile fabrication, sign placement, installation, safety, or legal
  compliance without the correct supplier, engineer, accessibility specialist,
  and jurisdiction owner. [MP-02, MP-12]
- **Do** hand Design/UI the same compact canonical record. Media may define
  static asset/export acceptance and carry UI receipts. **Do not** override an
  incumbent component system or claim `interaction-tested`; the UI owner must
  implement and exercise responsive behavior, semantics, states, focus, input,
  and recovery. [Core ownership; module-admission boundary]

### Causal critique format

Report each material issue as: **observable failure → likely production cause →
affected receiver/risk → smallest source repair → exact rerender/preflight/proof
that can close it**. Preserve successful choices. Separate binding failure,
current receiver fact, heuristic, and preference.

## 8. Architecture recommendation

### Decision: retain one leaf and deepen it

Choose candidate A: one `media-production-and-handoff` leaf with a common
artifact/evidence contract followed by flat, directly selectable internal gates
for SVG/raster, PDF/print, document/presentation, motion, and web/UI handoff.
The shared causal spine—authority source → derivative → validator → render →
semantic/access check → provider/physical proof → receipt—would be duplicated or
lost in an early split.

- **Current measured payload:** about 480 proxy tokens.
- **Professionally sufficient first candidate:** likely 2,800–4,000 tokens once
  the contract, medium gates, exceptions, repairs, ownership, and proof receipts
  are all expressed. This deliberately exceeds the 1,800-token cost target until
  an ablation proves a smaller payload non-inferior.
- **Expected load frequency:** low-to-medium and explicit; ordinary design does
  not load it, but every actual export, deliverable artifact, supplier transfer,
  or rebuildable handoff should.
- **Common combinations:** colour + media for managed print/reproduction;
  imagery + media for source/raster/crop variants; motion + media for encoded
  delivery; information/data + media for editable charts/data handoff; UI +
  media for asset/export contracts; sources/culture only when licensing,
  provenance, privacy, sustainability, or current facts are materially open.
  These are concern-driven combinations, not mandatory dependencies.
- **Progressive disclosure:** keep the Core route label and module entry compact;
  place one shared contract first, then clearly headed medium gates. Do not make
  the agent read one expert through another.

Candidate B—a split into `digital-artifact-validation` and
`print-accessible-handoff`—is premature and wrongly couples accessible documents
only to print. Reconsider flat leaves only after open routing data shows stable,
independent signals such as `print_prepress`, `accessible_document_handoff`, and
`motion_export`, and after multi-leaf tests show the common contract is not lost.
Candidate C—only external-specialist stubs—is too shallow: hashes, source-first
repair, format validation, render inspection, evidence labels, and ownership are
general completion duties even when a specialist must approve production.

No smallest tested non-inferior payload exists yet. Compression may remove
history, repeated examples, and tool-specific commands only after generation,
critique, repair, exception, ownership, and proof tests pass.

## 9. Tests and claim ceiling

### Smallest open Terra High falsification set

1. **Generate / cross-format handoff:** create a rebuildable live-text SVG plus
   two raster variants and an artifact manifest. Require declared dimensions,
   source/variant hashes, crop intent, fonts/license state, profile, parser pass,
   intended and alternate renders, and an explicit evidence receipt. Failure if
   text is silently outlined, external resources are undeclared, hashes do not
   match, or a render is called production proof.
2. **Critique / print:** inspect a supplied brochure or package PDF containing a
   mix of defects and legitimate exceptions: wrong/missing output intent, an
   unembedded font, accidental white overprint, receiver-specific low effective
   resolution, correct zero-bleed content, and one intentional spot/transparent
   element. The answer must distinguish PDF/X rules from receiver rules, find
   causes, preserve the exception, and request the missing supplier proof rather
   than invent numeric repairs.
3. **Repair / source-first:** repair a source deck/document with font
   substitution, clipped copy, wrong object/reading order, missing image
   alternative, and a broken PDF export. Require source change, rebuild, page/
   slide renders, content/geometry regression, exported-PDF tag/order inspection,
   and before/after hashes. Failure if only the derivative is patched or visual
   fit is called accessibility conformance.
4. **Motion delivery:** critique and repair a short loop whose frame rate,
   platform dimensions, last frame, captions/audio state, and reduced/static
   equivalent are inconsistent. Require timed playback evidence and exact export
   receipt; no fixed codec/frame-rate answer is Gold unless the receiver contract
   supplies it.
5. **Ownership/escalation:** hand off a responsive UI asset package and a
   wayfinding/package file. The Skill must define static artifact acceptance,
   route interaction/state testing to UI, and escalate physical/jurisdictional
   approval without claiming it.

Run current leaf, proposed full leaf, and compressed candidate on identical
prompts with frozen renderer/tool versions. Generation, critique, and repair
must each appear. A smaller payload is non-inferior only if it preserves every
hard contract, correct exception, causal repair, owner, and evidence boundary;
token reduction cannot offset a critical miss.

### Deterministic and human/domain evidence

- Deterministic: XML/OOXML/PDF parse; schema/build; resource resolution; hash
  graph; dimensions/page boxes; font/resource inventory; pixel dimensions and
  effective-resolution calculation; overflow/out-of-bounds checks; PDF metadata,
  tags, and declared conformance; codec/container/media probe; content/data diff.
- Rendered: intended size plus diagnostic alternate; page/slide contact sheet
  plus detail views; separations/overprint/soft-proof view where applicable;
  timed motion playback and sampled frames.
- Human/access: visual review, actual reading/tab order, alternative-text quality,
  screen-reader/keyboard check for the delivered format, and native-reader review
  where writing systems require it.
- Domain authority: current supplier preflight, calibrated proof or physical
  sample, prepress approval, and packaging/wayfinding/accessibility/jurisdiction
  specialist approval where the artifact crosses those boundaries.

### Claim ceiling

Passing these tests can support that the Skill produces traceable editable
artifacts, catches the tested production defects, repairs authority sources, and
labels tested evidence honestly. It cannot establish universal print readiness,
colour match, accessibility conformance, font/asset permission, physical safety,
packaging or wayfinding expertise, supplier acceptance, platform acceptance,
professional taste, or improvement on untested media. Automated validation and
one reviewer remain narrower than multi-tool, assistive-technology, supplier,
and physical-production qualification.

## 10. Priority (P0–P3)

### P0 — prevent false proof, access harm, and destructive production

1. Replace the unqualified `production-proofed` interpretation with a scoped,
   hash-bound receipt that names proof type, target/process/profile, conditions,
   date, result, and authority. A render or soft proof must never silently satisfy
   physical/provider proof.
2. Add conditional PDF/X/receiver preflight and explicitly reject universal
   resolution, bleed, rich-black, and flattening recipes. Missing output intent,
   fonts, page boxes, overprint, transparency, or receiver evidence can cause
   costly rework or content loss.
3. Add delivered-format accessibility gates for documents, decks, SVG, and PDF:
   semantics/tags, reading order, alternatives, language/structure, and manual/AT
   verification. Visual rendering alone is insufficient.
4. Preserve live/editable/semantic authority sources and make destructive
   outlined, flattened, or rasterized outputs named derivatives.

### P1 — complete the all-round production capability

1. Add the decidable artifact contract, source/derivative hash graph, rebuild
   record, current receiver version, and source-first repair rule.
2. Add the SVG/raster, print/PDF, font, document/presentation, and motion gates,
   each with failure → cause → repair → proof and justified exceptions.
3. Correct the Web/UI row so Media owns artifact/export evidence while UI owns
   component/framework implementation, responsive states, semantics, and
   interaction tests.
4. Expand the source map from broad textbooks/provider prompting to MP-01–MP-12
   or source-equivalent current standards and product documentation.

### P2 — depth and efficiency after coverage

1. Test whether print, accessible-document, and motion-export signals justify
   flat routed leaves; do not split on topic names alone.
2. Add tool-adapter examples only for validators/renderers actually available,
   with versions and failure meanings; keep commands out of the conceptual core.
3. Ablate the likely 2,800–4,000-token full leaf to the smallest non-inferior
   payload after all hard tests pass.

### P3 — enrichment only

- Historical prepress workflows, file-format chronology, broad vendor catalogs,
  and extensive worked examples may improve education but do not close a current
  outcome gap. Keep them out of the ordinary payload unless a later evaluation
  shows a specific need.
