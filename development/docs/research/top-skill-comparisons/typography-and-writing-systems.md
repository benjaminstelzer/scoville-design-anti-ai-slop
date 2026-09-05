# Stage-two Skill comparison: Typography and writing systems

Date: 2026-09-02
Capture: 2026-09-02T13:09:43Z
Target: `references/typography-and-writing-systems.md` and its expert-depth audit
Method: `reference-audit-method.md`, Stage two

Local successor baselines: [typography and typesetting](../../../../scoville-design-anti-ai-slop/references/typography-and-typesetting.md) and [font technology and script safety](../../../../scoville-design-anti-ai-slop/references/font-technology-and-script-safety.md)
and [expert-depth audit](../reference-audits/typography-and-writing-systems.md)

This is a current, bounded GitHub and public-Skill comparison. It ranks
repositories by captured GitHub stars only after an exact typography Skill or
directly usable typography instruction and an E1 or higher evidence artifact
were found. Repository popularity, exact-Skill adoption, evidence strength and
visible quality are separate. Public search used GitHub repository and contents
APIs, GitHub and web search, and skills.sh. Authenticated GitHub code search was
rate-limited during the search window, so the result is not globally
exhaustive. Private, renamed, newly published, non-English and service-hosted
Skills may be absent.

## Decision

The three qualifying repositories are `pbakaus/impeccable`,
`jakubkrehel/skills`, and `wondelai/skills`. Impeccable provides the strongest
proof topology and the only reproducible typography checks in the ranked set.
The other two provide inspectable worked CSS and decision examples, but no
rendered output, visual regression, typography evaluation or independent
review. None visibly proves professional typesetting, family pairing quality,
multiscript correctness, print quality or superiority to the current Scoville
reference.

Adopt only mechanisms through original synthesis. The best candidates support
separating visual assessment from mechanical inspection, assigning roles
before faces, testing real text and fallbacks, using high-level font controls,
and reporting unverified checks. The current Scoville audit remains materially
stronger on source bounds, family-count reasoning, character differentiation,
kerning versus tracking versus word spacing, paragraph and page rhythm,
justification and hyphenation, locale punctuation, OpenType and numerals,
fallback metric drift, multiscript shaping, bidi, vertical text, font rights,
and screen versus print proof.

## Qualification and star ranking

Evidence levels follow the audit method. E1 means an inspectable example or
output artifact. E2 means a reproducible test, evaluation or deterministic
check. E3 requires independent evaluation or external adoption evidence that
supports capability. Registry installs and stars remain popularity signals and
do not promote a candidate to E3.

| Rank | Repository and exact path | Stars at capture | Pin, activity and latest relevant update | Exact license and asset status | Evidence level and what it proves |
| --- | --- | ---: | --- | --- | --- |
| 1 | [`pbakaus/impeccable`, `.agents/skills/impeccable/SKILL.md`, `typeset` reference](https://github.com/pbakaus/impeccable/blob/c0f495212236129c2e92aaf7714a3a9914569d13/.agents/skills/impeccable/reference/typeset.md) | 64,867 | Active, not archived. Repository pin `c0f495212236129c2e92aaf7714a3a9914569d13`. Canonical `skill/reference/typeset.md` last changed in `2b1f36c43e51bb7ce12972b0fa7b25527457b773` on 2026-07-18. Repository pushed 2026-09-02. | Root [Apache-2.0](https://github.com/pbakaus/impeccable/blob/c0f495212236129c2e92aaf7714a3a9914569d13/LICENSE). No separate notice was found for the generated 1.1 MB Google Fonts fingerprint index. The demo loads Fraunces and Inter from Google Fonts, whose individual font licenses remain separate. | **E2.** Inspectable demo HTML, static and browser detector fixtures, design-system font tests, and a reproducible `font-match.mjs` measurement and proof-sheet workflow exist. They prove package and detector behavior for named fixtures and that measured font matching can be run. They do not prove pairing quality, long-form typesetting, multiscript correctness, print quality or independent visual superiority. The tests were inspected, not executed in this audit. |
| 2 | [`jakubkrehel/skills`, `skills/better-typography/SKILL.md`](https://github.com/jakubkrehel/skills/blob/267330e1adfc66a718fb65fa6918c1f06d0a689e/skills/better-typography/SKILL.md) | 4,754 | Active, not archived. Pin and latest relevant update `267330e1adfc66a718fb65fa6918c1f06d0a689e` on 2026-08-29. | Root [MIT](https://github.com/jakubkrehel/skills/blob/267330e1adfc66a718fb65fa6918c1f06d0a689e/LICENSE). No bundled font, data or visual asset exists in the exact Skill directory. Named commercial and external fonts retain their own licenses. | **E1.** Five progressive-reference files contain inspectable CSS, HTML, incorrect/correct and review-output examples. They prove that the instructions are concrete and implementable as examples. No rendered example, test, evaluation or independent reviewer result was found, so visual type quality and rule correctness remain unproved. |
| 3 | [`wondelai/skills`, `web-typography/SKILL.md`](https://github.com/wondelai/skills/blob/eade5d170b3a593c5b6ebcaca898102134aee108/web-typography/SKILL.md) | 2,079 | Active, not archived. Repository pin `eade5d170b3a593c5b6ebcaca898102134aee108`. Exact Skill last changed in `0dea03f507c913801c94516e352e6859116a02d5` on 2026-06-30. Repository pushed 2026-08-29. | Root and Skill frontmatter say [MIT](https://github.com/wondelai/skills/blob/eade5d170b3a593c5b6ebcaca898102134aee108/LICENSE). No separate bundled data or asset license was found. Font recommendations and external resources are not relicensed by the repository. | **E1.** The Skill and five reference files provide inspectable CSS, comparison tables, pairing examples and implementation patterns. They prove written coverage and example completeness only. No rendered page, visual comparison, test, evaluation or independent evidence was found. |

## Candidate 1: Impeccable `typeset`

### Claimed scope and observed mechanism

The exact `typeset` command is a directly routed typography instruction inside
a broader frontend Skill. It reads incumbent product and design context, then
runs two deliberately separated passes. The first pass inspects typographic
authority, role hierarchy, scale, reading conditions, stress states and
delivery. The second runs a mechanical detector. It then states the required
roles, contrast, measure, density, authoritative faces and constraints before
editing. Verification must cite rendered or source evidence.

The supporting `font-match.mjs` is more specific than ordinary font-name
recommendation. It measures cap height, width, apparent weight, tracking,
serif/density and shape features from a reference crop, ranks Google Fonts
candidates, renders them with the region's actual text, and can emit a visual
proof sheet. That mechanism is about matching one reference region. It is not
a family-pairing method and its distance score is not a readability or quality
score.

### What is better than the current Scoville reference

- Manual visual assessment is isolated from detector output before synthesis.
  This reduces anchoring and makes mechanical findings an evidence lane rather
  than the critique itself.
- “Use the fewest roles and families that make hierarchy unmistakable” is a
  better family-count posture than the fixed maxima in the other candidates.
- The command asks whether every family is necessary, which can become the
  audit's remove-one-family test.
- The measurement and proof-sheet path turns width, weight and cap-height fit
  into an inspectable comparison using actual text.
- Findings must name a file, selector or computed value and unverified checks
  remain explicit.

The current Scoville reference already owns the reading job, roles before
faces, actual language/content, fallbacks and target rendering. The useful gain
is therefore the two-lane inspection protocol and measured candidate proof,
not the surrounding frontend doctrine.

### Adoption-priority result

The inspectable landing demo uses Fraunces for display and Inter for body. Its
source shows hierarchy, optical sizing and role-specific sizes, but the exact
file has no media or container query and retains a fixed three-column grid.
It is one web marketing artifact with live Google Fonts, not responsive or
print proof. The detector tests establish fixture recognition and design-token
normalization. They do not show visibly better kerning, paragraph rhythm, rag,
hyphenation, page breaks or fallback behavior than Scoville.

### Reject or re-verify

- Do not adopt the 45 to 75 character range, 16 px floor, dark-surface
  compensation, paragraph-boundary rule or live-mode scale range as universal
  design laws.
- Do not adopt `overused-font` bans. The tests flag named popular fonts, which
  measures trend policy rather than task-specific suitability.
- Do not treat the font fingerprint distance, hand-tuned density weights or
  Google Fonts catalog as family compatibility, legibility or quality proof.
- Do not vendor the Google Fonts-derived index until its data provenance,
  refresh policy and reuse terms are explicitly cleared. Individual fonts
  still require their own license receipts.
- The exact command has no professional print, page-fragmentation, vertical,
  complex-script or native-reader workflow.

## Candidate 2: `better-typography`

### Claimed scope and observed mechanism

The Skill owns web text rendering, wrapping, mixed-direction details,
variable fonts, OpenType, scales and type review. It uses progressive
references for font choice, spacing/sizing, wrapping/punctuation, variable
features and access details. It prefers high-level CSS controls over raw
OpenType tags, preserves incumbent styling ownership, asks for rendered review,
and reports severity plus `Not verified` checks.

### What is better than the current Scoville reference

- The high-level property before raw tag rule is a compact and useful repair
  mechanism. It preserves fallback behavior where supported.
- Kerning and uniform letter spacing are explicitly distinguished.
- Heading-level collisions, wrapping, truncation and mixed-direction isolation
  have concrete source-level examples.
- Content-driven testing covers viewport resize, 200 percent zoom and RTL
  mirroring rather than code inspection alone.
- The finding table ties location, before, after and reader effect to one root
  cause.

### Adoption-priority result

The references include worked CSS and HTML, but no rendered output. They cannot
show that the proposed hierarchy, measure, leading, spacing or family choices
look good in any actual language or medium. The pairing logic mainly says
contrast rather than near-similarity and offers serif plus sans as the central
example. It does not compare cap height, x-height, width, stroke, terminals,
counters, texture, language repertoire, optical sizes or shared-line metrics
as one family decision.

### Reject or re-verify

- “Rarely more than three fonts,” thin-weight size thresholds, fixed leading,
  measure ranges and size floors remain contextual starting points, not gates.
- The category table repeats the unsupported claim that serifs guide the eye
  and overgeneralizes screen roles by category.
- Root font smoothing, universal `balance` or `pretty` wrapping, and the mobile
  input transform workaround require browser, access and interaction evidence.
- Web-only implementation does not cover font embedding for app, ebook or
  print, PDF preflight, native-reader review, complex shaping or vertical text.

## Candidate 3: `web-typography`

### Claimed scope and observed mechanism

The Skill presents a complete web workflow from reading context through face
evaluation, choice, pairing, scale, hierarchy, responsive sizing and font
loading. It is the most explicit ranked candidate about x-height, apertures,
confusable Latin characters, same-designer pairs, superfamilies, true styles,
glyph coverage and web licenses. Its supporting references contain structured
comparisons and CSS examples.

### What is better than the current Scoville reference

- Typeface screening puts technical, structural and practical checks before
  commitment.
- Pairing examples name same-designer and superfamily relationships rather
  than only serif versus sans.
- Real content, target screens, file size and license appear in the same
  decision flow.
- The Skill distinguishes “type for a moment” from sustained reading, which
  can inform role-specific test conditions.

### Adoption-priority result

No visible artifact or test supports the claims. The examples are code and
tables only. The Skill provides more nouns and fixed examples than a causal
repair system. It does not diagnose kerning versus tracking versus word space,
page fragmentation, fallback metric drift, bidi interaction, vertical flow or
print/PDF behavior at the depth required by the Scoville audit.

### Reject or re-verify

- Reject the ten-point score. Passing ten heterogeneous checks cannot measure
  typography quality.
- Reject one-to-two-family maximums, 66-character optimum, fixed ratio bands,
  200 KB payload gate and category-labelled “proven pairings” as universal.
- Claims about saccade length, word-shape reading, screen x-height, fixed mobile
  distances and feature effects need primary, population-specific evidence.
- A named font's external availability does not establish its current license,
  glyph support, embedding right, metric compatibility or rendering quality.

## Mandatory typography decision questions

### Typeface combination

| Required question | Best candidate evidence | Comparison with current Scoville | Decision |
| --- | --- | --- | --- |
| Roles before families | Impeccable states required roles and tests whether each family is necessary. Wondelai distinguishes momentary and sustained reading roles. | Already a current strength. The audit adds display, body, annotation, navigation, data, code, caption, action and fallback. | Retain Scoville ownership. Adapt Impeccable's necessity question and evidence fields. |
| Formal compatibility | Impeccable can measure cap height, width, weight, tracking, serif/density and rendered shape. Wondelai names x-height, counters and apertures. | No candidate covers x-height, cap height, width, proportion, stroke contrast, terminals, counters, apertures, stress, rhythm, texture and typographic colour together. | Use the audit's complete comparison specimen. Treat measurements as observations, not a similarity score. |
| Useful contrast versus accidental near-similarity | All three prefer clear contrast. Jakub and Wondelai use serif plus sans as the dominant example. | The audit correctly permits compatibility or deliberate contrast and rejects category-only pairing. | Keep contrast as one mechanism. Add a near-similarity and competing-voice check. Do not make serif plus sans the model. |
| Historical, cultural and tonal coherence | Wondelai names era and mood. The other candidates focus product voice. | None provides sourced history or cultural authority. | Keep as a contextual, source-bounded judgment. Deliberate tension is allowed when the role and compensation are stated. |
| Styles, axes, features and repertoire | Impeccable and Jakub inspect weights, variable settings, numerals and fallback delivery. Wondelai checks styles and Latin coverage. | The audit is stronger on italics, small caps, numerals, punctuation, language/script repertoire, shaping and optical-size behavior. | Retain the audit's actual-file and actual-language tests. |
| Metric compatibility | Impeccable is strongest because it measures rendered cap height, width and apparent weight. | The audit additionally requires advance widths, ascent, descent, line gap and fallback-chain drift. | Adapt rendered comparison and proof sheets. Do not use one fingerprint distance as approval. |
| Rendering, license, embedding and performance | All three mention web loading. Impeccable has executable font inspection. | The audit covers exact file/version/license, app/ebook/print rights, browser states and PDF/provider proof. | Keep Scoville's font receipt and proof lanes. Candidate guidance remains web-only unless verified. |
| Hierarchy without colour or decoration | Impeccable explicitly asks whether roles remain distinguishable. | Current leaf already uses several coordinated signals but does not state a colour-stripped test. | Add the colour/decoration removal test as an original, compact discriminator. |
| Real text at final size and medium | Every candidate asks for real content. Only Impeccable has an inspectable demo source and proof-sheet mechanism. | Current audit requires actual languages, critical strings, target size/distance/renderer and screen/print proof. | Keep the stronger audit contract. No candidate has visible cross-medium evidence. |

### Scoped family-count decision

The comparison does not support a universal count. The source and exception
basis is documented in the local expert-depth audit. Use this decision rule:

1. Start with one family or superfamily when it supplies every required role,
   weight, width, optical size, style, numeral form and language/script need.
2. Add a second family only when it supplies a distinct, legible function,
   voice, contrast, density, repertoire or production need that the first
   cannot supply cleanly.
3. Add a third or later family only for a separately legible role whose value
   exceeds added hierarchy, license, loading, rendering, fallback and
   governance cost.
4. Count families separately from weights, styles, widths, variable axes,
   symbol fonts, code roles and technical fallbacks.
5. Remove each non-primary family in turn. If meaning, hierarchy and character
   remain, the extra family is likely decorative redundancy.
6. Reject pairs whose difference looks accidental and sets whose voices compete
   without a declared hierarchy. Test all survivors on real content at final
   size, medium and fallback state.

One or two families are common web/product conventions in the inspected
Skills, not a professional maximum. Editorial systems, posters, historical
quotation, multilingual work, data/code interfaces and experimental display
work may justify other counts when each role remains coherent and proven.

### Typesetting coverage

| Topic | Ranked-candidate coverage | Required Scoville action |
| --- | --- | --- |
| Character differentiation | Wondelai names `Il1`, `O0` and `rn/m`. Impeccable can inspect rendered type. | Retain task-specific critical-string and fallback specimens. Separate ordinary reading from identifiers and security confusables. |
| Kerning, tracking and word spacing | Jakub distinguishes kerning and tracking. None supplies full word-space diagnosis across scripts. | Keep three separate causes, inspect real pairs and word boundaries, and avoid Latin tracking transfer. |
| Contextual measure and return sweep | All use fixed web ranges. | Keep language, type width, size, leading, task, distance, scrolling/paging and column context. Compare plausible settings instead of hard-passing `ch`. |
| Leading and paragraph rhythm | Impeccable links line height to face, width, language and contrast. | Extend to marks, glyph extents, baselines, paragraphs, columns/pages and spacing overrides. |
| Alignment, justification and hyphenation | Candidates mostly discourage interface justification. | Preserve language, dictionary, engine and medium distinctions. Inspect rag, rivers, expansion and consecutive hyphens. |
| Punctuation and microtype | Jakub has the strongest web examples. | Retain locale/house-style authority, semantic characters and renderer-specific optical behavior. |
| Numerals, OpenType and optical size | Impeccable and Jakub prefer high-level controls and role-specific numerals. | Retain actual-file feature checks, fallback behavior, data stability and no silent synthesis. |
| Widows, orphans and page/column breaks | Candidates discuss browser wrapping and last-line words only. | Keep fragmentation ownership, paragraph keep controls, reflow and print/PDF checks. Avoid manual breaks as default repair. |
| Fallback metric drift | Impeccable has stress and measured matching. | Keep explicit primary/fallback metrics, before/after load geometry and measured overrides. |
| Multiscript, bidi and vertical | Jakub gives basic `lang`, `dir` and `<bdi>`. Others mainly discuss glyph coverage. | Retain shaping, logical order, isolation, interaction, vertical orientation, native-reader and font-engineer escalation. |
| Access, render and print proof | All are web-centric. Impeccable and Jakub mention zoom and loading. | Keep exact WCAG scope, browser/OS states, font loads, PDF embedding/preflight, intended-size print and provider proof. |

## Mechanisms to synthesize and claims to withhold

### Adopt or test through original Scoville wording

1. Separate an unanchored visual assessment from a mechanical font/source
   inspection, then synthesize disagreements.
2. Add the family-necessity and remove-one-family tests to the audit's
   role-first decision rule.
3. Compare shortlisted faces and fallbacks with the actual strings at final
   size. Record cap height, x-height, width, apparent weight, texture and metric
   drift. Use proof sheets as evidence, never an automatic score.
4. Prefer supported high-level properties over raw feature tags, then verify
   the actual font, fallback and renderer.
5. Require location, observed effect, root owner, smallest repair, preserved
   strength and unverified regression states.

### Reject from the executable package

- fixed family maxima, serif/sans defaults and fashionable pairing lists
- universal size, measure, leading, tracking, weight, payload or scale numbers
- trend bans and named-font taste rules
- similarity, diagnostic or checklist totals presented as typography quality
- web-font availability presented as license or deployment clearance
- Latin examples presented as multiscript, bidi, vertical or native-reader proof
- one web demo or source fixture presented as print, responsive or professional
  typesetting evidence

## Search exclusions and limits

- `anthropics/skills` had 173,161 repository stars, but
  `skills/frontend-design` is broad frontend guidance and its exact directory
  contained no inspectable typography output, example or test artifact. It is
  E0 for this comparison and does not qualify despite popularity.
- `Owl-Listener/designer-skills` had 2,469 stars and exact critique/type-scale
  prose, but no exact-path example, output or evaluation was found. Its fixed
  ratios and minimums are E0 instructions, not evidence.
- `mblode/agent-skills` had 99 stars and a detailed 78-rule
  `typography-audit`. Its rule files contain useful incorrect/correct examples,
  but the exact Skill had no typography evaluation or rendered proof. It did
  not outrank the qualifying three.
- skills.sh listed the ranked standalone Skills and current install counts.
  Those counts demonstrate discoverability or installation, not output use,
  rule correctness or visual quality.
- No candidate supplied independent typography review, native-reader evidence,
  a browser/OS matrix, PDF/print proof, or several visible subjects and media.
  The cheapest decision-changing next test is the audit's open Latin editorial
  generation, typography critique and mixed-script/fallback repair set, run
  symmetrically with real fonts, content, renders and blinded human review.
