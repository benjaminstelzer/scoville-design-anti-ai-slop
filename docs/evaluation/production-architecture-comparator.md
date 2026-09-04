# Model-free production architecture comparator

Date: 2026-09-02  
Status: accepted architecture comparison; runtime unchanged; W-012 gate input  
Scope: successor `media-production-and-handoff` architecture only  
Method: repository evidence and token/read-graph forecast; no model call

## Decision

Retain one directly routed `media-production-and-handoff` expert leaf. Author it
as one compact cross-format production spine followed by internally headed gates
for:

1. SVG and raster;
2. print and PDF;
3. documents and presentations;
4. motion delivery; and
5. Web/UI artifact handoff.

Do not add flat format-production leaves or adapter modules now. The narrow
`production`/`handoff` route already excludes ordinary creation and intended
rendering. Once that route is justified, the authority, derivative, validation,
render, evidence, stale-receipt, source-first repair, and receiver contract is
material in every format. Splitting would reduce context for a single-format
technical question, but it would repeat the causal contract five times and make
the reviewed cross-format handoff exceed the four-leaf read limit.

This accepts candidate A from the production reference audit. It does not claim
that one leaf is permanently optimal. The falsifiers below can reopen the
decision after complete payloads and a larger model-free route corpus exist.

## Compared payload maps

### A — one unified production leaf

```text
media-production-and-handoff
├── receiver and artifact contract
├── authority → derivative graph and hashes
├── validator → render → semantic/access → provider/physical receipt
├── stale-evidence invalidation and source-first repair
├── SVG/raster gate
├── print/PDF gate
├── document/presentation gate
├── motion-delivery gate
└── Web/UI artifact-handoff gate and escalation
```

Core reads this one leaf only when technical export, rebuildability, preflight,
format-specific semantic/access validation, receiver/provider acceptance, or a
handoff record can change the outcome. Format headings are internal routing aids,
not sibling experts and not permission to apply every gate.

### B — five flat standalone format leaves/adapters

```text
production-svg-and-raster
production-print-and-pdf
production-documents-and-presentations
production-motion-delivery
production-web-ui-handoff
```

Under the accepted family contract, these cannot depend on a hidden common
production module. Each must repeat enough of the artifact contract, authority
graph, hash and rebuild rules, evidence labels, stale-receipt invalidation,
source-first repair, receiver state, and ownership/escalation floor to work
alone. A shared base plus thin adapters was rejected from this comparison because
it would create a sibling dependency or require a sixth routine co-load.

Tool-specific validator/renderer commands may later be documented as bounded
examples. They are not separate expert modules unless independent routing and
outcome evidence establishes that the tool adapter itself changes the required
decision contract.

## Shared causal spine

The invariant is:

```text
receiver contract
  → authoritative editable/build source
  → named derivative and hash relation
  → parser/schema/resource validator
  → intended and diagnostic render
  → delivered-format semantic/access inspection
  → provider, calibrated, physical, or runtime evidence where applicable
  → scoped hash-bound receipt
  → source-first repair and invalidation of stale derivatives/receipts
```

This is one causal chain, not a generic checklist. Removing an intermediate
link changes what later evidence means. A clean render cannot repair an unknown
source, a green parser cannot prove visual or semantic fit, a tagged file cannot
prove accessibility, and a monitor preview cannot become supplier acceptance.
The chain is therefore the strongest reason not to split before independent
route evidence exists.

## Ownership preserved by both options

| Concern | Canonical owner | Production-leaf boundary |
| --- | --- | --- |
| visual, responsive, fixed, or temporal design intent | owning Design craft/medium leaf | consume the intent; do not redefine it |
| file/build authority, derivatives, export, preflight, receiver contract, evidence transfer | Media Production | own and repair the artifact/evidence chain |
| framework components, DOM/native semantics, states, focus, input, announcements, runtime interaction proof | Scoville UI when active | may carry the UI receipt; never invent or self-certify it |
| colour roles and reproduction intent | Colour | Production executes export/preflight and binds provider/physical proof |
| page/slide/template/fold/face and fixed viewing intent | Fixed Media | Production verifies files, derivatives, receiver requirements, and proof |
| temporal thesis, beats, continuity, reduced/static equivalence | Motion | Production verifies encode, playback/output, platform contract, and receipt |
| licensing, factual evidence, culture, privacy, legal or physical safety | their domain authorities | preserve records, fail closed, and escalate; do not clear them |

The flat Web/UI alternative has the highest ownership-collision risk: a leaf
named `production-web-ui-handoff` could easily absorb responsive intent or UI
runtime proof. The unified leaf's explicit Web/UI gate can keep its scope to
static assets, builds/exports, manifest transfer, and externally supplied UI
receipts.

## Representative route comparison

`1 read` below means one expert-reference read in addition to Core and any
independently applicable craft/medium leaves.

| Technical-delivery route | Independent production evidence | Unified map | Flat map | Model-free judgment |
| --- | --- | --- | --- | --- |
| live-text SVG plus raster variants | parse/resource/embedding context, source and variant hashes, crop/profile/size records, receiver acceptance | 1 production read; shared spine + SVG/raster gate | 1 SVG/raster production read | Flat is smaller for this isolated route, but its repeated spine is still required. Format identity alone does not trigger either map. |
| print/PDF preflight and supplier handoff | named receiver/profile, output intent, font/page-box/separation/overprint/transparency checks, proof scope | 1 production read; commonly co-load Colour and/or Fixed Media | 1 print/PDF production read; same craft co-loads | Flat saves unrelated gates, but not the source, receipt, exception, receiver, or source-first repair floor. No current independent `print_prepress` signal exists. |
| editable document/presentation plus tagged/exported derivative | native styles/objects/data, page/slide renders, reading order/tags/language/alternatives, export hash | 1 production read; commonly co-load Fixed Media | 1 document/presentation production read; same Fixed Media co-load | Flat saves unrelated gates. The shared contract still dominates because visual rendering and semantic/access evidence must remain separate. |
| final motion encode/delivery | timebase, codec/container, captions/audio, safe/output conditions, playback, sampled frames, reduced/static derivative, receiver receipt | 1 production read plus Motion only when temporal intent is open | 1 motion-production read plus the same conditional Motion leaf | Flat has a single-route size advantage. C17 correctly proves that ordinary motion design does **not** load Production; only encode/receiver work does. |
| Web/UI artifact or asset handoff | rebuildable assets/build, manifest, variants, static semantic/access checks, supplied UI/runtime receipt | 1 production read; Web/UI leaves load only when their own intent/mechanics are open | 1 Web/UI production read; same conditional Web/UI co-loads | Flat has modest size benefit but the greatest duplicate-ownership and simulated-runtime-proof risk. |
| C18 cross-format repair: SVG/raster + print/PDF + tagged document/deck + fixed/colour context | authority/derivative hashes, source-first repair, syntax/render/semantic/preflight/provider separation | **3 total expert reads:** Production + Fixed Media + Colour | **at least 5 total expert reads:** SVG/Raster Production + Print/PDF Production + Document/Presentation Production + Fixed Media + Colour | Unified wins decisively. The flat graph exceeds the provisional maximum of four leaves and forces phasing of one causal handoff. |
| C22 rights/source package and output-attribution survival | stable source/asset IDs, released derivative hashes, attribution survival, handoff evidence | 3 total expert reads: Rights + Sources + Production | 3 reads for one output class; 4+ when the package spans formats | Unified preserves one package-level authority and correction graph. Flat routing scales with rendition count rather than with the one handoff outcome. |

## Signal independence and common co-load

The accepted registry exposes `production` and `handoff`, not
`print_prepress`, `accessible_document_handoff`, `motion_export`, or equivalent
format signals. That is deliberate:

- ordinary artifact creation and one intended render are negative boundaries;
- ordinary responsive/UI work stays with Web/UI and Scoville UI;
- temporal design and its intended proof stay with Motion until encode/platform
  delivery is materially open;
- fixed-medium intent stays with Fixed Media until file/preflight/provider proof
  is materially open.

The current 22-case contract matrix selects Media Production only in C18 and
C22. C18 is explicitly cross-format and C22 is package/handoff-wide. This is too
little evidence for five stable independent production signals, but it is direct
evidence that the reviewed critical routes need the common spine and can co-load
several format gates.

Expected concern-driven co-loads remain:

- Colour + Production for managed print/reproduction;
- Fixed Media + Production for documents, decks, print, package faces, and signs;
- Imagery + Production for raster/crop rendition families;
- Motion + Production for final encoded delivery;
- Information + Production for editable data and chart handoff;
- UI/Web + Production only when both design/runtime intent and artifact/export
  delivery are independently open;
- Sources/Rights + Production when source, licence, attribution, or output
  survival is materially open.

None is a dependency. A production leaf must remain independently usable when
the corresponding design decision is already supplied and closed.

## Provisional token and read-graph forecast

These are authoring forecasts, not caps or measured runtime payloads. The
unified range is inherited from the reviewed audit. Component ranges make the
duplication cost explicit and must be replaced by `o200k_base` measurements
after authoring.

| Payload component | Forecast tokens |
| --- | ---: |
| standalone shared spine, ownership, exceptions, receipt and repair floor | 1,150–1,550 |
| SVG/raster gate | 350–500 |
| print/PDF gate | 500–700 |
| document/presentation gate | 400–550 |
| motion-delivery gate | 300–450 |
| Web/UI handoff gate | 200–300 |

### Unified forecast

- one file/read for every production route;
- reviewed complete payload: **2,800–4,000 tokens** after cross-heading and
  ownership deduplication;
- isolated single-format routes load unrelated format gates, with a coarse
  arithmetic bound of about **550–2,650 tokens** depending on the gate and final
  compression;
- a two-, three-, or five-format handoff still loads **2,800–4,000 tokens** and
  consumes one expert-read slot.

### Flat standalone forecast

Each format leaf repeats the 1,150–1,550-token standalone floor:

| Flat leaf | Forecast tokens |
| --- | ---: |
| SVG/raster production | 1,500–2,050 |
| print/PDF production | 1,650–2,250 |
| document/presentation production | 1,550–2,100 |
| motion production | 1,450–2,000 |
| Web/UI production handoff | 1,350–1,850 |
| **whole flat production suite** | **7,500–10,250** |

The flat suite repeats **4,600–6,200 tokens** of the common spine beyond its
first necessary copy. An isolated route is cheaper than the unified leaf by
roughly 550–2,650 tokens. A three-format handoff loads about 4,700–6,400 tokens
across three production reads before craft/medium leaves; the full five-format
set loads 7,500–10,250 across five reads and cannot fit the four-leaf contract.

The unified map therefore spends more context on a narrow single-format
production question but materially less repository duplication and less
context/read-graph cost on the cross-format artifact and package outcomes that
currently justify the route.

## Exact accepted module-map consequence

ADR-0017's twenty-three-leaf map remains unchanged. The accepted successor
entry is exactly:

```yaml
- id: media-production-and-handoff
  status: retained-floor
  intervention: external-verification
  when_any: [production, handoff]
  owns:
    - artifact_contract
    - authority_derivative_graph
    - format_validation
    - render_contract
    - production_preflight
    - handoff_record
  requires: []
  conflicts: []
```

Consequences:

- no new expert IDs and no change from twenty-three leaves;
- no new format-specific route signals;
- no sibling read, common production dependency, or hidden adapter;
- one shared contract followed by the five internal gates in the order stated
  above;
- ordinary creation/rendering remains a negative route;
- format gates may be skipped semantically inside the loaded leaf, but they do
  not create separate read-graph nodes;
- tool-specific commands remain bounded examples outside the invariant
  conceptual spine until the actual available validator/renderer is known.

## Model-free checks

The following checks decide architecture without asking a model to judge
quality:

1. **Registry integrity:** exactly one production module; accepted
   `when_any`, `owns`, empty `requires`, and empty `conflicts`; no format
   production IDs or signals.
2. **Negative routing:** ordinary SVG/image creation, one intended render,
   ordinary motion design, responsive intent, and UI implementation do not load
   Production unless a technical delivery condition is present.
3. **Positive routing:** parser/resource validation, export/preflight,
   rebuildability, delivered-format semantics/access, receiver/provider proof,
   or a manifest/handoff receipt loads exactly one Production leaf.
4. **Format classification:** every production fixture selects one or more of
   the five internal gates from explicit task evidence; format words without an
   open technical condition select none.
5. **Read graph:** Core reads Production directly; Production reads no sibling.
   C18 remains three total expert reads and C22 remains three under its reviewed
   form.
6. **Ownership lint:** the production payload contains no Design decision for
   composition/type/colour/motion/responsiveness and no UI runtime-certification
   instruction; it consumes records and names the responsible proof owner.
7. **Contract completeness:** every gate preserves the ordered authority →
   derivative → validator → render → semantic/access → provider receipt chain or
   explicitly marks a non-applicable link; no gate promotes a weaker receipt.
8. **Standalone operation:** each representative single-format fixture can be
   completed from Core plus Production when design intent, rights, and receiver
   facts are supplied and closed.
9. **Token accounting:** measure Core, the complete leaf, each internal gate,
   common combinations, C18, and C22 with `o200k_base`; forecasts are replaced,
   not retrofitted to the result.
10. **Matrix validation:** the existing model-free validator passes before
    runtime authoring. At comparison time it reported
    `VALID leaves=23 cases=22 dimensions=6 canaries=5 hard_call_maximum=46`.

## Falsifier and mandatory revisit

Reopen the split decision before qualification if **any** of these occurs:

1. the authored unified leaf exceeds 4,000 `o200k_base` tokens and cannot reach
   4,000 without losing a binding floor, causal repair, justified exception,
   ownership boundary, or proof distinction;
2. a frozen corpus of at least twenty representative technical-delivery routes
   shows at least fourteen routes selecting exactly one stable format gate and
   no more than two routes selecting three or more gates;
3. stable positive and near-neighbor-negative fixtures justify independent
   format signals, and a split reduces median loaded production context by at
   least 30 percent without increasing false routes;
4. a complete standalone split keeps every shared causal contract intact,
   introduces no second owner, and every common route stays within four total
   expert leaves and 15,000 Core-plus-leaf tokens; or
5. unified-leaf ownership lint or deterministic route/read-graph checks fail in
   a way caused by the grouping rather than by wording.

A split is accepted only after all affected deterministic route, ownership,
contract, and token checks pass on both maps. Changing the reviewed one-leaf map
changes ADR-0017 and requires the focused review specified by the registry.
Until a falsifier is observed, author and test the unified leaf.

## Evidence used

- [`reference-audits/media-production-and-handoff.md`](../research/reference-audits/media-production-and-handoff.md)
- [`successor-module-registry.md`](../research/successor-module-registry.md)
- [`0002-professional-reference-depth-audit.md`](../audits/0002-professional-reference-depth-audit.md)
- [`open-successor-call-plan.md`](open-successor-call-plan.md)
- [`leaf-contract-matrix.yaml`](leaf-contract-matrix.yaml)
- [`ADR-0017`](../decisions/0017-adopt-professional-depth-successor-module-map.md)
- [`ADR-0018`](../decisions/0018-separate-medium-intent-and-keep-spacing-with-its-relationship.md)
- [`professional-reference-plan-review-round-1.md`](../reviews/0006-professional-reference-plan-review-round-1.md)
