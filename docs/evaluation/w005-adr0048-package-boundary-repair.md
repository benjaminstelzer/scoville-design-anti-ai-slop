# W-005 ADR-0048 package-boundary repair

Date: 2026-09-03  
Status: deterministic gates and one public post-fix call passed

## Reproduced defect

The one authorized source-cleared ADR-0047 Terra High call expected only
`diagrams-and-relational-information`. It authenticated and reported three reads:
Diagrams, Composition and Media Production. Composition was explicitly forbidden;
Media Production was also outside the exact Gold route. All non-route checks
passed.

- result:
  `96B6829FBE189560C4CCD23A66AD0CCE0F5457C6CAD1B4B535720DDB596BB1FF`
- validation:
  `7C594C8F457EFAE8A6D8387DC39CC85C17BB5516E6B1449FFB72844BB48B9457`
- raw events:
  `9D3D51DCE6B9B7E38581D411C78E118B1B83152B69A442BFF342BC7EE4AF2D2C`
- artifact:
  `1145AB10CB8BE99D611890C9847CE149056730EDE0D7C15164FB8BD4853CCA31`
- authorization:
  `487D4751302BF72582FC5DD9AA7956D5ACB666CCD0E95FDCFF4E855BA59C75E3`

The call used 144668 input tokens, 116736 cached input tokens, 3865 output
tokens and 1843 reasoning-output tokens. It made one provider call, zero retries,
zero sealed calls and zero renders.

## Minimal repair

ADR-0048 narrows two general routing boundaries without special-casing SVG or
the fixture:

- specialist-owned fixed geometry or labels do not add Composition when the
  general visual system is fixed;
- merely writing or syntax-checking the requested editable artifact does not add
  Media Production; that owner requires open production source/derivative,
  export, format/preflight, provider or handoff work.

RF50 captures the reusable fixed-specialist-diagram boundary. It expects
Diagrams and forbids Composition, Typography, Instructional and Media Production.

## Deterministic evidence

- package unit tests: 17 of 17 passed;
- route contract: 50 of 50 passed;
- package validator: valid with 28 modules and 12 advisory expert token-target
  warnings;
- Core tokens: 1465;
- generated index tokens: 1189;
- largest expert: 2340;
- Core plus index: 2654;
- Core plus largest phase: 11677;
- generated module index: current;
- Design/UI boundary: valid;
- Skill Creator validation: valid;
- whitespace validation: passed.

## Frozen package

- executable package manifest file:
  `F6A076D5C2272F4FAD23FB6C236523287D19E0C7EACF8484D5AD7993E0EAAD6F`
- inner manifest:
  `97A136E9F2CA012E10D4B6ADEECF7E5E45B47FC9F92B4F6F1B99A904CDE9283F`
- `SKILL.md`:
  `76CD2F7F86B0FF5494F090EA1C1911EED158D4AB5B7109F7BDD121D95B71B206`
- `modules.yaml`:
  `DABD01330E06290DB66DA22F0CC30B6DA8AD34CF01ED1104779F50F6A252F9A4`
- route fixtures:
  `F304500901834E2D56298A6F813258DE2D578FAB5EB2B8D48D7502B405E79396`

Deterministic evidence proves the package representation and frozen route
contract. The separately authorized source-cleared post-fix call subsequently
read exactly `diagrams-and-relational-information`, read zero forbidden experts,
aligned its terminal report, and passed every non-route check. Result SHA-256:
`050A8A24AD42494D225712B9927FB9940181BF37A41ADAA8387F37716AE3EC6E`.
The bounded qualification and its complete-holdout limitation are recorded in
`w024-targeted-qualification-ledger.md`. Publication, installation, commit,
push, tag and release remain prohibited.
