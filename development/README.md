# Development

The only installable Skill source is [`scoville-design-anti-ai-slop/`](../scoville-design-anti-ai-slop/).
This directory owns repository development and is not an installation package.

## Current size policy

ADR-0059 removes all package, Core, index, leaf and common-load size guidelines.
`scripts/validate_package.py` and runtime builds check structure and evidence
without token measurement or size warnings. `scripts/measure_package.py` is an
optional descriptive report and requires `tiktoken`; structural checks do not.
The package's existing module identities and metadata field formats remain
structural contracts.

Pre-PLAN-0008 Decisions, plans, evaluation contracts, matrices and receipts are
retained historical evidence. Their numeric package-size prescriptions are not
current authoring policy, including `successor-module-registry.md`,
`fable-implementation-contract.md` and the PLAN-0007 contract. The historical
`docs/evaluation/validate_open_call_matrix.py` and
`validate_successor_28_open_matrix.py` only reproduce their frozen old matrix
contracts; do not use their size gates to admit current work. Current checks
are the scripts under `scripts/` and tests under `tests/`. Actual provider or
explicit user limits and immutable evaluation controls remain applicable.

## Current layout

Paths recorded before the 2026-09-05 structure change are historical. Use this mapping
for current local files; frozen evidence retains its original contents and hashes.

| Former repository path | Current repository path |
| --- | --- |
| `docs` | `development/docs` |
| `tests` | `development/tests` |
| `scripts` | `development/scripts` |
| `evaluation` | `development/evaluation` |
| `PROJECT_INDEX.md` | `development/PROJECT_INDEX.md` |

Run development commands from this directory unless the command specifies otherwise.
The installable package is one directory above. Tests, when present, run with
`python -B -m unittest discover -s tests` in the existing development environment.
This move does not add dependencies or establish new model or host qualification.

The native planning root is this directory: [`PROJECT_INDEX.md`](PROJECT_INDEX.md),
`docs/plans/` and `docs/decisions/` moved together.

## Frozen control texts

These files are evaluation inputs, not additional installable Skills. Their bytes
are unchanged. A new evaluation must copy the chosen control into its isolated
run directory as `SKILL.md`; never restore that name in this repository.

| Former path after directory move | Stored fixture path |
| --- | --- |
| `development/evaluation/controls/core-only/SKILL.md` | `development/evaluation/controls/core-only/SKILL.fixture.md` |
| `development/evaluation/controls/full-bundle-candidate/SKILL.md` | `development/evaluation/controls/full-bundle-candidate/SKILL.fixture.md` |
| `development/evaluation/controls/generic-checklist/SKILL.md` | `development/evaluation/controls/generic-checklist/SKILL.fixture.md` |
| `development/evaluation/controls/no-skill/SKILL.md` | `development/evaluation/controls/no-skill/SKILL.fixture.md` |
| `development/evaluation/controls/style-focus/SKILL.md` | `development/evaluation/controls/style-focus/SKILL.fixture.md` |
| `development/evaluation/controls/wrong-expert-media-floor/SKILL.md` | `development/evaluation/controls/wrong-expert-media-floor/SKILL.fixture.md` |
