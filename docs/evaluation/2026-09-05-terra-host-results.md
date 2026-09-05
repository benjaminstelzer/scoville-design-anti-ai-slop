# Terra medium native host observations

Five single-run Codex desktop cases executed on 2026-09-05 under
PLAN-0006/W-004. Benjamin selected GPT 5.6 Terra Medium for the new tests.
This is a separate host observation set, not an edit or rerun of the frozen
Claude protocol or the original model-matched visual comparisons.

Inputs and actual tool/output receipts are under
`evaluation/plan-0006/terra-host-2026-09-05/`. The coordinating audit froze
the complete protocol before execution, SHA-256
`81e66cae7442e9629217696c8c2f4a10ba9d62d6f305774201d6441faba81e64`.
The host reports `gpt-5.6-terra`, effort `medium`, for all five executors.

| Case | Actual observation | Qualification limit |
| --- | --- | --- |
| DH1, open poster concept | Automatically reads installed Design Core and seven domain modules, then supplies a concrete chat-only art direction. | No rendered artifact requested or observed. A truncated grouped read is followed by further module reads. |
| DH2, backend-only review | No Design Skill read. Answers the backend question. | One negative activation observation. |
| DH3, grammar correction | No Design Skill read. Corrects grammar only. | One negative activation observation. |
| DH4, settled padding change | No Design Skill read. Changes only the supplied CSS value in chat. | No runtime or rendered UI proof. |
| DH5, hierarchy critique | Reads Design Core and returns a proportional read-only hierarchy critique. | Reads Core before the task file, then omits the materially applicable Composition module. Not a complete workflow pass. |

The installed package contains 34 files. Relative to the current 35-file
candidate, it lacks LICENSE and modules.yaml lacks only the new
`distribution_files: [LICENSE]` packaging declaration. All other common files
are byte-identical at freeze and verification. In particular, the actual Core
and read module texts match the candidate. This is not a whole-package
identity claim or permission to update an installation.

The positive hierarchy case demonstrates why correct activation must be
separated from full module routing. Core already requires selection of every
materially applicable module, and its direct index explicitly maps hierarchy
to Composition. The observed answer's plausibility does not prove that read.
Retain the output unchanged and investigate the narrow enforcement failure
before choosing a correction or a fresh affected follow-up case.

Original Claude activation failures remain historical observations. The
original proposal-session Fable final review remains unobserved. No new
installation, publication, render qualification, superiority claim or completed
W-004 follows from this host set. Sessions and tool receipts exclude hidden
reasoning and host prompts when exported to the local evaluation record.
