# Medium architecture question: responsive web and fixed print

Date: 2026-09-02  
Status: W-011 decision input; no runtime change

## Question

Should shared visual-design experts retain medium-specific branches, or should
the successor package add directly routed `web-and-responsive-design` and
`print-and-fixed-media-design` leaves?

The decision must preserve common design reasoning without pretending that a
responsive website and a fixed physical artifact are the same layout problem.

## Shared foundation

Keep these concerns medium-independent unless evidence shows otherwise:

- brief, audience, communication, concept, and required content;
- hierarchy, relationships, grouping, emphasis, and exceptions;
- type roles, voice, legibility/readability, and writing-system intent;
- colour roles, imagery thesis, art direction, style DNA, and ethics;
- critique method, preservation, causal repair, and evidence labels.

## Candidate web and responsive leaf

Potential ownership:

- content priority across widths rather than desktop-first shrinking;
- reflow, reorder, disclosure, density, navigation, and action persistence as
  design decisions;
- fluid type, spacing, measure, image crops, art-directed sources, and
  container relationships;
- continuity across desktop, tablet, mobile, zoom, text expansion, and
  orientation;
- static versus interactive/responsive evidence requirements;
- the canonical Design record that UI implements.

Boundary: Design owns intended transformation, priority, hierarchy, typography,
spacing, image behavior, and system decisions. Scoville UI owns framework
breakpoints, supported components, state semantics, focus/input behavior,
announcements, responsive mechanics, and rendered interaction proof.

## Candidate print and fixed-media leaf

Potential ownership:

- physical dimensions, viewing distance, fixed ratio, imposition context, and
  content density;
- page, spread, sequence, gutter/binding, fold, trim, bleed, safe zones, and
  finishing intent;
- typography and imagery at final physical size;
- substrate, ink/process, spot colour, overprint, black, trapping, resolution,
  and proof questions;
- fixed-media variants such as posters, editorial pages, packaging faces,
  signage, and handouts without collapsing their specialist limits.

Boundary: this leaf owns design and medium intent. Media production/handoff owns
preflight, export, file evidence, actual provider specifications, and proof
status. It cannot claim print readiness without the named supplier and physical
or provider-valid proof.

## Architecture options to compare

1. **Branches inside domain leaves.** Lowest route complexity; risks repeating
   web/print distinctions across typography, composition, colour, and imagery.
2. **Two direct medium leaves plus shared domains.** Better selective loading
   for web-only and print-only tasks; risks ownership duplication unless the
   medium leaves contain transformations and constraints rather than full
   restatements of typography/colour/layout.
3. **Responsive-web leaf plus editorial/fixed-production split.** Separates web
   clearly but recognizes that multi-page editorial logic is not reducible to
   generic print production; more modules and route combinations.
4. **Phase dossier only.** Keep current leaves and carry a medium contract
   through phases; lowest package growth but may not teach enough medium-
   specific behavior.

## Decision criteria

- Does the concern have an independent task signal?
- Can the leaf change an outcome without duplicating shared domain rules?
- Does it resolve observed failures in generation, critique, or repair?
- Does it preserve the Design/UI and design/production ownership boundaries?
- Can web-only, print-only, and cross-media tasks load the minimum sufficient
  set without hidden reference chains?
- Does the tested complete payload outperform a smaller branch-only or
  dossier-only mechanism?

## Required audit evidence

- composition, typography, colour, imagery, UI, and media-production audits;
- exact-domain web/responsive and print/fixed-media public Skill comparisons;
- source-backed Dos and Don’ts for each medium;
- one Terra High responsive recomposition case and one print/fixed-media case,
  executed one at a time only after a successor candidate exists;
- rendered multi-viewport evidence for web and final-size plus provider-bounded
  proof for print.

## W-013 resolution

The research and prior-art portion is discharged by the cross-domain audits and
two dedicated Stage-2 comparisons:

- [`web-and-responsive-design.md`](top-skill-comparisons/web-and-responsive-design.md)
- [`editorial-and-fixed-media-design.md`](top-skill-comparisons/editorial-and-fixed-media-design.md)

The comparisons support two direct medium leaves plus shared craft domains.
They do not establish visual superiority. Public Skills contribute content-
pressure inventories, comparison surfaces, final-context inspection, sequence
records, and format stress mechanisms. They do not justify fixed breakpoints,
device grids, font counts, layout templates, print numbers, or provider rules.

Responsive Design owns intended transformation; Scoville UI owns framework and
runtime mechanics/proof. Editorial/Fixed Media owns fixed context, sequence,
page/spread/fold/face and physical design constraints; Media Production owns
preflight, export, receiver and physical/provider proof. The W-012 Terra cases
C04, C05, C07, C08, C10, C14 and C18 remain the required applied/rendered
falsifiers; research completion does not substitute for them.
