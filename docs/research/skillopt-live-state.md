# SkillOpt live-state inspection

Inspected: 2026-09-01  
Workspace: `Z:\Projekts\AI\SkillOpt-Studio`

## Verified runtime

- Studio wrapper: `studio.ps1`
- Vendored Microsoft SkillOpt checkout:
  `vendor/SkillOpt` at detached commit
  `ba820b500f9da96685cf2780c7dc85ed4eb6563e`
- Vendored worktree: clean at inspection
- Runtime Python: `vendor/SkillOpt/.venv/Scripts/python.exe`, Python 3.11.15
- Default optimizer: `gpt-5.6-sol`, xhigh
- Minimum promotion target: `gpt-5.6-terra`, medium
- Default runtime network: disabled
- Default output location: Studio-local `runs/<run-id>`

## Canonical split vocabulary

Physical benchmark directories are `train/`, `val/`, and sealed `test/`.
SkillOpt evaluation aliases are:

| SkillOpt alias | Physical split | Intended role |
| --- | --- | --- |
| `train` | `train` | optimizer-visible examples |
| `valid_seen` | `val` | open validation during development |
| `valid_unseen` | sealed `test` | promotion-gated final holdout access |

The Studio adapter loads only Train and Validation initially. It opens Test
only after the benchmark seal is present and `valid_unseen` is explicitly
requested. The deterministic controller accepts only `train` and `val`; sealed
Test is intentionally outside that controller path until the separate
promotion gate.

## Commands to use later

```powershell
./studio.ps1 preflight
./studio.ps1 eval --run-id <baseline-id> --split valid_seen
./studio.ps1 train --run-id <train-id>
./studio.ps1 eval --run-id <holdout-id> --split valid_unseen
```

The last command is prohibited until implementation and SkillOpt candidate
selection are frozen and the independent custodian authorizes holdout access.

## Implications for Design and UI

1. Create separate Design and revised-UI benchmark roots with frozen
   `train/val/test` files and seals.
2. Keep permitted external comparison pairs only in Train and group them by
   source; they must not cross into Val/Test.
3. Optimize Design and UI independently before paired composition evaluation.
4. Use the controller for activation and reference-routing contracts, and the
   free-agent path for semantic execution. Neither path supplies a trustworthy
   automated aesthetic oracle.
5. Preserve the unoptimized Design package and current pre-rescope UI hashes
   for later human visual regression comparisons.
