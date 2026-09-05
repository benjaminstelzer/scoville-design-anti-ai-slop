# Comparative good/bad design references and test use

Date: 2026-09-01  
Purpose: determine which before/after, preferred/rejected, and critique sources
can inform or enter Scoville Design evaluation.

## Result

Yes: there is useful comparative material. The strongest sources are not all
usable in the same way. Third-party books, screenshots, comparison images, and
datasets are not stored in this repository. Repository records may cite them
and capture their license and methodological relevance. If a restricted source
is inspected during development, its local copy remains in a separate local
evaluation workspace outside the repository and is never published. The
decisive validation set consists of original, controlled pairs; only material
whose redistribution rights are independently verified may enter a public
fixture package.

## Source assessment

| Source | Comparison | Evidence value | Reuse decision |
| --- | --- | --- | --- |
| [Technical Writing: Basic Design](https://openoregon.pressbooks.pub/technicalwriting/chapter/basic-design/) | The same “A. Dawn Journal” web page before and after redesign; the chapter uses it to demonstrate alignment and usability. The chapter is CC BY 4.0 and identifies the paired image as CC BY 2.0. | Strong small didactic pair for alignment, proximity, hierarchy, and explaining a concrete repair. It is one author-selected example, not general proof of aesthetic superiority. | **Eligible with attribution and license receipt.** Preserve the source labels and test scoped observations, not a universal “after is beautiful” claim. |
| [W3C Before and After Demonstration](https://www.w3.org/WAI/demos/bad/) | The same fictional multi-page site in inaccessible and retrofitted accessible versions, with annotations and evaluation reports. | Excellent functional ground truth for headings, reading order, contrast, forms, keyboard access, and other documented accessibility barriers. It does not establish general visual taste. | **Use live or unmodified with attribution.** Most WAI material is under the W3C Document License, which permits copying complete documents but not derivative works. Prefer links or the complete official archive; create original synthetic analogues for mutable fixtures. |
| [Accessible University](https://projects.accesscomputing.uw.edu/au/) | The same fictional university page and documents before and after accessibility fixes, with issue explanations. | Useful second functional pair across web, Word, PDF, and PowerPoint. | **Reference-only for the commercial package.** CC BY-NC-SA 4.0 is incompatible with casually bundling modified fixtures in an MIT commercial Skill. |
| [Basics of Design: Layout & Typography for Beginners](https://books.google.com/books/about/Basics_of_Design_Layout_Typography_for_B.html?id=gTQKAAAAQBAJ), Lisa Graham | Side-by-side before/after page layouts with annotated strengths and weaknesses. | One of the clearest pedagogical models for teaching a critical eye and repair reasoning. | **Reference-only.** Commercial copyrighted book; do not copy pages, images, or annotations into the Skill or tests. |
| [Before and After Page Design](https://www.peachpit.com/store/before-and-after-page-design-9780201795370), John McWade | Before/after tutorials for publications, brochures, fliers, advertising, stationery, and business documents, explaining both how and why. | Excellent cross-format practitioner precedent for same-content redesign. | **Reference-only.** Copyrighted commercial material; use the method, not the artifacts or prose. |
| [Andrew Heiss flyer critique and redesign](https://datavizs22.classes.andrewheiss.com/example/02-example/) | A found flyer is critiqued and rebuilt in Canva and Illustrator, with final variants. | Useful trace of critique-to-revision and tool-independent reasoning. | **Reference-only by default.** Site content is CC BY-NC 4.0 and the original found flyer's rights are not established for redistribution. |
| [Apple RLDF designer-feedback dataset](https://github.com/apple/ml-rldf) | About 1,460 synthetic UI screenshots annotated by 21 professional designers via rankings, comments, sketches, and direct revisions; includes chosen/rejected screenshots and HTML plus improved variants. | Closest reviewed research model to the requested same-task better/worse and critique-to-revision evidence. It also demonstrates that comments and direct manipulation provide richer feedback than a single score. | **Method reference only.** The dataset license is CC BY-NC-ND 4.0; do not redistribute, adapt, or use as a commercial Skill fixture. |
| [TASTE](https://huggingface.co/datasets/purvanshi/TASTE) | Roughly 200 prompts, 1,000 generated design images, and 50,000 ranking rows; five outputs per prompt ranked by preference, typography, colour harmony/tone, hierarchy, and prompt fidelity. | Strong multi-dimensional pairwise calibration for general generated graphic design rather than UI alone. | **Potential external validation source.** Dataset is marked MIT, but its card warns that upstream image-generator terms may constrain output redistribution. Recheck each selected row/model and do not silently fold it into training or public fixtures. |
| [UICrit](https://github.com/google-research-datasets/uicrit) | 1,000 mobile UIs with enlarged release of 11,344 localized critiques and ratings; three annotators per screen. | Strong critique specificity, severity, localization, and disagreement reference; not same-brief before/after pairs. | **Eligible annotations under CC BY 4.0; screenshot rights require the underlying RICO terms.** Prefer annotation-shape calibration or independently licensed screens. |
| [Vibe Design Arena](https://huggingface.co/datasets/datapointai/vibe-design-arena) | All 1,770 pairs among 60 real web apps, with 30 human votes per pair, approximately 53,000 judgments. | Useful for checking whether a judge broadly tracks human visual preference and for measuring vote margin. Apps differ in content and purpose, so a win cannot identify a causal design rule. | **Supplement only.** Dataset is marked CC BY 4.0 but is access-gated; verify screenshot/source rights and terms. Do not use it as same-brief Gold. |
| [DesignPref](https://arxiv.org/abs/2511.20513) | 12,000 pairwise UI comparisons from 20 professional designers with preference strength and rationales. | Critical evidence against treating aesthetic preference as one objective label: reported binary agreement is low (Krippendorff's alpha 0.25) and rationales expose different priorities. | **Use the paper to design the rubric.** Dataset availability and reuse terms must be verified before any artifact use. Preserve rater disagreement rather than collapse it to false certainty. |
| [UIJudgeBench](https://github.com/gojiplus/uijudge-bench) | Frozen pages with machine-checkable accessibility/layout evidence and a defined pairwise design protocol. | Strong model for receipts, seeded mutations, separated task levels, frozen splits, and benchmark-defect handling. Its current design pilot pairs are explicitly unlabeled. | **Use the benchmark method, not unlabeled pilots as Gold.** Code is MIT; corpus uses source-specific licenses. Do not train on its public benchmark labels. |
| [GraphicDesignBench](https://github.com/lica-world/GDB) | Real graphic layouts across layout, typography, SVG, template, motion, and generation tasks. | Useful technical coverage for perception and production capabilities that preference-only datasets miss. | **Candidate technical comparator after dataset-license review.** Apache-2.0 covers the code, not automatically every underlying artifact. It is not a good/bad aesthetic oracle. |

## What the comparative sources teach

1. **Same task and content matter.** Cross-product popularity pairs confound
   content, brand, purpose, and implementation. Same-brief variants or seeded
   mutations isolate design judgment better.
2. **“Good” is multidimensional.** Function, accessibility, brief fidelity,
   hierarchy, typography, colour, concept, production, and preference can move
   in different directions.
3. **Critique must lead to a repair.** Before/after books are useful because
   they connect an observed problem to an intentional change, not because they
   offer a binary label.
4. **Aesthetic disagreement is data.** DesignPref reports low binary agreement
   even among trained designers. Tests need vote margins, rationales, and a
   valid “tradeoff/no decisive winner” outcome.
5. **Functional Gold is narrower but firmer.** W3C's BAD pair can establish
   specific accessibility failures. It cannot establish that its accessible
   version has the best art direction.
6. **License provenance is part of benchmark validity.** A public image and a
   downloadable dataset are not automatically safe to redistribute, modify,
   or use commercially.

## Recommended test design

### 1. Build original same-brief pairs

Create original fixtures with identical content, dimensions, audience, medium,
and constraints. Introduce one seeded change or a small interacting set per
pair. Record the exact source and expected effect. This yields reproducible
evidence without inheriting third-party artifact rights.

Pair classes:

- **functional mutation:** low contrast, broken reading order, missing label,
  clipped type, incorrect safe area, insufficient resolution;
- **craft mutation:** accidental misalignment, ambiguous grouping, flattened
  hierarchy, inconsistent type roles, uncontrolled spacing, arbitrary colour;
- **concept mutation:** generic decoration versus a subject-specific design
  idea with equally valid function;
- **production mutation:** RGB/CMYK assumption, bleed, crop, export, font or
  asset-license failure;
- **exception pair:** conventional competent version versus a deliberately
  broken grid, dense composition, expressive type, or ambiguity that remains
  functionally sound;
- **true tradeoff pair:** two strong but meaningfully different solutions for
  which no universal winner should be asserted.

### 2. Test three behaviors on separate cases

1. **Discriminate:** choose the stronger version by named dimension, or state
   that there is no evidence for a decisive winner.
2. **Critique:** localize the observed issue, state impact and confidence, and
   distinguish defect, tradeoff, preference, and intentional exception.
3. **Repair:** revise the weaker version while preserving brief, content,
   medium, existing owner, and intentional strengths.

A Skill that identifies the better screenshot but cannot produce the repair is
not qualified as a designer. A Skill that produces a clean result but cannot
explain what it changed is not yet a trustworthy critic.

### 3. Use independent evidence layers

| Layer | Ground truth |
| --- | --- |
| Constraint and accessibility | Exact brief, format requirement, license receipt, normative criterion, deterministic measurement |
| Layout and production | Seeded mutation receipt, computed geometry, browser/export inspection |
| Design judgment | Blind pairwise human review by declared rubric dimension, with vote margin and rationale |
| Intentional exception | Function survives, intent is legible, compensating structure exists, and blind review does not prefer the conventional version by default |
| Model critique | Region/element evidence and proposed repair match the actual rendered pair |

Automated aesthetic or VLM scores remain supporting evidence. They never
replace intended-context rendering and human judgment.

### 4. Prevent benchmark leakage

- Keep learning examples and public reference pairs outside sealed holdout.
- Do not put expected answers, comparator outputs, or holdout images in
  `SKILL.md` or routed references.
- Freeze original fixture hashes, mutation seeds, rubrics, split membership,
  and Skill hashes before SkillOpt proposals.
- Use `train` only for optimization, `valid_unseen` for promotion decisions,
  and a sealed non-optimization holdout for final qualification.
- Record and adjudicate a broken fixture separately; never rewrite Gold because
  the candidate disagreed.

### 5. Comparator suite

For the same frozen prompts and assets, compare no-Skill, Scoville Design,
Scoville UI fallback where applicable, composed Design+UI, and the strongest
relevant public Skill that can legally and technically run. Randomize display
order for human comparison. Report generation, critique, repair, routing,
framework conformance, and evidence honesty separately.

For landing pages, portfolios, and existing-site redesigns, the public suite
must include a commit-pinned Taste Skill v2 arm. Add its `gpt-taste` or
`image-to-code` variants only as separately named arms when the case matches
their declared mechanism. Exclude Taste Skill from general graphic, print,
packaging, and product-UI rankings outside its scope. Its examples and
self-reported production-test rules are comparator context, not qualification
Gold.

## Decision

Run the useful sourced pairs as a separate local external-material lane. Use
the A. Dawn Journal pair and W3C BAD material through source links or the
separate local evaluation workspace, not as vendored repository files. Use
TASTE, UICrit, Vibe Design Arena, Apple RLDF, or another dataset only after the
exact local evaluation/model-input/optimization use and output handling are
recorded. Permitted source- or human-labeled rows may enter SkillOpt Train but
never `valid_unseen`, sealed holdout, or qualification evidence. NC/ND material
remains unshared. Use commercial
before/after books, previews, and found-flyer work as human method and learning
references rather than copied fixtures. Original, source-cleared same-brief
pairs remain the decisive open Validation and independently sealed holdout.
No external fixture is committed merely because it is downloadable, and no
public report reproduces source material.
