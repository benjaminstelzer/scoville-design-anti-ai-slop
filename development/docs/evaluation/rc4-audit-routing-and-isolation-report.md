# RC4 package audit, routing, and isolation report

Date: 2026-09-02  
Model scope: GPT-5.6 SOL, xhigh reasoning  
Status: superseded by RC7 after later independent route findings  
Successor: [RC7 final audit and routing report](rc7-final-audit-and-routing-report.md)

## Why RC4 exists

An independent SOL read-only audit found four release blockers in the earlier
candidate:

1. critique could be interpreted as permission to create or modify an artifact
2. phase transfer and Design-to-UI handoff used different record schemas
3. privacy, sustainability, synthetic evidence, and recurring template routes
   were not visible enough in the direct index
4. only entrypoint hashes, not the complete executable package, had been bound
   to the first qualification attempt

The audit also found that a generic exception signal could over-route
Composition and that an over-broad Critique label could capture source-only
audits.

## Repairs

RC4 now:

- resolves mode before tools and makes `critique` read-only
- permits artifact changes only in authorized `repair`, `generate`, or creating
  `style-direction` work
- uses one canonical nine-field record for phase transfer and Design-to-UI
  handoff
- routes layout exceptions to Composition and general design exceptions to
  Critique without forcing Composition
- exposes privacy, sustainability, synthetic evidence, and jurisdiction duties
  to Culture and Provenance
- exposes recurring template systems to Brand and Visual Systems
- distinguishes a deep visual critique from a fact, license, privacy,
  jurisdiction, or source-only audit
- explicitly routes generated or documentary imagery to Imagery and Art
  Direction

Independent SOL re-review closed every original finding and found no new P1 or
P2 issue after the final route correction.

## Open regression history

The failed or ambiguous suites remain unchanged.

| Suite | Purpose | Train hard | Validation hard | Interpretation |
| --- | --- | ---: | ---: | --- |
| v3 / RC2 | First audit-driven routes | 2/5 | 3/5 | Four narrow or ambiguous Golds and one real imagery miss |
| v4 / RC3 | First adjudication plus router repair | 4/5 | 3/5 | Sustainability and synthetic-image defects closed, three audit/template boundaries remained |
| v5 / RC4 | Final adjudication plus source-only boundary | 5/5 | 5/5 | All ten open regression cases passed |

The final run IDs are `design-rc4-routing-train-r1` and
`design-rc4-routing-val-r1`. Their soft scores were 0.952028 and 0.944444.
These are open regression results, not unseen qualification evidence. No v3 or
v4 Gold was rewritten after execution.

## Executable identity

The executable package is exactly 17 files:

- `SKILL.md`
- `modules.yaml`
- `agents/openai.yaml`
- fourteen direct expert references

The canonical package manifest hashes sorted UTF-8 records of
`path\0byte_count\0file_sha256\n`.

- package manifest SHA-256:
  `D642852D18B01D6578526AD01568EA42C83CA3FC5DC5BCC9F7B8987E1334C8B2`
- `SKILL.md` SHA-256:
  `384F4DDEC526B3F3FA9148004AA31CE1731BC9BAAE66ABB8521B9C0CE527A4D8`
- `modules.yaml` SHA-256:
  `0152EE19319830887E3ECA55D6683C90CFA51246DF186204213DBF402A1BCA39`
- manifest file:
  [rc4-executable-package-manifest.json](rc4-executable-package-manifest.json)

`scripts/build_package_manifest.py --check` proves that the live package still
matches this manifest. The immutable SkillOpt snapshot is
`frozen-controls/scoville-design-rc4-final` in the separate local Studio.

## Holdout isolation defect

The first qualification attempt read live source directories. The custodian
stopped it before any result was accepted. Fifty-four completed executions and
three incomplete workspaces were invalidated. All 219 plaintext run files were
deleted. Product evidence retained from that attempt is zero.

The local-only infrastructure receipt has SHA-256
`8118a88721970a4e08b9d33c191bfad374764701edd55d73a2681632e34f9642`.
Its contents and the holdout remain outside both public repositories.

The clean rerun may read only custody-owned immutable snapshots of Design, UI,
and the pinned Taste comparator. Its preflight must bind full package manifests
before any case executes.

## Claim boundary

This report supports package identity, open routing regression, and quarantine
of an invalid infrastructure run. It does not prove broad design quality,
human preference, expert equivalence, or superiority over another Skill. Those
claims remain gated by the clean sealed results and the independent human
review protocol.
