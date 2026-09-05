# W-006 local release-candidate record

Date: 2026-09-03  
Status: local release candidate ready; unpublished and uninstalled

## Scoped candidates

### Scoville Design

- repository: `Z:\Projekts\AI\scoville-design-anti-ai-slop`;
- executable-manifest file SHA-256:
  `F6A076D5C2272F4FAD23FB6C236523287D19E0C7EACF8484D5AD7993E0EAAD6F`;
- inner executable-manifest SHA-256:
  `97A136E9F2CA012E10D4B6ADEECF7E5E45B47FC9F92B4F6F1B99A904CDE9283F`;
- `SKILL.md` SHA-256:
  `76CD2F7F86B0FF5494F090EA1C1911EED158D4AB5B7109F7BDD121D95B71B206`;
- `modules.yaml` SHA-256:
  `DABD01330E06290DB66DA22F0CC30B6DA8AD34CF01ED1104779F50F6A252F9A4`;
- `README.md` SHA-256:
  `BB317EA3BEDBE165DA7A3B7FCEA12F1E5BB61BA58F112607EB07EC533C1E6F26`;
- `CHANGELOG.md` SHA-256:
  `C31D92BBCD8530745F0222F6810191D18E4500554F0CC9C8EBE5D605FF129FF9`.

### Scoville UI composition candidate

- repository: `Z:\Projekts\AI\scoville-ui-anti-ai-slop`;
- five-file executable manifest SHA-256:
  `FD255A274E2D92C6DDA14CAD2A85FF0E7702960CEE6B2D3B9F20E04A78A78875`;
- `SKILL.md` SHA-256:
  `93763156A7CEC205AEE5C5068C53B1E3708EB21A35ABFBD4ED957D381D0E4674`;
- `README.md` SHA-256:
  `32155AE14FA703D5DCB646895E2EC0788980095D240164852960918C4748B611`;
- `CHANGELOG.md` SHA-256:
  `2FC3B856130E80F352DB4A93F46F7536C0BFC0A05AD3411121D6A2CEDE926C77`.

## Documentation and claim reconciliation

The Design README retains the canonical Scoville order: problem-first opening,
name, use, install, enforcement, mechanism, family, status, sources, and
licence. Its additional Design/UI section records the product-specific
ownership boundary. Both candidate READMEs list the eight current family
members and keep every sibling optional and independently usable.

Design package measurements now match the validator: Core 1465, generated
index 1189, largest expert 2340, and Core plus largest planned phase 11677.
README and changelog claims are limited to the targeted qualification in
`w024-targeted-qualification-ledger.md`: exact Terra High, local Windows host,
pinned CLI, frozen package, one source-cleared diagram-boundary replay, exact
authenticated route, zero forbidden reads, deterministic scorer, one model
response, and no render or visual panel. Qualification-v7 incompleteness and
the complete-holdout opt-out remain explicit. Historical SOL observations are
context only; Fable 5.1 is Plan review only; Opus 5 is untested.

The UI README and changelog identify their exact executable manifest and retain
only configuration-specific composition and adjudicated regression evidence.
They do not reuse historical 30/30 UI evidence or Design's targeted replay as a
complete UI qualification.

The cited SOL evidence used exact `gpt-5.6-sol` at `xhigh` on the local Codex
desktop host, with network disabled, an isolated Codex home, and SkillOpt commit
`ba820b500f9da96685cf2780c7dc85ed4eb6563e`. W-004 began from Design
`DEA073D4FB341BFEBCA0E1A14CAC78A758F3E07ECDED226CEF54A7BD9AF808D1`
and UI `5E4005BCC9EBC4476E3B2AB14CD4A4D5CEA7837A15EA17A3C39563E9E3575C48`,
retained the evaluated Design
`671B6BAC24569360D23AC0300BEFEC0B478FE035EC9EF79B19E144239369AEF8`
and UI `217F298D4B98808012FE41C024D5B92B01B6F06929245DCC3C8206CE288F462C`,
and later recorded independently adjudicated Gold defects rather than editing
the original results. The repaired v2 regressions were Design Validation 8/8,
Design consumed Test 3/4 raw with the remaining annual-report Gold defect, UI
Validation 3/3, and UI consumed Test 4/4. Those historical hashes and results do
not qualify the later 28-expert Design package. Current Design behavior is
claimed only from the exact Terra configuration and hashes in the targeted
ledger; the current UI package identity is the five-file manifest above.

## Source and link health

Public attribution remains in the distributable `references/source-index.md`;
the detailed licence/reuse/currentness record remains in
`docs/research/source-ledger.md`; 84 operational clusters remain bound in
`docs/research/rule-source-map.md`. Package validation resolved every runtime
source ID.

A redirected HTTP HEAD check covered 277 unique external URLs across the Design
README, source index, source ledger, and rule-source map. Results were 218
`200`, four `202`, 49 server-side `403`, and two rate-limited `429` responses.
One HEAD-incompatible UNESCO URL passed a direct GET. Two DOI links that a
simple Markdown URL extractor truncated at parentheses both passed direct
full-URL checks. The stale Design Atelier and OpenAI frontend-skill paths now
point to immutable historical commits; Refero points to its current Skill path;
Design With FontForge points to its reachable source repository; and the stale
SEGD resources index now points to the current organisation root.

The sole confirmed `404` is the future Design GitHub repository URL. The README
labels installation as available only after publication. Creating that remote
repository is outside this local candidate and remains unauthorized. All tested
local README, changelog, Skill, evidence, and licence links resolve.

## Validation

Design:

- package unit tests: 17/17 passed in the pinned SkillOpt Python environment;
- package validator: valid, 28 modules, 12 advisory token-target warnings;
- route contract: 50/50 passed;
- generated module index: current;
- Design/UI boundary: valid (`active_design=strict_ui`,
  `ui_only=greenfield_fallback`);
- Skill Creator validation: passed;
- native Plan profile: passed with zero errors and zero warnings;
- `git diff --check`: exit 0.

UI:

- current five-file manifest recomputation: exact match;
- Skill Creator validation: passed;
- static composition fixtures: schema v2, 11 cases;
- Design/UI boundary: passed from the Design validator;
- local documentation links: passed;
- `git diff --check`: exit 0;
- `.gitattributes` now fixes JSON to LF as well as Markdown and YAML.

The Design repository is a new all-untracked local worktree, so its zero-exit
`git diff --check` cannot inspect untracked content. Package, route, index,
Skill Creator, native Plan, Markdown-link, and whitespace-specific validators
supply the substantive checks until a separately authorized first commit.

No publication, installation, commit, push, tag, or release was performed.
