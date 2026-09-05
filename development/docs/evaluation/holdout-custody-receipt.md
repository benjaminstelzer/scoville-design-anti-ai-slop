# Holdout custody receipt

Creation date: 2026-09-01

Custodian target: `/root/design_holdout_custodian`

Total sealed cases: 30

Tranche one: 18 cases under suite `design-holdout-v1.0.0` and rubric
`design-holdout-rubric-v1.0.0`.

Tranche two: 12 cases under suite `design-holdout-tranche-2-v1.0.0` and rubric
`design-holdout-application-rubric-v1.0.0`.

## Archive and manifest hashes

| Tranche | Artifact | SHA-256 |
| --- | --- | --- |
| 1 | Encrypted archive | `3884433d5c10fab8763730c7f001501438620dc6a61d9f6cb4c53e67b9796bb7` |
| 1 | Opaque manifest | `4834ff6970a59d6826f951b24795a77409bae0d80187333d3bd10565d85b4fcf` |
| 2 | Encrypted archive | `5eb1e116329125d6f880c71e7de72c4e44c11ccc46b406f03e258ea0f62485f3` |
| 2 | Opaque manifest | `5c54b6542206dcccf58ac29e6145ac35cfa98069e90fd060036e81b210850531` |

Tranche one was resealed before implementation under a new independent
custodian-held key. Its current archive hash supersedes the earlier receipt.
The superseded ciphertext was removed after the replacement passed complete
round-trip verification.

## Aggregate mode coverage

| Mode | Cases |
| --- | ---: |
| Generation | 12 |
| Critique or discrimination | 7 |
| Repair | 8 |
| Ownership and activation boundaries | 3 |

## Application-first lane coverage

These are conservative explicit counts across the combined 30 cases. A case is
counted only when its sealed record directly tests the named lane.

| Lane | Cases |
| --- | ---: |
| Generation | 12 |
| Strong, weak, and generic-cliche discrimination | 5 |
| Targeted repair with rerender judgment | 8 |
| Professional style execution | 8 |
| Selective theory and history use | 5 |

## Aggregate domain coverage

| Domain | Cases |
| --- | ---: |
| Editorial and static graphics | 10 |
| Typography and writing systems | 9 |
| Brand systems | 5 |
| Information and data | 4 |
| Document output | 3 |
| Presentation output | 4 |
| Template output | 2 |
| Imagery and art direction | 4 |
| Greenfield UI | 2 |
| Incumbent UI systems | 3 |
| Accessibility | 17 |
| Motion and sequence | 2 |
| Production boundaries | 11 |
| Design-only | 2 |
| UI-only fallback | 2 |
| Composed Design plus UI | 2 |
| Installed but inactive | 1 |
| Opt-out ownership | 2 |

## Duplicate and overlap checks

Checks ran within tranche two and across tranche two against tranche one.

- Exact case and normalized-prompt equality used SHA-256.
- Near-duplicate detection used normalized 5-token shingle Jaccard similarity
  with a frozen threshold of 0.18.
- Semantic lexical overlap used TF-IDF cosine on normalized content words with
  a frozen threshold of 0.65.
- Numeric overlap used sorted prompt-number fingerprints.
- Manual adjudication compared artifact type, primary mode, transformation,
  protected dimensions, and causal task mechanism for the highest-scoring
  lexical pairs.

Result: passed. There were 0 exact case duplicates, 0 exact normalized-prompt
duplicates, 0 near-duplicate threshold pairs, 0 semantic threshold pairs, 0
numeric-fingerprint collisions, and 0 manually adjudicated mechanism
duplicates within tranche two or against tranche one.

## Encryption, integrity, and cleanup

- Encryption: AES-256-GCM whole-archive authenticated encryption with separate
  random 256-bit keys for the two tranches.
- Header encryption: passed. TAR filenames and headers are encrypted.
- Authenticated decryption: passed for both tranches.
- Archive round-trip: passed. Tranche one recovered 22 of 22 sealed files, and
  tranche two recovered 16 of 16 sealed files by relative path and SHA-256.
- Tamper rejection: passed for both tranches after a one-bit ciphertext
  mutation.
- Opaque-header scan: passed for both tranches.
- Plaintext cleanup: completed. Both resolved staging and verification trees
  were deleted after successful round-trip verification.

## Smoke and qualification limit

A smoke run can establish only case loading, tool availability, artifact
capture, and grader parsing. It cannot establish design quality, comparative
improvement, route stability across repeats, professional execution,
accessibility quality, or production readiness.

Qualification requires frozen comparator parity, repeated model runs,
deterministic gates, intended-context renders, required blind human review,
preserved disagreement, and symmetric benchmark-defect handling. The existence
of 30 sealed cases is not itself a qualification result.

The holdout prompts, case filenames, fixtures, expected outcomes, grader logic,
source assets, and decryption keys have not been provided to the parent agent or
Skill author. Both keys remain only in this custodian target's private
continuation context for later qualification after implementation is frozen.

