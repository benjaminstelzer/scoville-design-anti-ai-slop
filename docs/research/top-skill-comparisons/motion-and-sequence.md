# Stage-two Skill comparison: Motion and sequence

Date: 2026-09-02
Capture: 2026-09-02T13:41:58Z
Target: `references/motion-and-sequence.md` and its expert-depth audit
Method: `reference-audit-method.md`, Stage two

Local baselines: [current executable reference](../../../references/motion-and-sequence.md),
[expert-depth audit](../reference-audits/motion-and-sequence.md), and
[medium architecture decision](../medium-architecture-question.md)

This is a bounded current GitHub and public-Skill comparison. It searched
motion design, interaction motion, animation direction, kinetic typography,
storyboarding, sequence design, web motion, and motion production. A candidate
qualified only when an exact Skill or directly usable exact motion instruction
and an E1 or higher artifact were inspectable. Stars rank the qualifying
repositories. They do not rank the exact Skill or prove motion quality.

## Decision

The three qualifying repositories found are `pbakaus/impeccable`,
`remotion-dev/remotion`, and `MengTo/Skills`. Impeccable has the strongest
direct interaction-motion framing and reproducible checks, but those checks
detect a narrow set of CSS policies rather than evaluating motion craft.
Remotion has the strongest deterministic timeline and final-render mechanism,
but it is framework implementation under a bespoke license, not a general
motion Design owner. MengTo provides the strongest source-capture and
runtime-measurement workflow, but its included demo is a static handoff
artifact.

None of the top three includes a convincing rendered sequence, frame strip,
kinetic-type specimen, storyboard-to-output trace, multi-viewport interaction
recording, or independent motion review. None visibly proves better temporal
typesetting, spatial rhythm, negative-space choreography, hierarchy,
subject-specific composition, responsive preservation, or reduced-motion
equivalence than the current Scoville audit.

Retain one deeper `motion-and-sequence` Design leaf. Do not split interaction
motion, kinetic type, and storyboard yet because the common sequence, timing,
continuity, accessibility, and proof contract is larger than the specialist
differences. Design owns temporal meaning and judgment. UI or Code owns live
state, DOM, focus, input, preferences, cancellation, and runtime performance.
Media owns codec, export, asset, render, and delivery proof.

## Qualification and star ranking

E1 is an inspectable example or output artifact. E2 is a reproducible test,
evaluation, or deterministic check. E3 requires independent evaluation or
external adoption evidence that supports capability. No ranked candidate has
E3 evidence. Repository stars and public installation counts remain
popularity signals only.

| Rank | Repository and exact path | Stars at capture | Pin, activity, and relevant update | Exact license and asset status | Evidence level and what it proves |
| --- | --- | ---: | --- | --- | --- |
| 1 | [`pbakaus/impeccable`, `.agents/skills/impeccable/reference/animate.md`](https://github.com/pbakaus/impeccable/blob/c0f495212236129c2e92aaf7714a3a9914569d13/.agents/skills/impeccable/reference/animate.md) | 64,879 | Active, not archived. Repository pin `c0f495212236129c2e92aaf7714a3a9914569d13`. The exact command last changed in [`5d10bc842cbccd2ae7d3a88296d87d3be0b125b3`](https://github.com/pbakaus/impeccable/commit/5d10bc842cbccd2ae7d3a88296d87d3be0b125b3) on 2026-08-08. Repository pushed 2026-09-02. | Root [Apache-2.0](https://github.com/pbakaus/impeccable/blob/c0f495212236129c2e92aaf7714a3a9914569d13/LICENSE). The motion fixture is repository-authored. The wider demo uses externally delivered fonts whose licenses remain separate. No separate motion-data or motion-asset license was found. | **E2.** CSS motion fixtures and tests reproducibly detect named bounce or elastic curves and transitions of selected layout properties. They prove detector behavior for those rules. They do not prove authored motion quality, continuity, reduced-motion equivalence, performance, WCAG conformance, kinetic type, storyboard quality, or independent preference. Tests were inspected, not executed here. |
| 2 | [`remotion-dev/remotion`, `packages/skills/skills/remotion-markup/SKILL.md`](https://github.com/remotion-dev/remotion/blob/1d904f1ff6bfab045f395efe547a00b80ef86db2/packages/skills/skills/remotion-markup/SKILL.md) with [`remotion-render/SKILL.md`](https://github.com/remotion-dev/remotion/blob/1d904f1ff6bfab045f395efe547a00b80ef86db2/packages/skills/skills/remotion-render/SKILL.md) | 58,095 | Active, not archived. Repository pin `1d904f1ff6bfab045f395efe547a00b80ef86db2`. `remotion-markup` last changed in [`af717290f3561232a4597825cbd828e236ed8144`](https://github.com/remotion-dev/remotion/commit/af717290f3561232a4597825cbd828e236ed8144) on 2026-09-01. Repository pushed 2026-09-02. | Root [Remotion License](https://github.com/remotion-dev/remotion/blob/1d904f1ff6bfab045f395efe547a00b80ef86db2/LICENSE.md), reported by GitHub as `NOASSERTION`. Individuals, eligible small organizations, nonprofits, and evaluation have stated free-use rights. Other for-profit organizations require a Company License. Derivative resale or relicensing is restricted. No separate license was found for the exact Skill files or bundled Remotion icon. External fonts, media, maps, data, and Lottie assets retain separate rights. | **E1.** The exact Skill contains runnable React examples and detailed files for animation, timing, sequencing, transitions, text measurement, fonts, captions, media, multi-scene composition, and final rendering. They prove concrete framework implementation guidance. The repository has extensive product tests and showcases, but no trace was found that attributes a rendered motion artifact or independent quality result to this exact Skill. Skill capability remains E1. |
| 3 | [`MengTo/Skills`, `agent-skills/codex/html-to-interaction-prompts/SKILL.md`](https://github.com/MengTo/Skills/blob/321c769739b823de5eb94eb3a52aa1974fe783a2/agent-skills/codex/html-to-interaction-prompts/SKILL.md) and [`agent-skills/codex/optimize-web-animations/SKILL.md`](https://github.com/MengTo/Skills/blob/321c769739b823de5eb94eb3a52aa1974fe783a2/agent-skills/codex/optimize-web-animations/SKILL.md) | 5,727 | Active, not archived. Repository pin `321c769739b823de5eb94eb3a52aa1974fe783a2`. Both exact Skills last changed in [`a3d017f3cf1b9e04695be434593d66b2ed1ae900`](https://github.com/MengTo/Skills/commit/a3d017f3cf1b9e04695be434593d66b2ed1ae900) on 2026-07-07. Repository pushed 2026-08-28. | Root [MIT](https://github.com/MengTo/Skills/blob/321c769739b823de5eb94eb3a52aa1974fe783a2/LICENSE). The included demo HTML, JPEG preview, input, and expected output are repository-authored with no separate notice. Captured third-party websites, video, screenshots, fonts, and product assets retain source-specific rights that the repository license cannot grant. | **E1.** Both Skills include static HTML, JPEG, prompt, input, and expected-output demo artifacts. They prove a concrete capture or performance handoff shape and responsive demo composition. The exact demos contain no motion recording, profiler trace, executed optimization, or before-and-after sequence, so actual motion and performance remain unproved. |

## Candidate 1: Impeccable `animate`

### Claimed scope and observed mechanism

The direct command starts from a motion job rather than an effect. It asks for
one focal sequence, continuity needs, feedback needs, and an effect budget.
Motion may carry more voice in persuasion or experience surfaces, while
operational and reading surfaces prioritize state, feedback, and continuity.
Property choice follows meaning such as relationship, focus, reveal, material,
or state. Implementation guidance prefers the incumbent runtime and asks for
interruption, repeated use, target-device performance, and an intentional
`prefers-reduced-motion` branch.

The E2 evidence is narrower than the instruction. The
[`motion.html` fixture](https://github.com/pbakaus/impeccable/blob/c0f495212236129c2e92aaf7714a3a9914569d13/tests/fixtures/antipatterns/motion.html)
and [`detect-antipatterns-fixtures.test.mjs`](https://github.com/pbakaus/impeccable/blob/c0f495212236129c2e92aaf7714a3a9914569d13/tests/detect-antipatterns-fixtures.test.mjs)
check two bounce or elastic cases and eight selected layout-transition cases.
The wider unit tests also check textual detection. They do not execute an
authored sequence or assess meaning, pacing, continuity, interruption, access,
or visual quality. The inspected landing demo has a simple button transition,
not a focal motion artifact.

### What is better than the current Scoville reference

- A motion thesis explicitly separates focal authorship, continuity,
  feedback, and performance budget.
- Visitor mode changes the amount and job of motion instead of applying one
  product-animation norm everywhere.
- Property choice is connected to meaning. Transform and opacity are framed as
  foundations rather than the complete design vocabulary.
- Script failure cannot hide default content, and interruption, repeated use,
  target-device measurement, and dependency restraint are explicit.
- Supporting motion is tested by asking what meaning or authored character is
  lost when it is removed.

### Reject or revise

- The duration table, one named easing curve, faster-exit rule, and stagger
  posture are contextual starting points, not Design requirements.
- A detector that rejects bounce by name or overshoot curve cannot know brand,
  object material, accessibility context, gesture physics, or intentional
  character. Treat it as a review pointer, never a quality gate.
- Selected layout-property transitions can be expensive, but property name
  alone does not prove poor performance. Measurement on target hardware and
  browsers must decide.
- The command is interaction-web centered. It does not cover storyboards,
  kinetic typesetting, script-specific shaping, reading holds, frame-safe
  composition, edit rhythm, audio, export, or final-media proof.
- It mentions autoplay, sound, offscreen loops, and reduced motion but omits
  the exact WCAG Level A conditions for long automatic motion and flashing.

## Candidate 2: Remotion markup and render Skills

### Claimed scope and observed mechanism

`remotion-markup` is exact implementation guidance for frame-driven video in
React. It requires motion to derive from `useCurrentFrame()`, explicit frame
ranges, interpolation, easing, and composition timing rather than browser CSS
transitions that a deterministic video renderer may not reproduce. Supporting
files cover sequencing, transitions, text measurement, local and web fonts,
captions, Lottie, images, audio, video, multi-scene composition, effects, and
final rendering. `remotion-render` turns the composition into a concrete media
artifact.

The inspectable E1 examples are unusually executable. They show frame-based
opacity, scale, translation, rotation, clamping, easing, media placement, and
scene composition in actual React. This demonstrates a usable framework
mechanism. It does not show that the exact Skill generated the repository's
showcase videos, that its example composition is visually strong, or that an
independent reviewer preferred its motion.

### What is better than the current Scoville reference

- The frame clock, sequence ranges, composition duration, and final renderer
  form one deterministic time authority.
- Text measurement, font loading, captions, media duration, and final render
  are concrete production concerns rather than vague handoff notes.
- Browser-only CSS animation is rejected for a renderer-specific reason, not
  as a general aesthetic ban.
- Multi-scene composition, transitions, media, effects, and export share one
  implementation model.
- The final media file can be rendered and inspected instead of stopping at a
  source or browser preview.

### Reject or revise

- Remotion is a React video-rendering dependency, not the owner of interaction
  motion, responsive web behavior, story, pacing, or visual judgment.
- Inline interpolation, transform shorthands, component names, file placement,
  frame APIs, and render commands are framework instructions. They belong in
  Code or Media after Design chooses the sequence.
- Worked values, example easing, frame counts, type sizes, centered
  composition, and one code structure cannot become motion-design recipes.
- Fixed-resolution video composition is not responsive UI proof. Alternate
  aspect ratios, captions, platform overlays, safe areas, localization, and
  crop changes need explicit redesign and final-render evidence.
- The bespoke Remotion License is not an MIT-like default. Eligibility,
  company licensing, redistribution restrictions, bundled icons, fonts,
  media, maps, data, and third-party assets require separate review before
  dependency or source reuse.
- Repository tests prove the framework and packages, not the visual quality or
  routing accuracy of the exact Skill. Repository use does not establish Skill
  adoption.

## Candidate 3: MengTo interaction capture and animation optimization

### Claimed scope and observed mechanism

`html-to-interaction-prompts` reverse-engineers interaction ideas from HTML or
a live page. It asks the agent to inspect source behavior, capture actual live
states, record video when required, extract representative motion frames, keep
source metadata, and turn each distinct interaction into a portable prompt.
The strongest provenance rule rejects marketplace covers, screenshot pans, and
static slideshows as evidence of live-site motion.

`optimize-web-animations` owns a separate runtime problem. It profiles top,
middle, lower, and narrow states, counts running CSS animation, inspects canvas
and WebGL loops separately, records bounded idle and route-cycle evidence,
pauses offscreen work, cancels RAF, removes listeners, disconnects observers,
disposes resources, and reruns the same measurements. The
[`demo/index.html`](https://github.com/MengTo/Skills/blob/321c769739b823de5eb94eb3a52aa1974fe783a2/agent-skills/codex/optimize-web-animations/demo/index.html)
is a responsive static input-and-output card. It contains no animation or
performance measurement. Its visual polish cannot support a motion claim.

### What is better than the current Scoville reference

- Captured source behavior wins over inference from one still image.
- A still, recording, frame sample, actual page URL, source metadata, and
  fallback reason form distinct evidence fields.
- CSS animation, pseudo-elements, canvas, WebGL, RAF, timers, listeners,
  observers, media, and route cleanup have separate runtime checks.
- Baseline and after measurements use the same route and positions, which
  makes repair evidence comparable.
- Reduced motion and offscreen behavior are checked alongside ordinary
  playback instead of added only after visual approval.

### Reject or revise

- Exactly five inspirations, prescribed article sections, fixed image counts,
  exact crop structures, two-second waits, and named library menus are one
  publication workflow, not general motion-design rules.
- Extracting effects from a reference does not authorize copying expressive
  choreography, assets, trade dress, or source text. Scoville must synthesize
  from mechanisms and retain a rights record.
- `offscreenRunningCount: 0` is appropriate only for the named tested scope.
  It cannot become a universal ban on background work that remains necessary
  and proven.
- A screenshot or static demo proves neither playback nor performance. CPU,
  memory, frame pacing, cancellation, input, and export require their own
  evidence.
- The Skills offer little authored temporal hierarchy, kinetic typography,
  storyboard logic, line-break control, reading holds, loop design, or
  sequence-level critique.

## Unranked craft cross-check: LottieFiles `motion-design`

`LottieFiles/motion-design-skill` had 1,494 stars and therefore ranked below
the three qualifiers. Its exact
[`skills/motion-design/SKILL.md`](https://github.com/LottieFiles/motion-design-skill/blob/f9a8a041b85185ee4881b3471d3415e939aac772/skills/motion-design/SKILL.md)
is active, pinned at `f9a8a041b85185ee4881b3471d3415e939aac772`,
and uses [MIT](https://github.com/LottieFiles/motion-design-skill/blob/f9a8a041b85185ee4881b3471d3415e939aac772/LICENSE).
The exact Skill last changed in `b6606e101601ef027f01729a7289e97c329ad0cd`
on 2026-03-12. Its E1 director, pattern, reference, troubleshooting, and
worked recipe files prove breadth and recipe specificity. No rendered output,
motion file, frame strip, test, evaluation, or independent review was found.

### Claimed scope and observed mechanism

The Skill organizes motion around purpose, emotion, physics, narrative, and
choreography. Its director files cover personality, four-act micro-stories,
primary and supporting movement, counter-motion, paths, attention, depth, and
context. Pattern files cover entrances, exits, feedback, ambient loops, and
multi-element sequences. Reference files supply duration, easing, spring,
stagger, property, troubleshooting, performance, and accessibility tables.

The useful mechanism is that a sequence has a target emotion, primary action,
supporting reaction, resolution, and settled state. This creates a temporal
hierarchy that can be inspected beat by beat. The problem is that the Skill
turns nearly every judgment into a numerical or categorical prescription. No
artifact shows those prescriptions producing a strong result.

### What is better than the current Scoville reference

- Motion personality, narrative phase, property, path, temporal hierarchy,
  interaction frequency, and resolution are considered together.
- Worked examples expose choreography decisions rather than stopping at an
  easing token.
- The pattern set includes entry, exit, feedback, ambient, loop, and
  multi-element cases.
- The quality checklist at least separates visual, technical, emotional,
  performance, and accessibility questions.
- “Appropriate on the hundredth viewing” is a useful frequency stress question
  for recurrent interaction motion.

### Reject or revise

- Reject fixed duration bands, distance multipliers, entrance-to-exit ratios,
  stagger budgets, overshoot percentages, spring values, element sizes,
  element counts, frame-rate allowances, and personality tables as universal.
- Reject “always three motion layers,” “never opacity-only,” “never linear for
  spatial movement,” the one-third distance and density rules, and mandatory
  counter-motion or Disney-principle application.
- Emotion-to-motion labels such as curved equals friendly or vertical equals
  growth are cultural and contextual hypotheses, not semantic facts.
- The Apple and Material curve names, performance statements, and WCAG-like
  rules lack exact source bounds in the Skill. They must not enter Scoville as
  authority by citation through the candidate.
- “Animations over five seconds are pausable” is an imprecise conformance
  summary. The normative trigger depends on automatic start, duration,
  presentation alongside other content, and essentiality.
- No kinetic-type, script, localization, responsive, storyboard, output, test,
  or final-render evidence supports the breadth claims.

## Weighted adoption comparison

| Required concern | Impeccable | Remotion | MengTo | Current Scoville position and decision |
| --- | --- | --- | --- | --- |
| Motion thesis and subject fit | Strong focal moment, continuity, feedback, budget, and visitor-mode framing. | Primarily implementation. The exact Skill does not derive a story or subject-specific motion thesis. | Extracts interaction mechanisms from a real source, but mainly for reuse prompts and optimization. | Adapt the Impeccable thesis fields. Keep Brief, Concept, and Style responsible for subject-specific meaning. Reject generic effects and framework defaults. |
| Temporal hierarchy and sequence | One focal sequence plus quiet support, with no worked sequence artifact. | Strong deterministic frame, sequence, transition, and composition mechanics. Craft rationale is limited. | Motion frames and section handoffs are requested, but the included demo is static. | Keep primary, supporting, transition, and stillness roles. Each beat needs content, job, duration rationale, reading hold, overlap, and settled state before implementation chooses frames. |
| Continuity, interruption, and recovery | Strong on shared elements, dynamic runtime, interruption, and repeated use. | Deterministic prerecorded sequence, not a live interaction model. User cancellation, reversal, input races, and partial state are outside its main path. | Strong on live-source capture, RAF control, route cleanup, offscreen stop and resume. | Motion Design specifies what remains continuous and what cancel, reverse, interruption, and repeated activation communicate. UI or Code proves live state and cleanup. Media proves fixed playback. |
| Kinetic typography | No specialist mechanism. | Provides frame timing, text measurement, fonts, captions, highlighting, and render mechanics, but no specialist shaping or kinetic craft evidence. | Captured text effects can be described, but no kinetic-type demo exists. | Current audit is stronger. Test actual copy, language, shaping, fallback, line breaks, safe areas, entry, lock, emphasis, exit, bridge, readable holds, reduced/static equivalence, and export. |
| Typography, spacing, and negative space | The wider package has separate type and layout commands. The exact motion evidence does not show them surviving time. | Can measure text and load exact fonts. Its code examples do not prove typesetting, spacing rhythm, or composition quality. | Static demo shows hierarchy and responsive columns, not temporal typography. | Each frame and transition must preserve type roles, group relationships, quiet zones, edge clearance, negative-space purpose, and intended reading order. Motion cannot repair a weak still composition. |
| Storyboard and cross-medium sequence | No storyboard contract. | Multi-scene code and render contract are strong, but no general storyboard, interaction, or editorial decision method is supplied. | Evidence capture can provide frames and videos, but not an authored storyboard. | Retain one shared beat and frame contract for UI interaction, kinetic type, storyboard, and fixed media. Media adds shot, codec, audio, export, and delivery fields only when active. |
| Responsive and format translation | Names desktop, mobile, and target devices without a transformation record. | Fixed composition sizes and renderer output are not responsive behavior. Alternate ratios require separate design and render decisions. | Strong source captures and a static demo from 390 to 1440 px, but no motion at those widths. | Record what motion, type, crop, order, hold, safe area, input, and continuity preserve or change by viewport, container, ratio, platform, and reduced setting. |
| Loops and endings | Nonessential loops should stop offscreen or hidden. Seam, end-state, and replay logic are limited. | Explicit frame duration and final render make fixed endings testable. Live pause, replay, visibility, and loop control depend on the delivery player. | Strong operational stop, resume, visibility, and cleanup checks. | Every loop needs purpose, seam, interruption, stop control, resource policy, end state, replay behavior, and static equivalent. Decorative autoplay requires a deletion test. |
| Accessibility and control | Intentional reduced path, autoplay and sound awareness, offscreen stop. No exact flash rule. | Caption mechanics help media access. The exact motion guidance does not establish WCAG scope, player control, flash safety, or reduced equivalence. | Reduced motion and control are operational concerns. No exact flash threshold or static-equivalence proof. | Keep exact WCAG scope and a stricter product baseline where justified. Conformance, preference, equivalent information, captions, player controls, and comfort are separate questions. |
| Runtime and production proof | E2 detector fixtures, no sequence or performance result. | Strongest deterministic implementation and final-render route, with E1 Skill examples and extensive framework tests that do not prove Skill output quality. | Best baseline and after measurement procedure. E1 static artifact only. | UI or Code owns live frame pacing, cleanup, input, focus, cancellation, and preferences. Media owns render, codec, colour, audio, caption, platform, and final-file proof. |
| Visible quality | No motion artifact. | Repository showcases are not attributable outputs of the exact Skill. The exact examples are source code, not a reviewed motion artifact. | No motion artifact in the exact demos. | No candidate visibly proves superior temporal type, spacing, negative space, hierarchy, composition, continuity, or reduced equivalence. |

## WCAG scope correction

Candidate checklists must not be used as conformance authority. The exact web
scope is:

- [WCAG 2.2 SC 2.2.2, Level A](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)
  requires a pause, stop, or hide mechanism for moving, blinking, or scrolling
  information that starts automatically, lasts more than five seconds, and is
  presented alongside other content, unless essential. Automatic updating has
  a related but separate condition and no five-second exception.
- [WCAG 2.2 SC 2.3.1, Level A](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html)
  prohibits more than three flashes in any one-second period unless the flash
  remains below the general and red-flash thresholds. Test the largest
  delivered viewing condition, including full screen when available.
- [WCAG 2.2 SC 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)
  is Level AAA. Motion animation triggered by interaction can be disabled
  unless essential to function or information. It must not be cited as a
  universal Level AA requirement.
- `prefers-reduced-motion` is a useful input, not complete evidence. The
  alternative must preserve state, relationship, feedback, reading, and task
  information without merely freezing a confusing intermediate frame.
- A product may set a stronger baseline than WCAG, including an intentional
  reduced path for all nonessential motion. Label that as product policy, not
  as the normative wording of a success criterion.

## Specialist cross-check outside the top three

`geekjourneyx/hyperframes-motion-director` had 433 stars, so it does not enter
the top-three star ranking. Its exact
[`skills/hyperframes-motion-director/SKILL.md`](https://github.com/geekjourneyx/hyperframes-motion-director/blob/0b66750322ccb50ae56ace5a8d361da2c1f65400/skills/hyperframes-motion-director/SKILL.md)
is nevertheless the strongest inspected architecture for kinetic type and
storyboard production. It is active, pinned at
`0b66750322ccb50ae56ace5a8d361da2c1f65400`, and uses
[AGPL-3.0](https://github.com/geekjourneyx/hyperframes-motion-director/blob/0b66750322ccb50ae56ace5a8d361da2c1f65400/LICENSE).

Its E2 artifacts include structured evaluations, a storyboard template, beat
and motion-map templates, validators, release tests, asset manifests,
snapshots, final-render evidence, and a review-pack builder. The useful
mechanisms are source phrase to visual object mapping, keyword and action
object relay, entry-lock-emphasis-exit-bridge fields, readable holds,
transition-midpoint snapshots, deletion tests, visible-alpha bounds, composite
ownership, and final MP4 precedence over browser preview.

Adopt those mechanisms only through original synthesis. Do not copy the AGPL
Skill, code, templates, or tests into a differently licensed package. Reject
its default Simplified Chinese, 9:16, 1080 by 1920, black cinematic style,
first-two-second hook, three independent component minimum, mandatory
component-sheet posture, 100-point relay score, and pass threshold as general
motion rules. The candidate has excellent production structure but still no
included finished video or independent review that proves the score predicts
quality.

The lower-star `mblode/agent-skills` `ui-animation` Skill provides a useful
interaction-motion owner boundary and synthetic evaluation fixtures. It does
not displace the top three by stars. `LottieFiles/dotlottie-web` had 866 stars
but is a runtime and file-format implementation repository, not an exact
motion-direction Skill. Its tests cannot substitute for motion Design proof.

## Architecture and mechanisms to synthesize

1. Write a motion thesis with message, viewer or user job, focal sequence,
   continuity spine, feedback, character, medium, frequency, performance
   budget, reduced/static requirement, and removal test.
2. Build a beat record from actual content. Each beat names content, primary
   and supporting motion jobs, entry, readable hold, emphasis, exit, bridge,
   overlap, settled state, and why the time is sufficient. No duration table
   can replace content-specific reading and perception checks.
3. Build a motion map for element identity, trigger, origin, path, relation,
   occlusion, crop, group ownership, interruption, cancel, reverse, repeated
   activation, route change, and end state.
4. For kinetic type, test the actual script, shaping, glyphs, fallback, line
   breaks, case, punctuation, captions, safe areas, encoding, and final
   renderer. Record entry, lock, emphasis, exit, bridge, and reduced/static
   equivalence for every required phrase.
5. Treat static frames as composition gates. Inspect type hierarchy, spacing
   relations, quiet zones, negative-space job, crop, alignment, edge tension,
   and subject recognition before animation. Then inspect transition
   midpoints, not only hero frames.
6. Give every loop a purpose, seam, stop condition, user control, visibility
   behavior, resource policy, end state, replay behavior, and deletion test.
7. Separate evidence lanes. Source and storyboard prove intent. Browser or
   runtime traces prove interaction mechanics and performance. Frame strips and
   recordings prove visible motion. Final exports prove media delivery. User
   evidence proves only the population and task actually studied.
8. Require reduced and static variants from the first storyboard. Compare
   information, hierarchy, state, task, and identity rather than only the
   number of moving pixels.

## Failure to cause to repair tests

| Failure | Likely cause to test | Repair move | Evidence that can disprove the repair |
| --- | --- | --- | --- |
| Everything moves at once | No temporal hierarchy or protected reading hold | Keep one primary job, sequence support by causal relation, and add deliberate stillness | Frame strip and normal-speed review still show competing targets or unread content |
| Sequence feels like slides | Repeated fade, identical composition, no continuity carrier, or no state change | Add a subject-specific handoff, transformation, shared element, mask, crop, or deliberate hard cut | Removing the new bridge changes no understanding or the still frames remain interchangeable |
| Interaction teleports | Persistent object identity is lost between states | Preserve identity, origin, direction, and settled destination or use a deliberate cut with another orientation cue | Reversal, cancellation, keyboard use, or repeated activation reveals duplicate or incoherent states |
| Kinetic text is unreadable | Holds ignore actual copy, shaping, line breaks, size, safe areas, or export | Shorten or restructure copy, revise roles and breaks, and retime using the final renderer | Native-reader review, captions, frame strip, or platform crop still loses text |
| Motion feels generic | Effect was chosen before subject, product action, or style mechanism | Define a focal action and material idea tied to the subject, then remove unrelated effects | The same sequence can be relabeled for an unrelated subject without loss |
| Reduced mode loses meaning | Full motion carried state or relationship with no equivalent | Replace displacement with a stable state change, concise crossfade, direct update, or static sequence | Reduced users cannot identify cause, destination, progress, completion, or error |
| Loop distracts or wastes resources | No stop policy, seam, frequency rationale, or visibility control | Shorten, stop, pause, make user-controlled, or remove the loop | SC 2.2.2 conditions, target-device traces, or repeated-use review still fail |
| Motion is smooth but weak | Runtime performance was treated as design quality | Revisit hierarchy, pacing, still composition, consequence, and subject specificity | A smooth recording still lacks a clear focal path or task consequence |

## Reject from the executable package

- universal duration, easing, spring, stagger, overshoot, displacement,
  element-count, frame-rate, and layer-count recipes
- “motion must only clarify” and “motion may always decorate” as opposing but
  equally rigid rules
- bounce, parallax, scroll, opacity, transform, cards, fades, masks, or hard
  cuts treated as inherently good or bad
- a first or last frame treated as the static or reduced equivalent without
  information and task comparison
- screenshots treated as motion, performance, interruption, access, or export
  proof
- `prefers-reduced-motion` treated as full accessibility or WCAG conformance
- SC 2.3.3 described as a Level A or AA universal rule
- videos, fonts, screenshots, website captures, music, libraries, and generated
  assets assumed to inherit a repository license
- framework dependencies, browser tooling, render engines, or one media format
  made mandatory for Design ownership
- candidate prose, AGPL code or templates, fixed scoring rubrics, and asserted
  platform standards imported without primary-source verification

## Search exclusions and limits

- `anthropics/skills` and other high-star general repositories were not ranked
  when only broad frontend, GIF, slide, or video-production instructions were
  found without an exact motion-direction artifact.
- `LottieFiles/dotlottie-web` is a well-tested player/runtime, not a substitute
  for motion thesis, storyboard, kinetic typography, choreography, or reduced
  equivalence.
- `iart-ai/motion-skills` is primarily a catalog. Its repository stars and
  descriptions do not provide exact candidate evidence by themselves.
- Lower-star exact Skills such as HyperFrames, Mblode `ui-animation`,
  `soilmass/motion-design-agent`, `black12-ag/claude-skill`, and SkillMe motion
  entries were inspected or search-matched but did not outrank the top three by
  repository stars.
- Search used GitHub repository, commit, tree, and contents APIs, GitHub and web
  search, and skills.sh on 2026-09-02. Authenticated GitHub code search was
  rate-limited during the session. Private, renamed, deleted, service-hosted,
  recently published, and poorly indexed Skills may be absent. The result is
  current and bounded, not globally exhaustive.
- The cheapest decision-changing next evidence is a shared motion brief with
  one UI state transition, one interruptible gesture, one localized kinetic
  phrase, one finite narrative sequence, one loop, one narrow or alternate
  format, one reduced version, and one static version. Compare authored output
  at normal speed, frame strips, source behavior, target-device traces, exact
  WCAG checks, and final export. Blind reviewers should score meaning,
  continuity, reading, typography, spatial rhythm, negative space, hierarchy,
  subject fit, interruption, reduced equivalence, and evidence honesty
  separately.
