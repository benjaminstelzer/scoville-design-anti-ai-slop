# Qualification-v9 execution and acceptance report

## Status and scope

The frozen 150-job execution is complete. This is not a claim that every job
passed, that Scoville Design outperformed its controls, or that publication is
authorized. Separate ADR-0052/ADR-0053 adjudication is also complete, with
failures and evidential limits preserved.

The run used `gpt-5.6-terra` with high reasoning effort on the bound Windows
host, Codex CLI `0.147.0-alpha.1.2`, and Edge `152.0.4191.53`. Thirty fresh
synthetic cases supplied 150 registered jobs across the four preregistered arms.
The exact ADR-0048 Design and retained UI package snapshots remained frozen.

## Original frozen results

| Measure | Result |
| --- | --- |
| Registered / initially executed / terminal execution states | 150 / 150 / 150 |
| Regular terminal / unresolved execution | 149 / 1 |
| Unexecuted / open jobs | 0 / 0 |
| Provider attempts | 189: 150 initial plus 39 repair-slot attempts |
| Transport retries | 0 |
| Complete terminal model responses | 188 |
| Final automatic pass / fail / unavailable | 98 / 33 / 19 |
| Unavailable breakdown | 7 route-read errors; 11 Unicode parser errors; 1 missing terminal response |
| Final visual pass / fail / no verdict | 71 / 1 / 78 |

Automatic, visual, and execution results are different dimensions, not disjoint
failure counts. Missing visual verdicts include text-only jobs and jobs that
did not reach the required rendered assessment. They do not count as visual
passes. Original repairs were limited to the preregistered local correction
slots; no outcome retry was inserted into the frozen run.

| Arm | Jobs | Automatic pass | Automatic fail | Unavailable |
| --- | ---: | ---: | ---: | ---: |
| final_design | 55 | 18 | 26 | 11 |
| design_plus_revised_ui | 10 | 0 | 6 | 4 |
| no_skill | 75 | 70 | 1 | 4 |
| revised_ui_fallback | 10 | 10 | 0 | 0 |

Of the 33 automatic failures, 28 failed the route check and five failed the
forbidden-claim check. These are original check outcomes, not independent
causal diagnoses. Route criteria differ between Skill and no-Skill arms, so
these aggregate scores cannot establish comparative aesthetic quality. They
also do not support a blanket all-pass conclusion after technical recovery.

The one final visual failure retained an unchanged empty input template rather
than a completed requested artifact. That is an observed output failure, not
a renderer failure. The bounded rendered reviews address the preregistered
visible defects; they are not general accessibility, usability, or production
quality certification.

## Error attribution

Seven route-read errors share a nonexistent `references/core.md` target; six
were originally categorized as out-of-index reads and one as a failed command.
All seven had already read the actual `SKILL.md` and also read one or two real
expert references. The package does not link `core.md` or `design-core.md`.
The test prefixes say to read Design Core, while the Skill uses Core without
explicitly mapping that term to `SKILL.md`. A repeated model path invention
encouraged by naming ambiguity is a plausible interpretation, not an established
exclusive cause or proof of seven substantive design defects. No route score
has been waived or recomputed on this basis. Explicitly defining the Core is
a narrow future improvement, not a change made to this frozen package.

The eleven Unicode errors are a demonstrated harness boundary defect:
`splitlines()` partitions valid JSON strings containing Unicode separators.
LF-based decoding preserves the recorded JSON values. ADR-0053 permits only
model-free recovery of these eleven responses with unchanged Gold and scoring
rules, followed by required rendered review. Successful parsing alone earns no
pass.

The unresolved J-6F04714F845A slot-2 attempt belongs to the `no_skill` control
arm. It contains usage and a completed-turn event but no terminal agent message.
Its cause remains unknown; neither a timeout nor suspension causality is
established. It is not direct evidence of a Design Skill defect. ADR-0052
permits one separate comparable replay with zero retries or further repairs.

## Evidence and limits

Local evidence root: `Z:/Projekts/AI/scoville-design-eval-local/qualification-v9`.

- `diagnostics/adr0050-repair-continuation-v1/final-ledger.json`:
  `C389ADE647EC48A72AAC7FC48628727A2CA7CE8A632F9EA085B83720A9091C26`.
- `diagnostics/adr0050-repair-continuation-v1/FINAL-AUDIT.md`:
  `245C1D52D46F788133F2F0BF70841BDD495F79593BF3750C7B8E4A3BA4FA5B94`.
- `diagnostics/adr0050-repair-continuation-v1/final-ledger-validation.json`:
  `0E72774A48EE1C85145384C361E52EA5DBEF00B9F0BA5860288A6DD671625E60`.
- `unchanged-package-check-receipt.json`:
  `676FCA7228809949A5A45699040EEF7B8DAEF37F46FA9FFA5B839D8FAF7CBB85`.

The final audit verified 54 frozen bindings, all 150 job chains, 189 capture and
attempt-receipt pairs, 170 original score files, 18 original error files,
170 artifact hashes, and 111 render receipt/image/report chains. Its nine
focused accounting tests passed. Existing package, 50-case routing, generated
index, Design/UI boundary, Skill Creator, and 17 package tests passed without
package mutation. Twelve token-target warnings remain advisory. The initial
system-Python package check lacked tiktoken; the existing pinned environment
passed without installing a dependency. Unchanged checks were not repeated.

All-attempt observed usage: 17,257,056 input tokens, including 13,224,576 cached
input; 771,536 output and 234,397 reported reasoning output. These fields are
reported separately, not summed as disjoint charges. Attempt 171's observed
usage is preserved separately from its original receipt's missing usage.
Receipt timestamps do not establish monotonic provider durations; no exact
provider-duration median or causal cost-effectiveness claim is made.

## Separate user-adjudicated acceptance

The single authorized replay completed with one terminal model response and
confirmed direct-child exit. It used 93,164 input tokens, including 72,064
cached input, with 6,016 output and 2,847 reported reasoning output. Its measured
subprocess duration was 127.578 seconds, not a median for the original run.
No retry or additional repair followed. The original missing-response cause
remains unknown. The replay's ink labels still intersect the circle outlines,
so successful execution did not earn a visual pass.

All eleven existing parser-failed responses were assessed with the tested LF
adapter and unchanged Gold/scorer rules, without new model calls. All twelve
diagnostic artifacts were rendered and independently inspected by Root before
automatic-score disclosure. The Custodian separately compared the original
requirements and artifacts without disclosing private briefs or Gold to Root.

| Diagnostic dimension | Results across 12 assessments |
| --- | --- |
| Unchanged automatic checks | 5 pass; 7 fail |
| Independent visual review | 5 pass; 7 fail |
| Private substantive review | 9 pass; 3 indeterminate |
| All three acceptance dimensions pass | 1 |
| Failure or unresolved acceptance | 11 |

Only J-615266E887D5 earns a user-adjudicated pass. Three cases lack sufficient
source detail to establish full substantive fidelity; that uncertainty is not
a demonstrated Skill defect. Seven outputs have observed visual collisions,
and automatic failures remain visible independently. These counts overlap;
they must not be added as separate failed-job totals. The technical parser
defect itself is not counted as a negative Skill result, but its removal does
not waive actual output defects or missing proof.

The separate ledger is
`diagnostics/w003-adjudication-v1/final-adjudication-ledger.json`, SHA256
`4FA3F33F932F9BD5260F408DBB89EE73703EA50A1B62E4BC2C9ADC8E7679E33D`.
Its validation receipt is `final-adjudication-validation.json`, SHA256
`547E92CBF5933F882B7B554CE2E990D565E36C822A70D03EB02805A7A7F27496`.
All twelve assessment/review chains and original frozen bindings were verified.
The work used one added provider call, twelve assessments and renders, and
23 custody case-open operations. No unaffected jobs were rescored and no new
case/Gold plaintext files were persisted. Original scores, captures, errors,
Gold, snapshots and runtime states remain unchanged.

## Follow-up boundary

The user separately authorized the Core identity clarification in ADR-0054 and
PLAN-0003. That successor change and its seven affected loading checks are not
part of the original frozen measurements. They must not be presented as fixes
for the unrelated routing, claim, visual or source-sufficiency findings above.

No publication, installation, commit, push, tag, or release has occurred.
