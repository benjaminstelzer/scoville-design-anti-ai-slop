# Expert-depth audit: Typography and writing systems

Date: 2026-09-02  
Audit target: `references/typography-and-writing-systems.md`  
Method: all ten sections of `reference-audit-method.md`  
Mode: read-only audit of the executable package; no executable reference,
router, registry, benchmark, Gold, or Plan was changed

Research boundary: the audit inspected the current reference, Core router,
`modules.yaml`, source ledger, rule-to-source map, the SOL baseline and module
admission evidence, the open Terra High transfer report, three directly
relevant public Skills, current standards and technical documentation, open
learning sources, and bounded empirical typography research. Public sources
were inspected on 2026-09-02. The research is targeted, not a systematic
review. It is strongest for web and Latin typography; that limitation is part
of the recommendation rather than being filled with presumed expertise.

## 1. Current contract

### Registry and evidence contract

| Field | Current value | Audit reading |
| --- | --- | --- |
| Activation | Route label `type, script, localization`; signals `typography`, `writing_system` | The route correctly admits both ordinary type judgment and writing-system risk, but one leaf must currently absorb two materially different knowledge domains. |
| Owned concerns | `type_roles`, `typesetting`, `font_fallback`, `script_requirements` | Ownership is directionally sound. Glyph differentiation, shaping, bidi/vertical behavior, font features, type-specific access resilience, and font-rights evidence are only implicit. |
| Status | `retained-floor` | Appropriate for RC7: the current evidence admits functional and external-verification floors, not specialist-equivalent teaching. |
| Intervention | `external-verification` | Appropriate. Several decisive facts are file-, engine-, language-, license-, browser-, printer-, or native-reader-specific. |
| Registered sources | L-01, L-02, L-04, L-05, L-06, L-14, L-17, L-24 | Good foundational spread, but current rule mapping is much shallower than the available sources. |
| Model evidence | `SOL-B05` in the file header; module-admission evidence also cites the typography critique in all three SOL arms and a non-decisive full-bundle ablation | `SOL-B05` is actually the annual-report case, not the dedicated typography-critique case. The source header should not imply that it identifies the typography critique. |
| Terra evidence | Public `design-val-03-typography-critique`, RUN-001 | One Terra High response passed behavior and efficiency, returned five localized findings, separated observation from likely effect, preserved strengths, made no edit, and kept an honest unrendered boundary. It is one seeded Latin/English A5 critique, not long-tail qualification. |
| Token size | 544 `o200k_base` leaf tokens; 1,827 tokens with the then-current 1,283-token Core | The leaf is well below the 1,800-token ceiling. There is room to deepen it, but not enough to teach professional Latin typesetting, font technology, and multiscript layout with adequate routing precision in one compact leaf. |

### Current operational rules

**Generation.** The leaf frames the actual language, script, numerals,
punctuation, audience and viewing context; separates legibility, readability,
voice and coverage; assigns roles before faces; asks for hierarchy, measure,
leading, alignment, hyphenation and fallbacks against real content.

**Critique.** It asks the agent to read at intended distance and zoom and to
inspect line breaks, spaces, rivers, widows/orphans, hierarchy, tracking,
leading, contrast, missing glyphs, fallback shifts and resizing.

**Repair.** It supplies one useful causal priority: fix the highest reading
cost first while preserving successful character. It does not yet give
defect-specific repair operators or regression conditions.

**Exception.** It rejects a universal serif/sans winner and fixed numeric
recipes. Expressive distortion, unusual measure, tightness, or low contrast may
be deliberate only when task, audience, redundancy and context protect reading.

**Verification.** It requires target-size renders, approved fonts and
fallbacks, supplied languages, critical states, scoped WCAG use, current
script-specific W3C material, and native-reader or font-engineering review when
the model is not the authority.

## 2. What is already strong

1. **The frame starts with the reading job, not a font catalogue.** Language,
   content length, distance, lighting, medium, hierarchy and licensing are all
   variables that can change the decision. This is more useful than selecting
   a face by generic mood alone. [L-01, L-04, L-17]
2. **Roles precede faces.** Display, navigation, body, data, caption and
   fallback are explicit jobs. This supports generation and critique without
   assuming that every project needs multiple families. [L-01, L-04]
3. **Type selection already combines aesthetic and technical fit.** Required
   characters, weights, optical sizes, numerals, language support, rendering
   and licensing are named together. This prevents a visually attractive but
   non-deployable selection. [L-04, L-06]
4. **Hierarchy is multi-variable but restrained.** Size, weight, spacing, case,
   placement and contrast are treated as coordinated signals, with the useful
   warning not to make every distinction loud. [L-01]
5. **Text composition is contextual.** Measure, leading, paragraph spacing,
   alignment, hyphenation and tracking are set against real text at final
   context rather than prescribed as universal numbers. That is consistent
   with empirical variability in line length, spacing and alignment. [L-01;
   AT-13 through AT-15]
6. **The serif/sans ceiling is correctly narrow.** The leaf refuses a category
   winner instead of turning one study into a new absolute. [L-02; AT-11]
7. **Fallback is a controlled test condition.** The instruction to test
   substitution, rather than merely list a generic stack, is a functional
   floor and directly addresses layout drift. [L-04, L-06; AT-02]
8. **Latin defaults are explicitly bounded.** Arabic, Hebrew, CJK, Indic and
   vertical writing are named as distinct systems. The native-reader and
   font-engineering boundary is honest and necessary. [L-24; AT-04 through
   AT-08]
9. **Critique is causal and preservation-aware.** The current sequence can
   locate familiar high-cost defects and avoids a redesign reflex. That is
   consistent with the successful SOL and Terra open critiques.
10. **Evidence labels remain honest.** A source file is not treated as a
    render, and a render is not treated as native-reader, print-provider, or
    production proof.

These strengths explain why the existing leaf should not be replaced by a
generic checklist. The missing work is specialist discrimination and repair,
not a longer list of familiar typography nouns.

## 3. Missing professional capability

| Capability | Current gap | Required applied capability | Consequence if absent |
| --- | --- | --- | --- |
| Glyph differentiation and confusability | “Unsupported glyphs” is named, but visually confusable characters are not. | For critical strings, compare likely confusables within and across scripts at target size, weight, medium and fallback: for example `I/l/1`, `O/0`, punctuation, diacritics, similar numerals and script-specific pairs. Separate ordinary word reading, identifiers and security-sensitive confusables. | Codes, doses, dates, prices, account IDs, URLs or labels can remain technically present but functionally ambiguous. |
| Typeface selection | Voice plus job is present but no explicit inspection sequence exists. | Inspect actual font files and specimens for repertoire, combining marks, language-specific forms, italic/bold distinction, widths, x-height/counters/apertures, axes, features, hinting/rendering behavior, fallback metrics and license. Evaluate the text roles independently. | A catalogue name or marketing description can substitute for evidence. |
| Hierarchy | Signals are listed but hierarchy is not diagnosed across a content tree. | Map semantic roles to a visual hierarchy; compare adjacent levels and recurring roles; find both collisions and needless distinctions; repair the smallest shared token or style owner. | Local tweaks can make one heading look better while weakening the whole system. |
| Family combination | No fixed count is prescribed, which is good, but no decision test replaces it. | Start with one capable family; add or remove a family only when a role, voice, repertoire, density, production or fallback need materially improves. Test combinations on real pages and all scripts, not isolated alphabet specimens. | The model may still default to “display plus body” or copy a two-font recipe. |
| Kerning, tracking and word spacing | They are named together without distinct causes. | Distinguish built-in pair positioning, uniform tracking and word-boundary spacing. Inspect representative pairs, all-caps, small text, numerals, punctuation, diacritics and script shaping; maintain a readable contrast between intra-word and inter-word space. | A tracking fix can disable optional ligatures, damage joining scripts, or erase word boundaries. |
| Contextual measure | Measure is named but not tied to task, script, device, font or columns. | Evaluate characters/words per line together with angular size, font width, line height, reading versus scanning, scrolling/paging and narrow-column behavior. Compare at least two plausible settings when the choice is material. | A remembered `65ch` or `45–75 characters` becomes cargo cult. |
| Leading and paragraph rhythm | “Leading” and paragraph spacing are present but not coupled to glyph extents or fragmentation. | Inspect ascenders, descenders, marks, ruby, stacked diacritics, x-height, measure, line count, paragraph separation, baseline relationships, columns/pages and text-spacing overrides. Repair clipping or rhythm at the owning style, not by per-line nudges. | Latin line-height can clip or collide in other scripts; a baseline grid can overrule actual text. |
| Alignment, justification and hyphenation | Rivers are inspected, but the decision path is absent. | Choose leading-edge alignment, centering, or justification by reading job, language/script, measure, engine quality and medium. When justifying, inspect word/character expansion, hyphenation dictionary, consecutive hyphens, rivers and last lines. Do not assume Arabic or CJK expands like English. | “Never justify” rejects valid editorial systems; “justify for polish” creates rivers and language errors. |
| Punctuation and microtype | Punctuation is an input, not an operational check. | Verify locale-appropriate quotes, apostrophes, dashes, ellipses, spaces, decimal/grouping signs, brackets, emphasis marks, hanging punctuation and optical margin behavior. Preserve encoded meaning and use renderer-supported microtype only after actual inspection. | English smart-punctuation rules or unsupported optical tricks can be applied globally. |
| Numerals and OpenType | Numerals and optical size are selection inputs only. | Inspect supported axes/features and choose proportional/tabular, lining/oldstyle, slashed zero, fractions, small caps, language forms and optical sizing by role. Prefer high-level controls; test fallback and synthesis. | Features can silently do nothing, disappear in fallback, or make data unstable. |
| Widows, orphans and breaks | The critique list names widows/orphans but not the fragmentation system. | Diagnose whether the cause is text fit, paragraph style, keep options, column/page geometry, language-specific breaking or late font substitution. Repair with style-level break controls and reflow; avoid manual line breaks as the default. | One page is repaired while translation, resizing or font loading breaks the next. |
| Fallback metric drift | “Fallback shifts” is present without measurable owners. | Record primary and each operative fallback; compare x-height/aspect, advance widths, ascender, descender and line gap; test before/after font load and missing-script fallback; use metric overrides only from measured font data. | Font loading or substitution changes wraps, control sizes, page count and interaction position. |
| Multiscript shaping | Scripts are listed, but repertoire is not distinguished from correct shaping. | Verify code-point coverage, mark positioning, required substitutions/ligatures, language-specific forms, digits, punctuation and shaping-engine output for real strings. Escalate unfamiliar scripts to a native reader and font engineer. | A font can contain characters but still render broken clusters or inappropriate forms. |
| Bidi and mixed direction | No semantic direction or isolation rules appear. | Preserve logical string order; set language and base direction at semantic boundaries; isolate inserted names, IDs and values; test parentheses, punctuation, numbers, cursor/selection and copy/paste in mixed runs. | Visually plausible screenshots can hide corrupted order or interaction behavior. |
| Vertical writing | Vertical is only named in a prohibition. | Test block flow, glyph orientation, vertical alternates, punctuation placement, Latin/numeral orientation, ruby/annotations, columns and reading order with a relevant renderer and native reader. | Rotating a horizontal composition is mistaken for vertical typesetting. |
| Accessibility and text-spacing resilience | WCAG is cited only as a scope boundary. | On applicable web content, test 200% text resize, reflow and the WCAG 1.4.12 spacing overrides without clipping, overlap or unrecoverable truncation. Outside web conformance, define the actual access task and user authority. | A visually approved fixed state can fail when readers change text. |
| Licensing and deployment | Licensing is an input without a receipt or action boundary. | Record font identity/version/source/license, allowed web/app/ebook/print embedding and modification/subsetting, reserved names, attribution or supplier restrictions, and the exact files delivered. Treat each font license as separate from source-text reuse. | “Free” or locally installed is misread as embeddable, redistributable or modifiable. |
| Screen and print proof | Target renders are required but proof lanes are not distinguished. | Screen: verify requested browsers/OS/rendering states, actual font loads, fallbacks, zoom, density and narrow/wide layouts. Print/PDF: preflight embedding, missing glyphs, substitution and supplier profile; inspect target-size output and obtain provider/physical proof where required. | A local screenshot or editable source is overclaimed as production proof. |
| Critique, repair and exception | The general priority is good but repair operators are under-specified. | For every finding record observation, likely reading effect, severity, root owner, smallest correction, preserved strength and regression targets. For expressive exceptions, name purpose, protected floor and compensating structure, then test the whole. | The agent can identify a symptom but repair only taste, or erase the concept while fixing it. |

The largest structural gap is not “more type tips.” It is the absence of a
repeatable bridge from actual font/text evidence to a scoped decision, repair,
and proof lane.

## 4. Rule-quality audit

### Classification

| Class | Rules that belong here | Override condition |
| --- | --- | --- |
| Binding constraints | Required text and logical order; supplied language/script; approved font files and license terms; applicable accessibility criterion; required platform, printer or publisher contract; no invented glyph coverage or proof. | Only an authorized change to the brief, rights, compliance or production contract. |
| Evidence-bounded rules | No universal serif/sans legibility winner; text must survive scoped WCAG spacing/resize/reflow; bidi and line-break behavior follow the relevant standards; font feature and fallback claims come from the actual file/engine. | Different evidence, population, language, task, font, renderer or medium. The boundary must be named. |
| Contextual conventions | Role naming, hierarchy, paragraph indents versus paragraph space, ragged versus justified composition, hyphenation practice, quotation marks, numeral style, widow/orphan tolerance and optical punctuation. | Publication, locale, genre, design system, platform, house style or deliberate concept supplies a better convention. |
| Heuristics and starting hypotheses | One capable family before adding another; distinct but coordinated roles; body measure in a moderate range; tighter display leading than body; modest all-cap tracking; preserve visible word boundaries; avoid many consecutive hyphens; prioritize the highest reading cost. | Actual text, typeface, script, audience, distance, task, device, column, density or renderer contradicts the start. Test rather than defend the number. |
| Preferences | Serif/sans pairing, symmetric type scales, a baseline grid, oldstyle numerals in editorial text, hanging punctuation, a particular rag shape, very tight display type. | Preference never overrides content, rights, access, script correctness or production. |
| Justified exceptions | Distorted display lettering, unconventional pairing, dense or sparse measure, low contrast, extreme tracking, manual composition, deliberate widows, vertical or bidi counterstructure. | Purpose is explicit; required meaning and access floors survive; a stable compensating structure exists; the exception is limited to appropriate roles; the target render improves as a whole. |

### Universals and cargo-cult numbers to reject

- “Use exactly two typefaces” or “never use more than three.” Font count is an
  outcome of roles, repertoire, system ownership and production, not a quality
  metric.
- “Serif for print, sans for screen,” “serifs guide the eye,” or the reverse.
  Category labels do not establish legibility. [L-02; AT-11]
- One universal body size, `65ch` measure, `1.5` leading, modular scale, tracking
  value, or widow/orphan count. Each can be a bounded starting point, never an
  unexplained pass/fail gate. [AT-13 through AT-15]
- “Never justify” and “justified text is more professional.” Alignment,
  hyphenation and justification are one language-, measure- and engine-specific
  system. [AT-03, AT-05, AT-14]
- “Increase letter spacing for dyslexia.” One controlled study found that
  increasing letter spacing without a corresponding word-space distinction
  slowed both tested groups; the broader literature is mixed. [AT-10]
- “Use a dyslexia font” or “open apertures guarantee readability.” Specific
  features can affect specific recognition tasks; no tested face or feature is
  a universal accommodation. [AT-10, AT-12]
- “Always enable every ligature,” “always disable synthesis,” “always use a
  slashed zero,” or “variable fonts are better.” Features and axes must exist,
  suit the role, preserve meaning and work through fallback. [AT-02, AT-06]
- “Every font with the characters supports the script.” Correct shaping,
  language forms, marks and engine behavior are separate from a `cmap` hit.
  [AT-07, AT-08]
- “Rotate the page for vertical type” or “reverse RTL strings.” Both ignore the
  writing system's layout and logical-order model. [AT-04 through AT-06]
- “`font-display: swap` always solves font loading.” Loading policy trades
  initial availability, visual swap and layout stability; primary/fallback
  metrics and the content role determine the choice. [AT-02]
- “A successful render proves the font license, every browser, every language,
  print, or native-reader approval.” Each claim needs its own receipt.

## 5. Specialist Skill prior art

Search boundary: GitHub and web search for `SKILL.md` plus typography,
typesetting, font pairing, OpenType, bidi, vertical text, writing systems and
font fallback; direct inspection of the candidate entry points, relevant
references, repository file lists and license files. Broad frontend/UI Skills
were not counted as specialist prior art.

| Skill | Version basis and license | Mechanism worth learning from | Do not copy or generalize |
| --- | --- | --- | --- |
| [`better-typography`](https://github.com/jakubkrehel/skills/tree/267330e1adfc66a718fb65fa6918c1f06d0a689e/skills/better-typography), `jakubkrehel/skills` | Commit `267330e1adfc66a718fb65fa6918c1f06d0a689e`; repository [MIT license](https://github.com/jakubkrehel/skills/blob/267330e1adfc66a718fb65fa6918c1f06d0a689e/LICENSE) | The strongest direct comparator found: rendered-first review; clear type-rendering ownership; progressive references for font choice, spacing, wrapping, OpenType and access details; high-level CSS properties before raw feature tags; explicit bidi isolation; severity and verification output. | Web/UI-only authority; fixed size, weight, measure, line-height and font-count recipes; “serif guides the eye” and category-use tables; blanket font-smoothing direction; simplified web-format claims; limited print, licensing, glyph-confusability, shaping, multiscript and native-reader workflow. No independent benchmark was found. |
| [`font-pairing-skill`](https://github.com/bilioveloso/font-pairing-skill/tree/21060b8ce647b949fa259157c9fc967e0d928d7e), `bilioveloso/font-pairing-skill` | Commit `21060b8ce647b949fa259157c9fc967e0d928d7e`; no license file or reuse grant was present in the inspected repository, so treat as reference-only/all rights reserved | Makes the font-selection workflow explicit and links roles, features, loading and pairing instead of returning one unsupported font name. | “Never more than two,” fixed brand-tier recipes, “always safe” pairings, universal weights/tracking, hard-coded font lists/imports, unsupported file-size/subsetting percentages, cross-Skill dependencies, and any wording or structure without permission. It is Latin/web/branding-centered, not a typesetting or writing-systems authority. |
| [`taste-typography`](https://github.com/madebymustafa/design-taste/blob/c4a6bff0871eb4b15371b0e7d2751628b0ed4608/skills/taste-typography/SKILL.md), `madebymustafa/design-taste` | Commit `c4a6bff0871eb4b15371b0e7d2751628b0ed4608`; [MIT license](https://github.com/madebymustafa/design-taste/blob/c4a6bff0871eb4b15371b0e7d2751628b0ed4608/LICENSE) | Demonstrates that a compact type-specialist leaf can cover pairing, scales, rhythm and review separately from a broader design package. | “Two families max,” fixed display/UI scales, universal min/max sizes, “same species is safe,” fixed line length/leading and genre-font tables. Same-brief demos are not causal evidence or professional qualification. Multiscript, bidi, vertical, license and print proof are absent. |

**Landscape conclusion.** A credible specialist *web typography* Skill now
exists and offers useful packaging and review mechanics. The bounded search
found no credible public Agent Skill dedicated to professional typesetting and
writing systems across repertoire, shaping, bidi, vertical flow, script-specific
line breaking, native-reader escalation, font licensing, fallback metrics, and
screen/print proof. That absence must remain explicit. It is not evidence that
no such Skill exists, and it must not be filled by a broad UI Skill.

## 6. Authoritative research and learning sources

Existing ledger IDs retain their ledger meaning. `AT-*` IDs below are local to
this audit and should enter the central ledger only if accepted for W-012.

| ID | Source, version/date | License or status | Claim supported | Limit and packaging use |
| --- | --- | --- | --- | --- |
| L-01 | [*Graphic Design and Print Production Fundamentals*](https://opentextbc.ca/graphicdesign/), 2015 | CC BY 4.0 except noted material | Foundational type roles, hierarchy, spacing, composition and print workflow | Introductory and aging; original attributed synthesis is allowed, embedded items need separate checks. |
| L-02 | [Richardson, *The Legibility of Serif and Sans Serif Typefaces*](https://link.springer.com/book/10.1007/978-3-030-90984-0), 2022 | CC BY 4.0 per chapter | Corrects universal serif/sans claims | Narrow question and populations; may inform attributed original synthesis. |
| L-04 | [Google Fonts Knowledge](https://fonts.google.com/knowledge) and its [open source content](https://github.com/google/fonts/tree/main/cc-by-sa/knowledge), living | CC BY-SA 4.0 | Type terminology, selection questions, script-aware typography, variables and features | Google Fonts context and uneven depth; learn/link by default, adapted expression needs a ShareAlike decision. |
| L-05 | [OERT](https://www.oert.org/en/the-project/), living/undated | CC BY-SA 2.5 Argentina | Anatomy, spacing, kerning, tracking and publication exercises | Older and incomplete; original synthesis preferred, adapted expression needs license review. |
| L-06 | [*Design With FontForge* source](https://github.com/fontforge/designwithfontforge.com), living source repository | CC BY-SA 3.0 | Font metrics, spacing, kerning, validation and script mechanics | Typeface-construction/tool scope; do not copy adapted prose into the MIT package without a license decision. |
| L-09 | [*The Elements of Typographic Style Applied to the Web*](https://webtypography.net/toc), work in progress | CC BY-NC 4.0 | Professional web-type rhythm, measure, spacing, paragraph and numeral conventions | Noncommercial and convention-heavy; reference-only for a commercial reusable package. |
| L-12 | [Butterick's Practical Typography](https://practicaltypography.com/) and [legal page](https://practicaltypography.com/legal.html), living | All rights reserved | Practitioner cross-check for documents, punctuation and composition | Opinionated; reference-only, no copied or closely adapted expression. |
| L-14 | [WCAG 2.2](https://www.w3.org/TR/WCAG22/), Recommendation 2023, especially 1.4.4, 1.4.10 and 1.4.12 | W3C document terms | Normative web resize, reflow and text-spacing resilience | Exact criterion/level/scope only; the 1.4.12 values test content loss, not preferred default typography. Original synthesis may cite criteria. |
| L-17 | [RGD *AccessAbility 2*](https://accessability.rgd.ca/), 2025 | Freely accessible; reuse license not established | Broader cross-format accessible-graphic-design practice | Reference-only until terms are verified; not a substitute for user testing. |
| L-24 | [W3C Language Enablement Index](https://www.w3.org/International/typography/) and current reports | W3C document terms; reports have different maturity | Script-specific requirements, gap analyses and current verification paths | Exact script and report status only; no universalization; cite and synthesize. |
| AT-01 | [Unicode UTS #39](https://www.unicode.org/reports/tr39/), Unicode 17.0.0, revision 32, 2025-09-04 | Unicode terms; public-reference use, redistribution/adaptation restricted | Identifier confusable detection and explicit limits of visual confusability | Security identifiers, not general typeface legibility or display normalization; reference-only and never a design oracle. |
| AT-02 | [CSS Fonts Module Level 4](https://www.w3.org/TR/css-fonts-4/), current TR inspected 2026-09-02 | W3C document terms | Font matching, `font-size-adjust`, metric overrides, synthesis, variants, variation axes, optical sizing and loading policy | Web technical contract; feature support and actual font data still require testing. Original synthesis may cite exact properties. |
| AT-03 | [CSS Text Module Level 4](https://www.w3.org/TR/css-text-4/), current TR inspected 2026-09-02 | W3C document terms | Language-dependent line breaking, hyphenation, alignment, justification, letter/word spacing and punctuation controls | Draft features and browser support vary; not a readability prescription. |
| AT-04 | [CSS Writing Modes Level 4](https://www.w3.org/TR/css-writing-modes-4/), current TR inspected 2026-09-02 | W3C document terms | Horizontal, RTL/bidi and vertical flow, block direction and glyph orientation | Web layout contract; implementation gaps and native conventions remain. |
| AT-05 | [Unicode UAX #9](https://www.unicode.org/reports/tr9/), Unicode 17.0.0 revision 51; [UAX #14](https://www.unicode.org/reports/tr14/), Unicode 17.0.0 revision 55; [UAX #50](https://www.unicode.org/standard/reports/tr50/), current | Unicode terms; reference-only for this package | Bidi ordering, line-break opportunities and vertical orientation data | Algorithms permit higher-level tailoring and do not select a good composition. Do not reproduce restricted text/data into the package without permission review. |
| AT-06 | [OpenType 1.9.1 specification](https://learn.microsoft.com/en-us/typography/opentype/spec/) and [`opsz` axis](https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxistag_opsz) | Public Microsoft specification/documentation; reuse terms apply | Feature, metric, script/language, variation and optical-size semantics | Technical capability, not proof that a font implements it well; cite/reference, synthesize originally. |
| AT-07 | [HarfBuzz shaping concepts](https://harfbuzz.github.io/shaping-concepts.html), inspected 2026-09-02 | HarfBuzz project uses the Old MIT license | Distinguishes Unicode characters from script- and language-correct shaped glyph layout | A shaping engine does not prove the selected font, text, UI or language is correct; open implementation reference. |
| AT-08 | [`fontTools.ttLib.TTFont`](https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html), inspected 2026-09-02 | fontTools project MIT license | Programmatic inspection of repertoire, metrics, features, variations and font metadata | Tool capability only; needs a defined test corpus and does not confer rights or visual quality. |
| AT-09 | [SIL Open Font License 1.1 and FAQ](https://software.sil.org/oflt/), license 2007, FAQ update shown 2017 | OFL 1.1 | Use, embedding, bundling, modification, subsetting, redistribution and reserved-name conditions for OFL fonts | Applies only when the actual font is under OFL and its package/Reserved Font Names are checked; not legal advice. License text can be referenced; no generalized permission claim. |
| AT-10 | [Galliussi et al., “Inter-letter spacing, inter-word spacing, and font with dyslexia-friendly features”](https://pmc.ncbi.nlm.nih.gov/articles/PMC7188700/), *Annals of Dyslexia* 2020 | CC BY 4.0 for the article, with item exceptions | Controlled evidence that letterform and spacing effects interact; increased letter spacing without adequate word-space distinction impaired reading speed in the tested groups | 128 Italian children, print task and tested fonts/settings; not a universal dyslexia rule. Attributed original synthesis allowed. |
| AT-11 | [Arditi & Cho, “Serifs and font legibility”](https://pmc.ncbi.nlm.nih.gov/articles/PMC4612630/), *Vision Research* 2005 | Author manuscript publicly accessible; Elsevier copyright, reuse not assumed | Controlled serif-size/spacing study found no reading-speed advantage and only a tiny threshold effect tied to spacing | Lowercase Latin and specific experimental tasks; reference-only. |
| AT-12 | [Beier & Oderkerk, “Closed letter counters impair recognition”](https://pubmed.ncbi.nlm.nih.gov/35217404/), *Applied Ergonomics* 2022 | Peer-reviewed abstract inspected; Elsevier, all rights reserved | Closed apertures impaired parafoveal identification for tested Latin letters | One typeface family and recognition task, not continuous reading or a universal aperture threshold; abstract-level/reference-only. |
| AT-13 | [Dyson & Kipping, “The Effects of Line Length and Method of Movement on Patterns of Reading from Screen”](https://journals.uc.edu/index.php/vl/article/view/5671), *Visible Language* 1998 | Public article/PDF; reuse license not established | Reading speed, preference and measure can diverge; screen movement and task matter | Older screens, English/Latin and tested lengths; `55 characters` is a result, not a universal recipe; reference-only. |
| AT-14 | [Ling & van Schaik, “The influence of line spacing and text alignment on visual search of web pages”](https://research.tees.ac.uk/en/publications/the-influence-of-line-spacing-and-text-alignment-on-visual-search/), *Displays* 2007 | Peer-reviewed metadata/abstract inspected; Elsevier reuse not assumed | In the tested visual-search task, wider line spacing and left alignment improved performance while participants preferred justification | Abstract-level, older web context and one task; do not turn into a universal ban on justification; reference-only. |
| AT-15 | [CSS Fragmentation Module Level 4](https://www.w3.org/TR/css-break-4/), First Public Working Draft 2018 | W3C document terms | Technical behavior of `widows`, `orphans`, page/column breaks and keep constraints | Work in progress and engine support varies; default value is not a design optimum. |
| AT-16 | [Adobe PDF font embedding guidance](https://helpx.adobe.com/acrobat/desktop/create-documents/explore-advanced-conversion-settings/font-handling-distiller.html), updated 2025-09-23; [Adobe Preflight checks](https://helpx.adobe.com/acrobat/using/additional-checks-preflight-tool-acrobat.html), updated 2026-02-26; [Ghent Workgroup specifications](https://gwg.org/technical-specifications/) | Proprietary professional documentation/specifications; no open reuse license established | Embedding/substitution risk, font preflight and provider-specific PDF/X workflows | Tool/provider and target-profile specific; reference-only. Supplier contract outranks generic guidance. |

### Contradictions and evidence limits

- Controlled serif studies and the open Richardson review do not support a
  category winner. Differences among actual faces, spacing, size and task
  remain material. [L-02, AT-11, AT-12]
- Line-length studies can find different performance and preference outcomes.
  A moderate measure is a useful comparison condition, not a universal target.
  [AT-13]
- Spacing can help some readers and conditions, but an isolated increase in
  letter spacing can damage word segmentation. WCAG 1.4.12 is a robustness
  test, not a default-setting recipe. [L-14, AT-10]
- Alignment evidence is task- and language-specific; professional book
  justification, UI ragged text, Arabic elongation and CJK inter-character
  methods cannot be reduced to one rule. [AT-03, AT-05, AT-14]
- The strongest open empirical sources inspected are disproportionately Latin,
  European-language and screen/print reading studies. W3C and Unicode define
  technical requirements, but they do not replace native-reader evaluation or
  empirical work for each writing system.

## 7. Applied Dos and Don’ts

| Concern | Do | Don't | Basis |
| --- | --- | --- | --- |
| Glyph differentiation | Build a critical-string specimen from the actual content and likely confusables; test primary and fallback at target size, weight, distance and medium. For identifiers, add a UTS #39/security check and a human recognition check. | Do not reject a face from an alphabet chart alone or treat the Unicode confusables list as a universal legibility score. | L-02; AT-01, AT-11, AT-12 |
| Type selection | Assign roles, then inspect the actual files for repertoire, marks, styles, widths, metrics, axes/features, rendering and license. Compare candidates on the real text. | Do not choose by category, trend, a mood adjective, Google-font availability or one polished specimen. | L-01, L-04, L-06; AT-06, AT-08, AT-09 |
| Hierarchy | Map content roles and parent/child relationships before styling. Use the fewest distinct signals that make the intended scan and reading order obvious; repair shared owners first. | Do not make every role differ in size, weight, case, colour and spacing, or fix one heading with an isolated override. | L-01 |
| Family combination | Begin with one capable family. Add, retain or remove a family only when it improves a named role, voice, repertoire, density, fallback or production need; test the system together. | Do not enforce one, two or three families as a quality gate, and do not pair only because one is serif and one sans. | L-01, L-04; bounded professional rationale |
| Kerning/tracking/word spacing | Start from the font's positioning; inspect representative pairs, caps, numerals, punctuation, marks and all scripts. Track only for a role-specific reason and keep word boundaries perceptually distinct. | Do not use tracking to repair a poor face, apply Latin all-cap spacing to joining scripts, or change letter space without checking ligatures and word space. | L-05, L-06; AT-03, AT-10 |
| Measure | Evaluate measure with typeface width, size, line height, task, language, columns, scrolling/paging and viewport. Compare at least two plausible settings when the choice is material. | Do not hard-pass `65ch`, 55 characters, or 45–75 characters across scripts and formats. | L-01; AT-13 |
| Leading and paragraph rhythm | Set line and paragraph spacing from glyph extents, marks, x-height, measure, line count, medium and script. Inspect baselines and paragraph boundaries in the target render and spacing-override state. | Do not force a baseline grid, fixed pixel line height or Latin leading onto content that clips, collides or loses paragraph structure. | L-01, L-05, L-14; AT-10, AT-14 |
| Alignment/justification/hyphenation | Choose the system by task, language/script, measure, engine and medium. When justifying, inspect rivers, word/character expansion, hyphenation quality and consecutive breaks with the correct language data. | Do not “polish” UI text with block justification, ban all editorial justification, manually reorder Arabic, or run a dictionary for the wrong language. | L-24; AT-03 through AT-05, AT-14 |
| Punctuation and microtype | Use locale/house-style authority for quotes, dashes, ellipses, decimal/grouping signs, spaces, brackets and emphasis. Inspect optical/hanging punctuation in the actual renderer and keep encoded meaning intact. | Do not apply English punctuation globally, replace semantic characters for visual similarity, or promise unsupported hanging/optical behavior. | L-04, L-24; AT-03, AT-05 |
| Numerals/OpenType/optical size | Select proportional/tabular and lining/oldstyle numerals by role; use distinct zero where ambiguous identifiers need it; inspect actual axes/features and prefer high-level controls with verified fallback. | Do not enable features by tag from memory, synthesize missing forms silently, or assume every variable font has useful `opsz`. | L-04, L-06; AT-02, AT-06, AT-08 |
| Widows/orphans and breaks | Diagnose text fit, paragraph style, keep constraints, geometry, language breaks and font substitution together. Repair the style or layout and reflow all representative content. | Do not insert manual line breaks or nonbreaking spaces as the default repair, and do not use the CSS initial `2` as a universal aesthetic standard. | L-01; AT-03, AT-05, AT-15 |
| Fallback metrics | Record every operative fallback and compare actual x-height/aspect, widths, ascent, descent and line gap. Capture pre-load, loaded and missing-script states; derive metric overrides from measured files only. | Do not call a generic family name a controlled fallback or tune `size-adjust` by eye for one heading. | L-04, L-06; AT-02, AT-08 |
| Multiscript shaping | Use real native text, language tags, suitable script fonts and an actual shaping engine. Check repertoire, required substitutions, mark placement, language forms, numerals and punctuation; obtain native-reader/font-engineer review. | Do not infer correct shaping from character coverage, transliteration, a Latin companion or one screenshot. | L-24; AT-05 through AT-08 |
| Bidi | Preserve logical order; set `lang` and semantic `dir`; isolate inserted names, IDs and values; test punctuation, brackets, numbers, selection, cursor movement and copy/paste. | Do not reverse strings, use visual-order source text or use CSS direction overrides where semantic markup owns direction. | AT-04, AT-05 |
| Vertical text | Treat vertical flow as a writing mode: test block progression, glyph orientation/alternates, punctuation, Latin/numerals, annotations and reading order with native text. | Do not rotate a horizontal block and call it vertical typesetting. | L-24; AT-04, AT-05 |
| Access resilience | On applicable web work, run 200% resize, reflow and WCAG 1.4.12 spacing overrides; preserve all content, controls and recovery paths. Define non-web access needs separately. | Do not set the WCAG override values as the default design or claim access from an unchanged screenshot. | L-14, L-17 |
| License/deployment | Keep a font receipt: family, file/version/hash when appropriate, source, license, allowed embedding/subsetting/modification, reserved names and delivered files. Recheck commercial/service terms at use time. | Do not equate “free,” installed, open source, a web subscription or an image preview with redistribution/embedding permission. | AT-09, AT-16 |
| Screen/print proof | Screen: confirm actual font loads/fallbacks, target browser/OS states, zoom and responsive wraps. Print/PDF: preflight embedded/subset fonts and missing glyphs, inspect at target size and obtain supplier/physical proof when required. | Do not call editable source syntax, one local render or outlined text production proof; outlining also changes editability/search/access behavior. | L-01; AT-02, AT-16 |
| Critique/repair/exception | Report observation → likely effect → severity → root owner → smallest correction → preserved strength → regression targets. Re-render after repair. For an exception, state purpose, protected floor and compensation. | Do not diagnose only from code when rendering determines the result, erase successful character, or preserve expression by sacrificing required reading. | Current Core and leaf; L-01, L-17 |

## 8. Architecture recommendation

### Considered mechanisms

1. **Deepen the existing single leaf.** Lowest router churn and probably
   possible at a compressed 1,700–1,800 tokens, but it keeps ordinary Latin
   type selection, complex-script shaping, bidi, font forensics, access and
   print proof in every type route. Compression would likely restore noun-list
   coverage instead of applied professional decisions.
2. **Split into two named, directly routed flat leaves.** Separates visual
   type-system judgment from font/writing-system technology while keeping mixed
   work composable. It aligns with the existing `typography` and
   `writing_system` signals and preserves depth-one routing.
3. **Keep the compact leaf and require external checks.** Cheapest context, but
   the agent still lacks the decision and repair logic needed to know what to
   inspect. Tools cannot replace the missing professional frame.

### Recommendation: split into two flat leaves (`P1`)

**A. `typography-and-typesetting`**

- Route: type roles, selection, hierarchy, family combination, measure,
  leading, paragraph rhythm, alignment, justification, hyphenation,
  punctuation, numerals, microtype, widows/orphans, type critique, repair and
  expressive exceptions.
- Owns: `type_roles`, `glyph_differentiation`, `type_hierarchy`,
  `typesetting`, `type_exception`.
- Target: roughly 1,350–1,650 tokens after focused authoring.

**B. `font-technology-and-writing-systems`**

- Route: glyph repertoire, shaping, language forms, OpenType/variation,
  fallback metrics and loading, multiscript, bidi, vertical writing,
  text-spacing resilience, type-specific license/deployment questions and
  font/render proof.
- Owns: `font_technology`, `font_fallback`, `script_requirements`,
  `bidi_vertical`, `font_proof`.
- Target: roughly 1,350–1,650 tokens.

Both leaves must be direct Core routes with **no expert-to-expert read** and no
dependency edge. A typography-only task loads A. A script, fallback, font-tech
or deployment task loads B. A mixed task loads both. With a 1,283-token Core,
the forecast is approximately 2,633–2,933 tokens for one leaf and
3,983–4,583 for both, within the existing 3,800 and 7,000 ceilings.

Ownership boundaries remain explicit:

- Design makes and judges the type decision.
- UI implements it in the incumbent framework and proves interactive states.
- Media Production owns artifact/export/preflight execution and overall
  supplier handoff; B owns the font-specific requirements and evidence asked
  of that handoff.
- Sources and Attribution owns the durable source/license registry; B owns the
  rule that a font choice cannot ship without the applicable receipt.
- Native readers, language experts, font engineers, accessibility specialists
  and print providers remain authorities, not simulated Skill roles.

The split is an architecture recommendation for W-012, not authorization to
rename the current module during W-011.

## 9. Tests and claim ceiling

### Smallest open Terra High falsifiers

| Case | Seed and task | Falsifies if | Required evidence |
| --- | --- | --- | --- |
| G1: Latin editorial generation | Create a two-page reading guide from supplied real copy, data, names and licensed font files. The brief permits either one family or a combination and requires hierarchy, body reading, captions, tabular data, microtype and one intentional display exception. | The response imposes a font-count/ratio recipe, drops text, confuses data numerals, creates weak adjacent hierarchy, introduces bad spacing/rivers/breaks, or claims proof before render/preflight. | Source validity, exact-text check, font receipt, page renders at intended size, qualified typography review. |
| G2: mixed-script generation | Create a responsive Latin/Arabic service notice with mixed names, phone numbers and IDs, plus one supplied Japanese vertical annotation. Supplied fonts and fallbacks have explicit licenses. | Source strings are visually reordered, shaping/marks fail, inserted values are not isolated, vertical type is rotated horizontal text, fallbacks are uncontrolled, or the model self-certifies native quality. | `lang`/`dir`/logical-order checks, HarfBuzz/reference shaping sample, primary/fallback screenshots, native Arabic and Japanese review. |
| C1: typography critique | Critique an intended-size screen/print pair containing seeded `I/l/1` and `O/0` code ambiguity, overtracked small caps, cramped marked text, weak word-space distinction, a widow, one deliberate eccentric headline and an unknown fallback. No edit. | The critic reports generic taste, misses the task-critical ambiguity, treats the deliberate display exception as a defect, conflates kerning/tracking/word spacing, or claims rendered/font facts it did not inspect. | Source plus actual renders, finding localization, observation/effect separation, preserved-strength record, unknowns and evidence label. |
| C2: font-tech/writing-system critique | Inspect supplied font files and rendered Arabic, Devanagari and Latin samples with one missing mark, one broken fallback run, metric shift and bidi punctuation defect. | Character coverage is mistaken for correct shaping, a script-specific problem is “fixed” with Latin spacing, metric drift is missed, or no expert escalation is named. | `fontTools` tables/coverage/metrics, shaping output, before/after-load geometry, native-reader verdict. |
| R1: responsive repair | Repair a supplied HTML article whose primary/fallback metrics change wraps, whose fixed-height labels clip under WCAG text-spacing overrides, and whose hyphenation language is wrong. Preserve content and visual owner. | Repair uses manual breaks, hides overflow, erases the design system, fails fallback/loaded states, or loses content under spacing, resize or reflow. | Parsed source, computed styles, font-load receipts, screenshots before/after load at narrow/wide widths, 200% resize, reflow and 1.4.12 override results. |
| R2: paged/print repair | Repair an editable multilingual brochure with seeded unembedded font, fallback substitution, bad page/column break and a valid intentional widow in a display quote. | Text is outlined without authority, font rights are presumed, the valid exception is erased, body widows/orphans remain, or the PDF is called production-proofed without target preflight/provider evidence. | Editable master validity, exact-text comparison, font license/embedding record, PDF preflight, rendered pages, target-size proof, provider confirmation where required. |

The cases should be open and immutable once executed. Run each changed route
through the smallest relevant selected-expert, Core-only and necessary
ablation comparison; do not promote a payload merely because it produces more
findings. A useful change must improve the target failure without regressing
brief fidelity, content preservation, ownership, evidence honesty or context
cost.

### Deterministic checks

- all required source strings and Unicode code points preserved in logical
  order;
- source parses; declared dimensions and page/viewport contract remain valid;
- font file identities, hashes/version where appropriate, licenses and
  embedding/subsetting permissions recorded;
- required `cmap`, GSUB/GPOS, axes/features and horizontal/vertical metrics
  inspected from the supplied files;
- semantic language/direction markers present; mixed values isolated; no
  manual reversal;
- actual primary font loads in the loaded state; each declared fallback is
  observable when forced; missing glyphs and `.notdef` are rejected;
- before/after font-load line boxes and protected element bounds compared;
- required text remains available at representative localization lengths,
  narrow/wide contexts, 200% resize, reflow and applicable text-spacing
  overrides;
- print/PDF syntax and page count valid; required fonts embedded/subset under
  the target profile; no unauthorized outlining;
- evidence labels match actual source, render, interaction, preflight and
  physical/provider proof.

Deterministic checks can prove presence, syntax, coverage declarations,
metrics, logical order, bounding boxes and recorded rights facts. They cannot
prove that a typeface is readable, a pairing is appropriate, a script feels
native, a rag is good, a repair preserves voice, or a print result is approved.

### Required human/domain authority

- one qualified typography reviewer for hierarchy, spacing, measure,
  composition, repair and exception judgment;
- a native reader for every consequential unfamiliar language/script;
- a font engineer when shaping, feature, metric, hinting or font-file defects
  are material;
- an accessibility specialist or affected-user test when a consequential
  access claim exceeds deterministic conformance checks;
- the printer/publisher/platform owner for production-profile acceptance;
- legal or licensing authority where commercial font rights remain unclear.

### Claim ceiling after passing

Passing these open cases can support only that the changed leaves usefully
improved the tested generation, critique or repair behaviors under the recorded
fonts, texts, engines, languages, media and reviewers. It cannot support:

- universal legibility, readability, accessibility or “best font” claims;
- one optimal measure, leading, font count, pairing or type scale;
- coverage of all languages, scripts, bidi combinations or vertical practices;
- native-reader, font-engineering, legal, printer or market equivalence;
- production proof outside the exact inspected browser/OS/PDF/profile/provider;
- expert-equivalent typography, general visual quality, preference consensus or
  lower total cost from one small sample.

## 10. Priority

**Overall priority: `P1`.** The current leaf is a safe and useful retained
floor, and its explicit native-reader/current-verification boundary prevents a
`P0` classification. It does not, however, supply enough applied capability
for the stated all-round designer goal across professional typesetting, font
technology and writing systems.

| Priority | Gap clusters | Rationale |
| --- | --- | --- |
| P1 | Glyph differentiation; type-selection inspection; spacing distinctions; contextual measure/leading; alignment/justification/hyphenation; OpenType/numerals; fragmentation; fallback metrics; multiscript shaping; bidi/vertical; access resilience; licensing and font proof; defect-specific repair | These capabilities change whether required text is correctly recognized, shaped, ordered, fitted, deployed and repaired. Their absence blocks credible professional breadth. |
| P2 | Deeper pairing discrimination, microtypographic refinement, optical margin choices, baseline/rag polish, broader professional examples | Material quality and efficiency improvements after the P1 decision/proof spine exists. |
| P3 | Historical specimen enrichment or additional named type styles without an observed behavior gap | Useful study material, but not a current package outcome need. |

Conditional escalation: a live task involving safety-critical identifiers,
medical instructions, legal text, an unfamiliar script, restricted font rights
or a production print run becomes operationally `P0` if the required domain
authority or proof is absent. The Skill must stop or bound the claim; it must
not compensate with confidence.

### Open limits

- No native-reader or font-engineering review was performed in this audit.
- No font file, shaping output, browser matrix, PDF or physical print was tested.
- The public Skill search is bounded and may miss private, newly published or
  differently named Skills.
- Several professional and peer-reviewed sources are reference-only,
  abstract-level or rights-restricted; their expression must not be adapted
  into the distributable package.
- Browser, CSS, Unicode, OpenType, font-service and license facts are mutable;
  accepted W-012 rules must retain current-verification triggers.
- Empirical evidence remains concentrated in Latin typography and specific
  reader/task conditions. That is a reason to test and escalate, not to invent
  universal rules for underrepresented writing systems.
