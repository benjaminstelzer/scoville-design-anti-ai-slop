# SOL application baseline and payload ablation

Date: 2026-09-02  
Reviewer: one internal qualified reviewer  
Status: W-008 admission evidence, not product qualification

## Frozen scope

- Target and optimizer: `gpt-5.6-sol`, `xhigh`
- Host: local Codex desktop on Windows
- Network: disabled
- SkillOpt commit: `ba820b500f9da96685cf2780c7dc85ed4eb6563e`
- Renderer: local Chromium through Playwright; SVG viewport derived from the
  artifact's declared CSS dimensions or `viewBox`; HTML at 1440 px with a
  documented viewport fallback if a full-page capture exceeds browser limits
- Human evidence: one reviewer's intended-context visual judgment; no
  cross-person preference or market claim
- Holdout: not opened, rendered, or used

The benchmark and environment contract are frozen in
`docs/evaluation/preimplementation-freeze-v1.md`. Generated artifacts and
screenshots remain local evaluation output and are not package content.

## Arms and cost

| Arm | Skill tokens | Open cases | Hard results | Average total tokens | Interpretation |
| --- | ---: | ---: | ---: | ---: | --- |
| Neutral/no method | 64 | 15 | 14/15 | 40,005 | Base SOL prior knowledge |
| Core-only | 329 | 15 | 14/15 | 39,720 | Application loop without experts |
| Generic checklist | 195 | 15 | 14/15 | 39,746 | Conventional design-rule comparator |

The common 14/15 result is not a shared model failure. The presentation case
contains a hidden-key grader defect described below. The deterministic soft
score is mostly a prompt-size proxy and is not an aesthetic score.

Primary run IDs:

- `design-baseline-no-skill-train-r1`
- `design-baseline-core-only-train-r1`
- `design-baseline-generic-train-r1`
- `design-baseline-no-skill-val6-r1`
- `design-baseline-core-only-val6-r1`
- `design-baseline-generic-val6-r1`

Smoke run IDs:

- `design-baseline-no-skill-smoke-r1`
- `design-baseline-core-only-smoke-r1`
- `design-baseline-generic-smoke-r1`

## What SOL already did well

Across the open cases, all three arms produced strong examples of:

- original poster, editorial-page, information-design, presentation, motion,
  web, and UI composition;
- concrete critique of generic startup visual language and subject absence;
- preservation of an intentional grid violation when the brief documented the
  exception and compensating structure;
- useful typography diagnosis tied to audience, viewing distance, lighting,
  measure, alignment, contrast, fallback, and renderer uncertainty;
- art-direction systems with shot logic, crop planning, locality, consent,
  rights, anti-cliche controls, and production questions;
- recognizable 1980s computing, contemporary Neoclassical, and civic Brutalist
  directions without merely swapping palettes;
- information and motion systems whose data, timing, continuity, and reduced or
  static alternatives were explicit.

The neutral arm was often as strong as or stronger than prompted controls. The
generic checklist did not produce a repeatable advantage. This is evidence
against packaging broad textbook reminders, not proof that SOL has mastered the
long tail of any domain.

## Rendered findings

One reviewer inspected all extractable open artifacts at their declared size.
The most material observations were:

| Evidence ID | Arm/case | Observation | Disposition |
| --- | --- | --- | --- |
| SOL-B01 | Smoke poster | Neutral was the most energetic and information-rich; Core-only became more technical/dashboard-like; checklist was polished but more expected. | Do not treat more rules as better taste. |
| SOL-B02 | 80s web | All arms were professional and period-recognizable. Neutral was the most varied; none established a decisive method winner. | Use a compiler, not a style atlas. |
| SOL-B03 | Train poster repair | Core-only R1 emitted malformed SVG despite hard score 1.0; XML parsing failed at line 1, position 632. | Require source validation and rendered proof as a functional floor. |
| SOL-B04 | Data story | All were usable. Neutral clipped the title; checklist used less comfortable vertical labels; Core-only was clearest. | Preserve data/label floors; no aesthetic rule payload. |
| SOL-B05 | Annual report | All were professional; Core-only had the strongest editorial system, while checklist was clean but comparatively generic. | Report layout remains model knowledge plus production floors. |
| SOL-B06 | Clinic UI | Neutral was clearest in R1; Core-only collapsed a section heading; checklist invented operational-looking telephone details. | Design owns workflow judgment; UI/production must render and verify facts/states. |
| SOL-B07 | Neoclassical poster | All three were strong once rendered at the correct A2 viewport. | No style-history patch admitted. |
| SOL-B08 | Brutalist public-health page | All three were recognizable, direct, and accessible in structure. | No Brutalism recipe admitted. |
| SOL-B09 | Social crop repair | Neutral and checklist fit; Core-only R1 clipped right-side copy. | Keep cross-format fit/regression checks. |
| SOL-B10 | Motion storyboard | All three produced coherent six-frame data-to-title systems and static/reduced alternatives. | Motion production remains bounded; only the accessibility floor ships. |
| SOL-B11 | Presentation | Neutral was clean; Core-only R1 had overlapping labels and clipped recommendation copy; checklist clipped a small label. | Projection and render checks are mandatory; no repeated correction patch yet. |

## Repetition gate

The R1 production-integrity defects were retested with identical Core-only
inputs on three distinct tasks:

| Case | R1 | R2 | R3 | 2-of-3 failure? |
| --- | --- | --- | --- | --- |
| `design-train-04-poster-repair` | malformed SVG | clean | clean | no |
| `design-train-09-clinic-workflow-direction` | collapsed heading | clean | clean | no |
| `design-val-06-presentation-slide` | overlap/clipping | clean | clean | no |

Repeat run IDs use `design-core-production-<case>-r2` and `-r3`. XML/HTML
integrity and Playwright renders passed for all six repeated artifacts. The
failure family therefore does not satisfy the frozen threshold for a
SOL-specific correction or teaching payload. It still justifies a
model-independent `retained-floor` because editable validity, content fit, and
rendered verification are functional completion conditions.

## Payload ablation

Additional controls:

| Control | Skill tokens | Cases | Result |
| --- | ---: | --- | --- |
| Minimal style focus | 177 | 80s, Neoclassical, Brutalist | Three valid, professional outputs; no decisive advantage over neutral |
| Wrong expert: media floor | 127 | same three styles | Three valid, professional outputs; no style-specific degradation |
| Compact full bundle | 503 | 80s, typography critique, clinic UI | Valid and strong; no decisive advantage over smaller relevant or neutral context |

Run IDs:

- `design-style-focus-80s-r1`
- `design-style-focus-neoclassical-r1`
- `design-style-focus-brutalist-r1`
- `design-wrong-80s-r1`
- `design-wrong-neoclassical-r1`
- `design-wrong-brutalist-r1`
- `design-full-80s-r1`
- `design-full-type-r1`
- `design-full-ui-r1`

The expected-expert ablation did not measurably weaken the target dimension:
SOL remained stylistically capable even with no style method or the wrong
expert. The full bundle spent more context without a clear outcome gain. V1 may
therefore ship a bounded style compiler as a focus/stub, but no style-history
or named-style teaching patch is behaviorally admitted.

## Benchmark defect quarantine

`design-val-06-presentation-slide` told the model only that
`data_integrity` and `projection_checks` must be Boolean-valued objects. The
grader silently required exact keys such as `all_values_preserved` and
`large_text`. All three arms preserved every required datum and reported valid
Boolean checks under different descriptive keys, yet all failed
`expected_json_subset`.

This case is quarantined for deterministic score aggregation in suite v1. Its
artifacts remain usable for symmetric visual review. The frozen item is not
edited retroactively; a corrected contract requires a new suite version.

## Admission consequence

No topic-specific teaching payload met the behavioral admission bar. No domain
met the stronger zero-critical-failure reliability bar across three tasks and
three parity runs. V1 therefore uses:

1. a compact Core for ownership, modes, synthesis, exception discipline, and
   the make-inspect-repair loop;
2. source-bound `retained-floor` modules for accessibility, truth, rights,
   data, production, current verification, and rendered evidence;
3. bounded focus/stub modules that invoke SOL's demonstrated prior knowledge
   without restating a design curriculum;
4. no broad style atlas, numeric recipe catalogue, or full-bundle default.

This is an implementation decision, not a claim that the resulting Skill is
already qualified. W-005 still owns blinded outcome review and the sealed
holdout.
