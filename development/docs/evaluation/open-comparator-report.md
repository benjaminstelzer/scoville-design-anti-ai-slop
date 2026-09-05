# W-005 open public-comparator report

Date: 2026-09-02  
Target: `gpt-5.6-sol`, `xhigh`; Codex CLI `0.147.0-alpha.1.2`; network disabled

## Arms and scope

Three identical original briefs were run through:

- neutral no-method control:
  `95D2B635C6AE467C4DA363F0067F0DAA757E8F9D9FD7CCA1066321BEB525872F`;
- pre-W-004 Design on the 80s landing only:
  `DEA073D4FB341BFEBCA0E1A14CAC78A758F3E07ECDED226CEF54A7BD9AF808D1`;
- W4 Design candidate:
  `671B6BAC24569360D23AC0300BEFEC0B478FE035EC9EF79B19E144239369AEF8`;
- default Taste Skill v2:
  `2E064E92ACA020B2E0BAD69326FE7EA55D59005ED53D1A8CBCE1BD135D44B8B3`,
  repository commit `ccbc15639c97057cbfcf32ecebc38ef716e4bb37`.

Taste is MIT-licensed and publicly declares its default v2 scope as landing
pages, portfolios, and redesigns. It was not applied to print, packaging,
product UI, dashboards, or other out-of-scope domains. Sources:
`https://github.com/Leonxlnx/taste-skill` and `https://www.tasteskill.dev/`.

Frozen benchmark locks:

- Design-family arms:
  `910B92A4A6F723E57C6C394B1519FF4FD51001C4FCF106DC032A311DA9BDB0B7`.
- Taste arm:
  `57FADD308CA893394DE77F2D105523FA40A7BBAC3EFD95251CDDBDA0BDE79B02`.

## Cases

1. professional 80s-neon retro-computing festival landing page without a
   signifier pile;
2. contemporary-neoclassical architectural-photography portfolio without
   literal classical or luxury clichés;
3. existing museum marketing-page redesign preserving every supplied string
   and improving exhibition/visit workflow.

The Design-family and Taste benchmarks differ only in the observable Skill
path. Task and output-contract bytes are otherwise identical. Every arm used
the same model, reasoning, CLI, network state, timeout, output ceiling, and
renderer.

## Deterministic result

All ten generated HTML artifacts passed:

- output-contract and required-content Gold;
- agent/behavior/efficiency Hard;
- HTML parse and root-element inspection;
- local full-page render at 1,440 px;
- `lang`, viewport meta, one `main`, and one `h1` presence;
- no external script, stylesheet, or image reference.

Desktop horizontal overflow was zero for all ten. Mobile diagnostic rendering
at 390 px found two concrete defects:

- W4 Design candidate museum redesign: 416 px scroll width, 26 px overflow;
- Taste 80s landing: 518 px scroll width, 128 px overflow.

The other eight had no measured horizontal overflow. Scroll-triggered content
was exercised before final capture; reduced-motion top renders and mobile top
renders were also recorded.

## Context and execution cost

| Arm | Loaded Skill tokens per case | Provider total-token range |
| --- | ---: | ---: |
| Neutral | 64 | 33,353-48,468 |
| Pre-W-004 Design, landing only | 2,712 | 81,559 |
| W4 Design candidate | 2,739-2,744 | 82,618-102,946 |
| Taste v2 | 21,912 | 43,543-72,584 |

The W4 Design candidate used roughly one eighth of Taste's loaded Skill text
through selective experts. It nevertheless consumed more provider-total tokens
in these runs because its routed references required multiple agent turns.
This evidence supports a smaller active knowledge payload, not a blanket claim
of lower billed or total inference cost.

## Human-review boundary

A local arm-blind packet contains randomized desktop and mobile renders for
all three cases. Packet manifest SHA-256:
`24D0C81EC02DCCD75BCEBE9CEDC921132E443A315071064CDBD76421DBC49F56`.
The separate private mapping hash is
`654F5FCEA021643CE1E5B1E4424EB06CFFDAE9E7F45BACEABD44A256DF216B25`.

No three-reviewer panel has scored the packet. Therefore this report makes no
directional claim that Design, Taste, the pre-W-004 Skill, or the neutral arm
looks better. Attractive examples and the maintainer's unblinded diagnostic
inspection are not product-level preference evidence.
