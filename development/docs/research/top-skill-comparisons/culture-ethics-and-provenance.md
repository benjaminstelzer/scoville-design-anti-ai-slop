# Stage-two Skill comparison: Culture, ethics, and provenance

Date: 2026-09-02
Capture: 2026-09-02T13:50:32Z
Target: `references/culture-ethics-and-provenance.md` and its expert-depth audit
Method: `reference-audit-method.md`, Stage two

Local successor baselines: [culture and representation](../../../../scoville-design-anti-ai-slop/references/culture-and-representation.md), [people/privacy/media integrity](../../../../scoville-design-anti-ai-slop/references/people-privacy-and-media-integrity.md), [sustainability claims](../../../../scoville-design-anti-ai-slop/references/sustainability-claims.md), and [asset rights](../../../../scoville-design-anti-ai-slop/references/asset-rights-and-attribution.md)
and [expert-depth audit](../reference-audits/culture-ethics-and-provenance.md)

This is a current, bounded GitHub and public-Skill comparison for inclusive and
cultural authority, ethics, rights, privacy, provenance and sustainability
claims in design. A repository qualified only when it contained a concrete
exact-concern Skill or directly usable agent instruction plus E1 or higher
evidence. Generic policy prose, legal summaries, country-trait recipes and
untested commands remained E0. Captured GitHub stars rank only the qualified
repositories. They do not measure the exact Skill or its safety.

Search used authenticated GitHub repository, code, contents and commit APIs,
plus public web and Skill-directory discovery. Private, renamed, new,
non-English and service-hosted Skills may be absent.

## Decision

Only three qualifying E1+ repositories were found. They are
`jamditis/claude-skills-journalism`,
`mukul975/Privacy-Data-Protection-Skills`, and
`facebookresearch/secpriv-skill`. The useful mechanisms are narrow. They cover
field-level public-derivative metadata, a structured privacy assessment with
data flow and decision state, and a causal privacy source-to-sink audit with
false-positive accounting.

The result also exposes the main shortfall. No E1+ public Skill found combines
living-community authority, stereotype and tokenism diagnosis, sacred or
political material, maps and place names, participant consent, layered asset
rights, documentary and synthetic integrity, sustainability claims, and
release proof. None provides visible examples of culturally accountable
typography, spacing, hierarchy or subject-specific composition. The current
Scoville audit remains the professional baseline for those duties. Candidate
mechanisms should support the proposed flat leaves, not become cultural, legal,
privacy or sustainability authority.

## Qualification and star ranking

E1 means an inspectable example or output artifact. E2 means a reproducible
test, evaluation or deterministic check. E3 requires independent evaluation or
external adoption evidence that supports the capability. None of the ranked
candidates reaches E3 for design, privacy, culture or legal outcomes.

| Rank | Repository and exact path | Stars at capture | Pin, state and latest relevant update | License, data and assets | Evidence level and what it proves |
| --- | --- | ---: | --- | --- | --- |
| 1 | [`jamditis/claude-skills-journalism`, `journalism-core/skills/photo-metadata/SKILL.md`](https://github.com/jamditis/claude-skills-journalism/blob/902cc881b5f9c8a18053d1f60dcc456851db3ee4/journalism-core/skills/photo-metadata/SKILL.md) | 384 | Active, not archived. Repository pin `902cc881b5f9c8a18053d1f60dcc456851db3ee4`. The exact Skill last changed in [`3e0e3a8dffb4157d1ed7fc377cd9f88b90d55946`](https://github.com/jamditis/claude-skills-journalism/commit/3e0e3a8dffb4157d1ed7fc377cd9f88b90d55946) on 2026-08-18. Repository pushed 2026-09-02. | Root [MIT](https://github.com/jamditis/claude-skills-journalism/blob/902cc881b5f9c8a18053d1f60dcc456851db3ee4/LICENSE). Skill code, tests and documentation assets have no separate license notice. Actual photographs, captions, people, location facts, licenses and credentials processed by the tool remain separately governed. | **E2.** An executable embedder and focused tests cover field mapping, Digital Source Type validation, path escape rejection, GPS stripping, metadata round-trip, format differences and failure states. This proves named metadata operations and read-back checks for fixtures. It does not prove consent, factual captions, legal rights, C2PA truth, publisher acceptance or safe real-world release. Tests were inspected, not executed here. |
| 2 | [`mukul975/Privacy-Data-Protection-Skills`, `skills/privacy/conducting-gdpr-dpia/SKILL.md`](https://github.com/mukul975/Privacy-Data-Protection-Skills/blob/9b2ef9eae161c00a17241d42a388571321b33e9f/skills/privacy/conducting-gdpr-dpia/SKILL.md) | 264 | Active, not archived. Repository pin `9b2ef9eae161c00a17241d42a388571321b33e9f`. The exact Skill was added in [`2073373b7ac99dac2d642d914aebabf15b854cda`](https://github.com/mukul975/Privacy-Data-Protection-Skills/commit/2073373b7ac99dac2d642d914aebabf15b854cda) on 2026-03-14. Repository pushed 2026-03-16. | Root and Skill [Apache-2.0](https://github.com/mukul975/Privacy-Data-Protection-Skills/blob/9b2ef9eae161c00a17241d42a388571321b33e9f/LICENSE). The populated fictional template, references and Python script have no separate data license. They are examples, not real approvals or safe factual precedents. | **E2 functional.** A populated fictional DPIA, executable data structures and deterministic screening, safeguard and withdrawal functions are inspectable. They prove that the artifact structure and named calculations can be produced. They do not prove the legal rules, thresholds, facts, mitigation quality, DPO authority or compliance outcome. No independent or human-reviewed evaluation was found. |
| 3 | [`facebookresearch/secpriv-skill`, `SKILL.md`](https://github.com/facebookresearch/secpriv-skill/blob/f2c37778bd85ea9d0e5c510d4d741c3c2b766b27/SKILL.md) | 8 | Active, not archived. Repository pin `f2c37778bd85ea9d0e5c510d4d741c3c2b766b27`. The exact Skill last changed in [`22e3295f9462968c18122071f9cade37f1fcb955`](https://github.com/facebookresearch/secpriv-skill/commit/22e3295f9462968c18122071f9cade37f1fcb955) on 2026-05-20. Benchmark artifacts were updated through the pinned 2026-08-25 head. | Root [MIT](https://github.com/facebookresearch/secpriv-skill/blob/f2c37778bd85ea9d0e5c510d4d741c3c2b766b27/LICENSE). Experiment cases, ground truth, result JSON and runner code have no separate data notice. Treat them as repository fixtures, not transferable independent privacy evidence. | **E2.** The repository includes labeled privacy cases, matched safe cases, transformation microbenchmarks, evaluation runners, result artifacts and failure analysis. This proves a reproducible internal code-audit benchmark and explicit false-positive handling. It does not prove design privacy, consent, export metadata safety, legal compliance or independent effectiveness. The benchmark was inspected, not rerun. |

## Candidate 1: Journalism photo metadata

### Actual mechanism

The Skill creates a tagged derivative rather than treating a spreadsheet as
the final provenance state. It writes caption, credit, rights, accessible text,
Digital Source Type and location fields across EXIF, IPTC and XMP, then reads
the written file back. A separate public-derivative path can strip GPS while
preserving required editorial, rights and accessibility metadata. The workflow
also warns that editing metadata can invalidate a C2PA hard binding and that a
successful upload does not prove metadata survived at the destination.

The strongest implementation evidence is
[`embed.py`](https://github.com/jamditis/claude-skills-journalism/blob/902cc881b5f9c8a18053d1f60dcc456851db3ee4/journalism-core/skills/photo-metadata/embed.py)
plus
[`test_embed.py`](https://github.com/jamditis/claude-skills-journalism/blob/902cc881b5f9c8a18053d1f60dcc456851db3ee4/journalism-core/skills/photo-metadata/test_embed.py).

### What is better than the current Scoville reference

- It verifies the actual written file and can verify the destination copy.
- It separates a controlled master from a purpose-minimized public derivative.
- It treats GPS removal as a field-level privacy decision rather than stripping
  all provenance and attribution.
- It keeps caption, alt text, rights, source type and location as different
  fields with different purposes.
- It rejects path escape and invalid controlled-vocabulary values before
  writing.
- It explains that C2PA validation, metadata survival, disclosure, rights and
  factual truth are separate questions.

The current Scoville audit is stronger on participant use matrices, bystander
and child risk, layered depicted rights, documentary mode, legal authority and
release state. Metadata cannot supply those missing decisions.

### Adoption-priority result

This is a file-integrity mechanism, not visible composition evidence. Embedded
alt text, credits and disclosure still need legible placement in the delivered
artifact, but the repository does not show several rendered subjects or media
that prove typography, spacing, hierarchy or cultural representation quality.

### Synthesize, reject or re-verify

Synthesize the controlled-master versus public-derivative split, field-level
privacy decision, source and destination round-trip, C2PA invalidation warning,
and fail-closed tag validation. Apply the same receipt pattern to filenames,
sidecars, thumbnails, captions, URLs and delivery manifests.

Reject the newsroom-specific field recipe as a universal asset schema. Reject
caption judgments based only on visible pixels when verified editorial context
is required. Do not import external `exiftool` or C2PA tooling into the Design
leaf. Current law, platform behavior, metadata standards and exact file support
must be rechecked. A clean metadata round-trip is not consent, permission,
truth, anonymity or safe release.

## Candidate 2: Privacy Data Protection Skills DPIA

### Actual mechanism

The selected Skill turns privacy assessment into a staged record. It identifies
processing scope, data subjects and categories, systems and recipients, purpose,
necessity, proportionality, risk, mitigation, residual state, DPO advice and
data-subject views. Its populated
[`template.md`](https://github.com/mukul975/Privacy-Data-Protection-Skills/blob/9b2ef9eae161c00a17241d42a388571321b33e9f/skills/privacy/conducting-gdpr-dpia/assets/template.md)
shows the intended output. Its
[`process.py`](https://github.com/mukul975/Privacy-Data-Protection-Skills/blob/9b2ef9eae161c00a17241d42a388571321b33e9f/skills/privacy/conducting-gdpr-dpia/scripts/process.py)
creates structured screening and risk records.

### What is better than the current Scoville reference

- It makes system boundary, data flow, purpose, necessity and proportionality
  explicit before mitigation.
- It separates inherent from residual risk and records conditions.
- It gives DPO advice, owner sign-off and affected-person views distinct places.
- It demonstrates a populated artifact rather than only naming privacy risk.
- It keeps assessment reviewable over time instead of treating approval as a
  one-time boolean.

These mechanisms reinforce Scoville's proposed rights, privacy and provenance
leaf. They do not authorize Design to produce an approved DPIA.

### Adoption-priority result

The example is a dense report with tables and headings. It proves information
can be organized, not that the hierarchy is accessible or visually effective
in a final document. No intended-size render, screen-reader task, translated
version or decision-time study was found. Its fixed report form should not
become a composition template.

### Synthesize, reject or re-verify

Synthesize the data-flow record, stated purpose, less-invasive alternative,
inherent-versus-residual state, affected-person input, owner advice and review
event. In Design, use them to route the exact question and release condition to
privacy authority.

Reject its fixed likelihood percentages, risk multiplication, two-criterion
automatic rule, week-by-week schedule, annual review default, technical-control
catalogue and fictional enforcement facts as reusable authority. Reject one
compliance percentage as proof of privacy. Legal status, lawful basis,
necessity, proportionality and approval remain current jurisdictional decisions.

## Candidate 3: SecPriv Skill

### Actual mechanism

SecPriv analyzes source code through context, source, sink and transformation.
It generates candidate findings, then validates or suppresses them against
evidence. Its internal benchmark pairs privacy defects with safe cases and
transformation cases. The repository keeps ground truth, result JSON, runners
and failure analysis rather than publishing only a checklist.

Relevant evidence includes the
[`privacy` test cases](https://github.com/facebookresearch/secpriv-skill/tree/f2c37778bd85ea9d0e5c510d4d741c3c2b766b27/experiment/test_cases/privacy),
[`evaluate.py`](https://github.com/facebookresearch/secpriv-skill/blob/f2c37778bd85ea9d0e5c510d4d741c3c2b766b27/experiment/runner/evaluate.py),
and
[`analysis_output.json`](https://github.com/facebookresearch/secpriv-skill/blob/f2c37778bd85ea9d0e5c510d4d741c3c2b766b27/experiment/analysis_output.json).

### What is better than the current Scoville reference

- A privacy finding must trace a concrete source, transformation and sink.
- Matched safe cases make false positives visible instead of rewarding more
  alarming findings.
- Suppression and validator stages separate suspicion from supported defect.
- Machine-readable ground truth and results make regression review possible.
- Transformation cases test whether hashing, encryption or tokenization
  changes the risk rather than assuming any transformation is sufficient.

### Adoption-priority result

The evidence concerns Python, JavaScript and HTML source behavior. It provides
no visible-design evidence for representation, consent, public derivatives,
credits or disclosure hierarchy. Its value is the causal audit loop only.

### Synthesize, reject or re-verify

Adapt the loop to design artifacts as input or source, transformation, public
sink, candidate harm, validator evidence and justified suppression. Pair every
seeded failure with a legitimate exception or safe case so the Culture leaf
does not label every cultural reference, person or metadata field a defect.

Reject code-language categories, confidence thresholds and legal mappings as
design rules. Do not infer participant consent, anonymity, lawful basis or
compliance from static source. The mechanism should supplement the person/use,
metadata and release records, not own them.

## Weighted adoption comparison

| Candidate | Applied mechanism | Evidence strength | Visual-foundation evidence | Ownership and dependency fit | Net use |
| --- | --- | --- | --- | --- | --- |
| Photo metadata | Strong field-level provenance and public-derivative proof | E2 focused tests | None beyond documentation layout | Portable record logic, external metadata tools stay out | Best source for actual-file privacy and provenance proof |
| DPIA Skill | Strong structured assessment and populated example, weak legal calibration | E2 functional, no independent validation | Dense tables only, no render or access proof | Privacy/legal authority must remain external | Adopt data-flow and decision-state fields only |
| SecPriv | Strong causal audit and false-positive mechanism for code | E2 internal benchmark | None | Mechanism transfers, domain categories do not | Adopt source-to-sink and paired-safe-case evaluation |

## Mechanisms to synthesize and claims to withhold

### Adopt or test through original Scoville wording

- Record controlled master and distribution derivative separately.
- Inventory visible content, file metadata, sidecars and downstream channel
  behavior, then inspect the actual public artifact.
- Trace privacy risk through input or source, transformation, public sink,
  affected party and evidence-backed validator decision.
- Record purpose, necessity, less-invasive alternative, inherent risk,
  mitigation, residual state, owner, condition and review event.
- Pair failure fixtures with legitimate exceptions and safe cases.
- Keep current authority, dissent, uncertainty and release state explicit.

### Retain from current Scoville instead of importing

- living-community mandate and no cultural-safety self-certification.
- localized stereotype, tokenism, exoticization and erasure diagnosis.
- sacred, secret, political, map and place-name authority.
- participant, child and bystander use matrices.
- layered depicted rights and documentary-versus-synthetic mode.
- whole-impression sustainability claim review.
- smallest premise, source or authority repair with named release stops.

### Reject from the executable package

- country traits, cultural palettes, demographic quotas and generic inclusive
  layouts.
- fixed privacy scores, thresholds, schedules and control catalogues.
- legal conclusions, compliance verdicts or community approval generated by a
  model, template or scanner.
- metadata survival, C2PA, hashing, consent, consultation or certification
  presented as truth, anonymity, rights or lack of harm.
- tool and platform dependencies inside a routed Design leaf.
- copying Apache-licensed prose or code into the MIT package.

## Search exclusions and limits

- Higher-star repositories including `anthropics/claude-for-legal`,
  `revfactory/harness-100`, `mohitagw15856/pm-claude-skills`,
  `rampstackco/claude-skills`, `Klotzkette/claude-fuer-deutsches-recht` and
  `indranilbanerjee/digital-marketing-pro` had relevant Skills. Their exact
  concern remained E0 because no tied output, test or evaluation established
  the claimed privacy, cultural, sustainability or provenance behavior.
- `microsoft/cat-agent-skills` contains an exact EU greenwashing instruction,
  README and metadata only. It also turns scoped and proposed law into a
  mechanical compliance verdict. It remained E0.
- The search found no E1+ specialist for living-community authority, sacred or
  restricted material, stereotype repair, contested maps or environmental
  claim perception in visual design.
- Tests, examples and result artifacts were inspected at pinned commits but not
  executed. No participant, community authority, privacy officer, counsel,
  documentary editor, lifecycle expert or disabled reviewer evaluated an
  output.
- Repository stars can change after capture. They are used only for the frozen
  ranking among qualified candidates.
