# W-005 qualification-v5 provenance adjudication

Date: 2026-09-03  
Status: qualification-v5 closed as failed historical evidence  
Package change: none

## Frozen package inputs

- Design manifest: `3D19CE209E52AFCE91B888D6FB489E29EA9846A1442896129563D4B94ADC01C2`
- UI manifest: `FD255A274E2D92C6DDA14CAD2A85FF0E7702960CEE6B2D3B9F20E04A78A78875`

## Sealed outcome

The fresh-custody v5 generation registered 150 jobs in 75 arm-balanced shards.
Canary shards 1 through 4 passed, producing eight terminal passing jobs. Canary
5 stopped after its candidate's first terminal response, so its pristine
baseline, Canary 6 and the non-canary schedule were not started.

The candidate passed eight of nine private checks. Its applicable Design expert
was read, but the terminal `selected_experts` list was empty; only
`route / selected_expert_provenance` failed. The response was not retried or
edited. The adjudication classified the owning cause as indeterminate rather
than a demonstrated package, Gold, parser, scorer or runner defect.

- Fail-stop result: `0768CE0F1C1D18D975453A38CB144ACC574B1FC0C843A346D0D182C69EB88751`
- Sealing receipt: `6A256B7803522EBB32D6B79B9A8DADDFF53DC3885E67099BB7A4A8FDB018EECA`
- Fail-stop validation: `397656F0D9BC81A9C70045D6EE7D8D036718E574975C18DEEDE6BE016393E3B2`
- Adjudication receipt: `52C16926EA28E918AC8232E30B0A6BEBA55AFD0106984CD31C56AEAB3797C623`
- Adjudication validation: `439DFFE666E991A740CEB930A1BFB982BBD869626E65AB780E26D4796662F1DD`

## Public regression

ADR-0035 authorized one public, source-cleared Terra High regression under the
same composed candidate contract. The fixture was the already qualified C06
case at SHA-256
`FC026615496E9E1628C5870D53D2699FD93AFB39EE248565CBF4BB4077A31D7B`.
Preflight was zero-call and bound the frozen packages, prompt, schema, pinned
CLI and sandbox.

The single terminal call authenticated reads of
`brief-framing-and-criteria.md` and
`concept-development-and-selection.md`. The terminal response reported the
same two experts. The private omission therefore did not reproduce. This
result neither changes Canary 5 nor proves the omission impossible.

- Public provider calls: 1
- Public model responses: 1
- Sealed calls during regression: 0
- Raw events: `5F3254DFBB1148ADA193ACB78773D252971B955F35486ED222419ABF21EFDA15`
- Artifact: `15F77DDAFE36FD067910DDC95C2F192091DBA12EF2207B8E27EFD1B73C6B57E2`
- Run status: `5BDE37E41C9388232EFB7660E83086122D2657D3A3E1B05A73B348964F41487B`
- Result receipt: `879174C30184C201858194FCDDE00177C82C3F2B9B8CBD57D091F26BB56D5993`
- Final-state tests: 6 of 6 passed

## Decision and claim boundary

ADR-0036 closes v5 without retry, continuation or retrospective rescoring.
Qualification-v6 will score the expert files authenticated as actually read
and report terminal `selected_experts` alignment as a separate diagnostic. It
must use fresh sealed content and frozen controls; no v5 response receives v6
credit.

Observed v5 evidence is limited to four passed canary shards, eight passing
terminal jobs and one failed terminal candidate job. It does not qualify the
Skill, the remaining holdout or any cross-person visual preference claim.
