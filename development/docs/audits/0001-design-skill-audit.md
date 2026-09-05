# Audit: Scoville Design Anti-AI-Slop

Status: Research complete, implementation not started  
Date: 2026-09-01  
Target: `scoville-design-anti-ai-slop`  
Audience: Maintainers of the Scoville Skill family

## Direct answer

A separate Scoville Design Skill is justified. The current market has useful
design Skills, but none of the reviewed candidates combines all of the required
properties:

- cross-media graphic-design knowledge rather than frontend styling alone;
- both greenfield creation and evidence-based critique;
- typography, composition, colour, imagery, visual hierarchy, UI design, and
  design-system definition in one coherent judgment model;
- explicit distinction between enforceable constraints, evidence-backed
  defaults, craft heuristics, and conventions that may be broken;
- a disciplined exception mechanism that can preserve a successful rule break;
- optional composition with a framework-focused UI implementation Skill;
- visual validation that does not confuse source inspection with seeing the
  artifact.

The recommended product is not a larger checklist or a design-history
encyclopedia. It is an application-first design director with a compact Studio
Loop, SOL-tested routed interventions, two operating modes, and an explicit
judgment loop:

1. **Generate mode** defines intent, system, composition, and artifact direction
   and produces the requested artifact through the applicable format owner.
2. **Critique mode** observes, interprets, evaluates, and prioritizes without
   silently redesigning.
3. **Repair mode** makes targeted changes, rerenders, checks protected
   dimensions, and stops after at most two bounded passes.
4. **Style-direction mode** turns a named or inferred language into controllable
   design decisions without replacing the brief with a preset.

The exception protocol is a cross-mode gate, not a separate mode. It allows a
rule to be broken when the break has a named purpose, preserves required
communication and accessibility, gains more than it costs, and survives
inspection in the intended medium.

## Scope and method

This audit compares the current local `scoville-ui-anti-ai-slop` contract with
public Agent Skills and source material available on 2026-09-01. It focuses on
portable Agent Skills, not on a specific drawing application. The target Skill
should direct tools such as image generation, HTML/CSS, presentation, document,
and PDF tooling. It should not reimplement those tools.

Source priority was:

1. current Skill repositories and the [Agent Skills specification](https://agentskills.io/specification);
2. openly licensed books and original project/license pages;
3. standards and public design-system guidance;
4. peer-reviewed or open-access research;
5. secondary commentary only for discovery or a clearly labelled limitation.

## 1. Audit of the current Scoville UI boundary

### What the current Skill does well

The local UI Skill is strong where a design language already exists:

- `SKILL.md:3-7` makes the product design system and platform language the
  owner.
- `framework-alignment.md` distinguishes styled systems, headless libraries,
  utility frameworks, platform stacks, and deliberate local conventions.
- `validation.md` correctly separates source/build evidence from rendered,
  interaction, responsive, and accessibility evidence.
- It refuses generic fonts, colours, radii, shadows, card patterns, and pixel
  values when they would create a parallel visual language.

Those properties should remain in Scoville UI. They are implementation and
conformance strengths, not reasons to keep design ownership there.

### Responsibilities that should move to Scoville Design

The current UI Skill also owns decisions that the clarified family model now
places in Design:

| Current UI concern | Evidence | Recommended owner |
| --- | --- | --- |
| Greenfield visual direction | `SKILL.md:33-34`; `framework-alignment.md:100-122` | Design when active and applicable; UI fallback otherwise |
| Information hierarchy and arrangement | `SKILL.md:3, 6, 77`; `ui-quality.md:36-49` | Design decides; UI preserves and implements |
| General visual quality and readability | `SKILL.md:77`; `ui-quality.md:53-63` | Design judges; UI verifies implementation constraints |
| Workflow-oriented arrangement | `ui-quality.md:15-31` | Design owns the UI-design decision; UI owns interaction correctness in the framework |
| Typography and spacing judgment | `ui-quality.md:53-63` | Design owns optical and systemic judgment; UI maps to tokens/components |

### Required new boundary

The family should use **optional concern ownership**, not hard dependencies:

| Active and applicable Skills | Design decision owner | Implementation owner |
| --- | --- | --- |
| Design only | Design | Base agent and artifact tool, with evidence limits |
| UI only | UI's existing bounded Greenfield fallback or incumbent design system | UI |
| Design + UI | Design | UI |
| Existing design system, Design + UI | Existing system constrains both; Design may improve structure and workflow without gratuitous restyling | UI |
| Neither | Base agent | Base agent |

Installation alone does not transfer ownership. A Skill must be available,
active, and applicable to the concrete concern. Neither Skill may require,
install, simulate, copy, or reverify the other.

**Resulting definitions:**

- **Scoville Design** owns design-system definition, art direction, visual
  concept, information hierarchy, UI design and workflow arrangement,
  composition, typography, colour, spacing, imagery, and design critique.
- **Scoville UI** owns strict implementation through the selected framework,
  product design system, component APIs, tokens, platform conventions,
  responsive behavior, interaction states, accessibility mechanics, and
  rendered proof.
- If Design is unavailable or inapplicable, UI retains its present Greenfield
  capability as a standalone fallback. That fallback is surface-local and does
  not become a mature product-wide system by assertion.

This is a sharper boundary than the current Skill, but it preserves standalone
operation.

## 2. Existing design Skills

The list is representative rather than a claim that every public `SKILL.md` was
enumerated. It covers the strongest distinct mechanisms found in the first and
targeted research waves.

| Skill or collection | Mechanism and strengths | Material weaknesses for this target | License |
| --- | --- | --- | --- |
| [Anthropic `frontend-design`](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) | Grounds a direction in subject, audience, and task; asks for an intentional aesthetic risk; uses a design plan, token sketch, signature, and critique before code. The current version is less dogmatic than its earlier font-ban form. | Frontend-only; mixes design direction, copy, and CSS implementation; requires fixed palette/type-role shapes; does not provide a general graphic-design knowledge base, licensing ledger, or rigorous audit evidence model. | Apache-2.0 in the bundled [license](https://github.com/anthropics/skills/blob/main/skills/frontend-design/LICENSE.txt) |
| [Anthropic `canvas-design`](https://github.com/anthropics/skills/blob/main/skills/canvas-design/SKILL.md) | Directly targets posters, art, and static pieces; separates a visual philosophy from canvas execution; explicitly protects originality. | Treats a philosophy manifesto as the main design engine; prescribes a roughly 90/10 visual-to-text ratio and museum-level rhetoric; weak on typography as communication, design systems, UI, critique, and evidence; encourages aesthetic confidence without a source-grounded knowledge model. | Apache-2.0 in the bundled [license](https://github.com/anthropics/skills/blob/main/skills/canvas-design/LICENSE.txt) |
| [Impeccable](https://github.com/pbakaus/impeccable) | Most complete reviewed UI craft system: design context, typography, colour, spatial design, motion, critique, audit, browser iteration, and deterministic anti-pattern detection. It separates `PRODUCT.md` from `DESIGN.md` and offers focused commands such as typeset, layout, critique, and polish. | Still explicitly frontend/UI; complex runtime, commands, hooks, and generated state; several hard anti-patterns are taste claims rather than universal principles; deterministic scans can detect smells but cannot prove beauty or contextual fit. | Apache-2.0 |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Large searchable data corpus for styles, palettes, typography, UX, icons, charts, and framework-specific implementation; can persist a design system; license-aware font catalog. | Retrieval can substitute catalogue matches for original judgment; many numeric rules are presented more universally than the evidence supports; Python/CLI/data complexity; primarily UI and implementation rather than general graphic design. | MIT |
| [Taste Skill](https://github.com/Leonxlnx/taste-skill), pinned research snapshot [`ccbc156`](https://github.com/Leonxlnx/taste-skill/tree/ccbc15639c97057cbfcf32ecebc38ef716e4bb37) | One of the strongest direct anti-slop frontend competitors found: brief inference before styling, adjustable variance/motion/density, honest mapping to established design systems, audit-first redesign, a mechanical preflight, and separate image-generation, image-to-code, redesign, and style-specific Skills. The image-first sequence also makes render, inspection, extraction, and implementation fidelity explicit. | The default v2 is explicitly experimental and its 1,066-line main Skill is monolithic. It is scoped to landing pages, portfolios, and redesigns and explicitly excludes dashboards, data tables, multi-step product UI, and native mobile. Many fixed presets, font/palette bans, page-pattern quotas, motion defaults, and exact numeric limits are contextual taste hypotheses presented as hard gates; the GPT variant is more rigid still. The repository contains examples but no independent benchmark, validation suite, or sealed holdout, and its published research currently covers LLM output laziness rather than graphic-design or typography foundations. It combines art direction, UI, code, content, framework, and asset rules, so its ownership and context-cost model do not fit the proposed standalone general-design architecture. | MIT at the pinned snapshot |
| [Vercel Web Design Guidelines Skill](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md) | Compact review router to a maintained set of web-interface rules; strong for source-level UI audits, accessibility details, controls, forms, copy, and implementation hygiene. | Audit-only, web-only, and dependent on fetching mutable rules at runtime; not a greenfield design system; no art direction or general composition; source findings are not rendered visual proof. | MIT via the [guidelines repository](https://github.com/vercel-labs/web-interface-guidelines) |
| [Design Atelier](https://github.com/shaunandrews/agent-skills/blob/c6da55f4430422f2d46620f36e88c371727d72d7/skills/design-atelier/SKILL.md) | End-to-end brief, reference research, mood board, design-system document, parallel mockups, and gallery workflow. It correctly makes shared direction precede page variants. | Heavy infrastructure and agent orchestration; web prototypes only; rigid defaults such as white backgrounds, Google Fonts, CSS-only/no-image mockups; workflow strength exceeds its underlying design theory and critique evidence. | MIT via the [repository](https://github.com/shaunandrews/agent-skills); historical file pinned because current head removed it |
| [TypeUI Awesome Design Skills](https://github.com/rikre/design-skills) | Many ready-made visual systems with `SKILL.md` plus `DESIGN.md`; useful as style examples and for seeing how token sets, component rules, and quality gates can be packaged. | A style catalogue encourages choosing a look before understanding message, audience, and medium; many named styles are recipes; mainly UI components; volume does not equal validated design knowledge. | MIT |
| [Design Rules Companion](https://github.com/Kotelberg/design-rules-companion-skill/blob/main/SKILL.md) | Routes design questions into focused category references and acknowledges exceptions. | Relies heavily on secondary-source rules and numeric heuristics; useful packaging inspiration, not a sufficient evidence base. | Recheck repository license before reuse |
| [Refero Skill](https://github.com/referodesign/refero_skill/blob/master/skills/refero-design/SKILL.md) | Grounds UI design in reference research instead of pure model taste. | External-service and UI focus; reference retrieval does not itself supply critique, licensing, or general design competence. | Recheck repository license before reuse |
| Public brand, editorial, packaging, poster, and critic Skills listed in the [source ledger](../research/source-ledger.md) | Expose specialist deliverables and production concerns that general UI Skills miss. | Most are narrow recipes, make unsupported expertise claims, or lack a complete evidence model. They inform coverage and tests, not copied content. | Mixed; verify individually |
| Local `scoville-ui-anti-ai-slop` | Strong owner precedence, framework alignment, accessibility structure, responsive states, and honest rendered evidence. | Currently owns Greenfield direction, hierarchy, and general design judgment that should move conditionally to Design. It intentionally lacks general graphic, print, brand, imagery, and colour-management knowledge. | MIT |

### What should be borrowed as mechanisms

- From Anthropic: subject-specific direction and a memorable signature, without
  fixed palette/role counts.
- From Canvas Design: philosophy before pixels, without manifesto rhetoric or a
  fixed text ratio.
- From Impeccable: routed domains, explicit critique, design-context records,
  and bounded visual iteration.
- From UI/UX Pro Max: searchable knowledge and provenance, without turning the
  Skill into a style recommender database.
- From Taste Skill: infer the brief before selecting a language; expose a few
  high-level creative controls when they help; audit before redesign; use a
  strict completion preflight; and support image-to-analysis-to-implementation
  as one optional visual workflow. Keep the rules evidence-typed, routes
  modular, and exceptions contextual instead of importing fixed aesthetic
  bans, universal numeric recipes, or mandatory motion.
- From Design Atelier: references and system direction before parallel
  artifacts, without making orchestration a dependency.
- From Vercel and Scoville UI: evidence categories and precise implementation
  findings, without pretending source checks can judge a rendered composition.

No reviewed Skill should be copied wholesale.

## 3. Open and accessible learning corpus

“Available online” is not the same as “safe to adapt into a redistributable
Skill.” The proposed source policy therefore separates sources that permit
commercial adaptation, sources with ShareAlike or NonCommercial conditions,
NoDerivatives works, and read-only copyrighted material. The license summaries
below are operational screening, not legal advice.

| Source | Best use | License and packaging consequence | Limits |
| --- | --- | --- | --- |
| [Graphic Design and Print Production Fundamentals](https://opentextbc.ca/graphicdesign/) | Primary backbone for design process, elements, composition, grids, typography, colour systems, and production. Its contents explicitly cover design history, process, visual elements, compositional principles, organisational systems, colour management, and prepress. | CC BY 4.0. Adaptation and commercial reuse are allowed with attribution and change notice. Best candidate for directly traceable rule synthesis. | Introductory and 2015; its print-production chapters age faster; some examples and embedded media have separate licenses. |
| [The Legibility of Serif and Sans Serif Typefaces](https://link.springer.com/book/10.1007/978-3-030-90984-0) by John T. E. Richardson | Empirical typography baseline. The review finds no general serif-versus-sans legibility winner for print and largely no consistent winner on screens. It redirects judgment to actual typeface features, spacing, context, users, and medium. | CC BY 4.0 per chapter. Safe for attributed synthesis. | Narrow question; legibility is not the whole of typography or design quality. |
| [Introduction to graphic design and accessible design](https://ecampusontario.pressbooks.pub/incd2021/chapter/introduction/) | Inclusive visual-design baseline and the principle that accessibility begins with the design process. | CC BY 4.0 except noted material. | Short introductory chapter, not a complete design curriculum. |
| [Google Fonts Knowledge](https://fonts.google.com/knowledge) and its [license record](https://fuchsia.googlesource.com/third_party/github.com/google/fonts/+/refs/heads/upstream/davelab6-symbols-pure/cc-by-sa/README.md) | Current modular terminology, type technology, script-aware typography, font selection, and variable-font knowledge. | CC BY-SA 4.0. Link and learn freely. Copying or adapting expressive content into the Skill may trigger ShareAlike, so original synthesis and attribution are preferable unless licensing is deliberately designed around it. | Google Fonts context and uneven depth across topics. |
| [OERT: Open Educational Resources for Typography](https://www.oert.org/en/the-project/) | Typeface anatomy, structure, stroke, counter, spacing, kerning, tracking, publication use, exercises, self-assessment, and history. | CC BY-SA 2.5 Argentina. Same ShareAlike caution. | Older project, incomplete phases, and mixed Spanish/English coverage. |
| [Design With FontForge source](https://github.com/fontforge/designwithfontforge.com) | Typeface construction, optical judgment, spacing, metrics, kerning, script-specific work, and validation. | CC BY-SA 3.0. Same ShareAlike caution. | Tool- and typeface-design-specific; not a general guide to setting type or composition. |
| [Stop Stealing Sheep & Find Out How Type Works, 4th ed.](https://design.google/library/catching-up-with-erik-spiekermann) | Excellent visual eye-training, type character, purpose, whitespace, spacing, layout, and variable fonts. | CC BY-ND 4.0. It may be shared unchanged, but distributed adaptations are prohibited. Use as reference, not as text to transform into the Skill. | Introductory, practitioner-led, and not a complete evidence review. |
| [The Shape of Design](https://shapeofdesignbook.com/about/) by Frank Chimero | Design purpose, message-tone-format fit, constraints, improvisation, critique timing, and experienced rule breaking. It directly supports using structure to enable exploration rather than predetermine the result. | CC BY-NC-SA 3.0. NonCommercial and ShareAlike make it unsuitable as copied/adapted text in an unrestricted commercial Skill. Use as cited conceptual reading. | Reflective practitioner book, not empirical validation or a technical manual. |
| [The Elements of Typographic Style Applied to the Web](https://webtypography.net/toc) | Web adaptation of typographic rhythm, measure, leading, spacing, paragraphs, hyphenation, scales, and numerals. | CC BY-NC 4.0. Reference-only for a commercially reusable Skill unless separately permitted. | Work in progress; web-specific; derived from a copyrighted print tradition; some rules are conventions, not universal outcomes. |
| [Introduction to Art: Design, Context, and Meaning](https://open.umn.edu/opentextbooks/textbooks/introduction-to-art-design-context-and-meaning) | Visual language, elements and principles, formal analysis, interpretation, meaning, culture, and critique vocabulary. | CC BY-SA. Use for source-near learning with ShareAlike care. | Broad art survey, introductory, and reviewers identify Eurocentric gaps and limited depth in formal principles. |
| [The Art & Practice of Typography](https://library.si.edu/digital-library/book/artpracticeoft00gres) by Edmund G. Gress | Historical typesetting, advertising layout, specimens, and comparison material. | Smithsonian marks the digitization CC0/public domain. | 1917 technology and cultural assumptions are historical evidence, not current defaults. |
| [Butterick’s Practical Typography](https://practicaltypography.com/) | Practical reference for punctuation, type composition, page layout, documents, and screen reading. | All rights reserved under its [legal page](https://practicaltypography.com/legal.html). Freely readable is not openly reusable. Do not copy or adapt its prose into the Skill. | Strong practitioner guidance, but deliberately opinionated and not open-licensed. |
| [Government Design Principles](https://www.gov.uk/guidance/government-design-principles) and [USWDS Design Principles](https://designsystem.digital.gov/design-principles/) | UI-design grounding in real user needs, context, data, iteration, accessibility, and “consistent, not uniform.” Useful for workflow decisions before framework implementation. | Public government guidance. Preserve attribution and applicable site terms. | Public-service context; not a visual-style curriculum. |

### Licensing conclusion

The safest distributable knowledge base starts with CC BY 4.0, CC0, standards,
and independently written synthesis of facts and ideas. CC BY-SA sources can
remain linked reading unless the repository intentionally accepts ShareAlike
obligations for adapted passages. CC BY-NC, CC BY-NC-SA, CC BY-ND, and
all-rights-reserved works should remain reference-only. Creative Commons
confirms that [CC BY permits commercial adaptation with attribution](https://creativecommons.org/licenses/by/4.0/),
while [BY-SA adds a same-license condition](https://creativecommons.org/licenses/by-sa/4.0/),
[BY-NC-SA excludes commercial use](https://creativecommons.org/licenses/by-nc-sa/3.0/),
and [BY-ND prohibits distribution of adaptations](https://creativecommons.org/licenses/by-nd/4.0/).

### Professional competency gap check

The initial visual-craft map was incomplete. The
[NASAD communication-design competency summary](https://nasad.arts-accredit.org/wp-content/uploads/sites/3/2022/10/AD-BFA-CommunicationDesign-10-18-2022.pdf),
[ICoD professional guidance](https://www.theicod.org/resources/Professional-Code-of-Conduct/professional-performance),
[RGD AccessAbility](https://accessability.rgd.ca/), and
[AIGA Designer 2025](https://educators.aiga.org/aiga-designer-2025/) add the
following material abilities for an allround designer:

- diagnose briefs, research people and context, create alternatives,
  prototype, select, explain, and collaborate rather than jump to styling;
- understand semiotics, visual rhetoric, narrative, representation, culture,
  criticism, ethics, IP, privacy, sustainability, and social consequence;
- design information, diagrams, data visualization, navigation, wayfinding,
  spatial/distance conditions, sequences, transitions, and motion;
- stress content topology, localization, language expansion, script coverage,
  accessibility, and semantic non-visual alternatives;
- translate systems across screen, print, social, editorial, packaging, and
  brand touchpoints while respecting production and handoff constraints;
- separate observation, inference, preference, tradeoff, and verified defect
  when critiquing; calibrate confidence to the available artifact evidence;
- manage asset provenance and usage permission separately from the provenance
  of design knowledge.

These are not reasons to inflate the Core. They define the broad competency
map and the task-routed specialist and qualification lanes. A field is not
claimed as mature until its source, production, behavior, and visual evidence
passes its own cases.

## 4. What the research supports as applicable rules

### 4.1 Rule taxonomy

The Skill should never present all advice with the same force.

| Class | Meaning | Examples | May it be broken? |
| --- | --- | --- | --- |
| Constraint | Externally binding requirement | User brief, required content, output dimensions, trademark use, legally binding accessibility, font/image license | Only by an authorized change to the constraint, never by taste |
| Functional floor | Necessary for the artifact to perform its job | Essential information remains perceivable, reading order is recoverable, an interface action remains operable | Only if the function is intentionally removed or supplied through another valid channel |
| Evidence-backed default | Best-supported starting point for a class of contexts | Provide sufficient text contrast on the web; allow text spacing without content loss; use actual user needs to shape UI workflow | Yes, only where the source scope does not apply or an authorized target differs; preserve exact tradeoff |
| Craft heuristic | Reusable way to improve perception or coherence | Use alignment to expose relationships; establish contrast; build a grid; limit competing focal points; create typographic roles | Yes. These are tools, not laws |
| Convention | Familiar pattern whose value comes partly from recognition | Page numbers, navigation placement, genre signals, type classifications | Yes, if the replacement remains understandable or deliberate disorientation is part of the brief |

An **experiment** is a declared workflow state applied to a heuristic or
convention, not an authority type. A **tradeoff** is an evaluation outcome.
**Preference/taste** is non-defect evidence attributed to a named person or
audience. An untyped numeric prescription has at most craft-heuristic authority.

### 4.2 Design process before style

The BCcampus text frames communication design as delivering information to a
target audience through define, research, concept development, and
implementation. Chimero's message-tone-format model adds a useful creative
test: successful work makes all three support the objective, while fresh work
can deliberately explore different configurations. Therefore the Skill should
start with:

1. purpose and desired consequence;
2. audience and viewing/usage context;
3. message and required content;
4. medium, format, production, and accessibility constraints;
5. tone and visual concept;
6. only then palette, typography, grid, imagery, and detail.

A named style such as “brutalist,” “premium,” or “editorial” is evidence only
when it follows from this chain. It is not a substitute for it.

### 4.2.1 Design history and style direction

Style direction needs a dedicated, selectively loaded knowledge route. The
Skill must distinguish historical movements, period umbrellas, genres,
reduction methods, material techniques, moods, and incumbent systems rather
than flattening them into interchangeable presets. “1980s” is an umbrella;
Memphis, New Wave, punk, corporate postmodern, and synthwave produce materially
different systems. “Neon” is a light/material modifier. “Neoclassicism” is a
historical lineage. “Minimalism” is a reduction strategy whose result need not
be white or monochrome.

The selected direction should be expressed as a Design Language Brief covering
composition, typography, colour/light, imagery, form/ornament, material,
spacing/rhythm, motion, one subject-specific signature, clichés to avoid,
protected functional constraints, and intended validation. One structural
lineage is primary; additional influences have declared secondary or modifier
roles. The result is judged for brief fitness and structural coherence, not
only for recognizable decorative signs. The detailed source basis, initial
atlas, steering protocol, and tests are in the
[style-direction system](../research/style-direction-system.md).

### 4.3 Composition and perception

The open BCcampus design text treats point, line, plane, colour, negative
space, texture, and typography as elements, and alignment, contrast, grids,
hierarchy, and organisational systems as ways to structure them. It also states
that a grid is a bridge from rationale to implementation and may be a strict
discipline or a starting point. Modern perception research supports using
grouping and figure-ground as perceptual mechanisms, but describes open
limitations rather than timeless “laws.” See Wagemans et al.,
[A Century of Gestalt Psychology in Visual Perception](https://pmc.ncbi.nlm.nih.gov/articles/PMC3482144/).

Applicable rules should therefore be phrased as outcome tests:

- **Hierarchy:** Can the intended first, second, and supporting readings be
  perceived at the intended size without reading every word?
- **Grouping:** Do distance, alignment, enclosure, similarity, continuity, and
  shared movement communicate the intended relationships?
- **Contrast:** Does difference carry a real distinction in importance,
  category, state, or tone?
- **Balance and tension:** Is visual weight deliberately stable, directional,
  or unstable for the intended effect?
- **Rhythm:** Do repeated intervals and variations create a useful pace rather
  than accidental drift?
- **Negative space:** Does empty space separate, frame, or energize the active
  elements, or is it only unused area?
- **Grid:** Does the scaffold express relationships and enable variation? A
  visible break is valid when the grid remains legible enough for the break to
  have force.
- **Unity and variety:** Can the artifact be recognized as one system without
  making unlike information visually identical?

### 4.4 Typography

Typography must be evaluated at several levels:

- meaning, voice, and genre fit;
- script and language coverage;
- glyph distinction and actual typeface construction;
- display, text, label, caption, data, and utility roles;
- scale, weight, width, optical size, and contrast between roles;
- measure, leading, paragraph rhythm, alignment, hyphenation, tracking,
  kerning, and word spacing;
- fallback metrics, font loading, production, and licensing;
- actual reading context, size, substrate, resolution, distance, and user need.

Richardson's open systematic review is especially important because it rejects
the common shortcut “serif for print, sans for screens” as a universal
legibility rule. On paper, the modal finding was no difference. On screens,
results were also mostly no difference or inconsistent, with confusions tied
more closely to individual glyph design, width, spacing, size, and luminance.
The Skill should therefore never ban or prefer a broad type category without
context and rendered evidence.

Likewise, line-length, line-height, and type-scale numbers are candidate ranges,
not universal laws. [WCAG 2.2](https://www.w3.org/TR/WCAG22/) supplies real
quantitative requirements for scoped web accessibility, including 4.5:1 normal
text contrast at Level AA and survival under user-set text spacing. Its
80-character visual-presentation target is Level AAA and requires a mechanism,
so it must not be misreported as a universal 65-character design law.

### 4.5 Colour and imagery

Colour decisions should be based on role, relationships, medium, gamut,
environment, perception, accessibility, culture, and concept. The Skill should
not prescribe favourite palettes, ban purple, require tinted neutrals, or treat
a colour wheel as proof of harmony. It should distinguish:

- perceptual contrast from aesthetic harmony;
- semantic/state colour from atmosphere;
- local simultaneous contrast from a hex value in isolation;
- RGB emissive output from CMYK/spot/substrate reproduction;
- palette consistency from adequate distinction;
- cultural association from a universal emotional meaning.

Imagery should be judged for subject relevance, authorship/license, crop,
focal relationship, resolution, art direction, visual metaphor, consistency,
and integration with type and space. Decorative detail must either support the
concept or earn its cost through atmosphere, rhythm, or identity.

### 4.6 UI design inside Scoville Design

Design owns the UI-design question before implementation:

- identify the user's goal and the shortest coherent path;
- arrange information and controls according to decisions and prerequisites;
- decide hierarchy, grouping, disclosure, density, and feedback placement;
- define the visual system and its relationship to product tone;
- make variant and state direction coherent with the overall design;
- preserve accessibility as a design input, not a final code scan.

The [GOV.UK principles](https://www.gov.uk/guidance/government-design-principles)
support starting with user needs, designing with data, iterating, understanding
context, and being consistent rather than uniform. [USWDS](https://designsystem.digital.gov/design-principles/)
similarly treats real user needs, accessibility, and system use as evaluative
lenses. Design may recommend rearranging a page built with an existing design
system when the workflow or hierarchy is poor. It should not gratuitously
replace that system's components, typography, or tokens.

UI then translates the approved decision into the owning framework and proves
states, responsiveness, interaction semantics, and accessibility behavior.

## 5. Rule breaking without rationalized slop

“It looks good” matters, but it is not enough as an unexamined assertion. The
Skill needs an exception protocol that protects successful design experiments
without rewarding arbitrary inconsistency.

### Exception protocol

1. **Name the intended effect before rendering generated work.** Examples:
   urgency, interruption, intimacy, monumental scale, unstable tension,
   archival density, or playful ambiguity. For an existing artifact, mark
   intent as documented, inferred, or unknown; critique-time invention does not
   establish a successful exception.
2. **Name the normal principle being bent.** A broken grid is different from an
   accidental misalignment. Low contrast as atmosphere is different from
   unreadable required information.
3. **Protect binding constraints and the artifact's job.** Essential content,
   licensing, legal accessibility, safety, and user-authorized requirements do
   not disappear because a composition is attractive.
4. **Find the compensating structure.** A design can break alignment while
   retaining hierarchy through scale and value, or use density while retaining
   navigation through strong grouping and rhythm.
5. **Render the real artifact.** Judge it at intended size, medium, crop,
   content density, and viewing distance. For UI, include relevant states and
   viewports with Scoville UI when active.
6. **Compare.** Use the rule-following baseline or a controlled variant when the
   exception was undeclared, is challenged, touches a functional floor, or has
   a material and uncertain gain.
7. **Keep the exception if the whole improves.** Do not “correct” an intentional
   deviation merely because a checklist detects it. Record the gain and cost.

Chimero's freely readable CC BY-NC-SA book treats constraints as a framework that enables
improvisation and argues that criticism should become stricter as an idea
matures. The BCcampus text similarly treats organisational systems as
frameworks that enable varied layouts rather than predetermine results. These
sources support structured freedom, not unlimited post-rationalization.

## 6. Design and critique workflows

### Design mode

1. Resolve artifact, audience, purpose, message, medium, required content,
   constraints, and existing visual owner.
2. Inspect supplied references and assets. Extract principles and relationships,
   not an artist's signature style to imitate.
3. Define one clear design hypothesis in terms of message, tone, format, and
   intended viewer experience. When the brief contains consequential
   uncertainty, create a small set of materially different hypotheses through
   content-derived form, constraint inversion, material metaphor, narrative
   framing, or another subject-specific mechanism; reject cosmetic variants.
4. Establish the smallest coherent system for typography, colour, spacing,
   grid, imagery, shape, and motion where applicable.
5. Produce at least one composition. Generate materially different variants
   only when the brief leaves a consequential direction open.
6. Render the artifact through the appropriate execution Skill or tool.
7. Critique the render at system, composition, and detail levels.
8. Revise observed defects in one bounded pass, then verify the corrections.
9. Report evidence and residual uncertainty. Do not claim visual quality from
   source alone.

### Critique mode

1. Preserve the user's artifact. Audit means read-only unless changes are
   explicitly requested.
2. Describe what is visibly present before interpreting intent.
3. Separate observed fact, inferred intent, contextual constraint, taste, and
   accessibility requirement.
4. Evaluate in this order: purpose and workflow, hierarchy and grouping,
   typography, composition and space, colour and imagery, consistency and
   detail, medium-specific production.
5. Preserve strong choices and successful exceptions.
6. Prioritize findings by consequence, not by the number of rules touched.
7. For each finding, state evidence, viewer effect, likely cause, and the
   smallest coherent correction direction.
8. Do not rewrite or redesign unless requested.

Open art-education material describes formal analysis as a progression from
description through interpretation to evaluation, using visible elements and
principles as evidence. That is a better critique foundation than immediate
prescription. See [Introduction to Art](https://human.libretexts.org/Bookshelves/Art/Art_Introduction_and_Fundamentals/Introduction_to_Art%3A_Design_Context_and_Meaning_%28Sachant_et_al.%29/04%3A_Describing_Art).

## 7. Evidence and model limits

The Skill must be multimodal in practice. A text-only checklist cannot reliably
judge a finished design. Recent research supports both the usefulness and the
limits of vision-language models:

- [DesignProbe](https://arxiv.org/abs/2404.14801) separates element-level
  colour/font/layout recognition from overall style and metaphor. It found
  layout and font tasks difficult, while visual examples improved performance
  more than text descriptions in its tested setup.
- [AesEval-Bench](https://arxiv.org/abs/2603.01083) evaluates aesthetic
  judgment, affected-region selection, and precise localization across twelve
  indicators and reports clear gaps for current VLMs on nuanced graphic-design
  assessment.
- Adobe/UCSB research on [automatic layout planning](https://aclanthology.org/2024.alvr-1.14/)
  shows that purpose and canvas constraints can improve structured layout
  generation, but specialized training and benchmarks outperform generic
  few-shot prompting.

Consequences for the Skill:

- Require an actual render or supplied image for visual-quality claims.
- Use source inspection only for structure, tokens, assets, dimensions, and
  implementation intent.
- Use visual examples where licensing permits, not prose alone, in evaluation
  fixtures.
- Prefer comparative judgments over uncalibrated absolute scores.
- Treat aesthetic diagnosis as fallible. Localize the evidence and state
  uncertainty when the visual signal is ambiguous.
- Keep human preference and final approval authoritative.

### Minimum rendered checks

Use only checks that can change the decision:

- intended physical or pixel size;
- thumbnail/squint view for hierarchy and weight;
- actual-size reading for typography;
- grayscale/value view when hierarchy depends on colour;
- edge, crop, bleed, safe-area, and resolution checks for fixed media;
- representative content density and language;
- contrast and colour-vision checks where accessibility applies;
- relevant UI viewport, text-scale, state, and input conditions through
  Scoville UI when it is active.

## 8. Recommended Skill architecture

The [Agent Skills specification](https://agentskills.io/specification) recommends
progressive disclosure: metadata at discovery, a compact `SKILL.md` at
activation, and references/scripts only when needed. The corpus is too broad
for one always-loaded checklist.

Recommended package:

```text
scoville-design-anti-ai-slop/
├── SKILL.md
├── modules.yaml
├── agents/openai.yaml
├── references/
│   ├── brief-and-concept.md
│   ├── style-direction.md
│   ├── composition-and-layout.md
│   ├── typography-and-writing-systems.md
│   ├── colour-and-reproduction.md
│   ├── imagery-and-art-direction.md
│   ├── information-and-data.md
│   ├── brand-and-visual-systems.md
│   ├── ui-and-interaction-design.md
│   ├── motion-and-sequence.md
│   ├── media-production-and-handoff.md
│   ├── critique-and-validation.md
│   ├── culture-ethics-and-provenance.md
│   └── sources-and-attribution.md
├── scripts/
│   ├── build-module-index.*
│   ├── validate-package.*
│   └── route-probe.*
└── tests/
    └── evaluation-cases.json
```

### Core `SKILL.md`

The Core should contain only:

- trigger and exclusions;
- authority, applicability, existing-owner, and Design/UI handoff rules;
- optional Design/UI ownership composition, constraint loop, and UI fallback;
- the canonical `generate`, `critique`, `repair`, and `style-direction` modes;
- brief invariants and the bounded generate/render/critique/repair loop;
- rule taxonomy and functional accessibility floor;
- brief-to-render workflow;
- declared-versus-inferred exception gate;
- provenance and evidence boundary;
- reference router;
- family ownership summary.

The Core is capped at 1,500 `o200k_base` tokens. Ordinary single-domain active
context is capped at 3,800 tokens and ordinary mixed context at 7,000 tokens
with no more than three references unless a named design decision requires an
exception. The frozen route matrix is the behavioral contract, not the file
list alone.

The Core's direct module index is generated from a canonical `modules.yaml`
registry. This permits a task to select multiple one-level experts without
expert-to-expert chains or a second hand-maintained routing table. Module
content is admitted only as a tested SOL focus, correction, teaching payload,
or external-verification route. See the
[modular application architecture](../research/modular-application-architecture.md).

### References

The earlier principle-only entry shape is superseded by the application-first
expert payload contract. Each expert reference should use:

```text
Scope, owner, non-owner, and triggers
Observable inputs and failure signatures
Decision procedure
Generation actions
Domain critique discriminators
Repair operators
Style-direction effects where applicable
Rule strength, exceptions, and counterexamples
Rendered or deterministic verification
Source IDs, SOL evidence IDs, unknowns, and escalation
```

This turns knowledge into applicable judgment without pretending every
principle is a command.

### Scripts

Do not build an “aesthetic score” script. Deterministic helpers may calculate
contrast, inspect image dimensions/resolution, detect overflow, list fonts and
licenses, or overlay grids. Their output is supporting evidence only.

## 9. Required evaluation before release

The Skill needs isolated, adversarial cases rather than only attractive demos.

### Routing and ownership

1. Design active, UI absent.
2. UI active, Design absent, Greenfield fallback required.
3. Both active for Greenfield UI.
4. Both active with an incumbent framework design system.
5. Design explicitly excluded while UI remains active.
6. Neither active as a no-Skill control.
7. Static graphic where UI must not activate.
8. Existing UI implementation task where Design must not displace the system.

### Design capability

- poster with dense required event information;
- editorial spread with long text and images;
- social graphic with strict crop/safe-area constraints;
- brand direction without supplied visual system;
- Greenfield webpage requiring a new design system;
- product UI workflow inside a supplied component framework;
- multilingual typography and fallback;
- print/RGB-CMYK production boundary.

### Critique capability

- strong design with deliberate broken grid that must be preserved;
- polished but generic design with no subject-specific concept;
- visually exciting design with failed required-text legibility;
- mechanically aligned design with weak hierarchy;
- existing framework UI with poor workflow but correct components;
- source-only audit where rendered quality must stay unverified;
- culturally narrow or inappropriate imagery;
- inaccessible colour use where aesthetic intent does not waive the floor.

Each case should compare no-Skill and routed runs, score design outcome and
routing separately, and require evidence citations to the observed artifact.
One attractive generated example is not proof of general design competence.

### Comparative references and pairwise tests

The strongest reviewed comparison sources include the same-page A. Dawn
Journal redesign in the CC BY chapter
[Technical Writing: Basic Design](https://openoregon.pressbooks.pub/technicalwriting/chapter/basic-design/),
the annotated same-site [W3C Before and After Demonstration](https://www.w3.org/WAI/demos/bad/),
commercial before/after books by Lisa Graham and John McWade, Apple's
[designer-feedback dataset](https://github.com/apple/ml-rldf),
[TASTE](https://huggingface.co/datasets/purvanshi/TASTE),
[UICrit](https://github.com/google-research-datasets/uicrit), and
[DesignPref](https://arxiv.org/abs/2511.20513). Their applicability and license
limits are recorded in the
[comparative-reference assessment](../research/comparative-reference-material.md).

These sources support pairwise testing but not one universal beauty label.
DesignPref reports substantial disagreement even among trained designers.
Tests should therefore separate functional Gold from visual preference,
preserve vote margin and rationale, and allow “no decisive winner” when two
solutions express a legitimate tradeoff. The decisive suite should use
original same-brief pairs with seeded functional, craft, concept, production,
and deliberate-exception variants. It must test discrimination, critique, and
repair separately.

Third-party books, screenshots, comparison images, and datasets do not enter
the repositories. They remain linked research or, where needed and permitted,
local-only evaluation material outside the repositories. Repository fixtures
must be original or independently source-cleared.

## 10. Risks and unresolved decisions

1. **Knowledge breadth versus activation cost.** A general designer needs broad
   knowledge, but an oversized Core will reduce relevance. Progressive routing
   is necessary.
2. **Licensing.** ShareAlike, NonCommercial, and NoDerivatives sources cannot be
   casually blended into an MIT package. A source ledger and attribution policy
   are release blockers.
3. **UI boundary drift.** The current UI Skill still owns hierarchy and
   Greenfield direction. The family needs coordinated wording and routing tests,
   while retaining UI's solo fallback.
4. **Aesthetic overconfidence.** Vision models still struggle with layout,
   fonts, localization, and precise defect localization. Human approval and
   rendered evidence remain necessary.
5. **Numeric cargo cults.** Fixed spacing scales, type ratios, line lengths,
   font bans, golden-ratio layouts, and palette recipes are easy to follow but
   often falsely universal.
6. **Rule-break rationalization.** An exception protocol must require purpose,
   compensation, and rendered comparison, not merely a confident explanation.
7. **Cultural scope.** Much accessible design literature remains Western and
   Latin-script-heavy. The implementation plan must add script-, language-,
   culture-, and medium-specific counterexamples.
8. **Tool boundary.** Design directs artifact creation. Image, code, document,
   presentation, and PDF Skills still own their formats and technical proof.

## Recommendation

The independent Fable 5.1 High and fresh GPT-5.6 SOL XHigh reviews both returned
“revise before implementation.” They support the architecture but identified
the same material contract gaps: holdout timing, aesthetic SkillOpt objectives,
Design/UI applicability and handoff, post-hoc exception intent, context budgets,
source-depth claims, human-review protocol, and local-material permission.

Four user-selected directions remain accepted:

- Design owns design definition and judgment, UI owns strict implementation,
  and UI retains Greenfield fallback when Design is unavailable or inapplicable;
- rules are typed by authority and may be broken when the exception is
  intentional, functionally sound, compensated, rendered, and better for the
  whole artifact;
- substantial knowledge is loaded through a compact multi-route Core rather
  than on every task;
- the product follows a staged broad-and-deep architecture: cover the complete
  competency map, qualify a deep shared core, and claim specialist competence
  only after domain-specific evidence.

ADR-0003 is revised but remains proposed. ADR-0006 through ADR-0009 propose
operational successors or additions for ownership, exception epistemics,
progressive routing, and qualification. W-007 now freezes these contracts,
source/domain maturity, an independently held final holdout, and exact claim
boundaries before implementation. Implementation must not begin until the user
disposes every proposal explicitly and independent holdout custody is resolved.

## Research limits and stop condition

Searches covered public Skills, open books, licensing, visual design theory,
typography, accessibility, UI-design guidance, perceptual grouping, current VLM
evaluation, comparative before/after material, brand systems, data
visualization, writing systems, motion, editorial/multi-page work, photography,
wayfinding, packaging, and colour technology. Further broad searching was
stopped because additional results were predominantly style presets, mirrors,
derivative bundles, or repeated recommendations. Remaining gaps are maturity
gaps rather than broad-discovery gaps: specialist art direction and
commissioning, brand architecture, native-reader validation, current vendor
production, packaging fabrication, and human outcome evidence. The
[domain-maturity ledger](../research/domain-maturity.md) keeps those claims
bounded.
