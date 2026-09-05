# ADR-0054: Core loading clarification

## Change

After PLAN-0002 closed, replace the existing post-index loading sentence with:

> `SKILL.md` is the Core; load further files only via exact index links.

No design rule, expert reference, generated index, task prompt, Gold, or frozen
v9 result is changed. The clarification identifies the entrypoint and preserves
direct index-only loading without inventing an additional Core file.

- Original retained snapshot entrypoint SHA256:
  `76CD2F7F86B0FF5494F090EA1C1911EED158D4AB5B7109F7BDD121D95B71B206`.
- Final successor entrypoint SHA256:
  `A341CFDF23529180D72A92D9CD98144ECC44C4686866EB82E1174D2D3E67189C`.

## Structural evidence

The package comparison identified only `SKILL.md` as changed. The direct diff
is the two-line replacement above; the rest of the package remains unchanged.
The Skill Creator validator reports `Skill is valid!`.

The pinned package validator reports `VALID schema=successor-v1`, 28 modules,
core 1,468 tokens, index 1,189, largest expert 2,340, core plus index 2,657,
and core plus largest phase 11,680. The Core grows by three tokens. All existing
ceilings pass; twelve pre-existing advisory expert-token warnings remain.

An initial added paragraph exceeded four common-load ceilings: C03 was
4,629/4,600; C04 and C19 were 7,828/7,800; C08 was 7,721/7,700. That draft was
replaced by the shorter integration into the existing loading sentence. No
ceiling, validator, or design instruction was weakened to obtain a pass.

## Targeted behavioral scope

All seven original missing-Core slots completed once: J-0BB84E9A8A38,
J-331437B313D7, J-4CDEA7F7DAB0, J-ADA76AC2FF52, J-B63C26458B7B,
J-ED71159D5707, and J-923C67582F57. They represent five distinct original prompt
hashes, not seven independent tasks.

The original slot-1 task contexts and prefixes were unchanged. Isolated clones
used the clarified Skill with the same `gpt-5.6-terra` high-effort settings and
pinned CLI. Declared differences were clone workspace/schema/image paths,
TEMP/TMP and separate output locations. Seven calls completed with exit zero;
no retries, repairs, renders, Gold scoring or operational unseals occurred.

**All seven loading reviews passed.** Every trace contains a successful full
Core read and one to three actual reads of directly linked Design experts.
No invented Core path or failed package read recurred. The observer's three
automatic passes and four automatic flags remain unchanged: private path/body
inspection found that those four flags name valid UI references in combined
Design/UI commands, not nonexistent Design files. The final loading verdicts
are therefore reviewed trace results, not seven automatic-observer passes.

The final preservation check verified 302 original files, seven initial clone
inventories and seven capture/usage chains. The retained original entrypoint
and final candidate hashes match those above. No provider process remains.

Local evidence root:
`Z:/Projekts/AI/scoville-design-eval-local/development-regressions/adr0054-core-loading-v1`.

- `input-manifest.json`:
  `640BE797B653A10BA0275FE5014DCD42CF1C2C9E27F8AB5CC2864E03B5E2BFA5`.
- `final-loading-report.json`:
  `0C8B56CA1DDDF7253503920124DF772B92AC10BF47E726E7B2F4AE12B0CC5558`.
- `final-preservation-receipt.json`:
  `1FBF9A61C9028DDD7F2DB80F4899FB90AF2B9881408779177AE1EDF7CD4EC7A7`.
- `ui-namespace-evidence.json`:
  `F7CB82299CD33F37442201B912F9805FED3CE7F124114102243B0ED801057DF5`.
  This binds all seven valid UI-reference reads across the four flagged cases
  to successful command events and complete staged file contents.

Four focused observer tests passed before execution. Observed usage across the
seven calls was 647,245 input tokens, including 476,928 cached input, with
36,410 output and 9,921 reported reasoning output. These categories are not
summed as disjoint charges.

This is targeted development evidence on previously exposed failures, not a
new full holdout, a causal guarantee, or proof that unrelated design issues
were fixed. Original failed traces and scores remain retained.

No publication, installation, commit, push, tag, or release is authorized.
