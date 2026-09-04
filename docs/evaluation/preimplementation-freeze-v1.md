# Pre-implementation freeze v1

Frozen: 2026-09-01  
Status: frozen for W-008 baseline and W-002 implementation  
Hash algorithm: SHA-256 over exact UTF-8 file bytes

## Product and model scope

Priority order:

1. generate professional task-specific design;
2. discriminate effective, mediocre, defective, generic, and clichéd work;
3. repair localized causes and reassess a render;
4. execute recognizable professional style without template slop;
5. load theory/history only when it improves the first four.

Behavior target and qualification model: `gpt-5.6-sol` with `xhigh` reasoning.  
SkillOpt optimizer model: `gpt-5.6-sol` with `xhigh` reasoning.  
Host: local Codex desktop task on the recorded Windows workspace.  
SkillOpt network state: disabled.  
Token metric: `o200k_base`.  
Fable 5.1: Plan-review evidence only.  
Opus 5: untested.

Any model, effort, system-instruction, host, tool, or material renderer change
creates a different evidence scope and requires a new freeze or explicit
comparison record.

## Canonical modes and maximum module map

Modes: `generate`, `critique`, `repair`, `style-direction`.

Stable maximum IDs:

1. `brief-and-concept`
2. `composition-and-layout`
3. `typography-and-writing-systems`
4. `colour-and-reproduction`
5. `imagery-and-art-direction`
6. `information-and-data`
7. `brand-and-visual-systems`
8. `ui-and-interaction-design`
9. `motion-and-sequence`
10. `media-production-and-handoff`
11. `critique-and-validation`
12. `culture-ethics-and-provenance`
13. `sources-and-attribution`
14. `style-direction`

W-008 may assign only `admitted`, `retained-floor`, `stub`, or `withheld` to
these IDs. It may not add, remove, or rename one. Version-one expert `requires`
and `conflicts` remain empty. An enumerated signal catalogue owns routing
signals. Expert-to-expert reads are prohibited.

## Context ceilings

- Core including generated direct index: 1,500 tokens maximum;
- generated direct index sub-budget: 450 tokens maximum;
- ordinary expert leaf: 1,800 tokens maximum;
- ordinary Core plus one expert: 3,800 tokens maximum;
- ordinary Core plus up to three experts: 7,000 tokens maximum;
- more than three material experts require named sequential phases and carry
  forward only the compact Design Dossier.

The validator measures every required and conditional route phase. No required
expert may be omitted to meet a budget. A smaller selected payload is not a
claim of lower total latency, money, or token use.

## Knowledge admission

- `focus`, `correction`, and `teaching` are SOL behavioral-delta payloads and
  require the W-008 evidence contract;
- sourced constraints, functional floors, provenance duties, and
  `external-verification` use `retained-floor` and cannot be optimized away;
- unsupported specialist areas remain bounded `stub` or `withheld`;
- knowledge recall or historical explanation is not an applied outcome;
- self-critique and VLM aesthetic scoring are not independent visual proof.

## Evaluation gates

- original-pair mutation classes include `generic-cliché`;
- W-008 internal visual admission may use one qualified reviewer with rationale
  and produces no public cross-person claim;
- W-005 cross-person claims require at least three independent qualified
  reviewers and the frozen margin/disagreement protocol;
- a priority holdout lane below five sealed cases is smoke-only;
- domain qualification additionally requires sufficient open Validation;
- external permitted pairs may enter local SkillOpt Train only and never
  `valid_unseen`, sealed holdout, or qualification comparators;
- Taste Skill is a required commit-pinned comparator only inside its declared
  landing-page, portfolio, and redesign scope.

## Artifact and composition boundaries

The artifact-class source/render table and maximum two-pass repair loop in the
modular architecture are frozen. When the format owner or renderer is missing,
the Skill returns the best authorized source artifact and marks visual quality
unverified. Source inspection cannot substitute for a render.

Design/UI composition uses `scoville.design-direction/v1` with ADR-0006 fields.
Neither Skill searches for or requires the other. UI consumes the record only
when it is present and retains its standalone Greenfield fallback.

## Holdout custody

Combined sealed cases: 30 across two independent AES-256-GCM tranches.

- tranche-one archive:
  `3884433d5c10fab8763730c7f001501438620dc6a61d9f6cb4c53e67b9796bb7`
- tranche-one opaque manifest:
  `4834ff6970a59d6826f951b24795a77409bae0d80187333d3bd10565d85b4fcf`
- tranche-two archive:
  `5eb1e116329125d6f880c71e7de72c4e44c11ccc46b406f03e258ea0f62485f3`
- tranche-two opaque manifest:
  `5c54b6542206dcccf58ac29e6145ac35cfa98069e90fd060036e81b210850531`

The Skill writer has not inspected archive or manifest content. Decryption keys
remain only in the custodian's private continuation context.

## Frozen repository artifacts

```text
0f5a73b08e6cf893f8454ce4b2f5a3565ecf4d97ee7681ca266f1e2e836b6844  docs/audits/0001-design-skill-audit.md
020312f72a928f7e08c37b8bf77d2e4f323baac902689b87e887e7f33465932c  docs/decisions/0003-use-original-license-screened-source-synthesis.md
a7ae60ced02c4c15234e1a1151d9d4181a1eae92f64edbf187c75ddc4515da5a  docs/decisions/0005-build-staged-broad-and-deep-design-capability.md
54a313b92054c17b7ef6274f18c0ce42837167b3648e00194f5f200c9c1d4660  docs/decisions/0006-refine-design-ui-composition-contract.md
8adc76e2612a1d29f8cecf33d3eab20bee7e694105ece031c9e2450a99204b28  docs/decisions/0007-refine-rule-and-exception-epistemics.md
13cf1457dccccc202a10caec6705cb7cbd389aaee13fea43468d6ab3772d5105  docs/decisions/0008-freeze-progressive-route-and-context-contract.md
aa267e43b9cd0cd30c9bc581b2e15e156a2235ec246342bba99eca988691fc65  docs/decisions/0009-freeze-independent-qualification-before-implementation.md
fdf6a37ec7e6a686dc75b199434add52f3906de777d50525849cd8285a669155  docs/decisions/0010-use-permitted-external-pairs-in-local-skillopt-training.md
ec3de5f09039532f1d8fbfdfce73be77583dbdea50a58c1548cee978bc421497  docs/decisions/0011-prioritize-applied-design-and-measure-only-sol.md
f08ff7d6c2606210d5c5723aa37a6029c6a571b28cefaad820839def9ca9339c  docs/decisions/0012-use-flat-expert-modules-and-a-generated-direct-router.md
ebf20402404199d0cec4725cc5d348b68fd6a0ac8f934fba44fb86c19dd2e09f  docs/evaluation/preimplementation-contract.md
0219eaf0a35bd0fd6e59e59d1a31fcc46452e488263debd058d86c626573168e  docs/evaluation/holdout-custody-receipt.md
777ac4c7a63914054e3095d40d8af6fa5f8d8901704909541e901d043ff46f4e  docs/research/source-ledger.md
9fab2c1820c549583fef5a45641616c6e230a6fa3dc27578a2a43ef4a43b00f8  docs/research/domain-maturity.md
07d2323ee7aea5918030ad0f31661120c169bfb2b1f182de7e3cb019f60ce98c  docs/research/comparative-reference-material.md
939276eb9c8dd1a0f5e71edbdf6cb21c45947cb1ef3ad36aadc1e0fb34aa99f4  docs/research/modular-application-architecture.md
f9e3b51d00b5a3107f1023bcd20fdae9a6bc628d757a5e297e1dc7b66cfabfe8  docs/research/style-direction-system.md
54c097ea0cb2ffae38abb7f6684a05e8b54412527d6096d735678efb46035eb9  docs/research/imagery-art-direction.md
343ca63848db3d968f328eae066f484b060b825f50a75a71a30a94cf579caf7b  docs/research/skillopt-live-state.md
```

## Change rule

A changed hash invalidates freeze v1 for affected downstream evidence. Accepted
Decision history is never rewritten; material changes require a successor
Decision and `preimplementation-freeze-v2.md`. The active Plan is intentionally
outside this hash set because lifecycle transitions remain mutable.
