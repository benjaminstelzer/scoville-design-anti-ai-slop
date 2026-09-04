---
format_version: 1
id: ADR-0003
status: accepted
created: 2026-09-01
accepted: 2026-09-01
scope: knowledge/licensing
transition_batch: 2f8f411b120257971bedf6a858d451262a7857491826e9b29e4833c7ad439380
transition_batch_members: [ADR-0003, ADR-0006, ADR-0007, ADR-0008, ADR-0009]
---

# Use original, license-screened source synthesis

## Decision

Use CC BY 4.0, CC0/public-domain material, standards, and open research as the
preferred directly traceable source base. Write original Skill guidance from
verified facts, scoped findings, and ideas. Keep CC BY-SA works as linked
learning unless the repository intentionally accepts the applicable ShareAlike
obligations. Keep NonCommercial, NoDerivatives, and all-rights-reserved works
reference-only by default. Track knowledge-source provenance separately from
font, image, icon, template, dataset, and brand-asset permissions. Do not
vendor third-party books, screenshots, comparison images, or datasets in the
repository. When such material is useful for local evaluation, keep it in a
separate local-only workspace outside the repository only after the intended
use is permitted. Location never substitutes for permission.

Classify every contemplated external artifact before use:

1. **Public fixture:** redistribution, modification, commercial evaluation,
   model-input, logging, and evidence-publication rights are verified.
2. **Local evaluation only:** the exact evaluation and model-input use is
   verified, but redistribution or evidence publication is prohibited.
3. **Method/reference only:** no artifact download, model input, optimization,
   derived fixture, or output publication is permitted or needed.

Unknown or ambiguous permission defaults to Method/reference only. Version one
contains no adapted CC BY-SA expression. Reference-only expressive sources are
closed while distributable prose is authored; authors work from scoped claim
notes and then screen the result against accidental copying. The installed
Skill package carries its own source and attribution file because a repository
README does not necessarily travel with installation.

## Problem

The strongest design books and public Skills use mixed licenses. A public MIT
Scoville package cannot casually copy, paraphrase closely, adapt, or bundle all
of them. A URL proves provenance, not permission.

## Drivers

- The future README needs correct source and license attribution.
- The Skill should remain commercially reusable and independently authored.
- Source facts, empirical findings, practitioner heuristics, and expressive
  text have different reuse boundaries.
- Supplied and generated assets create separate permission and attribution
  obligations from the knowledge base.

## Considered alternatives

- Copy open web books and Skills into references. This risks ShareAlike,
  NonCommercial, NoDerivatives, attribution, and copyright conflicts.
- Cite sources without recording license or use. This is insufficient for
  redistribution and later maintenance.
- Use only public-domain historical texts. This avoids some rights issues but
  leaves contemporary media, accessibility, and technology gaps.

## Consequences

- A source ledger records author or publisher, title, date/version, URL, access
  date, license, claim/use, and restrictions.
- Repository tests use original or explicitly source-cleared fixtures;
  downloadable third-party evaluation material is not committed by default.
- An external-material receipt records source and item ID, rights holder,
  license/version and upstream terms, permitted operations, storage class,
  content hash, inspection date, log/output handling, retention, and deletion.
  It contains no restricted artifact bytes.
- The local evaluation workspace is the sibling directory
  `Z:\Projekts\AI\scoville-design-eval-local`, never a path below either
  repository. It is created only if a permitted local artifact is actually
  needed.
- README sources are generated from verified ledger entries.
- The distributable Skill package includes `references/sources-and-attribution.md`.
- Reference files cite their important factual and empirical bases without
  copying source prose.
- ShareAlike or restricted material requires an explicit later licensing
  decision before adapted expression enters the package.
- This screening is not a substitute for legal review where use remains
  ambiguous.

## Confirmation

Every public source claim and bundled asset resolves to a ledger entry with a
verified license or an explicit unknown/restricted status. Every contemplated
external evaluation artifact has one of the three use classes and a receipt;
unresolved material remains Method/reference only. Repository diff review
finds no copied passages or restricted fixture bytes. README attribution and
the bundled attribution file match the ledger and distributed package.

## Revisit when

The repository chooses a different license, obtains separate permissions, uses
substantial adapted CC BY-SA content, or needs to bundle restricted examples
for evaluation.
