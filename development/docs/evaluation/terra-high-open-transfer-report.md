# Terra High open transfer report

Date: 2026-09-02  
Status: in progress; one terminal open case  
Model: `gpt-5.6-terra`  
Reasoning: `high`

## Purpose

W-010 tests one known open case at a time before any sealed Terra call. It
measures actual provider usage, routing, output contracts, artifact integrity,
and the complete render path. It is not holdout or cross-person evidence.

## RUN-003 poster repair

Case: public `design-train-04-poster-repair`  
Design package manifest:
`623AF68CE12F8E8934DF3DACC7BD8A67CCCB37D0FD16EFFD3D0C1FBE8D74FE85`

Provider usage:

| Metric | Tokens |
| --- | ---: |
| Input | 92,716 |
| Cached input | 74,240 |
| Uncached input | 18,476 |
| Output | 4,188 |
| Reasoning output | 1,567 |
| Provider total | 96,904 |

Runtime was 98.413 seconds. The call loaded the 1,283-token Core and 2,812
Skill tokens in total: composition/layout, typography/writing systems, and
colour/reproduction. It made six shell calls and read exactly the Core, those
three experts, the brief, and the source SVG once each.

### Product result

- all required copy remained;
- black, cream, and signal-red identity remained;
- dimensions and XML were valid;
- the agent kept `rendered_status` unverified before external rendering;
- the immutable SVG later rendered completely and without clipping at intended
  size after a renderer-guard repair;
- one reviewer found a clear restrained editorial hierarchy and no critical
  visible defect. This is one reviewer's observation, not preference evidence.

Artifact SHA-256:
`3F66B139FA7D24CB26A0E260C35F67EE08C02E6E45D347FEB6C5092483225A61`

Intended PNG SHA-256:
`EF88CB0E8D7E6DD7E298DD0898E72839DEDEE5F04820C2AACB6CF5B48E006B2C`

### Quarantined benchmark and harness defects

The original terminal receipt remains unchanged and failed its combined hard
gate. The two failing signals do not establish a Terra product failure:

1. `no_new_claims` rejected the visible label `READING SERIES`. The supplied
   brief explicitly called the artifact a `reading-series poster`; the checker
   compared only required strings rather than all supplied source text.
2. The shell-call budget was five even though the case required six distinct
   once-only reads. A fixed command count below the minimum read graph is not a
   valid efficiency gate.

The first renderer observation also rejected the standard root declaration
`xmlns="http://www.w3.org/2000/svg"` as a remote reference. A model-free guard
repair passed 41 of 41 tests, preserved all prior negative controls, and
rendered the exact terminal artifact. The original failure and later render
receipt remain separate.

No Gold or RUN-003 receipt was edited. Any corrected scorer belongs to a new
open suite version and must apply prospectively or re-score immutable stored
responses with both original and corrected results retained.

## Evidence and limits

Primary terminal receipt SHA-256:
`BB47BC84FEF5124BE5D776C3F0507BD77BCFBDCD772FFC9A152FBB75864062C9`

Final evidence receipt SHA-256:
`53933132BC47E2FA23E3D143D5C7E8B1E65F96DD064D3E2149CA5C77E566488E`

Renderer repair receipt SHA-256:
`60E6005428006B6EB5822A17D4A2A10B4452C1D1A47F78E9923A609DC2CC175B`

This single open case supports only a narrow Terra transfer and cost
observation. It does not qualify critique, style direction, UI composition,
general visual quality, expert equivalence, or market leadership.

## Typography critique RUN-001

Case: public `design-val-03-typography-critique`

| Metric | Tokens |
| --- | ---: |
| Input | 62,139 |
| Cached input | 45,056 |
| Uncached input | 17,083 |
| Output | 3,095 |
| Reasoning output | 1,905 |
| Provider total | 65,234 |

Runtime was 67.371 seconds. The call loaded the Core plus only
`typography-and-writing-systems`, 1,827 Skill tokens total. Hard behavior and
efficiency passed. The response returned five localized findings with separate
observation and likely effect, severity, smallest correction, priority,
preserved strengths, no edit, and an honest unrendered evidence boundary.

The separate preflight read graph incorrectly expected
`critique-and-validation`. Current RC7 routing reserves that method expert for a
deep general audit, comparison, generic-cliche judgment, rule exception, or
rendered repair rationale. A bounded typography-only critique correctly loaded
only its domain expert. The passing benchmark result remains unchanged; the
extra read-graph failure is a harness defect, not a Terra or package failure.

Primary receipt SHA-256:
`3190A7282F83B92B533C05B2F9D8477041B999396C457BD0FB554A4AE607F9E1`

Final evidence receipt SHA-256:
`234BC6073BC32083C62A7A6463E33B9CFE87D5C51731CB1E0E8D65FA83BB54C7`

Together the two Terra calls used 162,138 provider-total tokens, including
119,296 cached input tokens. Uncached input plus output totaled 42,842 tokens.
Two cases remain cost and transfer observations, not general qualification.

## 80s neon web style RUN-001

Case: public `design-train-02-80s-neon-web`

| Metric | Tokens |
| --- | ---: |
| Input | 79,032 |
| Cached input | 61,184 |
| Uncached input | 17,848 |
| Output | 13,486 |
| Reasoning output | 1,177 |
| Provider total | 92,518 |

Runtime was 255.541 seconds. The call loaded 2,969 Skill tokens: Core,
style-direction, typography/writing systems, and UI/interaction design. The
calculated five-node read graph passed without a duplicate. Scorer-v2 passed;
the original public benchmark's two-call ceiling remains recorded as a legacy
benchmark defect.

The self-contained HTML preserved every required event item, contained no
external fetch asset or script, supplied semantic structure, visible focus,
reduced-motion handling, readable body type, and a visible access note. Two
literal checkers initially missed the access note and CSS-built VHS scanline
texture; source review confirmed both without changing the terminal response.

The static renderer initially classified non-fetching `mailto:` anchors as
Windows alternate-data-stream references. A model-free repair retained
navigation and external-protocol blocking, passed 60 of 60 guard tests, and
rendered the unchanged HTML at desktop and mobile. Input and 888 renderer-font
hashes remained identical.

One-reviewer visual inspection found:

- recognizable 1980s retro-computing DNA without a generic purple synthwave
  template;
- ASCII terminal, CRT/scanline texture, ticket logic, fluorescent accents, and
  compressed display type operating as one system;
- strong hierarchy and subject specificity;
- no visible collision or horizontal page overflow at either inspected width;
- character and legibility preserved on mobile rather than merely scaled down.

Artifact SHA-256:
`E0568CCDA1F6A5C3972708B1BA6ADAAC617C718E3C0E55AD938BAEAF93AACF63`

Desktop PNG SHA-256:
`4899E6797D3960C8D3FE74BBFC6BBA50197403302024063C21BCA43C449A2427`

Mobile PNG SHA-256:
`2AB670B1209EE0580926754B004EA978EBD79ABC095459CDD3BAC1916F5A878F`

Primary receipt SHA-256:
`6E317786733CEAF2617320B4C447387EF0B515239BB64648B15A44188C585AF0`

Final evidence receipt SHA-256:
`867A95AF263ED2C782FFBFC01FD5352D4F311DD5D1C6E1392186BB20914DC57E`

Renderer repair receipt SHA-256:
`15A2AA52D721733664E340C958E68E03F16574DC592CEBACD9D24A3F0572C2D7`

Across three Terra calls, provider-total usage is 254,656 tokens, including
180,480 cached input tokens. Uncached input plus output totals 74,176 tokens.
This remains a small open transfer sample, not holdout or market-quality proof.

## UI-only Greenfield fallback

The first public `ui-comp-train-ui-only` Terra run returned the correct owners
but loaded Framework, Quality, and Validation. That was a real Terra routing
and efficiency failure: a hypothetical owner classification needed only the
framework/fallback ownership reference.

The UI Core gained one 60-token `OWNERSHIP-ONLY` rule. The new immutable UI
snapshot is:

- `SKILL.md` SHA-256:
  `C785BABF95B600A503C0BA80DB349A915628997ED15AA133FE6A1D9A93D47554`
- five-file manifest:
  `2519263462CEF1E2B7008888AD601E4F56F486A1BF06D31558D9924A7E288FF7`

The exact one-case retest passed hard, behavior, and efficiency 1/1/1. It read
only Core and Framework, returned `ui-standalone-fallback / ui / ui`, and did
not discover or simulate Design. Provider-total usage was 37,213 tokens;
uncached input plus output was 26,205.

Retest receipt SHA-256:
`197FF013D6F0C4C53442E6F58823EE8B12C56988AB797CDF6EDDFE6A8FE2A124`

## Composed Design plus UI ownership

The public `ui-comp-train-both-active` Terra run returned the correct owners:
`design / ui / ui`. It read only the UI Core and did not read, discover,
simulate, or re-decide through the Design package. Provider-total usage was
23,697 tokens; uncached input plus output was 13,713.

The run's separate preflight read graph expected Framework. That expectation
is inconsistent with the current router: the supplied complete Design record
already settled ownership, and the task requested no framework path,
implementation mechanics, or proof. Core-only is the smaller correct route.
The terminal receipt remains unchanged; its semantic result is accepted and
the extra read expectation is recorded as a harness defect.

Composed receipt SHA-256:
`A4DBAD14A0A903F3760650A63E5A56F72521DB95CFBA1A386AFE31FAA5C50FB4`

## Open gate result

Six terminal Terra model responses across repair, critique, style, UI-only,
and composed ownership used 385,303 provider-total tokens, including 237,568
cached input tokens. Uncached input plus output totaled 147,735 tokens. The
per-call provider-total range was 23,697 to 96,904.

Observed package behavior passed after preserving original receipts and
separately correcting or classifying:

- two deterministic scorer assumptions;
- two renderer URL-classification defects;
- one Terra-specific UI over-read repaired in the UI Core; and
- two overbroad open read-graph expectations.

This is sufficient to continue one sealed Terra canary at a time. It is not a
claim that all Terra tasks, Design domains, UI mechanics, or visual preferences
are qualified.
