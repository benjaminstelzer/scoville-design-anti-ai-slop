# Style direction and design-history system

Date: 2026-09-01  
Status: pre-implementation research extension  
Related: `AUDIT-0001`, `PLAN-0001`, `ADR-0006`, `ADR-0007`

## Why a style list is not enough

There is no single canonical, complete list of design styles. The terms users
apply to visual work belong to different classes:

1. **historical movements and lineages**, such as Neoclassicism, Art Nouveau,
   Constructivism, the International Typographic Style, or Postmodernism;
2. **period umbrellas**, such as “1980s,” which contain several conflicting
   movements and commercial or subcultural languages;
3. **genres and contemporary aesthetics**, such as synthwave, luxury,
   editorial, cyberpunk, or brutalist web design;
4. **methods and reduction strategies**, such as minimalism or maximalism;
5. **materials and techniques**, such as neon, risograph, halftone, collage,
   letterpress, chrome, pixel art, or glass;
6. **moods and brand attributes**, such as calm, playful, severe, intimate,
   institutional, or futuristic;
7. **incumbent systems**, such as an established brand system, product design
   system, or framework language.

Treating all of these as interchangeable presets creates costume design: a few
recognizable signs are applied without understanding their origin, structure,
purpose, or medium. Scoville Design instead needs a design-language synthesis
method backed by design history, formal principles, actual artifacts, and
rendered judgment.

## Application priority

This research file is a maintainers' coverage map, not a requirement to load a
style encyclopedia at runtime. The released Skill starts with one compact
style-direction expert that focuses SOL's existing knowledge on generation,
discrimination, repair, and translation. Individual history/style patches ship
only when SOL baseline and ablation evidence shows that a compact focus or
correction materially improves an applied result. History remains available
for ambiguity, provenance, anachronism, and unfamiliar directions, but does not
outrank professional composition, typography, concept, craft, or rendered
revision.

## Public-source foundation

The foundation is not Taste Skill's style recipes. The main reusable backbone
is the CC BY 4.0 *Graphic Design and Print Production Fundamentals*, whose
history curriculum covers Arts and Crafts, Werkbund, Bauhaus, Dada,
International Typographic Style, Late Modern, and Postmodern design and ties
movements to culture, technology, and predecessor influence. The CC BY-SA
*Introduction to Art: Design, Context, and Meaning* supplies formal analysis,
context, meaning, and critique rather than a style lookup alone.

Historical range and visual verification should then use expert museum
records and rights-screened objects. The Metropolitan Museum of Art's
Heilbrunn Timeline provides expert chronological and geographical context;
only object images explicitly included in The Met's Open Access/CC0 program
are reusable. Smithsonian Open Access and the Cooper Hewitt collection provide
CC0-designated design artifacts and metadata across periods, media, and
regions. Owen Jones's public-domain *The Grammar of Ornament* can support
historical pattern analysis, but its nineteenth-century categories and
colonial viewpoint must be treated as historical evidence, not a neutral
taxonomy of cultures.

Open access does not make a source complete or unbiased. The initial corpus is
stronger for Western modern graphic design than for global, vernacular, and
contemporary digital languages. Those gaps remain explicit in the maturity
ledger and require item-level sources and, where relevant, cultural authority.

## Working style atlas

The atlas should be broad enough to recognize and research a direction, but it
must not claim that a row fully defines a movement. Each shipped profile needs
sources, historical context, formal grammar, variants, common misreadings,
medium translations, and open artifact examples.

### Executable style-profile contract

A profile is not complete because the agent can describe it. It may ship only
when it can support four operations:

1. **generate** an artifact whose structure and surface are recognizably rooted
   in the direction;
2. **critique** both fidelity to that direction and fitness for the brief;
3. **repair** weak or clichéd execution without erasing the requested identity;
4. **translate** the same design language to the relevant medium rather than
   scaling one composition.

Every atlas profile therefore needs an agent-facing tutorial with:

```text
Name, aliases, term class, dates/places, and source status
Historical/cultural/technical origin
Communication attitudes and typical subject matter
Structural grammar: composition, grid, hierarchy, density, rhythm
Typography: classifications, roles, setting, and script limits
Colour/value/light and reproduction behavior
Image, illustration, icon, symbol, and ornament behavior
Material, texture, production, motion, and interaction behavior
Recognizable signatures, optional signatures, and false stereotypes
Compatible modifiers and incompatible or high-friction combinations
Medium-specific translations and accessibility/production compensation
Design procedure, critique questions, repair moves, and rendered checks
Open artifact references plus provenance and claim limits
Generation, critique, repair, and cross-medium evaluation cases
```

Descriptive knowledge without these design actions remains research-only and
does not justify an advertised style capability.

### Historical and modern lineages

| Family | Initial profiles and distinctions to cover |
| --- | --- |
| Classical and revival | Classical Greek/Roman visual orders; Renaissance/humanist page traditions; Baroque and Rococo as distinct systems; Neoclassicism and Empire; Gothic and later Gothic Revival. Avoid collapsing architecture, fine art, ornament, and graphic translation into one look. |
| Industrial reform and ornament | Victorian/eclectic display; Arts and Crafts; Aesthetic Movement; Art Nouveau, Jugendstil, and Vienna Secession as related but non-identical; Sachplakat/Plakatstil; Art Deco and Streamline Moderne. |
| Early avant-garde | Cubist influence; Futurism; Dada; Russian Constructivism; Suprematism; De Stijl; Bauhaus; New Typography. Preserve their different politics, composition, type, image, and production logics. |
| Systematic modernism | International Typographic/Swiss Style; Ulm functionalism; Isotype and information design; Mid-century modern; New York School; corporate modernism and identity systems. “Minimal” is not a synonym for all modernism. |
| Counterculture and postmodern | Pop Art; Op Art; Psychedelia; Situationist/DIY and protest graphics; Punk and zine; New Wave typography; Postmodern eclecticism; Memphis; early digital expression; deconstruction and grunge. |
| Digital and contemporary | Early web and pixel vernacular; Y2K; skeuomorphic, flat, Material, and spatial interface languages; vaporwave, synthwave, and cyberpunk; contemporary editorial, neo-grotesque minimalism, neo-brutalism, maximalism, organic/biophilic, generative, 3D/chrome, and mixed-media collage. Trend names need dated sources because meanings drift. |
| Regional and vernacular | Place-, script-, community-, craft-, signage-, print-, and subculture-specific visual languages. Never reduce a living culture to decorative motifs; require precise origin, artifact sources, script knowledge, permission, and representation review. |

### Expressive strategies and material modifiers

These are separately routable because they can modify many lineages:

- minimalism, maximalism, restraint, density, symmetry, asymmetry, rawness,
  precision, play, luxury, institutional authority, intimacy, spectacle;
- neon/emissive light, fluorescent ink, duotone, monochrome, high-key,
  low-key, metallic/chrome, transparency, grain, noise, patina;
- collage, photomontage, cut paper, risograph, screen print, letterpress,
  halftone, dithering, pixel, bitmap, vector-flat, painterly, photographic,
  illustrative, diagrammatic, typographic;
- editorial, cinematic, documentary, technical, retail, activist,
  entertainment, fashion, cultural, scientific, and public-service genres.

## Design-language steering protocol

### 1. Classify the request

Do not assume every named term is a complete style. Identify whether it is a
lineage, period umbrella, genre, method, material treatment, mood, or incumbent
system. Preserve supplied references and existing brand/system ownership.

### 2. Establish fit before appearance

Resolve purpose, audience, message, medium, context, content, accessibility,
production constraints, and desired consequence. A direction is valid only if
it helps those conditions rather than merely resembling a mood board.

### 3. Resolve consequential ambiguity

If an umbrella term would produce materially different artifacts, either infer
from strong brief evidence or present a small set of genuinely different
directions. “1980s,” for example, may mean:

- **Memphis/postmodern consumer:** playful geometry, pattern, high chroma,
  deliberate imbalance, laminate/plastic material cues;
- **New Wave/editorial:** Swiss structure disrupted through layered type,
  diagonals, scale changes, photostat/digital texture, and active depth;
- **synthwave/night technology:** emissive accents, dark fields, horizon or
  perspective devices, chrome and display lettering derived from retro-future
  media rather than the whole decade;
- **corporate postmodern/early digital:** cleaner grids mixed with expressive
  geometry, early desktop-production signals, and controlled eclecticism.

These are not interchangeable “80s colours.”

When the user supplies several mutually reinforcing signals, do not dilute
them by over-clarifying. For “typical 1980s neon, ASCII art, old-school retro,
neon vibes, VHS look,” the Design Language Brief can resolve directly to:

- **primary language:** 1980s retro-computing/synthwave entertainment rather
  than Memphis or corporate postmodernism;
- **composition:** strong horizon or frame logic, terminal/display zones,
  oversized title, layered depth, deliberate screen-era geometry;
- **type:** a period-recalling geometric display face plus monospace/pixel or
  ASCII roles, while body copy stays readable and supports the language;
- **colour/light:** near-black or deep blue-violet field with a controlled
  magenta/cyan/electric accent relationship and real emissive hierarchy;
- **imagery:** subject-specific ASCII hero, limited wireframe/grid or chrome
  device where it supports the subject, not a generic asset pile;
- **surface:** selective scanlines, tracking noise, chromatic separation,
  bloom, timestamp or tape artifacts with enough restraint to keep content
  legible;
- **motion:** optional signal acquisition, cursor, tracking, or flicker cues
  with reduced-motion and static equivalents;
- **signature:** one concept-specific combination of the subject and the
  retro-computing language, so the page is not merely a synthwave template;
- **protected floor:** glow does not blur body type, noise does not cover
  controls, fake terminal decoration does not imply false functionality, and
  mobile hierarchy remains clear.

Because the request says “typical,” familiar signifiers are part of the brief.
The anti-cliché rule does not ban them; it prevents unselected repetition and
requires them to form one coherent, subject-specific system.

### 4. Build a Design Language Brief

Use one **primary structural lineage**, optional **secondary influence**, and
only the material or mood modifiers that serve the brief. Record:

- purpose, audience, message, medium, and viewing/usage context;
- primary lineage and the reason it fits;
- secondary influence and how it relates rather than averages;
- composition and grid behavior;
- typographic voice, roles, setting, and script needs;
- colour, value, light, and reproduction behavior;
- imagery, illustration, icon, and symbol system;
- form, edge, ornament, surface, and material behavior;
- spacing, rhythm, density, scale, and focal structure;
- motion or sequence only when the medium and purpose require it;
- one subject-specific signature move;
- forbidden clichés and irrelevant signifiers;
- functional, accessibility, brand, rights, and production invariants;
- evidence still needed and the intended rendered validation.

Use verbal intensity bands such as `restrained`, `clear`, and `dominant` unless
an actual measurable variable exists. A 1-10 “style strength” number creates
false precision.

### 5. Translate, do not copy

Extract relationships and principles from references rather than reproducing
a named designer's recognizable expression. Preserve the lineage's structural
logic while adapting it to the artifact. A neon treatment may modify a
Neoclassical composition: axial order, proportion, measured type, and
restrained ornament remain primary while emissive light is limited to
hierarchy or atmosphere. That is more coherent than mixing every stereotypical
sign equally.

### 6. Render, inspect, and revise

Judge the artifact at intended size, distance, medium, state, and content. Test
both style coherence and design fitness:

- Does the result communicate the brief before the style label is explained?
- Are the structural traits present, or only decorative tokens?
- Is the historical or cultural reference specific and defensible?
- Does the medium translation preserve function and production reality?
- Are typography, hierarchy, spacing, and imagery coherent as one system?
- Is the result distinctive without depending on a pile of clichés?
- Does any deliberate rule break improve the whole and preserve invariants?

## Four calibration examples

### Minimalism

Minimalism is a reduction strategy, not “white background + sans serif + lots
of empty space.” It removes elements that do not advance meaning, hierarchy,
operation, or atmosphere, then makes the remaining relationships exact. It can
be colourful, typographic, image-led, warm, or dense where the task requires.

### Brutalism

Architectural Brutalism, raw print languages, punk/DIY graphics, and web
brutalism overlap but are not one style. Useful traits can include exposed
structure, material directness, unsoftened hierarchy, hard contrast, visible
systems, and refusal of cosmetic polish. Military terminals, scanlines,
uppercase monospace, red accents, and zero radius are possible subgenre signs,
not universal requirements.

### Neon

Neon is primarily a light, colour, and material modifier. It involves emissive
contrast, bloom, edge light, surrounding darkness or controlled ambient light,
and reproduction-specific gamut limits. It is not automatically 1980s,
cyberpunk, or a black background. Glow must not destroy letterform edges,
small-text contrast, hierarchy, or print translation.

### Neoclassicism

Neoclassical translation starts with order, clarity, proportion, axial or
balanced composition, controlled dramatic emphasis, classical references, and
measured ornament. It does not automatically mean black, gold, marble, Roman
columns, and a high-contrast fashion serif. Contemporary work may express the
lineage through spacing, geometry, typographic proportion, borders, and image
staging with very little literal ornament.

## Progressive-disclosure package design

The Skill Core should only classify the term and route the task. Version one
ships a direct `style-direction.md` expert. Additional direct leaves are added
only for SOL-proven gaps rather than preloading the whole research atlas:

```text
references/
├── brief-and-concept.md
├── style-direction.md
└── style-<qualified-gap>.md        # optional direct leaf after evidence
```

Normal design work loads no style file unless a named, inferred, or comparative
direction can materially change the result. A named style loads the compact
style-direction expert plus only a qualified gap leaf when one exists. A
cultural or regional request also loads culture, ethics, and provenance. The
source-and-attribution reference is loaded only for a provenance audit or
maintainer work, not every design task.

## Required qualification cases

1. Disambiguate “80s” into materially different directions instead of one
   synthwave stereotype.
2. Apply neon as a restrained modifier to a non-1980s primary language.
3. Produce a colourful minimalist system without adding nonessential parts.
4. Produce a readable, usable brutalist interface without military-terminal
   cosplay.
5. Translate one Neoclassical language across a poster, editorial spread, and
   responsive web surface without scaling one layout.
6. Reject or repair an artifact that matches decorative signs but contradicts
   the style's structural logic.
7. Handle an unfamiliar cultural or vernacular request by locating authority
   and stating uncertainty instead of inventing motifs.
8. Mix two compatible influences with declared dominance, and reject an
   incoherent equal-weight mashup.
9. Design from an objective with no named style and avoid forcing a catalogue
   label when the concept is stronger without one.
10. Generate, critique, repair, and responsively translate the explicit
    1980s-neon/ASCII/VHS web brief above; fail if the result is only a generic
    modern dark page with coloured glow or if stylistic noise defeats use.

## Claim boundary

Version one can ship a source-grounded style-analysis and synthesis protocol
plus selected well-sourced profiles. It cannot honestly claim exhaustive
knowledge of every historical, regional, vernacular, subcultural, or emerging
style. The atlas grows by adding sourced profiles and behavior tests, not by
adding unsupported adjective lists.
