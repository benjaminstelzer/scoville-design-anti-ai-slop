# Composition and layout

Status: `draft`  
Intervention: `external-verification`  
Sources: `SRC-COMPOSITION-CANON`, `SRC-GESTALT-EVIDENCE`, `SRC-TYPE-DETAIL`, `SRC-PROFESSIONAL-SCOPE`, `SRC-CRITIQUE-CANON`, `SRC-PACKAGE-LOCAL-SYNTHESIS`

## Load when

Load for consequential within-page or within-frame hierarchy, semantic spacing,
negative space, grid, balance, density, content fit, or a challenged spatial
exception. Do not load only because an artifact has a layout. Cross-page/slide
sequence and templates belong to fixed-media design; responsive transformation
intent belongs to web design; glyph-to-paragraph spacing belongs to typography;
file, bleed, trim, safe-area, preflight, and supplier acceptance belong to
production. Load each of those owners independently when its concern is open.

## Inputs and formal variables

Inspect the artifact or real content, not a verbal summary. Record only open relevant fields; otherwise use the Core minimal record:

- `C`: required content units, semantic groups, consequence, dependencies, and
  allowed omission or disclosure;
- `O`: importance, narrative, task, visual, programmatic, and focus orders;
  these may differ, so name which order the composition should express;
- `F`: target frames, intended size/distance, viewing sequence, fixed edges,
  incumbent system, and relevant crops;
- `A`: repeated anchors and alignment candidates: edge, axis, baseline, centre,
  contour, or optical relation;
- `P`: protected content, identity, source order, access floors, and deliberate
  character;
- `X`: stress content: shortest/longest text, unbreakable strings, missing or
  extra items, image-ratio extremes, data outliers, and supplied locales;
- `E`: available source, render, interaction, print, and human evidence, plus
  what remains unverified.

Translate the brief into a spatial thesis: primary entry, lead/support groups,
intended progression or task path, density, rhythm, negative-space jobs, and
protected adaptation behaviour. Treat any predicted scan path as a hypothesis,
not eye-tracking evidence.

## Generate and decide

1. **Order before coordinates.** Make required semantic and task order coherent;
   then decide visual entry, subordinate reads, and exit/action. Do not make all
   distinctions loud. Check whether hierarchy survives a thumbnail, blur, or
   colour-removal diagnostic as appropriate; these views diagnose structure,
   not audience behaviour.
2. **Relationships before values.** Group what shares meaning; separate changes
   in task, topic, status, or sequence; align where a common relation clarifies;
   offset where tension or distinction is intentional. Label intervals by job—
   within group, between groups, section, edge, sequence—not by one universal
   scale. Optical equality may override geometric equality when rendered masses
   differ.
3. **Choose the least-complex useful spatial system.** Derive candidate columns,
   modules, margins, spans, and recurring anchors from repeated units, longest
   measures, media ratios, alignment needs, and protected edges. Distinguish a
   conceptual design grid from a baseline grid, page geometry, or CSS layout.
   Use the grid to make relationships repeatable; break it only deliberately.
   When the spatial system is open, test a constant derived from the subject:
   product module, document format, data cadence, route, material unit or
   manufacturing tolerance. Mark its origin `supplied | measured | inferred |
   default`. A useful default is legitimate; settled geometry needs no new
   constant. Judge whether the relation improves content consequence, not
   whether it merely has an original rationale.
4. **Give negative space a job.** It may separate, group, frame, pace, direct,
   pause, or intensify. Empty area is not inherently premium; filled area is not
   inherently clutter. Tune density to information consequence, comparison,
   task, distance, medium, and concept.
5. **Build rhythm through expectation and variation.** Repeated anchors and
   intervals establish continuity; variation signals hierarchy, transition, or
   emphasis. Inspect macro rhythm across the frame and micro rhythm within
   groups. Do not repeat one spacing value until all relationships have equal
   weight.
6. **Compose with final-form content.** Use real text, labels, imagery, and data.
   Fit all declared `X` cases rather than an ideal placeholder. Never hide,
   crop, truncate, or reorder required meaning merely to make the frame clean.

## Working from content to geometry

For an open grid, place the longest required unit and a representative repeated
unit first. Compare a shared reading column with a lead/support split; keep the
split only if the support content still fits at its intended reading size. For
equal tracks inside usable width `W`, `n` tracks and gap `g` give
`track = (W - (n - 1) * g) / n`. This computes a chosen system, not the correct
track count. Derive spans from the content that must align, then test the most
demanding group before extending the grid.

Tune visual weight through a named variable: occupied area, size, tonal or hue
contrast, isolation, edge/axis position, or detail density. If a small dark
image overpowers a large pale heading, compare reducing the image's contrast
or area before enlarging every heading. Judge the whole frame again.

For a detached caption, compare its distance to its image with its distance to
the next group. Move the shared caption/image relation before changing all
page gaps. Check whether similarity or an enclosing box still implies the
wrong group. A deliberately remote caption can work when a clear reference
link preserves association. These are local comparison procedures, not fixed
spacing ratios or a requirement to replace a useful incumbent grid.

## Critique: signatures and causes

Run an unanchored whole-view assessment before overlays or measurements. Then
localise evidence. Geometry tools can point to a condition; they cannot decide
hierarchy, meaning, balance, or taste.

| Failure signature | Likely parent cause to test |
| --- | --- |
| Everything competes or nothing leads | content consequence unresolved; too many simultaneous hierarchy signals; scale/contrast range collapsed |
| Related items detach or unrelated items merge | spacing job wrong; proximity conflicts with similarity, enclosure, connection, or alignment |
| Layout feels arbitrary despite alignment | grid came before content; spans or anchors do not express semantic relations |
| Layout feels rigid or monotonous | every group uses the same interval, scale, alignment, or module without consequential variation |
| Trapped hole, dead margin, detached label, false group, or edge tension | negative space has no declared job; container or alignment relation is wrong |
| Dense work becomes cluttered, or sparse work becomes empty | hierarchy and grouping do not carry the chosen density; information consequence is mismatched to area |
| Tangency, near-alignment, collision, or accidental crop | parent container/span/crop is wrong, or a deliberate offset lacks enough separation to read as intentional |
| One fix produces many local nudges | canonical content order, container, measure, grid track/span, or shared spatial token remains wrong |
| Uniform card/bento grid or blanket centring | container preceded content relations; every unit received equal consequence and span |
| Identical section heights and rhythm | section library displaced argument order and content consequence |

Peer cards and repeated sections are valid when the content has those relations.
Otherwise rank consequence, regroup and vary span/density by the actual relation;
removing boxes or adding asymmetry alone does not repair the cause.

Name the perceptual cue behind a grouping judgment. Proximity, similarity,
common region, connection, continuity, and figure-ground can conflict; they are
context-bound hypotheses, not universal laws or aesthetic verdicts.

## Smallest repair and preservation

Freeze `P` before editing. Diagnose in this order, stopping at the first cause
that explains the failures: requirement/content -> semantic or order relation
-> container/measure -> grid/track/span -> scale/density -> crop/source ->
local optical correction. Repair the owning parent once and inspect every
consumer. Preserve successful hierarchy, asymmetry, rhythm, subject relation,
and recognisable character. Reject local nudges, blanket centring, extra cards,
more whitespace, clipping, or one-column stacking when they only conceal the
cause. Revert or narrow a repair that creates a new order, fit, access, crop, or
identity regression.

## Rules and exceptions

Binding requirements come only from the brief, incumbent system, applicable
standard, or actual platform/production authority. Grids, ratios, columns,
alignment, symmetry, scan patterns, spacing scales, and whitespace levels are
contextual mechanisms—not laws. Any numeric value must be labelled as supplied,
measured, standard-scoped, provider-specific, or a provisional hypothesis.

For off-grid placement, asymmetry, overlap, crop, irregular rhythm, or deliberate
density, declare before judgment: the broken convention, intended gain,
protected reading/access floors, stable counterstructure, accepted cost, and a
falsifier. Keep the exception when the whole gains and required meaning
survives; do not rationalise an accidental defect after seeing it.

## Proof, ownership, and claim ceiling

Inspect affected target frames at intended size. Include other supplied frames
when shared changes can affect them or the agreed proof requires them; add a
diagnostic thumbnail when hierarchy or density is in question.
Compare before/control/after under identical content, dimensions, crops, fonts,
assets, and renderer conditions. Check exact content, edges, overflow, group
relations, hierarchy, reading/order intent, critical `X` cases, and protected
regions. Use overlays or geometry only as annotated pointers and keep unrun
checks `unverified`.

Composition owns within-frame spatial relations. Typography owns type setting;
fixed-media design owns cross-page sequence; web design owns responsive
recomposition intent; UI owns framework implementation and runtime behaviour;
production and providers own technical/physical acceptance. Do not infer user
scan behaviour, comprehension, accessibility, cultural fitness, production
readiness, market preference, or universal quality.
