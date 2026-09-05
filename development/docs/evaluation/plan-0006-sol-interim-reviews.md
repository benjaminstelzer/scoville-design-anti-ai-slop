# PLAN-0006 interim SOL reviews

User-authorised reviewer contingency: ADR-0056. Requested reviewer model:
`gpt-5.6-sol`; fresh host-native subagents with `fork_turns=none`. No Fable
verdict is attributed to SOL. No original artifact is overwritten.

## Installed runtime review

Reviewer: `/root/sol_runtime_independent_p6`.
Package: 34 files at
`C:/Users/benja/AppData/Local/Temp/design-plan6-focused-v1-20260904/candidate`.
Manifest: `246B03A84383C1E2AB7A4928F597F1F5A32B014734D6AD3A6ED1FBEE65368655`.
Only this installed-form directory was supplied. No repository, previous
findings, targeted questions, test evidence or expected verdict was supplied.

The initial response disclosed truncated reference reads. The reviewer was
asked to complete those reads, without directing its judgment. Final verdict:

> No material issue found after completing the review.
>
> Exact coverage: Read the complete contents of all 34 files in the supplied
> directory: SKILL.md, modules.yaml, agents/openai.yaml, all 30 routed expert
> references, and the complete 637-line references/source-index.md. Previously
> truncated material was reread in bounded, untruncated calls. Checked all 30
> direct reference links, reference inclusion in the manifest, and source-ID
> resolution against the bundled index.
>
> The instructions consistently distinguish scoped work from release
> acceptance, preserve read-only critique, and avoid requiring unavailable
> sibling Skills. No concrete broken reference, missing runtime dependency,
> or material internal contradiction was identified.
>
> Limits: Static installed-package review, not execution-based behavioral
> testing. External publications, URLs, licences, and recorded historical
> inspection claims were not independently verified. No files outside the
> supplied directory were inspected; no files were changed.

## Blinded paired artifact review

Reviewer: `/root/sol_blind_artifacts_p6`.
Only `C:/Users/benja/AppData/Local/Temp/design-plan6-neutral-review-a71d` was
supplied: raw task/input, A/B sources and actual PNGs, plus the image brief for
T2. No Skill directories, package identities, earlier findings, expected fixes
or author-process diagnoses were supplied. Assignment was randomised per pair
and retained separately in plan-0006-blind-assignment.json.

Decoded after the verdict: T1 A=current and B=baseline; T2 A=current and
B=baseline; T3 A=baseline and B=current. The reviewer was not given this map.

### T1 / C1 small repair

No meaningful difference, high confidence. Both outputs are byte-identical,
changing only paragraph line-height from .7 to 1.4. The real 600px proof shows
no overlap; exact words, poster dimensions and heading/footer placement remain.

The reviewer corrected one proof-limit sentence after receiving only renderer
metadata: screen-390.png was captured at a 390px viewport with fullPage:true.
The protected 600px poster overflows, so the full-page PNG is 600px wide. This
does not demonstrate narrow-layout fitness; preserving that width was required.

### T2 / C2 named-style web/brand artifact

Modest preference for B (baseline), medium confidence, with corrections needed
in both alternatives. B's station rows and larger schematic make names, storeys
and explanations easier to compare. A is legible but its mobile
`.parts-notes{display:block}` is overridden by a later `.parts-notes{display:none}`;
the hidden table column therefore lacks its intended replacement notes.
Most facts remain elsewhere, so this is a local implementation defect.

Both preserve named parts and stated counts, distinguish the unknown vocational
wing count, label constructed/non-measured drawings and disclaim official
identity. B incorrectly says the studio is the tallest named part despite
missing counts/heights, and its One to five statement needs stated-count scope.
A adds at-the-foot viewing advice while claiming nothing beyond the source.
Both image briefs are coherent and do not claim existing photography. B is
more specific about placement/licensing; A includes photography-rule/release
clearance. This is not a demonstrated improvement of the new package.

### T3 / C3 quiet utility

No meaningful difference, high confidence. Both outputs and the supplied source
are byte-identical. Paired PNGs match; desktop peer cards and narrow stacking
remain readable. No cosmetic redesign was introduced.

The review bundle omitted author explanations to avoid process-induced bias;
the reviewer correctly withheld a judgment on that deliverable. Original notes
are retained with the execution attempts and checked separately by the host.

### Limits and next step

This review used actual static renders and source, not live interaction or
external source verification. Initial findings remain authoritative history.
Only T2 correction proposals and separately versioned renders are requested;
no rerun of T1/T3 or full holdout is justified by these findings.

## T2 targeted correction verification

The same still-blinded SOL session proposed the smallest five corrections.
The host materialised new `artifact-v2.html` files, retaining each original:

1. A: relocate the default parts-notes CSS before the narrow media query.
2. A: remove the unsupported at-the-foot location from viewing advice.
3. A: replace the universal source-fidelity assertion with an explicit label
   for the guide's own suggested counting exercise.
4. B: qualify the one-to-five range as stated counts and name the missing count.
5. B: replace tallest-part wording with highest stated storey count.

The host rendered both versions at actual 1440px and 390px browser viewports
using the same Chromium 151.0.7922.34 harness. Sources and PNGs were copied to
T2/A/v2 and T2/B/v2 without exposing arm identity. Final reviewer response:

> All five corrections verified. No introduced material defect observed at
> either supplied width.
>
> A's mobile replacement notes now appear beneath the parts table, fit their
> column, and remain separated from the next section. On desktop those notes
> remain hidden and the full table stays intact. Both text corrections render
> cleanly. B's qualified summary and replacement of the height superlative are
> visible at both widths, without clipping, overlap or broken spacing.
>
> Preference unchanged: modest preference for B, medium confidence. A's mobile
> omission is resolved and no longer counts against it. B still provides more
> directly associated name/count/explanation groupings, useful section
> navigation and a larger desktop schematic. This remains a presentation
> preference, not a finding that A fails the task.
>
> These are host-corrected v2 artifacts following this review, not independent
> new generations. Verification covers source diffs and four supplied static
> renders, not live interaction or other widths. T1/T3 outcomes are unchanged.

No runtime instruction was changed in response. The cascade error is directly
located in generated HTML; both arms' factual overclaims are first-pass output
defects. Existing evidence/validation requirements already cover their repair.
This does not prove that further package hardening could never help. It does
not justify blanket rewrites, rerunning unrelated cases, or claiming a new
package visual advantage that this pair did not demonstrate.
