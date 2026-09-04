# Stage-two Skill comparison: Brand and visual systems

Date: 2026-09-02
Capture: 2026-09-02T13:29:08Z
Target: `references/brand-and-visual-systems.md` and its expert-depth audit
Method: `reference-audit-method.md`, Stage two

Local baselines: [current executable reference](../../../references/brand-and-visual-systems.md)
and [expert-depth audit](../reference-audits/brand-and-visual-systems.md)

This is a current, bounded GitHub and public-Skill comparison for brand
identity, visual systems, governance and mark reproduction. Generic marketing,
campaign-copy and social-template Skills were excluded unless they contained a
directly usable identity-system mechanism and an E1 or higher artifact.
Repositories are ranked by captured GitHub stars only after qualification.
Stars describe repository popularity, not evidence for the exact Skill.

Search used authenticated GitHub repository, code, contents and commit APIs,
plus public web and Skill-directory discovery. Private, renamed, new,
non-English and service-hosted Skills may be absent. Visible typography,
spacing, negative space, hierarchy and subject-specific composition were the
primary adoption lens. Governance prose alone did not count as visible quality.

## Decision

Only three repositories found met the exact-domain and E1 threshold:
`rampstackco/claude-skills`, `tight-studio/OpenBrand`, and
`magnus919/agent-skills`. Rampstack supplies the strongest visible identity
examples, though it relies heavily on numerical recipes and broad unsupported
claims. OpenBrand provides a useful source-URL and candidate-asset inventory,
but extracts site signals rather than approved identity rules. Magnus provides
the strongest durable brand-book registry and validation mechanism, but its
templates and tests do not demonstrate design quality.

The current Scoville audit remains stronger on authority and status,
primary-versus-signature-versus-supporting cues, invariant and variable grammar,
recognition claim ceilings, mark and touchpoint stress, campaign expiry,
canonical registry repair, rights escalation and Brand-to-UI ownership. The
best synthesis is therefore narrow: combine visible direction comparison with
a candidate-source inventory and a validated asset/status registry. Do not
import logo, palette, type, spacing, maturity, governance or recognition
recipes.

## Qualification and star ranking

E1 means an inspectable example or output artifact. E2 means a reproducible
test, evaluation or deterministic check. E3 requires independent evaluation
or external adoption evidence that supports the capability. None of the three
ranked candidates reaches E3 for identity quality, recognition or governance
outcomes.

| Rank | Repository and exact path | Stars at capture | Pin, state and latest relevant update | License, assets and data | Evidence level and what it proves |
| --- | --- | ---: | --- | --- | --- |
| 1 | [`rampstackco/claude-skills`, `skills/brand-identity/SKILL.md`](https://github.com/rampstackco/claude-skills/blob/a67dd34c609f034c0cfd736a348659bbdf1605bf/skills/brand-identity/SKILL.md) | 812 | Active, not archived. Repository pin `a67dd34c609f034c0cfd736a348659bbdf1605bf`. The exact Skill last changed in [`ac2b078f5025336c475d72a6fafa256d28aa6173`](https://github.com/rampstackco/claude-skills/commit/ac2b078f5025336c475d72a6fafa256d28aa6173) on 2026-05-07. Repository pushed 2026-08-28. | Root [MIT](https://github.com/rampstackco/claude-skills/blob/a67dd34c609f034c0cfd736a348659bbdf1605bf/LICENSE). Skill, references and showcase images have no separate asset notice and are repository assets under MIT. The fictional-looking marks remain examples, not cleared marks for reuse. Any imported fonts, references or generated assets need their own rights and trademark checks. | **E1.** Desktop and mobile showcase images give inspectable logo, mark and art-direction examples. They prove visible variety and a comparison presentation exists. They do not prove the Skill produced them, that users recognize the identities, that marks survive production stress, or that rules improve outcomes. No exact-Skill output test or evaluation was found. |
| 2 | [`tight-studio/OpenBrand`, `SKILL.md`](https://github.com/tight-studio/OpenBrand/blob/a21d34fadc3dcf15271d71fdb3f7d95baf7578d8/SKILL.md) | 791 | Active, not archived. Repository pin `a21d34fadc3dcf15271d71fdb3f7d95baf7578d8`. The exact Skill last changed in [`dd919d17b2da39d1125a4ef0201140b6baf9ba92`](https://github.com/tight-studio/OpenBrand/commit/dd919d17b2da39d1125a4ef0201140b6baf9ba92) on 2026-03-18. Repository pushed 2026-05-12. | Root [MIT](https://github.com/tight-studio/OpenBrand/blob/a21d34fadc3dcf15271d71fdb3f7d95baf7578d8/LICENSE) for code and Skill. Extracted logos, images, fonts and site content remain owned and licensed by their source sites. MIT does not clear those outputs for reuse. The tool requires local Node dependencies and may use remote service or fallback access. | **E2.** Demo output and integration tests for GitHub, Stripe and example.com are inspectable. They prove that candidate asset URLs, dimensions, colours and structured results can be extracted for named live sites and that failure paths exist. Live-site tests are mutable. They do not prove that results are approved, canonical, complete, rights-cleared or correctly assigned to brand roles. |
| 3 | [`magnus919/agent-skills`, `brand-designer/SKILL.md`](https://github.com/magnus919/agent-skills/blob/de968dfdfb5ac92336a4915dad4bb56a27fe0207/brand-designer/SKILL.md) | 65 | Active, not archived. Repository pin `de968dfdfb5ac92336a4915dad4bb56a27fe0207`. The exact Skill last changed in [`035e58d3e39690361596901ab8f17222ab9baf02`](https://github.com/magnus919/agent-skills/commit/035e58d3e39690361596901ab8f17222ab9baf02) on 2026-09-02. Repository pushed 2026-09-02. | Root [`LICENSE.md`, MIT](https://github.com/magnus919/agent-skills/blob/de968dfdfb5ac92336a4915dad4bb56a27fe0207/LICENSE.md). The exact Skill also declares MIT. Templates and scripts are repository-authored. Generated or imported marks, fonts and images remain subject to their own rights. Image-generation backends are optional external dependencies. | **E2 functional.** Seven brand-book templates, an asset inventory, a CLI and [`brand-book_test.sh`](https://github.com/magnus919/agent-skills/blob/de968dfdfb5ac92336a4915dad4bb56a27fe0207/brand-designer/scripts/brand-book_test.sh) are inspectable. The test proves initialization, expected files, validation, strict mode, compilation, JSON output and refusal on a non-empty directory. It does not prove the content is true, the design is professional, the brand is recognized, or the governance is adopted. Generic eval prompts are not run outcome evidence. |

## Candidate 1: Rampstack `brand-identity`

### Claimed scope and observed mechanism

The Skill assumes an approved name and positioning, then routes mark, colour,
type, imagery, iconography, motion and application work into a visual identity
system. It separates neighboring concerns such as early ideation, brand voice,
style-guide documentation and UI implementation. It asks for variants,
context stress, font licensing, fallbacks and representative applications.

Its references are much more prescriptive than its useful routing boundary.
They include fixed counts, pixel sizes, palette sizes, type-family counts,
scale sizes, line-height and measure ranges, mockup counts and a near-universal
sequence. Those values are examples at best, not identity-system laws.

### What is better than the current Scoville reference

- It starts only after name and positioning are established, which reduces
  accidental strategy invention.
- It distinguishes identity production from ideation, voice, documentation and
  product-UI implementation.
- Mark variants, application stress, font license and fallback, imagery
  direction and motion are concrete work areas rather than a palette-only view.
- It shows multiple visibly distinct directions together, which supports
  comparative critique better than an isolated single mark.
- It recognizes that marks, type, colour, imagery and applications form one
  system rather than a logo file plus templates.

The Scoville audit is still stronger on evidence states, approved versus
proposed rules, canonical masters, variable grammars, campaign lifecycle,
consumer-recognition ceilings, exception governance and parent-cause repair.

### Adoption-priority result

The inspected [`logo-design-showcase-desktop.png`](https://github.com/rampstackco/claude-skills/blob/a67dd34c609f034c0cfd736a348659bbdf1605bf/assets/showcase/logo-design-showcase-desktop.png)
presents six fictional directions in a readable grid. The directions vary in
mark construction, serif and sans treatment, wordmark versus symbol, tone and
category signal. Labels and spacing support comparison without overpowering
the work. This is useful visible E1 evidence.

The same grid cannot prove that a direction survives small size, one-colour,
reversal, distance, localization, co-branding or dense real content. It also
cannot prove distinctiveness in memory, legal clearance or professional
governance. The gallery format may reward surface variety while hiding whether
the identity grammar works across actual touchpoints.

### Synthesize, reject or re-verify

Synthesize the approved-input gate, neighboring-owner separation, simultaneous
direction comparison, application stress categories, font-rights check and
fallback requirement. Use the showcase pattern only as a comparison aid, then
test selected systems on real-content extremes and required production forms.

Reject fixed clear-space or minimum-size values, palette counts, family counts,
type scales, line-height ranges, measure ranges, mockup counts and universal
workflow order. Reject unsupported cost, prevalence, frame-rate or recognition
claims. Brand may define identity expression, but UI owns functional semantic
states and implementation proof.

## Candidate 2: OpenBrand

### Claimed scope and observed mechanism

OpenBrand accepts a website URL and returns candidate logos, images, colours,
fonts and structured JSON. It records source URLs, file types, dimensions and
other extraction details. A local CLI, API and MCP path use site metadata,
markup and visual assets, with remote fallbacks available.

This is a discovery and inventory mechanism, not proof of an approved brand
system. Website signals can contain campaigns, obsolete favicons, tracking
assets, UI state colours, vendor marks or default black and white. The tool's
role labels are inferences unless an owner or canonical registry confirms them.

### What is better than the current Scoville reference

- Candidate assets retain source URLs and machine-readable metadata instead of
  arriving as unexplained downloads.
- Multiple logos and image variants can be surfaced for conflict detection.
- The raw structured output can support a later canonical-asset audit.
- Failure handling prevents every empty extraction from being presented as a
  complete identity.
- A visual result and raw result are separate, which supports human comparison
  and reproducibility.

This mechanism concretizes the Scoville audit's requirement to distinguish an
observed asset from an approved, released, rights-cleared or registered asset.
It does not supply the missing authority.

### Adoption-priority result

The inspected demo result for Tight Studio uses clear grouping, readable asset
labels, generous spacing and a simple source-to-result sequence. It displays
candidate favicons, touch icons, colour swatches and an image. The visible
result also exposes the core failure mode. White, black and gray are assigned
primary, secondary and accent labels from site signals. That is a clean
inventory presentation, not proof of brand roles or an identity grammar.

No artifact demonstrates intended typography selection, mark reproduction,
co-branding, responsive identity application or governance. The visual output
should therefore inform source collection only.

### Synthesize, reject or re-verify

Synthesize a read-only candidate inventory with canonicalized source URL,
capture date, media type, dimensions, checksum and observed context. Label each
item `observed` until a named owner or authoritative registry supplies its
status. Preserve conflicts rather than choosing the most convenient file.

Reject automatic conversion from scraped asset to approved master, primary
colour, official font, reusable image or complete style guide. Reject live
network and remote service dependencies in the executable leaf. Never treat
the MIT tool license as permission to reuse third-party outputs. A later
production task must verify source rights, trademark status, technical quality
and current owner authority.

## Candidate 3: Magnus `brand-designer`

### Claimed scope and observed mechanism

The Skill builds a brand-book directory with strategy, visual identity, voice,
applications, governance, asset inventory and a compact brand card. Its CLI can
initialize, validate and compile the structure. It also provides optional image
generation and a decision tree that changes process by company maturity.

The durable artifact topology is the valuable mechanism. The included
templates are empty scaffolds, and several contained values and maturity rules
are recipes. A complete file set proves administrative completeness, not an
approved or effective identity.

### What is better than the current Scoville reference

- Brand guidance is a versionable artifact graph rather than one long prose
  response.
- Strategy, visual rules, voice, applications, governance and assets have
  distinct files and can retain different owners and statuses.
- Asset inventory and governance are required deliverables rather than optional
  afterthoughts.
- Initialization, validation and compilation are separate operations.
- Strict validation and refusal to overwrite a non-empty directory are useful
  integrity mechanisms.

The Scoville audit already specifies the richer semantic contract those files
need: source, owner, version, state, scope, approval evidence, rights,
supersession, deprecation and migration.

### Adoption-priority result

No populated brand-book example or rendered identity family was found in the
exact Skill. The templates and CLI tests therefore provide no visible evidence
for typography, spacing, negative space, hierarchy, mark reproduction or
subject-specific composition. They should not influence visual rules. Their
value is restricted to artifact completeness and state management.

### Synthesize, reject or re-verify

Synthesize a small canonical registry and a separate validation or compilation
step. Require stable IDs, source, owner, status, version, scope, rights,
approval evidence, successor and affected consumers. Compile human-readable
guidance from that record without changing its facts.

Reject company-size decision trees, universal section order, imported gold
standard claims, fixed clear space, minimum size, type values, CMYK or spot
completeness without production authority, automatic UI functional colours,
fixed governance cadence and semantic-versioning recipes. Do not add image
backend dependencies. Empty templates and passing structure tests cannot
authorize strategy, assets or release.

## Weighted adoption comparison

| Candidate | Identity judgment and repair | Visible typography, spacing and composition | Evidence and reproducibility | Ownership and dependency fit | Net use |
| --- | --- | --- | --- | --- | --- |
| Rampstack `brand-identity` | Broad generation guidance, weak authority and causal repair | Strongest visible E1 comparison, but gallery-only and recipe-heavy | Examples without exact-Skill outcome tests | Mostly portable concepts, several Brand-to-UI and rights hazards | Adopt comparison and stress mechanisms, reject numbers and claims |
| OpenBrand | Strong candidate discovery, no approved-system judgment | Clean inventory output, no identity application proof | E2 live-site integration tests with mutable inputs | External network and third-party asset rights are major blockers | Adopt source inventory pattern only |
| Magnus `brand-designer` | Strong artifact scaffolding, weak professional design reasoning | No populated or rendered identity evidence | E2 functional CLI checks only | Portable registry idea, templates and optional backends must stay out | Adopt status registry and validation split only |

## Mechanisms to synthesize and claims to withhold

### Adopt or test through original Scoville wording

- Start from supplied approved strategy, name, claims and canonical assets.
- Compare materially different visual directions together before selecting one.
- Inventory observed assets with source, date, dimensions and checksum, but do
  not assign approval or identity role without authority.
- Maintain one canonical asset and rule registry with stable IDs, owner, state,
  version, scope, rights, approval, successor and consumer references.
- Separate registry validation from human-readable guideline compilation.
- Stress the system across actual required small, one-colour, reversed,
  localized, dense, responsive, co-brand and production contexts.
- Trace visible drift or uniformity to the canonical rule, alias, status or
  campaign-lifecycle cause before repairing consumers.

### Retain from current Scoville instead of importing

- proposed, approved, released, deprecated, cleared and registered evidence
  states.
- primary identifiers, signature cues, supporting rules and channel variables.
- invariants with allowed transformations, prohibited transformations and
  fallbacks.
- recognition as a hypothesis until target participants provide evidence.
- campaign ownership, scope, inheritance, expiry and retirement.
- canonical-parent repair, deprecation and migration rather than artifact-by-
  artifact patching.
- Brand-to-UI, production, rights, trademark, strategy and specialist-mark
  boundaries.

### Reject from the executable package

- fixed font pairings, family counts, palette counts, spacing values, type
  scales, clear-space values, minimum sizes, layout grids and application
  counts.
- universal style, maturity, governance-cadence or workflow recipes.
- scraped or generated assets presented as approved, owned, cleared or
  canonical.
- website colours promoted directly into product semantic roles.
- external network, MCP, image-generation or proprietary service dependencies.
- claims that examples, CLI tests, stars or extractor success prove consumer
  recognition, distinctiveness, legal clearance, adoption or professional
  visual quality.

## Search exclusions and limits

- `majiayu000/claude-skill-registry` is a generated mirror. Its brand entries
  did not provide a tied E1 output or reproducible test, and individual
  third-party licenses remained controlling. It was excluded at E0.
- `claude-office-skills/skills`, `gtmagents/gtm-agents`, `JetBrains/skills` and
  `tonone-ai/tonone` contained exact or neighboring brand prose, templates or
  structural tests. No populated exact-Skill output or outcome test established
  E1 for professional identity design, so they were not ranked.
- Generic marketing, voice, campaign, social-template, logo-prompt and UI theme
  Skills were excluded. A brand mention is not identity-system ownership.
- Tests and artifacts were inspected at pinned commits but were not executed in
  this comparison. No mark source was preflighted, no production variant was
  rendered, no audience recognized a system, no trademark search occurred, and
  no brand owner approved an artifact.
- Repository stars can change after capture. They are used only to apply the
  frozen ranking rule among qualified candidates.
