# Design v1.1.0 release validation

Checked on 2026-09-05 for the release requested after PLAN-0008. This release
ships the practical-guidance additions and removal of package-size guidelines.
Publication is authorized separately from the local-only scope of those plans.

## Candidate checks

- 26 unit tests pass with Python 3.14 and no installed `tiktoken`.
- Package validation passes for 30 modules with zero warnings. The generated
  index is current, 60 route cases across 44 signals pass, and the Design/UI
  boundary passes. These fixtures do not establish automatic host discovery.
- Agent Skill validation and the required Skill repository layout check pass.
- Native planning validation passes with eight plans, 49 work items and
  59 decisions, with zero errors or warnings.
- The new isolated runtime export contains 35 files, including the exact MIT
  license. Source, exported runtime and ZIP members match byte for byte.
- The eight public Scoville members, their default branches and literal
  installation directories were checked through GitHub. Each directory
  contains `SKILL.md`. The complete-suite prompt matches that set, and the
  canonical family blocks agree. The profile contains one Design entry under
  Scoville family. No profile or sibling repository change is needed.

## Package and assets

The installable source remains `scoville-design-anti-ai-slop/`. Development
files, local trial output and model transcripts are not installation assets.

- Runtime manifest SHA-256:
  `236BB694B0DF74294E758D0AA560754C79B6BD96CB0DA0C0B4347DF08637BD69`.
- Asset: `scoville-design-anti-ai-slop-v1.1.0.zip`.
- ZIP SHA-256:
  `3742a7401b92138694871c3d15ed3663d0ee8b72d3f4a509f8938026aeda5ffe`.
- Checksum asset: `scoville-design-anti-ai-slop-v1.1.0.zip.sha256`.

The ZIP contains one top-level `scoville-design-anti-ai-slop/` directory.
Its 35 files match the canonical package. The archive integrity check passes.
The two v1.0.3 assets have these verified successors. The v1.0.3 README-link
correction remains recorded in the changelog. Old release records and tags
are retired only after GitHub verification of the replacement.

## Artifact evidence and limits

The [implementation report](evaluation/plan-0008-implementation.md) and
[receipts](evaluation/plan-0008-receipts.json) retain exact scope, outcomes and
source hashes. Three separate supplementary model calls produced six rendered
artifacts. They exercise coupled typography settings and line/area map-label
placement at two sizes. Six Motion-state checks cover the corrected coordinator
derivative. Original results remain unchanged, including failed observations.

These are local source and artifact observations, not evidence of a general
model advantage or complete host qualification. The original PLAN-0006 W-004
work remains unfinished. The focused Terra host critique that omitted
Composition is still not a workflow pass. Its unrendered host cases are
distinct from the later locally rendered studies.

Historical records retain their original paths, protocols and hashes. The
three measurement receipts produced with CRLF retain those exact bytes through
explicit Git attributes. Their values describe the historical runs and impose
no current size guideline. External trial and custody files remain outside the
repository and release assets. No local Skill installation is part of this
publication request.
