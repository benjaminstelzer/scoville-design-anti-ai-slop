# Stage-two Skill comparison: Information and data

Date: 2026-09-02
Capture: 2026-09-02T13:29:08Z
Target: `references/information-and-data.md` and its expert-depth audit
Method: `reference-audit-method.md`, Stage two

Local successor baselines: [information design](../../../references/information-design-and-data-visualization.md), [cartography](../../../references/cartography-and-spatial-data.md), and [diagrams](../../../references/diagrams-and-relational-information.md)
and [expert-depth audit](../reference-audits/information-and-data.md)

This is a current, bounded GitHub and public-Skill comparison. It covers
charts, maps, diagrams, tables and dashboards. Repositories are ranked by
captured GitHub stars only after an exact-domain Skill or directly usable
agent instruction and an E1 or higher artifact were found. Stars describe
repository popularity, not the quality or adoption of the exact Skill.
Search used authenticated GitHub repository, code, contents and commit APIs,
plus public web and Skill-directory discovery. Private, renamed, new,
non-English and service-hosted Skills may be absent.

## Decision

The three most-starred qualifying repositories found are
`yizhiyanhua-ai/fireworks-tech-graph`, `bruin-data/dac`, and
`openai/role-specific-plugins`. Their strongest reusable mechanisms are a
typed diagram intermediate representation with deterministic semantic and
geometry checks, a reviewable source-to-metric-to-widget dashboard contract,
and an explicit dashboard purpose, grain, freshness and reconciliation pass.

No ranked candidate is a complete information-design curriculum. Fireworks
explicitly excludes quantitative charts. DAC and the OpenAI dashboard Skill
focus on application delivery and do not cover cartographic projection,
normalization, classification, boundary vintage or spatial privacy. The
current Scoville audit remains stronger on chart-versus-table decisions,
causal encoding critique, uncertainty and missingness, map truth, locale,
accessible equivalence, cross-media handoff and evidence ceilings. The useful
external mechanisms should therefore be synthesized into the proposed three
flat leaves, not imported as one product-bound dashboard or diagram stack.

## Qualification and star ranking

E1 means an inspectable example or output artifact. E2 means a reproducible
test, evaluation or deterministic check. E3 requires independent evaluation
or external adoption evidence that supports the capability. None of the three
ranked candidates reaches E3 for design quality.

| Rank | Repository and exact path | Stars at capture | Pin, state and latest relevant update | License, assets and data | Evidence level and what it proves |
| --- | --- | ---: | --- | --- | --- |
| 1 | [`yizhiyanhua-ai/fireworks-tech-graph`, `skills/fireworks-tech-graph/SKILL.md`](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/e9c7a9351dee5861707a7ec5560248bf5e7b84b5/skills/fireworks-tech-graph/SKILL.md) | 11,063 | Active, not archived. Repository pin `e9c7a9351dee5861707a7ec5560248bf5e7b84b5`. The exact Skill last changed in [`ba625a6f1f2f8d21219d122856e527bf9f804f25`](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/commit/ba625a6f1f2f8d21219d122856e527bf9f804f25) on 2026-07-17. Repository pushed 2026-08-25. | Root and Skill [MIT](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/e9c7a9351dee5861707a7ec5560248bf5e7b84b5/LICENSE). Bundled glyphs are provider-neutral. The [icon manifest](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/e9c7a9351dee5861707a7ec5560248bf5e7b84b5/assets/icons/cloud/manifest-v1.json) keeps official vendor packs external and links their sources. Sample diagrams are repository assets under MIT. External vendor marks remain separately governed if later installed. | **E2.** Sample PNG/GIF outputs, interactive HTML, semantic-contract tests, geometry-contract tests and SVG validators are inspectable. They prove that the typed IDs, edge roles, collision and crossing rules, reserved regions, paint order and output validation exist for fixtures. They do not prove source-model truth, professional visual quality, accessibility or independent adoption. Tests were inspected, not executed here. |
| 2 | [`bruin-data/dac`, `.claude/skills/create-dashboard/SKILL.md`](https://github.com/bruin-data/dac/blob/db4aeb73fc8597bf1f3718ac654ae37621dc6f4e/.claude/skills/create-dashboard/SKILL.md) | 726 | Active, not archived. Repository pin `db4aeb73fc8597bf1f3718ac654ae37621dc6f4e`. The exact Skill last changed in [`8443e753d13ddaa8a645609441af33f63ac863a4`](https://github.com/bruin-data/dac/commit/8443e753d13ddaa8a645609441af33f63ac863a4) on 2026-09-01. Repository pushed 2026-09-01. | Root [AGPL-3.0](https://github.com/bruin-data/dac/blob/db4aeb73fc8597bf1f3718ac654ae37621dc6f4e/LICENSE). Skill, examples and demo are not separately licensed. The example database has no separate provenance notice, so it is suitable as a repository fixture only and not evidence about real-world data rights. AGPL code or prose must not be copied into the MIT Scoville package. | **E2.** Runnable YAML and TSX examples, a self-contained Vega-Lite example, validator tests and a rendered demo GIF exist. They prove parsing, schema, filter and encoding checks, local-data restrictions and dashboard source structure for named fixtures. They do not prove statistical truth, visual quality, responsive behavior, accessibility or successful agent adherence. Tests were inspected, not executed here. |
| 3 | [`openai/role-specific-plugins`, `plugins/data-analytics/skills/build-dashboard/SKILL.md`](https://github.com/openai/role-specific-plugins/blob/fe5608d2512a7d6a7b9821ce8a88c48464ecd6e4/plugins/data-analytics/skills/build-dashboard/SKILL.md) | 522 | Active, not archived. Repository pin and latest relevant update [`fe5608d2512a7d6a7b9821ce8a88c48464ecd6e4`](https://github.com/openai/role-specific-plugins/commit/fe5608d2512a7d6a7b9821ce8a88c48464ecd6e4) on 2026-07-13. | Root [MIT](https://github.com/openai/role-specific-plugins/blob/fe5608d2512a7d6a7b9821ce8a88c48464ecd6e4/LICENSE). Skill, HTML widgets and tests inherit that license. The bundled demo CSV has no separate provenance notice, so it proves fixture handling only and should not be treated as a rights-cleared external dataset. Connected-source data remains governed by its source and connector terms. | **E2.** HTML chart, table and report artifacts plus axis-domain, tooltip, transform, renderer, layout, table-sizing, source-discovery and delivery tests are inspectable. They prove internal runtime and contract behavior for named cases. They do not prove the model follows the Skill, the metrics are correct, or the resulting dashboard is independently usable, accessible or visually superior. Tests were inspected, not executed here. |

## Candidate 1: Fireworks Tech Graph

### Claimed scope and observed mechanism

The Skill produces engineering diagrams such as architecture, data flow, UML,
ER, network and event-flow graphics. It explicitly says it is not for
quantitative charts. Its workflow converts supplied structure into a typed
diagram intermediate representation, allocates reserved regions, creates
semantic node and edge IDs, renders SVG, validates syntax and geometry, then
performs a visual review at target size. Optional interaction and motion are
separate layers rather than substitutes for the static semantic diagram.

The strongest evidence is not the catalogue of twelve visual styles. It is the
contract around node and edge inventory, direction, relation type, marker use,
port capacity, clipping, crossing and overlap. For example,
[`test_semantic_contracts.py`](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/e9c7a9351dee5861707a7ec5560248bf5e7b84b5/tests/test_semantic_contracts.py)
and
[`test_geometry_contracts.py`](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/e9c7a9351dee5861707a7ec5560248bf5e7b84b5/tests/test_geometry_contracts.py)
make several otherwise subjective review prompts executable.

### What is better than the current Scoville reference

- A typed intermediate representation makes omission, reversal and accidental
  merging of relationships testable before visual polish.
- Semantic IDs and edge roles give each line a reviewable meaning rather than
  treating arrows as decoration.
- Reserved regions, port capacity, paint order and crossing checks localize
  diagram failures to geometry without changing the source model.
- Static, interactive and motion forms share a semantic base, which reduces
  handoff drift.
- Syntax validation and target-size visual inspection are separate evidence
  steps. A parseable SVG is not called a good diagram.

The current Scoville audit already identifies diagram notation, direction,
cardinality, source-model parity, accessible structured explanation and
smallest-cause repair as required capabilities. Fireworks supplies a more
concrete deterministic implementation pattern for part of that floor.

### Adoption-priority result

The inspected [`sample-style1-flat.png`](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/e9c7a9351dee5861707a7ec5560248bf5e7b84b5/assets/samples/sample-style1-flat.png)
has clear title hierarchy, coherent layer grouping and an explicit arrow
legend. It also shows the limit of the evidence. Some secondary labels are
close to boundaries, one internal node treatment is crowded, and the style is
one general architecture composition. The render proves competent grouping
and readable sequencing for that fixture. It does not prove subject-specific
composition, responsive recomposition or superiority across diagrams.

### Synthesize, reject or re-verify

Synthesize the typed source inventory, semantic edge contract, reserved-region
model, fail-closed geometry checks and syntax-then-visual evidence sequence.
Express them in original Scoville wording and keep domain notation dependent on
the actual model.

Reject the fixed style catalogue, view boxes, node counts, word limits,
gutters, animation timings and motion templates as general rules. Do not import
provider marks or external icon packs. Do not treat a user-approved manifest
as proof that the underlying architecture is true.

## Candidate 2: Bruin DAC dashboard Skill

### Claimed scope and observed mechanism

DAC treats a dashboard as reviewable source. SQL or semantic models provide
metrics and dimensions, YAML or TSX describes widgets and layout, and commands
query data, validate syntax and check the project. Examples cover charts,
tables, filters, funnels, semantic joins and Vega-Lite. Validation includes
field references, encodings, filters, inline-data boundaries and remote-data
restrictions.

This is mainly an implementation and handoff system. It demonstrates a useful
artifact contract, but its product schema and runtime are not general design
authority.

### What is better than the current Scoville reference

- Source, semantic model, metric, filter and widget are explicit inspectable
  layers rather than one opaque rendered dashboard.
- A cheap validation ladder separates no-op UI checks, query execution,
  document validation and wider project checks.
- Declarative examples make source-to-display reconciliation and regeneration
  feasible.
- Tables are first-class dashboard elements rather than a fallback after chart
  generation.
- Self-contained Vega-Lite and local-data restrictions reduce hidden remote
  dependencies in examples.

The Scoville audit goes further on deciding whether a chart, table or text is
right, whether scales and uncertainty tell the truth, and whether the output
remains equivalent across access, locale, print and responsive contexts.

### Adoption-priority result

The inspected [`resources/dac_optimized.gif`](https://github.com/bruin-data/dac/blob/db4aeb73fc8597bf1f3718ac654ae37621dc6f4e/resources/dac_optimized.gif)
shows a readable board-meeting dashboard with a clear summary-to-detail order,
consistent alignment and generous spacing. It also relies on a familiar KPI
grid, uses small low-contrast labels, and gives charts limited annotation. The
artifact proves a rendered dashboard exists and that the source can be edited
alongside it. It does not prove an information hierarchy derived from a
specific decision, narrow-screen recomposition or accessible task completion.

### Synthesize, reject or re-verify

Synthesize the reviewable source-to-metric-to-widget chain, validation ladder,
local fixture discipline and explicit regeneration path. Apply it equally to
charts and tables, and add Scoville's source, grain, transform, freshness and
evidence labels.

Reject AGPL copying, the required DAC database and renderer stack, the fixed
twelve-column layout, suggested KPI counts, standard 8/4 arrangements and
chart catalogues as design logic. SQL execution and product implementation
remain Code or platform ownership. The design leaf should define intended
information and proof, not adopt one dashboard runtime.

## Candidate 3: OpenAI `build-dashboard`

### Claimed scope and observed mechanism

The Skill starts with audience, purpose, source of truth, grain, freshness and
metric families. It distinguishes hero outcomes, diagnostic drivers and
guardrails, asks for a useful default view, limits filters to meaningful
questions and requires cards, charts and tables to reconcile. Its progressive
references then route to HTML, BI, Streamlit or MCP-artifact delivery.

The package includes concrete widgets, a demo data fixture and runtime tests.
The most relevant checks include
[`chart-axis-domain-contract.test.mjs`](https://github.com/openai/role-specific-plugins/blob/fe5608d2512a7d6a7b9821ce8a88c48464ecd6e4/plugins/data-analytics/tests/chart-axis-domain-contract.test.mjs),
[`html-report-layout.test.mjs`](https://github.com/openai/role-specific-plugins/blob/fe5608d2512a7d6a7b9821ce8a88c48464ecd6e4/plugins/data-analytics/tests/html-report-layout.test.mjs),
and
[`table-sizing.test.mjs`](https://github.com/openai/role-specific-plugins/blob/fe5608d2512a7d6a7b9821ce8a88c48464ecd6e4/plugins/data-analytics/tests/table-sizing.test.mjs).

### What is better than the current Scoville reference

- Source-of-truth conflict is a stop condition rather than a footnote.
- Audience, purpose, cadence, freshness and decision are established before
  choosing widgets.
- Outcome, driver and guardrail roles create a causal information hierarchy
  without prescribing a universal KPI count.
- Cross-panel reconciliation is an explicit requirement.
- Default-state usefulness, limited filters, source path, freshness and handoff
  are treated as part of the result.

These mechanisms address the current audit's dashboard-purpose and state gap.
They do not replace Scoville's deeper chart, table, uncertainty, cartographic,
access or cross-media rules.

### Adoption-priority result

The repository has inspectable HTML report and widget artifacts, but no pinned
visual outcome was found that demonstrates the exact Skill across materially
different subjects or viewports. The layout tests check containment, overflow
and a fixed reading shell. They do not prove typography, spacing, negative
space, hierarchy or responsive composition. No visible-quality rule should be
adopted from test success alone.

### Synthesize, reject or re-verify

Synthesize the pre-widget purpose record, source/grain/freshness gate, metric
roles, cross-panel reconciliation, useful default state and limited-filter
discipline. These belong in a general dashboard information contract.

Reject dependencies on connected MCP sources, BI tools, Streamlit, Recharts,
Vega or neighboring Skills. Reject the fixed HTML shell and implementation
mechanics as design rules. Do not infer source truth from connector access or
test coverage. A production dashboard still requires domain, statistical,
accessibility and platform evidence.

## Weighted adoption comparison

| Candidate | Exact-domain judgment and repair | Visible typography, spacing and composition | Evidence and reproducibility | Ownership and dependency fit | Net use |
| --- | --- | --- | --- | --- | --- |
| Fireworks Tech Graph | Strong for semantic diagrams and geometry repair, absent for charts and maps | One competent diagram family with clear grouping, but formulaic style recipes and no broad subject proof | Strong E2 fixture contracts | Mostly portable concepts, optional icon and motion dependencies must stay out | Best mechanism source for the proposed relational-diagram leaf |
| Bruin DAC | Moderate for declarative dashboards, weak for causal information critique | Clean rendered demo with a conventional KPI grid, no responsive or access proof | Strong E2 schema and validator evidence | Product runtime and AGPL are major blockers | Adopt artifact and validation pattern only |
| OpenAI `build-dashboard` | Strong for purpose, source state and cross-panel reconciliation | No qualifying pinned visual outcome for general quality | Broad E2 internal runtime tests | Heavy surface and neighboring-Skill routing | Adopt the dashboard information contract only |

## Domain coverage and shortfall

| Required area | Evidence among ranked candidates | Result |
| --- | --- | --- |
| Charts | DAC and OpenAI provide declarative or rendered chart paths and mechanical tests | Useful implementation evidence, not a complete chart-selection or truthful-encoding curriculum |
| Tables | DAC and OpenAI make tables inspectable and test containment | Missing professional table semantics, precision, repeated headers, responsive strategy and programmatic header proof |
| Dashboards | DAC and OpenAI provide the strongest ranked evidence | Adopt purpose, source state, metric roles, reconciliation and regeneration mechanisms |
| Diagrams | Fireworks provides typed semantics, geometry and rendered examples | Strongest exact mechanism, but notation and source truth still require domain authority |
| Maps | No E1+ exact cartography Skill was found in the bounded search | Do not fill the gap with chart libraries or generic visualization advice. Retain the audit's proposed cartography leaf and current authoritative research |

[`antvis/chart-visualization-skills`](https://github.com/antvis/chart-visualization-skills/tree/d168980d14218c2bf0cd153e111abd404c231482) had 473 stars at a later spot check and qualified at E2 through chart, graph and editor Skills plus internal evaluation fixtures. It ranks below the top three by stars. Its retrieval and renderer ecosystem is useful implementation prior art, but it does not close the cartography gap or establish independent visual superiority.

## Mechanisms to synthesize and claims to withhold

### Adopt or test through original Scoville wording

- For diagrams, require a typed node and edge inventory before geometry, then
  validate semantics and geometry separately.
- For dashboards, record audience, decision, cadence, source owner, extraction
  time, grain, transformations, freshness, metric roles and filter effects
  before selecting widgets.
- Keep charts, tables and cards reconciled to one inspectable metric model.
- Use a layered validation ladder, starting with deterministic source and
  structure checks, followed by target-size render, task and access review.
- Keep the default view useful without hover or hidden filter state.
- Preserve regeneration inputs and receipts in static, print and handoff forms.

### Retain from current Scoville instead of importing

- task-based chart, table, text and map selection.
- truthful baselines, transformed scales, uncertainty and missing-state logic.
- map projection, normalization, classification, boundary and privacy duties.
- locale-aware formatting and accessible equivalents from the same data.
- responsive recomposition rather than uniform shrinking.
- observation-to-reader-error-to-cause-to-smallest-repair critique.
- domain, statistical, cartographic, accessibility and production claim limits.

### Reject from the executable package

- fixed chart catalogues, dashboard grids, card counts, spacing values, node
  counts, view boxes, typography scales or animation timings.
- product-specific SQL, renderer, database, connector or BI workflows as Design
  ownership.
- copied AGPL language or code in the MIT package.
- external vendor marks or datasets without separate rights and provenance.
- claims that deterministic fixture tests prove source truth, usability,
  accessibility, visual quality or independent adoption.
- substitution of generic chart advice for missing cartographic expertise.

## Search exclusions and limits

- `majiayu000/claude-skill-registry` had more stars than several candidates but
  is a generated mirror. The exact data-visualization entries had prose and
  snippets without a tied output or reproducible test, so they remained E0.
- Chart libraries, visualization component collections, generic UI Skills,
  data-analysis prompts and dashboard marketing templates without an exact
  Skill plus E1 evidence were excluded.
- The bounded search found no qualifying cartography Skill that combined map
  choice, projection, normalization, classification, boundary vintage,
  spatial uncertainty, privacy and proof.
- Tests and artifacts were inspected at pinned commits but were not executed in
  this comparison. No model run, source dataset calculation, responsive render,
  assistive-technology task, print proof or independent human review occurred.
- Repository stars can change after capture. They are used only to apply the
  frozen ranking rule among qualified candidates.
