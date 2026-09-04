# W-005 ADR-0047 targeted boundary diagnostic

Date: 2026-09-03  
Status: package boundary mismatch remains; one public falsifier ready

## Proportional scope

The user rejected a complete 150-job rerun as unnecessary token expenditure.
ADR-0047 therefore superseded the full v8 rebuild and restricted verification to
the one defective v7 contract boundary.

The partial v8 zero-call build was removed from the active path and placed in a
non-executable retirement quarantine. It made zero provider or sealed calls,
registered zero runtime jobs, left zero locks and private plaintext files, and
contributes no product evidence. Retirement receipt SHA-256:
`3D155D2D4DBEC08E28B1BDA91311F0ECD2B3F209EA2DE284A57EA6DC25E514DF`.

## Model-free corrected diagnostic

The independently corrected private contract expects one Design expert read.
Immutable v7 Candidate evidence contains three authenticated reads, and the
terminal report aligns with those three.

- corrected expected reads: 1;
- authenticated reads: 3;
- terminal selected reads: 3;
- exact route: fail due to additional authenticated reads;
- terminal alignment: pass;
- classification: `gold_defect_closed_package_boundary_mismatch_remains`;
- retrospective qualification credit: none.

Diagnostic receipt SHA-256:
`F0A6C0022DE96301BBFA7F9AF5C0B39156B2451E3390F2DE807F8F9BE7021DC8`.
Validation SHA-256:
`3F72514B451DB8639773C20B3DFB5E5DEC2E58E95A545AA6596F84F5C4A3F3E0`.

## Public falsifier readiness

A newly authored source-cleared public case isolates the disputed boundary
without reusing private facts. Its exact Gold route is
`diagrams-and-relational-information`. It forbids
`composition-and-layout`, `typography-and-typesetting`, and
`instructional-and-explanatory-design`.

All 12 zero-call tests passed. The execution contract permits exactly one Terra
High public call, no retry, zero sealed content and fail-closed result scoring.

- descriptor:
  `32A1D85B0542B15FF64EBE7E30FB69F543C937FD3B28BC05FD430ED1F6F47CC4`
- zero-call preflight:
  `8C97BA0E5A4959A8C0D383D71E4E8E2D3AF2182EF0D38106E2423077B288B835`
- validation:
  `B6AB6D4A3C1EE6493C36D19703B6E79D097D3D4100BB1FBB6BDDBB7749CEF7D2`

No public provider call is authorized by readiness alone. Publication,
installation, commit, push, tag and release remain prohibited.
