# W-005 qualification-v6 Canary 1 fail-stop

Date: 2026-09-03  
Status: qualification-v6 failed and stopped  
Decisions: ADR-0036 through ADR-0038

## Result

The signed v6 authorization admitted only the six preregistered canary shards
and the remaining holdout after all six passed. Canary 1
`S-E0FB91B47A62` registered exactly its two arm-parity jobs. The baseline passed
9 of 9 scorer checks. The candidate passed 8 of 9 and failed the route gate.

- Canary shards passed: 0 of 6
- Canary shards started and completed: 1 of 6
- Terminal jobs: 2 of 150
- Model-response calls: 2
- Transport attempts: 2
- Retries: 0
- Renders: 0
- Aggregate scorer checks: 17 of 18
- Non-canary jobs started: 0

The candidate's authenticated staged-package reads contained one expert against
three preregistered expected experts. Its terminal route report aligned with
the single observed read, so terminal self-reporting did not conceal the
mismatch. No later canary or holdout job started.

## Bounded adjudication

The receipt classifies the failed gate as `authenticated_route_gate` and the
primary cause as `skill_package_defect`. The expected files existed in the
frozen snapshot. No parser, scorer, runner, transport or observed Gold-integrity
error explains the mismatch.

This classification is bounded rather than conclusive. Existing public tests
cover authenticated-read extraction but not the same three-owner behavioral
route selection. ADR-0038 therefore requires one newly authored source-cleared
public regression before any package change. If it does not reproduce, the
sealed result alone cannot justify a routing patch.

## Integrity evidence

- Execution authorization:
  `8989CA4B7C6BCBB0695953A34FAF95AB9377F2D32B3A28ACAAC5BDB4D7C41A5C`
- Runner manifest:
  `186C42F7ED1F11257D336B0AC5C300272D1B79A19939AD2C843FDA72C9F658B5`
- Fail-stop receipt:
  `DC8B0DD8995CE97561E095FF358E411A7B576E9C4D26232542C1FF54B51187C2`
- Failure adjudication:
  `093E193A10F949D851AEE1F5D66A45D9DB8D7392E13A551B5B3F5DA56BED07DF`
- Sealed failure result:
  `8C4D5DA1805C4EEC03B6710DB9DD64618019C13E4F7DB1F0B4682192AC0C677D`

The encrypted result passed authenticated round-trip and tamper rejection.
After fail-stop, no plaintext run files or active shard lock remained, sealing
made no provider call, the Custodian disclosed no keys, and scope did not
expand.

## Claim limit

Qualification-v6 is failed historical evidence, not a partial pass. It proves
the signed authorization and canary fail-stop operated on the first failing
shard. It does not establish the cause beyond the bounded adjudication, does not
qualify the product, and does not authorize publication or release operations.
