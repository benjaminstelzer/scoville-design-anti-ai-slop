# W-024 targeted qualification ledger

Date: 2026-09-03  
Status: targeted qualification passed; complete sealed holdout not run

## Qualification scope

The user explicitly replaced a complete sealed-holdout rerun with proportional
verification of the one demonstrated v7 routing boundary. This ledger therefore
records a targeted package-boundary qualification. It does not convert failed or
incomplete sealed suites into passes and does not claim full holdout coverage,
broad model superiority, or general domain competence.

## Exact tested configuration

- model: exact `gpt-5.6-terra`;
- reasoning effort: `high`;
- host: local Windows Codex execution host;
- CLI: `codex-cli 0.147.0-alpha.1.2`;
- CLI SHA-256:
  `FA960EC081BEC3629F40C63ED610EBC49C7E5E077DFB42322B08CB6D460F0B8A`;
- provider calls: 1;
- transport attempts: 1;
- retries: 0;
- sealed calls: 0;
- renders: 0.

The executable package was frozen before the call:

- executable-manifest file SHA-256:
  `F6A076D5C2272F4FAD23FB6C236523287D19E0C7EACF8484D5AD7993E0EAAD6F`;
- inner package-manifest SHA-256:
  `97A136E9F2CA012E10D4B6ADEECF7E5E45B47FC9F92B4F6F1B99A904CDE9283F`;
- `SKILL.md` SHA-256:
  `76CD2F7F86B0FF5494F090EA1C1911EED158D4AB5B7109F7BDD121D95B71B206`;
- `modules.yaml` SHA-256:
  `DABD01330E06290DB66DA22F0CC30B6DA8AD34CF01ED1104779F50F6A252F9A4`;
- route-fixtures SHA-256:
  `F304500901834E2D56298A6F813258DE2D578FAB5EB2B8D48D7502B405E79396`.

## Reproduced case and post-fix result

Case `ADR0047-PUBLIC-DIAGRAM-BOUNDARY-01` is original and source-cleared. Its
fixed diagram system requires only `diagrams-and-relational-information` and
forbids Composition, Typography, Instructional Design, and Media Production.

Before ADR-0048, one authorized public Terra High call read Diagrams,
Composition, and Media Production. All non-route checks passed, isolating a
package routing-boundary defect. Result SHA-256:
`96B6829FBE189560C4CCD23A66AD0CCE0F5457C6CAD1B4B535720DDB596BB1FF`.

After the minimal ADR-0048 repair, the one authorized replay:

- authenticated exactly one read: `diagrams-and-relational-information`;
- reported the same exact terminal selection;
- read zero forbidden experts;
- passed every non-route artifact and relation check;
- used 98132 input tokens, including 77312 cached input tokens, and 3511
  output tokens, including 1664 reasoning-output tokens.

Receipts:

- descriptor SHA-256:
  `933BACBC1BD7DD27B042CA508CC33B9C4B8DB1529D931D27C28C34D777E7DBD0`;
- authorization SHA-256:
  `CD5D91716D7A30BD51CADE01037C22083F17904D5C990E28623CCEE7FC0A8B7B`;
- result SHA-256:
  `050A8A24AD42494D225712B9927FB9940181BF37A41ADAA8387F37716AE3EC6E`;
- validation SHA-256:
  `C1E87B44A6AFAA3CD53EF52027BEEEC6783D60575A4A1A9ACEB06C1A385BE32E`;
- raw-events SHA-256:
  `9755198AC3F53673380F71EFE1C296C91E6C78655BE25C2667A3369589338EFC`;
- artifact SHA-256:
  `D04BD972B4F8C4D119F2CCA4111E21A753845E48A1A6B476817552F5CD9E5100`.

## Deterministic package evidence

The final package passed 17 of 17 unit tests, 50 of 50 route fixtures, package
validation, generated-index drift validation, the Design/UI ownership-boundary
validator, Skill Creator validation, and whitespace validation. Measured common
loads are Core 1465 tokens, generated index 1189, largest expert 2340, Core plus
index 2654, and Core plus the largest planned phase 11677. The package validator
reports 12 advisory expert token-target warnings and no hard failure.

## Reviewer basis and limits

The post-fix behavioral evidence is one exact Terra High model response scored
by deterministic authenticated-read, terminal-alignment, and artifact checks.
It is not a multi-reviewer visual panel and made no render. Earlier SOL reviews
are historical planning or package-review context only. Fable 5.1 is a Plan
reviewer only, and Opus 5 remains untested; neither supplies product-behavior
evidence.

Qualification-v7 stopped after three calls: Canary 1 passed, then Canary 2
exposed the subsequently adjudicated Gold defect and package boundary mismatch.
No holdout shard ran. The planned complete sealed rerun was explicitly omitted,
W-005 is cancelled, and no retrospective sealed qualification credit is granted.

The supported release claim is limited to this: on the frozen ADR-0048 package,
deterministic contracts passed and one source-cleared Terra High replay resolved
the reproduced fixed-specialist-diagram over-read with exact authenticated
routing. Publication, installation, commit, push, tag, and release remain
separately prohibited.
