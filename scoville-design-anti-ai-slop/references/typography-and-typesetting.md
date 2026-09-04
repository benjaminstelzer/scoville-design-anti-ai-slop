# Typography and typesetting

Status: `draft`  
Intervention: `external-verification`  
Sources: `SRC-TYPE-CANON`, `SRC-TYPE-SELECTION`, `SRC-TYPE-DETAIL`, `SRC-TYPE-EMPIRICAL`, `SRC-FONT-TECH`, `SRC-PACKAGE-LOCAL-SYNTHESIS`

## Load when

Load when type roles, face selection or combination, Latin glyph
differentiation, hierarchy, measure, leading, paragraph rhythm, alignment,
justification, hyphenation, punctuation, numerals, microtypography, breaks, or
an expressive type exception materially affects the design. Do not load for a
font-file, coverage, shaping, fallback-metric, bidi, vertical, embedding, or
licence problem alone; that is font-technology ownership. Non-Latin work gets
only the stop/escalation floor here, not simulated native typesetting advice.

## Inputs and formal variables

Work from real text and actual fonts. Record only open relevant fields; otherwise use the Core minimal record:

- `R`: semantic roles and reading priority—display, heading levels, body,
  navigation, action, caption, annotation, data, code/identifier, and fallback;
- `T`: exact strings, language/locale, case, numerals, punctuation, critical
  confusables, longest/shortest values, and translation variants;
- `V`: target size, distance, medium, column/viewport, scrolling or paging,
  lighting, resolution, and intended renderer;
- `F`: candidate family files, styles, weights, widths, optical sizes, axes,
  features, repertoire, metrics, fallback, licence, and delivery constraints;
- `P`: protected content, hierarchy, brand voice, layout relations, access
  floors, and intentional character;
- `E`: source, font inspection, render, print, native-reader, and human-review
  evidence, with untested states named.

Separate legibility (character recognition), readability (sustained use),
hierarchy, voice, and technical coverage. A face may succeed at one and fail at
another.

## Generate and decide

1. **Assign roles before faces.** Map content relationships and required
   distinctions. Use the fewest coordinated signals—size, weight, width, style,
   spacing, case, placement, or colour—that make adjacent and recurring roles
   clear. Do not vary every signal at once. Test hierarchy without decorative
   colour or containers when useful.
2. **Screen each face by job and evidence.** Inspect actual text for character
   differentiation, counters/apertures, x-height and cap height, width and
   proportion, stroke contrast/stress, terminals, texture/typographic colour,
   true italic/bold distinction, required numerals/punctuation, available
   styles/features, and target rendering. For codes, prices, dates, URLs, IDs,
   or safety-critical strings, build a target-size specimen of likely
   confusables such as `I/l/1` and `O/0`; ordinary word reading and identifier
   recognition are different tasks.
   Where a subject has its own typographic environment, inspect its documents,
   labels, signage, packaging, code, data, era or script. Compare the candidate
   with the platform default: does hierarchy, voice or recognition change?
   No change can be correct for utility; retain it instead of decorating it.
3. **Treat family count as an outcome.** Start with one family or superfamily
   when it covers the roles. Add another only for a named gain in function,
   voice, contrast, density, repertoire, fallback, or production. Compare
   families by proportions, x/cap height, stroke and terminal character,
   texture, metrics, and deliberate contrast—not merely serif versus sans.
   Reject accidental near-similarity or competing voices. Remove each extra
   family in turn; if hierarchy and character survive, it is probably redundant.
4. **Set text as a coupled system.** Tune size, measure, leading, paragraph
   spacing/indent, alignment, columns, and line/paragraph breaking together on
   actual copy. Measure depends on face width, language, task, distance,
   scrolling/paging, column context, and leading. Compare plausible settings;
   do not pass a remembered character count or ratio automatically.
5. **Separate spacing causes.** Kerning is pair positioning; tracking changes a
   run; word spacing marks boundaries. Begin with the font's positioning, then
   inspect representative pairs, caps, small text, numerals, punctuation,
   marks, and word boundaries. Do not use tracking to rescue an unsuitable face
   or apply Latin all-cap logic to another writing system.
6. **Set paragraphs and details deliberately.** Choose leading-edge, centred,
   or justified setting by reading job, language, measure, engine, and medium.
   For justification, inspect rag/control, word and character expansion,
   dictionary/language, consecutive hyphens, rivers, and last lines. Apply the
   applicable locale or house style to quotes, apostrophes, dashes, ellipses,
   spaces, decimal/grouping signs, brackets, emphasis, and optical punctuation.
7. **Use numerals and font features by role.** Choose proportional/tabular,
   lining/oldstyle, fractions, small caps, distinct zero, and optical size only
   when the actual font supports them and the role benefits. Prefer supported
   high-level controls; never assume a feature tag, axis, or synthesised style
   works because its name is known.
8. **Compose breaks as a system.** Inspect widows, orphans, headings stranded
   from content, short final lines, column/page breaks, and reflow. Repair text
   fit, paragraph style, keep settings, measure, or geometry before inserting
   manual breaks or nonbreaking spaces.

When font substitution can affect the delivered artifact or a requested
editable derivative, declare a controlled fallback and inspect a substitution
render. A fixed raster-only deliverable has no runtime font fallback; do not
invent that check. Escalate when metrics, features, loading, embedding, shaping,
or unfamiliar scripts become material.

## Critique: signatures and causes

| Failure signature | Likely cause to distinguish |
| --- | --- |
| Adjacent levels collide or one role has many arbitrary variants | semantic role map or shared type style is wrong, not one heading |
| Pair looks accidental or families compete | insufficient structural/voice contrast, mismatched metrics, or no distinct job |
| `I/l/1`, `O/0`, punctuation, or numerals are ambiguous | face/weight/size/fallback fails the actual recognition task |
| Uneven pairs, uniformly loose/tight runs, or blurred word boundaries | kerning, tracking, and word spacing have been conflated |
| Cramped or disconnected lines; weak paragraph rhythm | leading is mismatched to glyph extents, measure, marks, line count, or paragraph treatment |
| Rag is distracting; rivers or colour bands appear | measure, justification, hyphenation language/engine, or word-space expansion is wrong |
| Punctuation or numerals feel inconsistent or change meaning | locale/house style, glyph feature, or role-specific numeral choice is wrong |
| A widow/orphan returns after resize, translation, or font load | manual patch hides a paragraph-style, geometry, language-break, or substitution cause |
| Fallback changes wrapping, density, control size, or page count | primary/fallback metrics differ; route the technical repair rather than nudging layout |
| Tight-tracked geometric display sans with gradient fill on every heading | template scale displaced a role map; display treatment spread to ordinary reading roles |
| Eyebrow, display size or weight jump with no role change | hierarchy signal applied by habit rather than a real distinction |

Keep a repeated treatment when it consistently marks a real role. Otherwise
repair the role map and remove only redundant signals, preserving useful defaults.

Localise the observation, likely reading effect, severity, confidence, parent
owner, smallest repair, preserved strength, and regression target. Do not turn a
reviewer's stylistic preference into a defect.

## Smallest repair and preservation

Freeze `P`. Repair in causal order: wrong content/role -> unsuitable face or
combination -> shared hierarchy style -> measure/leading/paragraph system ->
alignment/hyphenation/justification -> feature/numeral/punctuation -> break
control -> local optical adjustment. Apply the change at the shared owner and
rerender all consumers. Preserve exact copy, successful voice, clear hierarchy,
layout intent, valid eccentric display work, and data alignment. Revert a repair
that improves one specimen but harms body reading, fallback, translation,
responsive fit, pagination, or production.

## Rules and exceptions

There is no universal family count, serif/sans pairing, body size, measure,
leading, modular scale, tracking value, or alignment. Numerical guidance is a
supplied constraint, a standard in exact scope, a measured observation, or a
provisional comparison value—not an unexplained quality gate. Category labels,
font popularity, similarity scores, and specimen charts do not prove fit.

Expressive distortion, extreme tightness/spacing, unusual measure, deliberate
widow, low contrast, or unconventional pairing may serve a bounded display
role. State purpose, protected reading/access floor, compensating structure,
accepted cost, and falsifier. Do not let display freedom silently govern body,
data, navigation, identifiers, or unfamiliar scripts.

## Proof, ownership, and claim ceiling

Render real `T` at intended `V`: whole hierarchy, paragraph/page context,
critical strings and applicable narrow/wide, column or substitution states. Compare
candidates or before/after with non-intervention variables held constant,
including content, size, width, renderer, colour and assets where unchanged.
Declare the intended variables and their dependent effects, such as changed
line breaks after a size repair. Inspect detail plus whole-page/sequence context.
For print, inspect target-size output and request the relevant font/preflight/
provider evidence; for web, test actual loading and applicable resize, reflow,
and text-spacing states through their owners. Mark every unrun lane unverified.

Typography owns type roles, selection/combination, hierarchy, typesetting, and
Latin microtype. Composition owns macro spatial relations; fixed media owns
page/sequence context; font technology owns files, metrics, shaping, fallback,
scripts, deployment, and font proof; UI owns framework implementation; production
owns export and supplier acceptance. Do not infer universal
readability, accessibility, native quality, licence clearance, print approval,
audience preference, or an objectively best typeface or pairing.
