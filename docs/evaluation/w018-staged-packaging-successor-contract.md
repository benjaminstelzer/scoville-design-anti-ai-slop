# W-018 staged packaging successor contract

Date: 2026-09-02  
Status: development contract; not yet executed

## Reason for staging

D28-PK1 combined two complete SKU flats, an assembled lineup, a repair record
and extensive source validation in one call. It reached the fixed 300-second
timeout after creating artifacts but before a terminal response. Renderer access
does not reduce that workload. The successor splits causal work without raising
the timeout or weakening proof.

## Stage PK2-A — one canonical carton template

- Inputs: one supplied immutable dieline, one SKU, exact content and known
  panel/type defects.
- Open owners: Packaging + Typography only.
- Forbidden: Composition, Fixed Media, Production, Colour.
- Output: one editable flat SVG and compact panel/type repair record.
- Proof: exact panel/fold/safe/barcode IDs, exact content, parent render at fixed
  conditions and one injected render-feedback repair only if a visible defect
  remains.
- Stop: inspect terminal receipt and render before PK2-B.

## Stage PK2-B — family application and assembled comparison

- Inputs: accepted PK2-A canonical template/source, second SKU exact content,
  both parent renders and unchanged dieline.
- Open owners: Packaging + Typography only.
- Output: second flat plus identical-context front/side lineup.
- Proof: template parity, exact SKU-variable diff, name-plus-band redundant
  distinction, identical scale/view and parent-render inspection.
- Stop: no third call or broad validation retry without a new contract.

## Claim boundary

The staged cases test graphic mapping, typesetting and visible family
differentiation only. They cannot establish structure, material fitness,
barcode validity, regulation, print/provider acceptance, shelf performance or
purchase behavior. They are development cases and do not reuse W-017 as a
holdout.
