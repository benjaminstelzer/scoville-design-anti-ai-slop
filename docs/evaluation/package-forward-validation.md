# Pre-SkillOpt package validation

Date: 2026-09-02  
Scope: W-002 implementation candidate; not final qualification

## Candidate identity

- W-002 forward-run `SKILL.md` SHA-256: `6F6BC5605CB4745CA013A412868CA8F4C1AD14CBB3223AAFBFDD48AF80D5E5B7`
- Post-W-003 canonical-record `SKILL.md` SHA-256: `DEA073D4FB341BFEBCA0E1A14CAC78A758F3E07ECDED226CEF54A7BD9AF808D1`
- `modules.yaml` SHA-256: `CF8757F1BB825E42543F067F9B525B16BFD99FB88F9F2D465C0E6ACAB84EDEF3`
- `agents/openai.yaml` SHA-256: `B37AC0963B79B2064CAE877FAF8EE05CDBB2278FE3F26194927B4F7107BE07DC`
- Target: `gpt-5.6-sol`, `xhigh`, local Codex desktop, network disabled
- SkillOpt commit: `ba820b500f9da96685cf2780c7dc85ed4eb6563e`

The artifact forward runs use the W-002 hash. W-003 changed only the
Design-to-UI record field names to the exact accepted schema; static validation
and the paired composition suite cover the later hash. W-004 must record new
hashes for any promoted SkillOpt candidate.

## Static results

- Package validator after W-003: `VALID modules=14 core_tokens=1120
  index_tokens=450 max_expert_tokens=1762 core_plus_three=4074`
- Generated-index check: current
- Skill Creator quick validation: valid
- Native Scoville Plan validation: 0 errors, 0 warnings

The package validator also confirmed canonical module order, allowed status and
intervention enums, empty version-one dependency/conflict lists, closed routing
signals, unique ownership keys, direct one-level links, no orphan references,
resolved source IDs, no expert-to-expert links, metadata constraints, and all
frozen context budgets.

## Selective routing

Final routing runs:

- `design-routing-train-r2`: 10/10
- `design-routing-val-r2`: 8/8

Coverage includes Core-only, every one of the fourteen module IDs, three mixed
three-expert routes, exact-once reads, ordered Core-before-expert phases,
forbidden expert reads, and a forbidden neutral fixture. Earlier R1 failures
were benchmark defects or deliberately broad single-expert wording; targeted
R2/R3 probes established the corrected boundaries before the complete R2 run.

## Forward behavior

Focused run IDs:

- `design-package-poster-r1`
- `design-package-style-r1`
- `design-package-critique-r1`
- `design-package-repair-r1`
- `design-package-imagery-r1`
- `design-package-ui-r1`
- `design-package-type-r1`
- `design-package-motion-r1`

All eight output contracts passed. Six old baseline graders reported only
`shell_call_budget` because their pre-package limit did not include routed
expert reads; no expected-answer, protected-content, source-read, or output-
shape invariant failed. Active Skill contexts were:

| Case | Loaded Skill tokens | Routed experts |
| --- | ---: | --- |
| Poster | 2,632 | composition, typography, colour |
| 80s web style | 2,757 | style, UI, typography |
| Generic landing critique | 1,103 | Core only |
| Poster repair | 2,632 | composition, typography, colour |
| Imagery system | 2,659 | imagery, brand, culture/provenance |
| Clinic UI | 2,727 | composition, typography, UI |
| Typography critique | 1,647 | typography |
| Motion storyboard | 2,556 | motion, composition, information/data |

Every routed context stayed below the 3,800-token Core-plus-one ceiling or the
7,000-token mixed-route ceiling as applicable. The Core-only critique confirms
that the package does not force a reference when SOL can complete the task from
Core and supplied inputs.

## Artifact proof

The poster, 80s web page, repaired poster, clinic UI, and motion storyboard were
extracted, parsed, rendered locally through Playwright, and inspected by one
reviewer. All three SVGs passed XML parsing; both HTML documents exposed an HTML
root; all five renders existed.

Reviewer observations:

- The poster is a coherent editorial signal atlas with strong hierarchy and all
  required programme information legible.
- The repaired poster preserves all supplied content and replaces the broken
  hierarchy with a restrained, readable system.
- The 80s computing page is recognizable and subject-specific across the full
  page, with terminal, ticket, fluorescent, CRT, and analog-noise logic used as
  one system rather than a detached hero effect.
- The clinic UI has a clear three-step flow, factual prototype boundary, strong
  selected state, and no visible overflow/collision in the desktop render.
- The motion sheet has six coherent frames, a persistent datum/continuity spine,
  explicit timing, and a reduced/static equivalent.

This is single-reviewer internal evidence. It does not establish cross-person
preference, production proof, mobile interaction quality, style mastery, or
general market superiority. Those remain W-005 concerns.
