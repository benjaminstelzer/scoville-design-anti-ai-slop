# Reference audit: colour and reproduction

**Audit date:** 2026-09-02  
**Executable reviewed:** [`references/colour-and-reproduction.md`](../../../../scoville-design-anti-ai-slop/references/colour-and-reproduction.md), [`SKILL.md`](../../../../scoville-design-anti-ai-slop/SKILL.md), [`modules.yaml`](../../../../scoville-design-anti-ai-slop/modules.yaml)  
**Evidence reviewed:** [`source-ledger.md`](../source-ledger.md), [`rule-source-map.md`](../rule-source-map.md), [`sol-baseline-report.md`](../../evaluation/sol-baseline-report.md), [`module-admission-ledger.md`](../../evaluation/module-admission-ledger.md)  
**Method:** all ten sections of [`reference-audit-method.md`](../reference-audit-method.md); mixed Development, Academic, and General research. A bounded three-mechanism architecture brainstorm was generated before the external landscape was exposed, then reconciled against the evidence. No isolated generator slot was available, so the architecture comparison is useful but carries no diversity or originality claim.

## 1. Current contract

The current leaf is a retained professional floor with an `external-verification` intervention. Its contract is deliberately compact:

- choose colour by communicative role rather than by accumulating attractive swatches;
- judge contrast relationally and at the actual size and area, not from an isolated colour value;
- avoid encoding information by colour alone and preserve redundant cues;
- treat screen and print as different destinations rather than assuming one palette reproduces identically;
- in critique, identify the failing relationship, repair the role system, apply accessibility criteria only to their real scope, and verify production work with the provider profile, separation preview, and physical proof when required.

The route is appropriately owned by Design. It covers creating, distinguishing, critiquing, improving, and applying colour style inside a visual artefact. It does not make this leaf the owner of interface structure, general composition, data truth, source verification, or legal claims. When the task is a UI, the UI Skill remains authoritative for interaction and accessibility implementation; this leaf contributes colour judgment only when routed. When the task is a colour-managed print or cross-media handoff, the leaf may specify evidence gates but cannot manufacture a press profile, measurement, or proof that does not exist.

The current grounding is narrow but real: L-01 and L-14 support role/contrast and WCAG scope, L-17 supports broader accessibility, L-23 supports data colour, and L-32 supports modern CSS colour spaces. The evaluation evidence (B04, B07, B08) shows that SOL can already produce strong data storytelling and distinct Neoclassical and Brutalist colour decisions. It does **not** establish a specialist advantage in colour appearance, ICC workflow, ink behaviour, proofing, HDR, or cross-media reproduction.

## 2. What is already strong

1. **Roles before recipes.** The leaf asks what a colour does before asking which hue looks appealing. That prevents palette-first drift and transfers across branding, editorial, data, packaging, and screen work.
2. **Relational judgment.** Contrast, area, adjacency, type size, substrate, and output are treated as interacting variables. This is more professional than declaring a swatch intrinsically accessible or harmonious.
3. **Scoped accessibility.** The current wording avoids turning WCAG ratios into a universal aesthetic law. It can distinguish text, non-text functional elements, incidental/decorative material, and non-Web output.
4. **Redundant encoding.** Meaning is not entrusted to hue alone. This is a durable rule for status, charts, maps, diagrams, and warnings.
5. **Screen/print nonidentity.** The leaf already rejects naïve RGB-to-CMYK equivalence and asks for destination evidence.
6. **Causal repair direction.** “Fix the role system” is better than globally raising saturation or contrast. It points toward correcting ownership and relationships rather than treating symptoms.
7. **No universal harmony claim.** The leaf does not promise that complementary, analogous, triadic, or culturally stereotyped colours will automatically produce professional work.
8. **Appropriate admission status.** The module-admission evidence supports retaining an actionable floor, not adding textbook colour theory. The SOL baseline gives no reason to duplicate broad knowledge that the model already applies competently.

These strengths should remain the invariant core. The audit therefore recommends deeper decision and proof gates, not a catalogue of palette formulas, colour names, press recipes, or numerical defaults.

## 3. Missing professional capability

### Perception and context

The leaf says colour is relational but does not yet operationalize adaptation, surround, illumination, stimulus size, viewing sequence, or display-versus-reflective appearance. CIECAM16 is explicitly viewing-condition-specific, and CIE guidance shows that incomplete adaptation can matter when comparing screen and paper. A professional critique should therefore record the intended observer, surround, illumination, medium, and scale before diagnosing the colour itself.

### Role systems, states, and themes

Roles are present, but there is no compact testable model for base/alias/component roles, semantic states, interaction states, light/dark themes, high-contrast or forced-colour modes, and destination variants. Without a role/state/theme matrix, a repair may fix one screenshot while breaking hover, disabled, error, print, or dark-mode output.

### Accessibility and colour-vision deficiency

The leaf needs a clearer distinction among: WCAG-conformance checks for rendered Web content; non-colour redundancy; CVD stress review; and direct task/user evidence. Simulation is useful for finding collisions but is not proof that every observer can discriminate the result. CIE 240:2020 also rejects a single universal enhancement method: recolouring, edge enhancement, and patterning have different applications.

### Semantic and data colour

“Do not rely on colour alone” is necessary but insufficient. Continuous, diverging, cyclic, ordinal, categorical, and threshold data require different mappings. A visually dramatic rainbow or non-uniform scale can insert false boundaries or emphasis. The leaf needs to couple scale choice to data semantics and require a legend/scale, monotonic or deliberately documented lightness behavior, redundant critical markers, and grayscale/CVD/output stress checks.

### Colour spaces, gamut, and transforms

The current screen/print distinction does not identify the source colour space, destination colour space or printing condition, embedded profile, output intent, rendering intent, gamut-mapping decision, and fallback. Relabelling numbers with a new profile is not conversion. Clipping, profile loss, or a late conversion can change hierarchy and brand distinction even when the source file appears correct.

### Proofing and production variables

Soft proof, hard-copy contract proof, and a production sample are not interchangeable. The leaf lacks viewing-condition and calibration caveats, substrate/white-point/optical-brightener effects, total area coverage and black-generation dependencies, and a clear boundary for spot colours, ink opacity, print sequence, overprint, transparency blending, varnish, metallic, fluorescent, and pearlescent inks. Many of these cannot be faithfully simulated from generic values.

### Gradients, dark mode, WCG, and HDR

Gradient interpolation space changes the path and may create dull midpoints, hue excursions, or false data structure. Dark mode is not palette inversion: relative emphasis, surfaces, images, status roles, and user-forced colours must be reviewed again. WCG and HDR introduce destination capability, fallback, tone/gamut mapping, peak-luminance and area effects, and immature platform behavior; an SDR screenshot cannot prove the HDR appearance.

### Cross-media evidence and exceptions

The leaf needs an explicit cross-media rule: preserve semantic hierarchy, not identical device coordinates. It also needs a bounded exception record. Deliberate low contrast, out-of-gamut spot colour, non-uniform emphasis in data, or an unaltered brand mark may be valid only when the affected content, reason, alternative cue, destination, and proof are named. “Art direction” alone is not an exception.

## 4. Rule-quality audit

| Rule class | Status | Audit judgment | Required form |
|---|---|---|---|
| Colour carries a named role | Strong heuristic with testable implementation | Keep. It prevents palette drift but does not choose the right role automatically. | Name role, state, theme, destination, and dependent elements. |
| Text and functional contrast meets applicable WCAG criteria | Normative Web constraint | Keep and scope. Do not apply ratios indiscriminately to logos, incidental imagery, print, or all palette pairs. | Test the rendered foreground/background pair at actual state and size; cite applicable success criterion and exception. |
| Information is not conveyed by colour alone | Normative accessibility constraint for covered Web content; strong cross-media principle | Strengthen. Hue differentiation alone fails under CVD, monochrome reproduction, and many viewing conditions. | Add label, shape, pattern, position, icon, or text; verify the redundant cue remains perceivable. |
| Palette is harmonious because it follows a colour-wheel formula | Preference heuristic | Reject as a rule. Complementary/analogous relations can suggest candidates but cannot establish fit, hierarchy, culture, accessibility, or reproduction. | Explain communicative purpose and evaluate in context; allow a wheel relation only as one option. |
| A colour has a fixed emotion or cultural meaning | Unsupported universalization | Reject. Research finds both cross-cultural regularities and culture-specific effects; context and learned association matter. | Treat meaning as a hypothesis; verify audience, domain, locale, and brand usage. |
| Use CMYK for print / RGB for screen | Overbroad shorthand | Replace. Device-independent/profiled workflows and spot/multichannel processes cannot be reduced to mode labels. | Identify source, destination/printing condition, profile/output intent, conversion responsibility, ink system, and proof. |
| A calibrated soft proof proves the press result | False overclaim | Reject. Soft proof quality depends on display, viewing conditions, profiles, and effects that may be unmodellable; a contract proof or production sample may still be required. | State proof class and limitations; require physical evidence when colour acceptance is contractual or material-dependent. |
| Never use red and green | Overbroad accessibility recipe | Replace. The risk is insufficient discriminability and hue-only meaning, especially at similar lightness, not the words “red” and “green” by themselves. | Test contrast/discrimination and add non-colour cues; retain semantically necessary colours when the system still works without hue. |
| Use perceptually uniform colour maps for quantitative data | Strong domain rule, not universal palette law | Keep with scope. Uniformity and order protect quantitative interpretation; categorical or deliberately thresholded data require different logic. | Match map class to data semantics, retain scale/legend, document deliberate discontinuities, stress-test output. |
| Dark mode is an inversion of light mode | False rule | Reject. Adaptation, contrast, surface hierarchy, images, shadows, and system colours change nonlinearly. | Reassign semantic roles for the dark theme and test every functional state plus forced-colour behavior. |
| Wide gamut or HDR is automatically better | Preference/technology overclaim | Reject. Unsupported destinations, mapping, luminance sensitivity, and fallbacks can degrade or alter the intended hierarchy. | Declare destination support, SDR fallback, mastering/reference condition, and evidence limit. |
| A deliberate exception may violate a default | Valid only with governance | Add. Exceptions are professional when bounded, not when implicit. | Record rule, affected content, rationale, risk, compensating cue, owner, destination, and proof/review trigger. |

The central quality correction is to express each serious rule as **condition → causal risk → intervention → proof**, while keeping taste decisions as hypotheses that must survive comparison in the intended context.

## 5. Specialist Skill prior art

GitHub code and repository search found several colour-adjacent Skills, but no credible peer that combines colour appearance, accessible semantic systems, data integrity, ICC workflow, and print-production proof at professional depth. The snapshot is pinned so later drift does not silently change the comparison.

| Skill snapshot | Date / licence | Useful mechanism | Do not import |
|---|---|---|---|
| [`clawic/skills: skills/color/SKILL.md`](https://github.com/clawic/skills/blob/f825206afbf1c697202533a9187be68c7b697e0e/skills/color/SKILL.md) at `f825206afbf1c697202533a9187be68c7b697e0e` | 2026-07-27; MIT | Explicit routing among UI systems, palettes, accessibility, data visualization, branding, print, and colour spaces demonstrates useful progressive disclosure. | Domain commands and attractive palette recipes are not evidence of perceptual, accessibility, or production correctness. |
| [`ilikescience/design-tokens-skill`](https://github.com/ilikescience/design-tokens-skill/blob/787f9724ecc171715d132cdde2215a7ab88d8b0d/SKILL.md) at `787f9724ecc171715d132cdde2215a7ab88d8b0d` | 2026-06-17; MIT | Structured tokens, aliases, explicit colour spaces, theme contexts, and validation make role/state changes testable. | Token syntax is architecture, not visual judgment; a valid token graph can still be inaccessible or badly reproduced. |
| [`louisedesadeleer/color-correct`](https://github.com/louisedesadeleer/color-correct/blob/4c38e5cff615eef58ec3b3197a02b8df472a5f50/SKILL.md) at `4c38e5cff615eef58ec3b3197a02b8df472a5f50` | 2026-07-09; no repository licence detected | A closed loop—extract/measure, establish intent, grade, compare across representative frames, adjust, preserve metadata—transfers well to evidence-based critique and repair. | It is a video-colourist workflow, not a general graphic-colour authority. Hard-coded looks and thresholds do not transfer. No text or assets may be reused without a licence. |
| [`yanliudesign/mono-color-skill`](https://github.com/yanliudesign/mono-color-skill/blob/de607fedfff647eaf5400e0aa43085787d7d1fca/SKILL.md) at `de607fedfff647eaf5400e0aa43085787d7d1fca` | 2026-08-31; MIT | Separating ink plates by content role and inspecting the generated artefact can create coherent limited-colour editorial work. | Fixed palettes, percentage gates, hue-to-topic aliases, and universal layout ratios are style-system choices, not general colour or print-production rules. |
| [`omer-metin/skills-for-antigravity: packaging-print-production`](https://github.com/omer-metin/skills-for-antigravity/blob/e8dcf4e8737921a10088bd5c9eb65e81f74c051f/skills/packaging-print-production/SKILL.md) at `e8dcf4e8737921a10088bd5c9eb65e81f74c051f` | 2026-01-22; Apache-2.0 | It usefully exposes production concerns such as separations, spot colour, overprint, dielines, and vendor handoff. | Universal CMYK, rich-black, bleed, minimum-type, and other numeric recipes are unsafe without process, provider, substrate, standard, and jurisdiction. This is negative prior art for cargo-cult production advice. |

**Prior-art conclusion:** adopt the routing clarity, role graph, representative-sample loop, and explicit production handoff. Reject fixed harmony formulas, topic-to-hue mappings, generic press recipes, and tool output presented as proof.

## 6. Authoritative research and learning sources

### Technical, normative, and evidentiary sources

| Topic | Authoritative source | Learning transferred to the leaf | Source/licence treatment |
|---|---|---|---|
| Perception, adaptation, and context | [CIE 248:2022, CIECAM16](https://www.cie.co.at/publications/cie-2016-colour-appearance-model-colour-management-systems-ciecam16); [CIE 162:2010](https://www.cie.co.at/publications/chromatic-adaptation-under-mixed-illumination-condition-when-comparing-softcopy-and) | Colour appearance is viewing-condition-specific. Screen/print comparisons can involve mixed and incomplete adaptation. Record medium, surround, illumination, scale, and viewing sequence before diagnosing a mismatch. | CIE metadata is public; reports are copyrighted/commercial reference material. Paraphrase principles only. |
| Viewing and soft-proof conditions | [ISO 3664:2025](https://www.iso.org/standard/83759.html); [ISO 12646:2015](https://www.iso.org/standard/57311.html); [ISO/TC 130 production-guidelines map](https://committee.iso.org/files/live/sites/tc130/files/Resources/Guidelines%20for%20using%20print%20production%20standards%20v2%20Jan%202024.pdf) | Reflective viewing, soft-proof displays, measurements, PDF/X, and hard proof have separate standards. “Looks right on my monitor” is not a production criterion. | ISO metadata/guideline is referenceable; standards are copyrighted and commonly paywalled. Do not reproduce requirements or tables. |
| Role systems and colour spaces | [DTCG Color Module 2025.10](https://www.designtokens.org/TR/2025.10/color/); [DTCG Resolver Module](https://www.designtokens.org/tr/drafts/resolver/) | Store explicit colour space and components; separate base, alias, and component decisions; represent theme contexts. Validate conversions and interpolation rather than assuming a hex value is canonical everywhere. | W3C Community Group final-specification terms; cite and paraphrase, do not copy examples wholesale. Resolver remains draft/current-work material. |
| Web contrast scope and colour-only meaning | [WCAG 2.2](https://www.w3.org/TR/WCAG22/), especially [Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color) and [Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | Apply criteria to the covered rendered content and states. Preserve non-colour information. Keep formal exceptions such as logos/incidental content in scope rather than turning ratios into taste rules. | W3C document licence; normative Recommendation plus non-normative Understanding guidance. |
| CVD enhancement | [CIE 240:2020](https://www.cie.co.at/publications/enhancement-images-colour-deficient-observers) | Recolouring, edge enhancement, and pattern superposition are different repair classes; no technique covers all cases. Simulation is a stress view, not universal proof. | CIE copyrighted/commercial reference; paraphrase only. |
| Semantic/data colour | [Crameri, Shephard & Heron 2020](https://www.nature.com/articles/s41467-020-19160-7); [Nuñez, Anderton & Renslow 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6070163/) | Match sequential/diverging/cyclic/categorical mapping to data semantics. Uneven lightness can create false boundaries and emphasis. Maintain a scale/legend, CVD and grayscale robustness, and output-aware testing. | Crameri article: CC BY 4.0; Nuñez article: CC0. Attribution remains required by this audit even where waiver terms apply. |
| Profiles, spaces, gamut, and rendering intent | [ICC.1:2022 profile specification](https://www.color.org/specification/ICC.1-2022-05.pdf), [ICC Getting Started](https://www.color.org/getting-started/), [ICC white papers](https://www.color.org/whitepapers/) | Name source and destination, preserve embedded profiles, distinguish assignment from conversion, select intent for the actual transform, preview out-of-gamut consequences, and retain an output intent where the format/workflow supports it. | ICC material is publisher-copyrighted reference material. Use concepts, not copied prose or tables. |
| Soft proof and physical proof | [ICC White Paper 23](https://www.color.org/ICC_white_paper_23_RGB_Workflow.pdf); [ISO 12647-7:2016](https://www.iso.org/standard/66426.html); [Fogra proof substrates](https://fogra.org/en/certification/materials-environment/proofsubstrate) | Soft proof can be useful without being an accurate prediction of hard copy. Contract proof depends on a defined printing condition, measurement/viewing criteria, and substrate properties; critical jobs need the agreed physical evidence. | ICC/Fogra public proprietary references; ISO standard copyrighted/paywalled. No thresholds should be invented from metadata. |
| Spot inks, overprint, substrate, and transparency | [ICC White Paper 31](https://www.color.org/whitepapers/ICC_White_Paper_31_Flexible_colour_management_for_graphic_arts.pdf); [ICC CxF/X-4 spot-ink test](https://www.color.org/cxf_test/); [Ghent Workgroup specifications](https://gwg.org/technical-specifications/) | Spot/process combinations depend on measured colour, opacity, print order, substrate, and blending space. Some varnish/special-ink appearance cannot be accurately simulated. Require provider data, separation/overprint checks, and physical evidence. | ICC and GWG copyrighted reference material; cite and paraphrase. |
| Gradients and modern CSS colour | [CSS Color 4](https://www.w3.org/TR/css-color-4/) | Interpolation space changes the result; Oklab/Lab, linear-light RGB, polar spaces, and legacy sRGB serve different goals. Choose deliberately and inspect the final rendered bit depth/size for banding and gamut mapping. | W3C permissive document licence; Candidate Recommendation Draft, not universal design law. |
| Dark mode and forced colours | [Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/); [CSS Color Adjustment Level 1](https://www.w3.org/TR/css-color-adjust-1/) | Respect `prefers-color-scheme` and user-forced palettes. Avoid opting out of forced colours unless the component itself fully preserves the user’s colour and contrast needs. | W3C document licence; draft/Recommendation-track status must be retained. |
| WCG and HDR | [CSS Color HDR Level 1](https://www.w3.org/TR/css-color-hdr-1/); [ITU-R BT.2100-3](https://www.itu.int/rec/r-rec-bt.2100) | WCG and HDR are distinct. PQ/HLG, headroom, mapping, display capability, SDR fallback, and very bright-area sensitivity affect appearance. Critical review requires a capable reference path; the CSS module is still a Working Draft. | W3C draft under W3C licence; ITU Recommendation is authoritative and copyrighted. Cite status/version and avoid copied parameter tables. |
| Cross-media output | [Ghent Workgroup PDF/X output-intent guidance](https://gwg.org/pdf-x-output-intents-white-paper/); [ICC specifications](https://www.color.org/specifications/) | Preserve the same semantic hierarchy across destinations while allowing different coordinates, separations, fallbacks, and proofs. An output intent names a printing condition; it does not guarantee every device result. | Public proprietary reference material; paraphrase only. |

### Harmony, preference, and cultural meaning

[Palmer and Schloss’s ecological valence theory](https://doi.org/10.1073/pnas.0906172107) supports the idea that preference is affected by associations with coloured objects; [Ou et al. on two-colour combinations](https://doi.org/10.1002/col.20024) provides empirical models for a bounded study context; and [Jonauskaite et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC6774957/) finds both shared and culture-specific colour–emotion associations. These sources justify **questions and comparisons**, not universal rules such as “blue means trust,” “red is aggressive,” “complements are harmonious,” or “60/30/10 is professional.” They are publisher-copyrighted or open-access research to cite, not prose or formula banks to import into the executable leaf.

**Evidence conclusion:** technical and normative constraints can define failures and proof obligations. Empirical perception research can explain likely causal mechanisms. Harmony, emotion, and preference research can generate candidates, but final judgment remains audience-, task-, culture-, context-, and output-specific.

## 7. Applied Dos and Don’ts

| Area | Do | Don’t | Causal critique → repair → proof |
|---|---|---|---|
| Perception/context | Review the complete artefact at intended scale, surround, illumination, distance, and medium. | Approve an isolated swatch or infer print appearance from a luminous screen. | “Accent loses separation on warm stock under the agreed light” → change role value/ink or substrate strategy → compare under defined viewing conditions. |
| Role system | Name background, text, border, action, status, data, and brand roles; map every state/theme/destination. | Name production tokens only by hue or mutate one screenshot locally. | “Disabled and secondary share one token, erasing state” → split semantic aliases → run the role/state/theme matrix. |
| Contrast | Test actual rendered pairs, size, weight, state, overlap, and applicable WCAG scope. | Demand that every palette pair pass a text ratio or use a brand swatch as evidence. | “Body text fails because the surface changed, not because blue is always too light” → repair the pair → automated and visual check in every state. |
| CVD/accessibility | Add text, shape, icon, pattern, position, or line style; use simulations as stress views and include users/tasks when risk warrants. | Treat red–green avoidance, grayscale, or one simulator as universal proof. | “Success/error differ only by hue” → add label/icon and sufficient pair contrast → verify without colour and in representative modes. |
| Data colour | Match map class to continuous, diverging, cyclic, ordinal, categorical, or threshold semantics; retain scale/legend. | Use rainbow or arbitrary brand ramps for quantitative values; crop the colour bar. | “Yellow creates a false peak in a linear field” → choose/test a perceptually ordered map → compare increments, CVD, grayscale, and final output. |
| Colour management | Preserve source profile; convert intentionally to named destination/printing condition; record intent and output intent. | Assign a destination profile to unchanged numbers, discard profiles, or say “CMYK-safe.” | “Late unprofiled conversion collapses two status roles” → convert from known source with provider condition → separation/gamut review and proof. |
| Soft/physical proof | Calibrate/characterize the display and environment; identify soft proof, contract proof, press proof, or production sample. | Call a screenshot, office print, or generic CMYK export a contract proof. | “Metallic accent is unmodellable on the soft proof” → keep simulation illustrative and order the agreed material proof → sign off physical sample. |
| Ink/substrate/overprint | Obtain provider specs; name process/spot inks, substrate, print order, opacity, overprint, transparency/blending, TAC/black policy where relevant. | Reuse universal rich-black, ink-limit, bleed, or spot-to-process recipes. | “White set to overprint disappears; spot/process overlap shifts by sequence” → fix object/plate settings and communicate ink data → inspect separations/output suite and physical proof. |
| Gradients | Choose interpolation space by perceptual, physical-light, chroma, or compatibility goal; render at final size/bit depth. | Tween legacy hex values blindly or mistake browser preview for every export. | “sRGB midpoint becomes muddy and banded” → select/test interpolation and dither/export path → inspect representative devices/files. |
| Dark/forced modes | Re-evaluate surfaces, text, statuses, images, shadows, focus, selection, and every interaction state per theme; honor system colours. | Invert the palette or disable forced colours for branding convenience. | “Dark theme keeps light-theme error red and loses boundary” → remap semantic role/add redundant cue → theme/state/forced-colour matrix. |
| WCG/HDR | Name supported destination, transfer/colour space, reference condition, mapping, SDR fallback, and luminance-risk review. | Promise identical appearance on unknown displays or use HDR brightness as hierarchy without fallback. | “Highlight owns the composition only on one HDR panel” → cap/remap role and design SDR hierarchy → review capable HDR path plus alternate displays. |
| Cross-media | Create destination-specific values/exports that preserve role order and meaning; compare under intended conditions. | Use one master numeric palette as proof of identity across Web, office print, offset, and signage. | “Brand accent clips in print and becomes equal to action colour” → choose approved print variant or spot process → side-by-side defined proofs. |
| Exceptions | Record rule, scope, rationale, risk, compensation, owner, destination, and proof trigger. | Use “creative intent” to waive functional access, data truth, or production evidence. | “Low-contrast display lettering is decorative and duplicates no content” → document scope/alternative → verify essential reading and states remain compliant. |

## 8. Architecture recommendation

The bounded brainstorm compared three materially different mechanisms:

1. **Deepen the existing single leaf with four gates:** semantic role; perception/accessibility; destination/reproduction; evidence/exception.
2. **Split into flat specialist leaves:** colour judgment/accessibility versus colour management/reproduction.
3. **Keep the floor nearly unchanged and route all specialist work to current external verification.**

**Recommendation: mechanism 1.** Keep `colour-and-reproduction` as one leaf because professional colour decisions frequently cross the screen/print boundary and because a split would add router ambiguity (“is this palette critique theory or reproduction?”). Add only a compact decision sequence:

1. **Frame:** intent, audience, essential meanings, medium/destinations, environment, existing system, non-negotiable colours.
2. **Model:** semantic roles plus states/themes/destinations; data scale class when applicable.
3. **Diagnose:** observation → perceptual/technical cause → consequence; distinguish normative failure from preference disagreement.
4. **Repair:** smallest role- or destination-level intervention that preserves intent; add redundant cues rather than merely recolouring.
5. **Verify:** applicable contrast/non-colour checks, CVD/output stress views, profile/separation/proof evidence, and recorded exception.

The reference should contain decision gates and compact failure patterns, not standards tables, palette libraries, profile recipes, or copied implementation syntax. Exact changing criteria remain in authoritative sources and the source ledger. A future split is justified only if one of these is demonstrated: the leaf cannot stay within the package token ceiling; routing tests consistently distinguish pure prepress work from design colour work; or a specialist prepress owner is added with independent validation.

Progressive disclosure remains intact:

- Direct Index trigger: colour role/palette, contrast/CVD, data colour, colour space/gamut, screen–print/HDR, ink/overprint/proof.
- Leaf: the five decision gates, causal repair patterns, exceptions, and proof ceilings.
- External sources/provider data: current criteria, printing condition, profiles, measurement, and job-specific acceptance.

No new top-level owner, nested chapter tree, or automatic composition load is warranted. Colour-specific exceptions remain in this leaf; composition is loaded only when the repair materially changes hierarchy or spatial relationships.

## 9. Tests and claim ceiling

### Required behavioural tests

1. **Create / role system:** Given brand constraints and light/dark/forced-colour states, produce a semantic role matrix and a palette whose essential meaning survives without hue. Fail if the answer is only a swatch list.
2. **Critique / causal chain:** Diagnose a design where an accent works in isolation but fails against its real surround. Require observation, cause, consequence, smallest repair, and proof. Fail generic “increase contrast.”
3. **Improve / WCAG scope:** Repair low-contrast body text while preserving a decorative low-contrast element that is outside essential content. Fail if every colour is globally darkened or a WCAG exception is invented.
4. **Style / non-cliché colour:** Apply a named visual style without fixed topic-to-hue stereotypes. Require role, context, and output reasoning. Fail if style is reduced to a stock palette.
5. **CVD / redundancy:** Repair status indicators and a chart that use hue alone. Require a non-colour cue and task-level verification; fail simulator-only confidence.
6. **Data semantics:** Select and justify a scale for sequential, diverging, cyclic, and categorical cases. Require legend/scale and output stress checks; fail rainbow/default-brand mapping.
7. **Profile pipeline:** Given a profiled RGB source and a provider printing condition, distinguish assignment, conversion, output intent, rendering intent, gamut preview, separation, and proof. Fail generic “convert to CMYK.”
8. **Spot/overprint/substrate:** Audit a spot-plus-process package with overprint and special substrate. Require provider measurements/specs, print-order/opacity caveats, separations, and physical proof; fail hard-coded rich-black/TAC claims.
9. **Gradient:** Compare legacy sRGB, linear-light, and perceptual interpolation goals and require final-size/bit-depth inspection. Fail universal “always Oklab.”
10. **Dark/HDR/WCG:** Preserve hierarchy across light, dark, forced colours, SDR, and an HDR-capable destination with explicit fallbacks. Fail inversion or “HDR is better.”
11. **Cross-media:** Produce screen and print variants that preserve semantic hierarchy while allowing different values. Fail numerical sameness as proof.
12. **Exception governance:** Accept a legitimate decorative or material exception only when scope, alternative cue, risk, owner, and evidence are recorded. Fail blanket “creative intent.”

### Architecture and regression tests

- Router selects this leaf for explicit palette/colour-management/print-reproduction concerns and does not automatically add composition, brand, UI, culture, or sources unless their independent trigger is present.
- UI-only work still loads the UI fallback owner; the Design colour leaf does not overwrite incumbent framework/design-system colour tokens without evidence.
- Source/fact/licence verification routes to Sources; colour-production rights or provenance do not become this leaf’s responsibility.
- The leaf remains usable in create, critique, improve, and style modes and preserves the current B04/B07/B08 strengths.
- Index wording covers general imagery colour, data colour, standalone colour-management/print tasks, dark/HDR, and domain-specific exceptions without enumerating every technology.

### Claim ceiling

After the recommended revision the Skill may claim that it can frame, create, distinguish, critique, and improve colour systems with professional causal reasoning; scope accessibility checks; plan colour-managed and cross-media handoffs; identify evidence gaps; and avoid common harmony and production clichés.

It must **not** claim universal harmony, universal cultural meaning, device-independent visual identity, press-ready correctness without the actual provider condition/profile, WCAG conformance without testing rendered output, CVD inclusion from simulation alone, accurate special-ink/varnish/HDR appearance from a generic preview, contract-proof equivalence, or autonomous measurement of a physical result. The audit is research evidence for rules; it is not a completed executable intervention or qualification result.

## 10. Priority (P0-P3)

### P0 — unsafe or materially false if omitted

- Replace generic screen/print language with a named source → transform → destination/output-intent → proof chain.
- Explicitly distinguish profile assignment from conversion and soft proof from physical/contract proof.
- Add spot/process ink, substrate, opacity/print-order, overprint/transparency, and special-finish limits; prohibit universal press recipes.
- Scope WCAG and colour-only meaning correctly; require redundant essential cues and reject CVD simulation as sole proof.
- Separate normative/technical constraints from harmony, emotion, and preference heuristics.

### P1 — required for professional causal performance

- Add viewing context/adaptation and actual-size/surround diagnosis.
- Add semantic role × state × theme × destination modeling.
- Add data-scale semantics, perceptual-order/uniformity reasoning, legends, and output stress tests.
- Add causal critique and smallest-repair/proof structure for all modes.
- Add bounded exception governance with compensating cue and evidence.
- Add cross-media preservation of semantic hierarchy rather than numeric identity.

### P2 — current/high-value edge capability

- Add deliberate gradient interpolation and final render/banding inspection.
- Add dark-mode and forced-colour state checks.
- Add WCG/HDR destination, fallback, mapping, and claim limits while marking CSS HDR as immature draft technology.
- Add test cases for mixed soft/hard-copy adaptation and material-dependent appearance.

### P3 — defer unless evidence justifies cost

- Do not add palette libraries, universal harmony ratios, hue-to-industry or hue-to-emotion tables, or generic CMYK/rich-black/bleed values.
- Do not copy standards thresholds or implementation tutorials into the leaf; keep current details in cited authorities/provider specifications.
- Do not split the module or add a prepress owner until router, token, or evaluation evidence proves the single-leaf architecture insufficient.
- Do not claim spectral, multichannel, fluorescence, metallic/pearlescent, or full HDR mastering expertise; route high-risk jobs to qualified production specialists and measured proofs.

**Overall audit result:** retain the leaf and deepen it selectively. Its professional advantage should come from better framing, causal diagnosis, destination-aware repair, and honest proof—not from more colour trivia or more confident recipes.
