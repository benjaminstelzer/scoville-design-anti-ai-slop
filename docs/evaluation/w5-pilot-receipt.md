# W-005 four-pair pilot receipt

Date: 2026-09-02  
Candidate: Design `671B6BAC24569360D23AC0300BEFEC0B478FE035EC9EF79B19E144239369AEF8`  
Model: `gpt-5.6-sol`, `xhigh`  
Codex CLI: `0.147.0-alpha.1.2` through SkillOpt Studio  
Network: disabled

## Fixtures and freeze

Four original local same-content pairs were rendered at 1,200 × 760:

- functional button-contrast mutation:
  `8AF16153994EE18017067AEC03636600B7EB6B32BF89A63A3E28DE0B1F183E3A`;
- craft alignment/grouping mutation:
  `4C8712E285350E392E4FE6BC72BF70EA7267BA0688E67E32E5B3014A1B513276`;
- deliberate off-grid exception:
  `2DE69C3DE5F18960B4E1549429603CDD59603019309D711A1494566935C17BF3`;
- true editorial-versus-modernist tradeoff:
  `AAC702F96077035ED865607942D3DAD71B8E9EAF746CEDFF726AB0FC1667F8B9`.

Assets and binary benchmark payloads remain under the local-only evaluation
workspace. The adjudicated report-schema benchmark v2 lock is
`BD287228C7DC8ED82998F8856D5931E0D6C4EC8A587C9D2DDC508C457BD9A10C`.
Benchmark v1 remains unchanged after exposing ambiguous enum semantics and
over-specified route Gold.

## Result

SOL produced the intended semantic decision on all four pairs:

- functional: B; functional contrast defect;
- craft: B; accidental craft defect;
- deliberate exception: B; exception valid, no protected regression;
- tradeoff: no decisive winner.

The v2 exact report schema also passed 4/4. Selective-loading Hard passed only
2/4: Craft and Exception passed; Functional used Core only in v2 after having
loaded Colour plus UI in v1; Tradeoff alternated between Brief and Typography
while preserving the correct no-winner result. This is routing instability,
not visual-semantic failure, and remains visible for the holdout.

Raw split results:

- `design-w5-pilot-v2-train-r1`: 1/2 Hard;
- `design-w5-pilot-v2-val-r1`: 1/1 Hard;
- `design-w5-pilot-v2-test-r1`: 0/1 Hard, semantic contract passed and only
  exact expert-set gates failed.

## Frozen holdout execution settings

- One execution for deterministic routing, ownership, source, accessibility,
  and production cases.
- Three executions per arm for generative, repair, style, exception, and visual
  discrimination cases; identical repeat count for every applicable arm.
- Target timeout 300 seconds for audit/routing and 900 seconds for editable
  artifact generation; network disabled; workspace writes allowed only inside
  the per-case isolated output directory.
- Use the Studio-local Codex CLI `0.147.0-alpha.1.2`, not a different globally
  installed CLI.
- Render every artifact at intended context plus one diagnostic alternate.
- No model/VLM aesthetic score. Deterministic and source/function gates may be
  aggregated before human review.

The blind review packet contains the brief, required content, intended-size and
diagnostic renders, randomized arm and repeat labels, protected dimensions,
and a blank per-dimension rubric. Arm keys remain separately encrypted. A
three-reviewer directional claim requires the frozen two-thirds and one-third
margin; until such a panel exists, the report may state no cross-person visual
preference result.

