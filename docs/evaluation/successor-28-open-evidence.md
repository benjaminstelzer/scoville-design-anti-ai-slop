# W-017 Terra Medium open evidence

Date: 2026-09-02  
Status: W-017 in progress after explicit removal of the cost stop  
Contract: [`open-28-leaf-call-plan.md`](open-28-leaf-call-plan.md)

## Configuration and cumulative use

- Model: exact `gpt-5.6-terra`
- Reasoning: exact `medium`
- Current package manifest: `84CA08F6239EEBE92A175C6988B45B8091E03CFD13FA5745B63BBDF066B185D6`
- Completed Medium calls: `10`
- Timed-out Medium calls without terminal usage: `1` (`D28-PK1`)
- Provider-total tokens: `1,583,416`
- Uncached-input-plus-output tokens: `407,864`
- Coverage reserve consumed: `1 of 1`
- Named case passes: `0`
- Named bounded failures: `D28-EH1`, `D28-CI1`, `D28-CI2`, `D28-CI3`, `D28-MK1`, `D28-IN1`, `D28-AD1`
- Provider lane: all named cases attempted; no SkillOpt pair became eligible

One earlier W-015 Terra High call was interrupted after the user changed the
model requirement. The wrapper had not written raw events, status or usage.
Possible billing is unknown and qualification credit is zero.

## D28-EH1 evidence-honesty canary

Both Medium runs used the same prompt and the same two initial image hashes:

- wide: `2E30B7FD4F1A34CFBE5FC28B735D8D1799D72B1967876FFDD3AB24EDBE420CCB`
- narrow: `C83C9F8AF5AB56348AAF4AC0835E4889EDC5BEC5CA94FBA6FE92C449F1121A0F`

### R1

- Package manifest: `5B31F10DFBC9EB605A2DD1D73F9B4CD2B3915341F26370134ECD9F81DBA5ACA6`
- Raw events: `C3BB099828192F871C4375C7DFCCAE1DB57EC4A5818F5E0D38569CC39F0BE53D`
- Usage: `93,101` provider total; `30,509` uncached plus output
- Result: strong render-specific findings and correct exception preservation;
  failed exact route by additionally reading Composition.
- Harness finding: the CLI records initial images in preflight/run status but
  does not echo them as separate view events. The future contract therefore
  requires those hashes plus observations from each render that source alone
  cannot establish.

### Coverage reserve CR1

- Package manifest: `B93CDFF3449CAF659F312A0D42AC4674D1BA140BAC1A08B80BCDAA3EC02704EE`
- Raw events: `CF0D13039344126F55C009527D90351E9E3E30F0332815E04E4FF7F8C6DA5992`
- Usage: `93,218` provider total; `30,626` uncached plus output
- Result: Composition over-read was removed. The executor selected Typography,
  Web, Style and Critique, preserved the accepted display exception and again
  localized image-specific narrow clipping, type spacing and style-system
  causes.
- Benchmark defect: the frozen Gold forbids Critique while the prompt requests
  a separate multi-domain causal critique and Core explicitly allows Critique
  in that condition. Gold is not changed after output and no third run occurs.

Neither attempt receives qualification credit. A later suite version must
either expect Critique or narrow the task so its separate finding lifecycle
cannot change the result. This bounded benchmark failure does not erase the
observed content quality and does not qualify the case.

## D28-CI1 corporate visual-identity generation

- Package manifest: `84CA08F6239EEBE92A175C6988B45B8091E03CFD13FA5745B63BBDF066B185D6`
- Raw events: `1F3D981726759D9F499811049BE174C4E3D82AA10B9942BAA6DD3E51C0C3C290`
- Usage: `180,840` provider total; `42,600` uncached plus output
- Model evidence: created a substantive identity contract and editable SVG;
  validated XML/content/colour/font references; honestly reported
  `render_inspected: false`.
- Route result: read Brand, Composition, Typography and Font Technology rather
  than the frozen Brand-only Gold. Complete artifact execution left spatial,
  typesetting and local-font questions open, so the Gold under-specified craft
  ownership; the observed four-leaf route stayed within the package maximum.
- Evaluator render: local Edge rendered the SVG to PNG. The A3 event title runs
  beyond the right panel and is visibly clipped. Other panels show a coherent
  record-band/locator system and exact content, but the uninspected high-impact
  overflow makes the visual outcome fail.
- Cost stop: provider total exceeded the ordinary-call ceiling of `160,000`.
  ADR-0023 stopped W-016 at this point. The user later explicitly removed the
  cost stop through ADR-0024; the failed case still receives no credit or rerun.

D28-CI1 receives zero qualification credit. The result demonstrates useful
system reasoning and evidence honesty, but also demonstrates why generated
visual artifacts require a render-and-return repair loop before professional-
quality claims.

## D28-CI2 mandatory-CI repair

- Package manifest: `84CA08F6239EEBE92A175C6988B45B8091E03CFD13FA5745B63BBDF066B185D6`
- Raw events: `B7AE2C3FD9CCC539382B1ECF7A2ED6E3D2F562374492B0F98846BBB56BC4788B`
- Usage: `187,530` provider total; `45,450` uncached plus output
- Result: removed the unauthorised RC mark, gradients, glow, purple/cyan/black
  field, rounded card and waveform; used only the mandatory CI palette, type
  roles and exact two-green/one-red device; preserved every required string;
  invented no exception.
- Evidence honesty: XML/source checks passed after two visible command errors;
  the model correctly reported `render_inspected: false`. Evaluator-owned Edge
  rendering then showed a clean unclipped poster with coherent asymmetric
  hierarchy and functional negative space.
- Exact-route failure: observed Brand + Composition + Fixed Media versus frozen
  Brand + Composition. Because fixed A3 poster structure was open, the medium
  owner was materially applicable and the Gold was under-specified.

D28-CI2 receives zero exact-route qualification credit and is not rerun. Its CI
conformance, local repair, exception discipline and evaluator-rendered visual
result remain positive bounded evidence. The paired CI2 SkillOpt call is not
eligible because the named case did not pass its frozen route contract.

## D28-CI3 conflicting-CI-authority audit

- Package manifest: `84CA08F6239EEBE92A175C6988B45B8091E03CFD13FA5745B63BBDF066B185D6`
- Raw events: `F92A137FE219E3032D1B739030A7396FB9BD4038E00D7AD109D720D8C02CB032`
- Report: `84C1A84F39A9BD76DBF6FFFCAB45F638F061AB1575F3C40DD6E34D62906C0652`
- Usage: `230,155` provider total; `48,139` uncached plus output
- Result: preserved both manual positions, distinguished declared cover status
  from verified current authority, localized every conflicting rule and all
  four dependents, blocked non-provisional mutation/release, and required a
  recorded Brand Council decision followed by the Design Operations register
  update. It chose no palette, type system, device or aesthetic compromise.
- Evidence honesty: the report labels every input as local evidence, leaves
  current authority unresolved, names missing approval/migration evidence, and
  correctly reports no render inspection.
- Exact-route failure: observed Brief + Brand + Source Verification + Production
  versus frozen Brand + Source Verification. Brief plausibly followed Core's
  explicit `field authority` route, while Production followed derivative and
  release language. Those overlaps exceed the frozen owner-local Gold.

D28-CI3 receives zero exact-route qualification credit and is not rerun. The
authority audit itself is strong bounded evidence; the extra leaves expose a
routing-boundary overlap that a later suite or Skill revision must resolve
without rewriting this frozen result.

## D28-MK1 identity-mark mechanism generation

- Package manifest: `84CA08F6239EEBE92A175C6988B45B8091E03CFD13FA5745B63BBDF066B185D6`
- Raw events: `8073048EAD287752F8A1122007DD0F9FE5C9A3A375599316FCECB963EF5CF91A`
- SVG: `58F5F815B7A610B1BD28189BDC8829BD5A3CCBA06648ADDBB1D78C867AF783DA`
- Evaluator render: `E05D0CC7B1073CA7779BC93B2C7AA89F328430A71F6575354E353F780A6ADE51`
- Usage: `160,494` provider total; `53,486` uncached plus output
- Exact route: pass. The executor read only Mark and correctly excluded Brand,
  Typography and production work.
- Structural and boundary result: editable valid SVG, three named candidates in
  all four required conditions, appropriate provisional selection, and honest
  denial of render inspection and rights/recognition/production claims.
- Evaluator visual result: fail. A and C are close variants of one fork/arrow
  construction and B is a generic X-like crossing. All survive mechanically at
  small size, but the set does not provide three materially different,
  subject-specific professional mechanisms; it resembles ordinary interface
  glyph exploration more than a resolved identity-mark study.

D28-MK1 receives zero overall qualification credit and is not rerun. It is
positive exact-routing and evidence-boundary proof, but negative generation and
visual-quality evidence.

## D28-IN1 instructional procedure repair

- Package manifest: `84CA08F6239EEBE92A175C6988B45B8091E03CFD13FA5745B63BBDF066B185D6`
- Raw events: `9A3746A9585365589347D738CF88E9F707A53AF4FFF425692AC8C5B4351A4850`
- SVG: `E32DFE6B131573E4CD185D80B7BB6C3AC27968C70777D2F1B394672BAD8305D7`
- Evaluator render: `8D2951C022309CE57072BDD42EDE93CC1A76D6866876CB5714F766DB7485D5EA`
- Usage: `209,110` provider total; `41,174` uncached plus output
- Exact route: pass. The executor read only Instructional + Diagrams and
  excluded UI.
- Structural and boundary result: exact authoritative wording, nine-node and
  seven-edge parity, explicit YES/NO branches, terminal STOP, bounded
  comprehension protocol, and honest denial of safety, access, participant and
  render proof.
- Evaluator visual result: fail. The Preconditions-to-Step-1 connector crosses
  directly through the red warning text, harming legibility and creating an
  ambiguous relation. The decision diamond is also empty and depends on the
  preceding card for its referent. Static source validation missed both rendered
  communication defects.

D28-IN1 receives zero overall qualification credit and is not rerun. It proves
exact routing, source-model preservation and safety-boundary discipline, but
not a professionally resolved visual repair.

## D28-AD1 placement-native campaign generation

- Package manifest: `84CA08F6239EEBE92A175C6988B45B8091E03CFD13FA5745B63BBDF066B185D6`
- Raw events: `4A258F4A2FA321F2A6E8F5B98101B266F0404F9000A9ACCF5C8658DD6D8AA18C`
- Square render: `9B6C5FB0B0F050F04DD7569855CB5BC077121E7F41098875427285FF0A56BC6A`
- Story render: `601897B091A509C56102CCD0F7986D152B142CC74BADDFE82C0791D666B0FB66`
- Landscape render: `315A2FECFB375E033362FF9697EB37D6EC21D7D4CA745418F98150A0E08E8373`
- Usage: `188,033` provider total; `42,369` uncached plus output
- Exact route: pass. The executor read only Brand + Advertising + Imagery and
  excluded Concept.
- Structural result: exact copy and CI palette, recognizable supplied recorder,
  coherent campaign device and genuinely different placement compositions.
- Evaluator visual result: fail. In landscape, the orange route and locator
  cover the material `Booking required.` qualifier despite the explicit
  no-cover constraint. In story, the route collides with the CTA. The square is
  coherent, but the family cannot pass when two required placements damage
  action or disclosure content.

D28-AD1 receives zero overall qualification credit and is not rerun. Its exact
routing and campaign-system reasoning remain positive bounded evidence. D28-SO2
is ineligible because the paired named case did not pass.

## D28-PK1 packaging repair timeout

- Package manifest: `84CA08F6239EEBE92A175C6988B45B8091E03CFD13FA5745B63BBDF066B185D6`
- Raw events: `7E8833C3545B9A8A0C4EC45BEE14B35B1E37CEB75BC5B12AE32EB511F2619527`
- Wrapper state: timeout at `300.092` seconds; no terminal agent message and no
  `turn.completed` usage record. Possible billing is unknown and excluded from
  confirmed cumulative usage.
- Partial artifacts: flat `3E4E54C483532C387C3907752067CFBF1855A26E1A70AE425AA09BD1DA861819`;
  lineup `EF3BA961CD596DDAA338BA1D8F1A1109FD766E275719B7CB9797B999C30F4D03`.
- Observed route before timeout: Packaging + Typography + Composition versus
  frozen Packaging + Typography. Exact routing would fail.
- Evaluator-only inspection: the lineup is orderly and variants are redundant,
  but the flat view clips guide labels and places large front text tightly
  against panel boundaries. These partial artifacts are not scored as a
  completed model result.

D28-PK1 receives zero qualification credit and is not rerun. D28-SO3 is
ineligible. The known wrapper-timeout classification remains visible without
granting product evidence or changing confirmed token totals.

## D28-WF1 physical wayfinding repair

- Package manifest: `84CA08F6239EEBE92A175C6988B45B8091E03CFD13FA5745B63BBDF066B185D6`
- Raw events: `92CF6B989BC16F4C89186C5B7574C5A26A1AFC36C271617C6215CA33DA70C437`
- Evaluator render: `4911EC0A7F2278EAC2401685D602991401B9DEEFE6C04BD7AE8DC1EB84C270A4`
- Usage: `149,001` provider total; `37,897` uncached plus output
- Route result: failed. Observed Wayfinding + Diagrams + Instructional versus
  frozen Wayfinding + Cartography; Cartography was omitted.
- Content result: preserved route topology, names, node/edge IDs, north-up
  orientation, advance/decision/confirmation schedule and recovery over only
  the existing J1-J2 path. Claim boundaries remained honest.
- Evaluator visual result: generally clear, but orange recovery arrows and
  explanatory text crowd and overlap the central J1-J2 map relation.

D28-WF1 receives zero qualification credit and is not rerun. It supplies
bounded positive journey/system evidence but negative routing evidence.

## D28-BO1 Design/UI/Scribe ownership handoff

- Package manifest: `84CA08F6239EEBE92A175C6988B45B8091E03CFD13FA5745B63BBDF066B185D6`
- Raw events: `37EF62A853BA1DE2EE4AEF1C9C72BB4F51C78B84BC606C7CDB1862F8ABE490C2`
- Evaluator render: `F0DB37D9031FD3590A0D24D3F7ED3B4F3F85C18D42E2F096827708F1F7D7EBAB`
- Usage: `91,934` provider total; `35,614` uncached plus output
- Exact route: pass. The executor read only Design UI Workflow + Web and
  excluded Critique.
- Ownership result: strong. Design owns task flow and responsive intent; UI
  retains Mantine primitives, semantics, focus, validation, persistence,
  accessibility and runtime proof; Scribe retains final wording/localization.
- Evaluator visual result: fail. Timeout and decline paths cross or appear to
  terminate at Confirmation, contradicting non-success/return semantics, and
  several action labels are clipped.

D28-BO1 receives zero overall qualification credit and is not rerun. It proves
the requested ownership boundary and exact routing, but not professional visual
flow execution.

## W-017 terminal finding

All ten named cases have receipts or a visible timeout receipt. No named case
passed every required dimension, so no paired SkillOpt call was eligible. The
suite does **not** qualify the current candidate. Textual reasoning, authority
boundaries and several routes are strong; unrendered SVG generation repeatedly
introduces collisions, clipping, generic forms or misleading geometry. A
corrected evaluation must expose a renderer inside the model call and fail fast
on one render/repair smoke case before another broad suite. Frozen route Gold
also needs independent reconciliation where it contradicted Core or omitted a
material craft owner; no observed Gold was retroactively changed.
