# W-005 public three-owner routing regression

Date: 2026-09-03  
Status: passed; sealed failure not reproduced  
Decisions: ADR-0038 through ADR-0041

## Question

Qualification-v6 Canary 1 observed one authenticated Design expert read against
three private Gold owners. The public falsifier asks whether the unchanged
package also fails when a newly authored source-cleared brief requires the same
three owner IDs without revealing any private case fact.

The public Gold owners are:

- `editorial-and-fixed-media-design`;
- `colour-and-reproduction`;
- `media-production-and-handoff`.

The fixture reused no private facts, wording, artifacts, scores, signatures or
mechanism-specific details. Its normalized five-token overlap with private
model-visible wording was zero; only the three explicitly authorized owner IDs
were derived.

## Execution history

Attempt 1 and attempt 2 were rejected before inference by the provider response
schema. Attempt 1 lacked explicit types on three constant properties. Attempt 2
retained unsupported `uniqueItems`. Both failures are preserved separately and
contain zero model response, output, usage, authenticated read or behavioral
evidence. Neither was an outcome retry.

ADR-0040 normalized attempt 3 to property shapes already accepted by the same
pinned CLI and provider in qualification-v6. Twelve of twelve model-free tests
passed before execution. Attempt 3 then produced one terminal response with no
retry.

## Route result

The raw command events contained one successful `Get-Content` command for all
three exact staged expert files. PowerShell emitted doubled but valid Windows
path separators. The canonical extractor originally rejected that spelling
before route comparison. ADR-0041 added separator-only canonicalization while
retaining exact filename, staged containment, completed-command, non-empty
output, no-wildcard and single-terminal-message gates. Fourteen of fourteen
tests pass, including outside-workspace, traversal, UNC, wildcard and unknown
expert rejection.

Immutable replay then produced:

- authenticated Gold reads: 3 of 3;
- terminal selected experts: the same 3 of 3;
- route gate: pass;
- terminal-report alignment: pass;
- public result contract: pass;
- completed command events: 5;
- terminal model responses: 1;
- outcome retries: 0;
- sealed calls: 0.

The requested `production-plan.md` exists and preserves the brief's unknown
printer, profile, ink, proof and acceptance boundaries. No render or production
proof was requested or claimed.

## Evidence hashes

- Attempt-1 failure receipt:
  `EFEA0954AEAEB1EC6B98CE0D9E32DCD9AA50CD24010082725C93B1827543BF98`
- Attempt-2 failure receipt:
  `1D35810907F4ECB46CBD26A0151948F0C7DC6BB42A8B614DA7807F654CD9D352`
- Attempt-3 raw events:
  `BBBF33A0573359AFEB5129591A086CFF443639A78AEAA56731695B9B45EFA9BF`
- Attempt-3 artifact:
  `35A0EF4E38935F3980322C627403D09BE7B9B2A6EE463E245DB6EE4500200A29`
- Repaired route extractor:
  `7708F1994AE5966A14E48180D1AC03AE85CBA1A5B1B92B3049F5656FD5AB065A`

## Verdict and claim limit

The public three-owner regression did not reproduce the sealed one-of-three
read failure. Under ADR-0038, the sealed cause therefore remains unconfirmed and
the package must not change from that private result alone. qualification-v6
remains failed historical evidence; the public pass neither qualifies the
package nor permits continuation of v6, publication or release operations.

A broader diagnostic requires a separate accepted decision and must preserve
the private case boundary. Any future sealed suite using the repaired route
extractor requires a new runner manifest and fresh generation.
