# Release validation v1.2.0

Checked on 2026-09-08 in an isolated publication worktree. The release contains
the final canonical Skill and selected reproducible development checks. Local
session transcripts, frozen candidate copies and raw blind-review archives
are not publication inputs.

## Observed checks

- All 65 Python unit tests pass in the prepared public tree.
- Package validation passes for successor-v2 with 30 modules and zero warnings.
- The direct index is current. All 65 static route cases and the Design/UI
  ownership boundary check pass.
- Skill Creator validation and the GitHub Skill repository-structure check pass.
- The measurement helper passes real Edge/Playwright cases for relationships,
  style drift, invalid evidence and preservation controls.
- The SVG inventory helper passes transformed instances, nested and oversized
  bounds, repeated anchors, adjacent art and text, unsupported-source handling
  and unchanged-DOM checks. An inventory does not issue a design verdict.
- The runtime builder exports 54 files. The release ZIP is checked against
  every canonical package file and includes the MIT license. Its SHA-256 file
  accompanies the asset.

## Development evidence and limits

The [development summary](evaluation/human-blind-test-development.md) records
five human-reviewed Astra Medium rounds, 28 pairs and 56 designs, with separate
AI reviews and retained disagreement. Those experiments used evolving package
revisions and changing briefs. They do not qualify the final package as
generally superior to an unassisted model.

The final compound-join follow-up used visual and measured local specimens.
No new broad behavioral test or unseen holdout was run for publication.
Passing source, helper and routing checks does not prove that an agent will
notice every visual failure, load every applicable module or produce a
professional result on every brief. Physical production and host-specific
behavior still require task-appropriate evidence.

## Distribution

The installable package is the single top-level
`scoville-design-anti-ai-slop/` directory. Research and development tooling stay
under `development/` and are excluded from the runtime ZIP. Older release notes
remain in the changelog. The v1.2.0 ZIP and checksum replace the v1.1.0 assets
when the new release has been verified.
