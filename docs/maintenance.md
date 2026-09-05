# Repository maintenance

The root `SKILL.md`, `modules.yaml`, `agents/` and `references/` own the
authoring source. The nested `scoville-design-anti-ai-slop/` package is generated
by `scripts/build_runtime_package.py`. It is not a second authoring source.

Development tools remain in `scripts/`. Unit tests are in `tests/` and run with
`python -B -m unittest discover -s tests` from the repository root using an
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

The runtime builder includes the repository's exact LICENSE through
`modules.yaml`'s `distribution_files`. The current runtime contains 35 files.
Earlier 34-file manifests remain historical evidence. This source change does
not update installed or published copies.

PLAN-0006 W-004 retains the original proposal-session final review and the
remaining host-routing work. Five focused Terra Medium host observations are
documented in [the current record](evaluation/2026-09-05-terra-host-results.md).
The hierarchy critique omitted Composition, and no artifact was rendered.
File organization and deterministic checks do not resolve those limits.
