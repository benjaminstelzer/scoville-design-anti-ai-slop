# Repository maintenance

The repository's `scoville-design-anti-ai-slop/` directory owns the only Skill
source: `SKILL.md`, `modules.yaml`, `agents/`, `references/` and `LICENSE`.
There is no root authoring copy. Development lives under `development/`.

Development tools remain in `scripts/`. Unit tests are in `tests/` and run with
`python -B -m unittest discover -s tests` from `development/` using an
already configured development environment. This cleanup does not supply a new
dependency setup or replace the separately deferred reproducibility work.

## Path changes on 2026-09-05

| Recorded historical path | Current development owner |
| --- | --- |
| `scripts/test_validate_package.py` | [tests/test_validate_package.py](../tests/test_validate_package.py) |
| `scripts/test_successor_v2.py` | [tests/test_successor_v2.py](../tests/test_successor_v2.py) |
| `scripts/test_design_ui_boundary.py` | [tests/test_design_ui_boundary.py](../tests/test_design_ui_boundary.py) |

The hash-bound Fable implementation contract, original acceptance receipt and
release validation record retain their original paths and commands as history.
Use the mapping above for current development. No acceptance condition, fixture
or test was removed. The original 32 unit tests pass at their new location.

`docs/` retains provenance, Decisions, Plans and evidence needed by the existing
owners. `evaluation/` retains the frozen fixtures and focused artifacts they
reference. Their old failures and manifests are not superseded by a newer
package build. Browser working copies and Python caches are not distributed.

## Current package and evidence

From the repository root, run `python -B development/scripts/generate_module_index.py --check`
and `python -B development/scripts/validate_package.py`. The generator updates
only the canonical package's module index. The validator checks its references
against the separately retained development source map and evidence receipts.

`python -B development/scripts/build_package_manifest.py --output <new-manifest.json>`
records the canonical package; `--check` detects manifest drift.
`python -B development/scripts/build_runtime_package.py --destination <new-directory> --receipt <new-receipt.json>`
exports the same 35 package files byte for byte to a new external directory.
It refuses existing or overlapping destinations. Legacy comment stripping is
retained only for historical synthetic fixtures. It never recreates root sources.

The runtime builder includes the package's exact LICENSE through
`modules.yaml`'s `distribution_files`. The current runtime contains 35 files.
Earlier 34-file manifests remain historical evidence. This source change does
not imply new model or host evaluation.

PLAN-0006 W-004 retains the original proposal-session final review and the
remaining host-routing work. Five focused Terra Medium host observations are
documented in [the current record](evaluation/2026-09-05-terra-host-results.md).
The hierarchy critique omitted Composition, and no artifact was rendered.
File organization and deterministic checks do not resolve those limits.
