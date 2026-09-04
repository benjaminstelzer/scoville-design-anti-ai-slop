# Stage-two Skill comparison: Sources and attribution

Date: 2026-09-02
Capture: 2026-09-02T13:50:32Z
Target: `references/sources-and-attribution.md` and its expert-depth audit
Method: `reference-audit-method.md`, Stage two

Local successor baselines: [source verification](../../../references/source-verification-and-evidence.md) and [asset rights and attribution](../../../references/asset-rights-and-attribution.md)
and [expert-depth audit](../reference-audits/sources-and-attribution.md)

This is a current, bounded GitHub and public-Skill comparison for factual claim
verification, citation support, source inspection, licensing, attribution,
asset ledgers and provenance. Broad research Skills did not qualify merely for
producing links. A candidate needed a concrete exact-concern Skill or directly
usable instruction plus E1 or higher evidence. Captured GitHub stars rank only
qualified repositories and do not measure capability.

Search used authenticated GitHub repository, code, contents and commit APIs,
plus public web and Skill-directory discovery. Private, renamed, new,
non-English and service-hosted Skills may be absent.

## Decision

The three most-starred qualifying repositories found are
`NousResearch/hermes-agent`, `semaphoreui/semaphore`, and
`Spark-To-Paper-Skills/paperjury`. They contribute three distinct mechanisms.
Hermes binds citation IDs to retrieval-time URLs and mechanically verifies the
rendered source block. Semaphore compiles dependency records into a shipped
attribution artifact with a fail-closed policy stage. PaperJury keeps durable
claim and citation repair state, detects cross-document dependencies and shows
before-and-after evidence.

No candidate covers the combined professional scope in the current Scoville
audit. Hermes does not determine whether a paraphrase is semantically supported
or a source is independent and current. Semaphore is a repository-specific
software notice generator with unsafe universal license rules. PaperJury is a
CS-paper editing system, not a fact checker or asset-rights manager. The
mechanisms support the audit's proposed split between source verification and
asset rights/attribution. They do not replace source, domain, rights or legal
authority.

## Qualification and star ranking

E1 means an inspectable example or output artifact. E2 means a reproducible
test, evaluation or deterministic check. E3 requires independent evaluation or
external adoption evidence that supports the capability. Repository use or
stars do not elevate internal tests to E3.

| Rank | Repository and exact path | Stars at capture | Pin, state and latest relevant update | License, data and assets | Evidence level and what it proves |
| --- | --- | ---: | --- | --- | --- |
| 1 | [`NousResearch/hermes-agent`, `skills/research/grounded-citations/SKILL.md`](https://github.com/NousResearch/hermes-agent/blob/87ad7aa0b072e621c5d4e437b7345471e66f395d/skills/research/grounded-citations/SKILL.md) | 239,839 | Active, not archived. Repository pin `87ad7aa0b072e621c5d4e437b7345471e66f395d`. The exact Skill last changed in [`c49fa88b80753071e7b7bb83e2882232e43e87c0`](https://github.com/NousResearch/hermes-agent/commit/c49fa88b80753071e7b7bb83e2882232e43e87c0) on 2026-08-30. Repository pushed 2026-09-02. | Root and exact Skill [MIT](https://github.com/NousResearch/hermes-agent/blob/87ad7aa0b072e621c5d4e437b7345471e66f395d/LICENSE). Script and tests have no separate data or asset notice. Retrieved pages and stored evidence retain their original rights, privacy and quotation limits. | **E2.** Focused tests cover URL registration, stable IDs, concurrent writes, rendered source blocks, unknown-ID rejection, URL mismatch, verbatim evidence matching, evidence gates and idempotent replacement. This proves ledger and structural citation behavior for fixtures. It does not prove semantic support, source truth, independence, currentness, lawful quotation or factual correctness. Tests were inspected, not executed here. |
| 2 | [`semaphoreui/semaphore`, `.claude/skills/semaphore-third-party-licenses/SKILL.md`](https://github.com/semaphoreui/semaphore/blob/89a2c01a203b715eb6f49d95fdf96f75f0fc1b80/.claude/skills/semaphore-third-party-licenses/SKILL.md) | 14,090 | Active, not archived. Repository pin `89a2c01a203b715eb6f49d95fdf96f75f0fc1b80`. The exact Skill last changed in [`652993ccb9e5108b1331a7440cc734820811b82f`](https://github.com/semaphoreui/semaphore/commit/652993ccb9e5108b1331a7440cc734820811b82f) on 2026-05-27. Repository pushed 2026-09-02. | Root Skill and scripts [MIT](https://github.com/semaphoreui/semaphore/blob/89a2c01a203b715eb6f49d95fdf96f75f0fc1b80/LICENSE). The generated inventory describes separately licensed Go and npm dependencies. Root MIT does not license those components or their notices. The exact license texts and provider metadata remain external evidence. | **E1.** Collection, classification and generation scripts plus a populated 116-component [`THIRD-PARTY-LICENSES.md`](https://github.com/semaphoreui/semaphore/blob/89a2c01a203b715eb6f49d95fdf96f75f0fc1b80/THIRD-PARTY-LICENSES.md) are inspectable. They prove that a repository-specific dependency inventory was generated and formatted. No focused tests or independent legal review were found, so they do not prove completeness, license interpretation, compatibility or contractual compliance. |
| 3 | [`Spark-To-Paper-Skills/paperjury`, `SKILL.md`](https://github.com/Spark-To-Paper-Skills/paperjury/blob/53c75e86285dc5b38e8d60c6eb0b0adaf4838250/SKILL.md) | 1,067 | Active, not archived. Repository pin `53c75e86285dc5b38e8d60c6eb0b0adaf4838250`. The exact Skill last changed in [`07a24c06b10f7740d8932d0c2693c1e342f090b7`](https://github.com/Spark-To-Paper-Skills/paperjury/commit/07a24c06b10f7740d8932d0c2693c1e342f090b7) on 2026-06-12. Repository pushed 2026-08-14. | Root and exact Skill [MIT](https://github.com/Spark-To-Paper-Skills/paperjury/blob/53c75e86285dc5b38e8d60c6eb0b0adaf4838250/LICENSE). Tests and dogfood reports have no separate asset notice. The included original and revised papers are repository evidence, not reusable source material or independent review. | **E2.** Ledger, cross-reference, compile, compliance and document tests plus original/revised PDFs and a run report are inspectable. They prove durable issue state, cross-reference risk detection, named deterministic gates and a self-reported repair example. They do not prove source retrieval, citation entailment, external factual correctness, asset rights or independent outcome quality. |

## Candidate 1: Hermes grounded citations

### Actual mechanism

Hermes registers a source URL at retrieval time, assigns a stable local ID and
generates the source block from that ledger. The model cites only IDs the script
issued. High-stakes mode can attach a verbatim excerpt only when it appears in
the supplied fetched text. Verification rejects unknown IDs, mismatched URLs,
missing source blocks and cited sources without evidence. The implementation is
[`sources.py`](https://github.com/NousResearch/hermes-agent/blob/87ad7aa0b072e621c5d4e437b7345471e66f395d/skills/research/grounded-citations/scripts/sources.py),
with focused coverage in
[`test_grounded_citations_skill.py`](https://github.com/NousResearch/hermes-agent/blob/87ad7aa0b072e621c5d4e437b7345471e66f395d/tests/skills/test_grounded_citations_skill.py).

### What is better than the current Scoville reference

- Source identity is created at retrieval time, not reconstructed from prose.
- Citation IDs, URLs and rendered source blocks have one mechanical owner.
- Verbatim evidence must occur in the inspected text supplied to the script.
- Unknown IDs and source-block drift fail rather than produce plausible output.
- Concurrent writers have a shared-ledger mechanism and stable identities.
- Unverified model knowledge can remain visibly unresolved.

The current Scoville audit is stronger on atomic claim types, source role,
semantic evidence relation, origin independence, valid time, corrections,
rights, asset scope and authority ceilings.

### Synthesize, reject or re-verify

Synthesize retrieval-time registration, stable claim and source IDs,
mechanically compiled source blocks, quote-to-inspected-text matching,
idempotent regeneration and explicit structural-versus-semantic proof labels.
Add inspected scope, locator, source role, version, relation and correction
events before calling the record professional.

Reject the fixed maximum citation count, citation-density threshold, bracket
style and Hermes cache dependency. An `[unverified]` marker must not count as
positive evidentiary coverage. Exact quotation proves byte-level presence, not
that the source supports the paraphrase. URL normalization must not collapse
materially different versions or query-selected records. Stored excerpts must
remain within privacy, confidentiality and copyright limits.

## Candidate 2: Semaphore third-party licenses

### Actual mechanism

The Skill collects Go and npm production dependencies into caches, classifies
detected licenses, stops on forbidden or unknown states, then compiles a sorted
human-readable notice. It asks for a diff against the prior artifact and keeps
the dependency manifests read-only. The populated notice provides inspectable
output rather than only a template.

### What is better than the current Scoville reference

- Collection, policy classification and final attribution output are separate
  stages.
- Unknown license state is visible and can stop output generation.
- Component, version, detected license and source URL are compiled from records.
- Production scope is declared instead of automatically listing every
  development tool.
- The generated artifact is diffable and reproducible from named commands.
- A second guard in the generator refuses to bypass an unresolved policy state.

These mechanisms are useful for Scoville's proposed asset-rights and
attribution leaf. The current Scoville audit remains stronger on exact legal
instrument, asset-level exceptions, intended use, fonts, images, data,
generated assets, attribution placement and counsel review.

### Adoption-priority result

The generated Markdown has a readable summary and alphabetical component
tables. That is useful information organization, not proof that the notice is
complete, accessible or legally sufficient in the shipped product. The Skill
also says full license texts are embedded while the inspected generated file
links to sources and says texts are preserved elsewhere. That inconsistency
must block any claim of complete notice output.

### Synthesize, reject or re-verify

Synthesize the inventory-to-policy-to-output pipeline, fail-closed unknown
state, generated notice, prior-output diff and final package coverage check.
Use stable asset IDs and hashes rather than package name alone, and compile the
actual medium-specific credit or notice from verified records.

Reject the allowlist and denylist as universal legal interpretation. Reject the
static-link, subprocess, dual-license and production-only conclusions outside
the exact package and counsel-approved policy. Do not automatically choose the
shortest license in an `OR` expression. Detected metadata, SPDX identifiers and
repository roots do not prove rightsholder authority, compatibility or absence
of undeclared assets. Do not copy project-specific scripts or policy prose.

## Candidate 3: PaperJury

### Actual mechanism

PaperJury keeps a machine-authoritative issue ledger with stable passage
references, state transitions, reasons for dropped issues and close criteria
for repairs. Before editing, deterministic guards compare changed salient
tokens, citations, labels, numbers and symbols against other passages. Compile
and meaning checks follow the patch. The included
[`RUN_REPORT.md`](https://github.com/Spark-To-Paper-Skills/paperjury/blob/53c75e86285dc5b38e8d60c6eb0b0adaf4838250/samples/dogfood/RUN_REPORT.md)
reports fixed contradictions, a dangling citation, fabricated claims and
remaining unresolved items against original and revised PDFs.

### What is better than the current Scoville reference

- Claim and citation repair is treated as a dependency problem across the
  whole artifact.
- A durable JSON record, not a prose summary, owns issue state.
- Dropped findings need reasons and fixable findings need closure criteria.
- Cross-reference checks detect when a local number or citation edit can make
  another section stale.
- The before-and-after report preserves unresolved failures instead of claiming
  perfect completion.
- Compile and meaning review are separate gates after editing.

The current Scoville audit is stronger on retrieval, actual source inspection,
claim-to-evidence relations, correction history across downstream artifacts and
all asset-rights concerns.

### Synthesize, reject or re-verify

Synthesize stable claim IDs, dependent-artifact mapping, append-only repair
events, explicit close criteria, cross-reference risk scanning and a final
reconciliation of source records, claims, captions, credits and exports.

Reject the multi-agent courtroom, fixed reviewer counts, quorum thresholds,
CS-venue profiles, update check, auto-edit loop and LaTeX-specific machinery.
An internal consistency fix is not factual verification. A resolved dangling
citation can mean deletion, replacement or source inspection, depending on the
claim. Human-verified dogfood by the authors is useful E2 evidence, not
independent E3 validation.

## Weighted adoption comparison

| Candidate | Claim or rights mechanism | Evidence strength | Output quality evidence | Ownership and dependency fit | Net use |
| --- | --- | --- | --- | --- | --- |
| Hermes grounded citations | Strong source identity and structural evidence chain | E2 focused tests | Generated source blocks only | Portable concepts, Hermes paths and citation style stay out | Best source-verification mechanism |
| Semaphore notices | Strong inventory-to-output path, unsafe legal policy | E1 populated artifact and scripts | Readable tables, no access or legal sufficiency proof | Repository and ecosystem specific | Adopt compiler and fail-closed state only |
| PaperJury | Strong correction dependency and durable repair state | E2 tests plus dogfood output | Before-and-after PDFs exist, self-reported outcome only | Heavy academic workflow must stay out | Adopt dependency-aware correction record only |

## Mechanisms to synthesize and claims to withhold

### Adopt or test through original Scoville wording

- Register sources and assets when actually inspected or acquired.
- Assign stable claim, source and asset IDs and derive visible source or credit
  output mechanically from verified records.
- Separate byte-level evidence presence, structural coverage, semantic support,
  rights review and production shipment.
- Keep unknown, inaccessible, unsupported, disputed and rejected states
  distinct and fail closed for consequential unresolved facts or rights.
- Map claim and asset dependencies before repair, then update every affected
  caption, figure, credit, export and notice.
- Preserve append-only correction history and explicit closure evidence.

### Retain from current Scoville instead of importing

- atomic claim wording, type, scope and checkability.
- source role, inspected scope, locator, evidence relation and origin chain.
- publication, effective, observation, retrieval, correction and recheck dates.
- exact license instrument, material, rightsholder and intended-use matrix.
- separate branches for images, cultural objects, fonts, data and generated
  assets.
- actual medium-specific attribution plus package coverage and human authority.

### Reject from the executable package

- citation counts, coverage percentages, fixed source caps and confidence
  scores.
- universal license allowlists, deny lists, compatibility shortcuts or one
  attribution template.
- repository license, URL, DOI, checksum, SPDX, C2PA or exact quote presented as
  truth, permission or completeness.
- product-specific caches, toolchains, network checks, workflows and automatic
  editing.
- copied third-party scripts, policy prose, papers, datasets or notice text
  without compatible license and need.
- fact-checker, archivist, rights-manager or lawyer equivalence claims.

## Search exclusions and limits

- `huytieu/COG-second-brain` and `wasabeef/claude-code-cookbook` had more stars
  than PaperJury and exact neighboring Skills, but no tied example, output,
  test or evaluation raised those Skills above E0.
- `laadtushar/fact-checker-AI-Skill`, `SkillMedev/skills`,
  `starshard-ai/skill-provenance`, citation-check Skills and image-license
  Skills supplied useful prose mechanisms but lacked stronger E1 evidence or
  ranked below the selected candidates.
- Generic web research, academic writing, SBOM, legal and repository-compliance
  Skills were excluded unless the exact source, citation, rights or attribution
  mechanism had inspectable evidence. PaperJury qualified only for its directly
  evidenced claim, citation and correction subsystem.
- Tests and artifacts were inspected at pinned commits but not executed. No
  source corpus was fact-checked, no license package was cleared, no production
  attribution was rendered, and no editor, subject expert, rights holder,
  archivist, disabled reviewer or counsel approved an output.
- Repository stars can change after capture. They are used only for the frozen
  ranking among qualified candidates.
