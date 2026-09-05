# Design v1.0.0 release validation

Checked on 2026-09-04 against the source and installable directory included in
this release. These are structural and packaging checks, not a new visual
benchmark or a guarantee of host selection.

## Current checks

- 32 unit tests passed with `python -m unittest discover -s scripts`.
- Source and runtime package validation passed for 30 successor-v2 modules.
- The generated index is current. The interpreted route contract passed 60
  cases across 44 signals. These fixtures do not exercise host discovery.
- The Design/UI boundary check passed against the UI v1.1.0 candidate.
- Canonical Agent Skill validation passed for both installable packages.
- Native Plan structural validation passed with no errors or warnings.
- The 34-file runtime was checked byte-for-byte against both local Design
  installations and the final reviewed runtime. No instruction changed for
  publication.

Fifteen module-size notices exceed advisory targets, not binding acceptance
limits. The authoring Core plus index measures 3,086 `o200k_base` tokens. The
runtime version measures 3,072 after removing the generator comment. File token
counts are not provider-total cost or a context limit.

The initial whole-repository whitespace scan reports existing Markdown hard
breaks and extra terminal blank lines in historical records and modules. Those
bytes were retained rather than changing frozen evidence or the reviewed
runtime to satisfy a formatting check. The frozen receipt with CRLF endings
is explicitly exempt from Git line-ending conversion.

## Package identity

- Source manifest: `7049686B1672BF04EAFF12A69F8A713770E26218730193F961DB64DB1CA15B9D`.
- Runtime manifest: `B8874386F46DA1319FA75502887152D247318BEE1B50D4F64C9E5D84B9986F9C`.
- Manifest algorithm: SHA-256 of sorted UTF-8 rows containing relative path,
  NUL, byte count, NUL, uppercase file SHA-256 and LF.

The root `SKILL.md`, `modules.yaml`, `agents/` and `references/` are the
authoring source. The nested `scoville-design-anti-ai-slop/` directory is a
generated installation derivative. Do not edit it independently.

To reproduce it, run `scripts/build_runtime_package.py` with a new destination
outside the repository and a new receipt path outside that destination. The
builder validates the source, removes exactly one generator-comment line plus
LF from `SKILL.md`, preserves every other byte and validates the derivative.
Copy the verified derivative into the nested distribution directory only after
checking its complete inventory and manifest. Never install development
records, test cases or benchmark tools with the Skill.

## Evidence limits

Historical evaluation records retain their original candidate hashes, failures
and scope. Focused successor cases and subsequent instruction clarifications
are separate stages, not one unchanged benchmark result. A complete holdout
was not repeated for the shipped successor. Genuine host activation checks and
the original proposal-session package/evidence review remain unverified under
PLAN-0006 W-004. The separate package-only review does not substitute for them.

Publication was explicitly authorised separately from that unfinished work.
No general visual-superiority, professional-competence or cost-saving claim is
made. External raw traces and sealed custody material are not runtime inputs
or release assets. Repository evidence paths may describe local historical
runs that another machine cannot replay without their original harness.
