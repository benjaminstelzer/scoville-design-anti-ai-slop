# W-005 qualification-v6 zero-call readiness

Date: 2026-09-03  
State: `v6_zero_call_readiness_verified_then_authorized`  
Decisions: ADR-0036 and ADR-0037

## Frozen scope

- Design manifest: `3D19CE209E52AFCE91B888D6FB489E29EA9846A1442896129563D4B94ADC01C2`
- UI manifest: `FD255A274E2D92C6DDA14CAD2A85FF0E7702960CEE6B2D3B9F20E04A78A78875`
- Fresh source-cleared cases: 30
- Jobs: 150
- Arm-balanced shards: 75
- Fresh preregistered canary shards: 6
- Runtime jobs registered: 0
- Provider calls: 0
- Sealed calls: 0
- Sealed calls authorized at freeze: false
- Later execution-authorization receipt: present and hash-bound

The new custody uses two AES-256-GCM tranches. Authenticated round-trip and
tamper rejection passed, substantive five-token maximum Jaccard similarity is
0.09, the private generator is absent, and no plaintext run file or active lock
remains.

## ADR-0036 evidence policy

The route score is derived from authenticated completed command events that
read exact expert files inside the frozen staged package. Missing, forbidden,
malformed, ambiguous and out-of-snapshot reads fail closed. Terminal
`selected_experts` is retained as a separate `reported_route_alignment`
diagnostic and cannot create route credit without an authenticated read.

Public synthetic confirmation passed all eight required categories. The first
readiness review then found that the runner reported an unauthorized state but
did not enforce it before protected commands. ADR-0037 corrected that bypass
without changing the schedule, canaries, packages, ciphertext or outcomes.

The final root-side suite passed 38 of 38 tests:

- 13 signed-authorization, finalizer and gate-before-effect tests;
- 10 route/scorer tests;
- 4 zero-call runner registration, idempotency, lease and shard tests;
- 11 adversarial readiness-validator tests.

The adversarial set includes v5-score reuse, custody reuse, package-manifest
tampering, route-authority tampering, schedule-count tampering, duplicate
canaries, synthetic-case loss, absent or tampered execution receipts and
premature authorization. The real runner CLI rejects registration before
creating runtime state when the live receipt is absent.

## Frozen hashes

- Authorization policy: `A2F5CAE30CD5B41790376755A0A77CF7A4ACAFA0845A35243EC47014077A1F92`
- Authorization verifier: `3E8173E2E5B7D1230A4D35705431936D2F053FEE464239CC4873BC8DC6C14779`
- Authorization finalizer: `2BBAAC83704B86F92B88D5C573D7924BA3D7DD4E053BAA1CD944A9DD42852DCF`
- Sealed runner: `BB969F1D1B83A90A45FB0A5800287CD02A1357FE0E4E78BEA457E2B96EEDF494`
- Runner manifest: `186C42F7ED1F11257D336B0AC5C300272D1B79A19939AD2C843FDA72C9F658B5`
- Readiness receipt: `931448508DE340518E0CE4AE9BCB6C0221FB98C04637E6ABAB6D5E43C1069343`
- Readiness validation: `58F4CC38CCA0516FBA87DEADB5E5CE068B87DCCDDF3A76BCC216CE4A08418C40`
- Schedule: `03EAC61F18F40E58552EDB1268AD616EA10A6652721EF656A109093CC4DE8BB5`
- Job classification: `E505CD5C8299411F5702961059FA1C0D0D6D81CA8712327B5DE869D4A4E60626`
- Canary preregistration: `26620149CF99C35B28638F5A04937AE4334CD0CE8323C5B2E045212E3B57E294`
- Custody receipt: `1C4439AE4A2879F2BEC36754560F016230AD5B9364915ABE2DF33EED18F40E49`
- Synthetic receipt: `179FBBC9644A28B3F96F16C80B2DEE53A492711B597A0CECACCAFC5EBAC4A66B`
- Cipher tranche 1: `C668217E08E31CC197BBCEABC2275C421A023F04431AF376A7399A6191F1C312`
- Cipher tranche 2: `593D2CC231319EF77D777BDDC53D6F6F4BB8B7992798F3E9D3A914CFEC5D2C8A`
- Opaque manifest tranche 1: `B03D6E6C89BCAF46E74F1439BC9EE271B9746F173DADB8D30DF23CEE39FC632D`
- Opaque manifest tranche 2: `962B6F6A8FFE8EA4BC29816A0C50353E091A859A4D27BE4BF03039E6C3BA6E56`

## Remaining gate

This document records the final zero-call freeze. The user later authorized the
exact six-canary scope under receipt
`8989CA4B7C6BCBB0695953A34FAF95AB9377F2D32B3A28ACAAC5BDB4D7C41A5C`.
Canary 1 then failed its authenticated route gate and the suite stopped. See
`w005-v6-canary-fail-stop.md`; the remaining five canaries and 138 non-canary
jobs stay closed.
