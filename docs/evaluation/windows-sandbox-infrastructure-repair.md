# Windows sandbox infrastructure repair

Date: 2026-09-02  
Scope: non-holdout capability diagnosis for local qualification

## Defect

The first clean-snapshot RC7 batch completed 150 CLI processes with exit code
zero but produced no surviving artifacts or renders. Candidate-level status was
125 blocked, 17 partial, and 8 completed. Because artifact-required rows could
not satisfy their contract, the entire batch is infrastructure-invalid and
contributes zero product evidence.

The custodian encrypted and integrity-checked the quarantine, removed plaintext
runs and staging, and did not produce a blind review packet. The local defect
receipt SHA-256 is
`0DC18EEAF222604C225B09313D010AE2F8FA6B183EA2AECD90A4DB7F7B6EFB04`.
The encrypted quarantine archive SHA-256 is
`38B53BAA677C27C567E71A8E17242C6CD9A28F9EA4A22610AB0394039FF2A294`.

## Root cause

On this Windows host, `workspace-write` without an explicit native Windows
sandbox implementation fell back to read-only behavior. Patch streaming and
ordinary writes were rejected even though the process itself exited zero.

The current Codex manual states that native Windows offers `elevated` and
`unelevated` sandbox implementations. `unelevated` is the documented fallback
with a restricted token, ACL filesystem boundaries, and environment-level
offline controls. See the official
[Windows sandbox documentation](https://learn.chatgpt.com/docs/windows/windows-sandbox)
and [sandbox overview](https://learn.chatgpt.com/docs/sandboxing).

## Non-holdout probes

All probes used empty synthetic workspaces and no holdout content.

1. CLI `0.151.0-alpha.7.2` with implicit Windows configuration reproduced the
   read-only write rejection.
2. CLI `0.151.0-alpha.7.2` with
   `windows.sandbox="unelevated"` created and byte-verified
   `WORKSPACE_WRITE_OK\n`.
3. The preregistered CLI `0.147.0-alpha.1.2` with the same explicit setting
   created and byte-verified the identical file.
4. CLI `0.147.0-alpha.1.2` then created `LOCAL_WRITE_OK\n` and attempted one
   HEAD request to `https://example.com`. The request failed with exit code 1
   because the offline proxy at `127.0.0.1` rejected the connection.

The effective repaired invocation keeps:

- `sandbox=workspace-write`
- `windows.sandbox="unelevated"`
- `sandbox_workspace_write.network_access=false`
- `approval_policy="never"`
- the same pinned CLI, model, reasoning, package manifests, prompts, budgets,
  and repeat policy

It does not use `danger-full-access`.

## Rejected qualification-v2 paths

Explicit `unelevated` sandboxing repaired source writes but could not launch
Playwright's child processes inside the nested CLI. The first synthetic smoke
therefore produced no browser render. Its receipt SHA-256 is
`9FF0B92EA21D1E4F1616646C17C665C888FB77AE8466923F63565F233DE5CB35`.

A second smoke verified source writing and outbound-request denial but again
produced no accepted render. Two fallback PNGs were not treated as evidence.
Its receipt SHA-256 is
`0BD7B7FEB3611C513D7A5AD5C1A19BC11349F91D1EF34795A0BBA5B5276255C0`.

An `elevated`-sandbox probe never began the task within 300 seconds and was
stopped without accepting a UAC prompt or changing host policy. Its receipt
SHA-256 is
`EBC52E1854364E7A5ABD0320C0FE6B9FF087AD7B3D158C8820A96ADB5EAE4A2C`.

All three paths remain infrastructure evidence only and contribute zero
product evidence.

## Qualification-v3 renderer gate

Qualification-v3 keeps the exact nested CLI source-only and renders its output
through a parent-owned Playwright process. The renderer requires Chromium's
process sandbox, rejects `--no-sandbox`, separates read-only inputs from all
writable output, profile, temporary, cache, and crash paths, and verifies the
complete declared input and renderer-font graphs before and after rendering.
Canonical path guards, read-only ACL probes, credential-free environment,
offline browser context, route and event blocking, null proxy, resolver and
launch flags, and an explicit negative matrix provide layered application-level
containment.

The first external-renderer smoke stopped at an input-ACL ordering defect
before rendering. Its receipt SHA-256 is
`D62C5F1031AFAA6E2726A801C42D3FC3570D5E86E15A48E2835CFBBD8AAF1CD1`.
Revision 4 produced both positive PNGs but passed only 11 of 13 negative cases.
Its receipt SHA-256 is
`B00F1FAEF6C98CF8798C3A736F5292832C24615CF4794EA4D455BB3724EA0FA5`.
Revision 5 passed 12 of 13; the remaining out-of-root file request was blocked
but assigned the wrong failure class. Its receipt SHA-256 is
`902977C503A42A2AE528A727945B8B29B6621CD577561DFF4B47D4985F034C82`.
None authorized holdout execution.

Revision 6 passed the classification fixtures 8 of 8 and the full negative
matrix 13 of 13. It preserved the input graph and all 888 renderer-font files,
blocked child write, append, delete, and create probes, rendered the intended
and alternate viewports, launched Chromium with its process sandbox and
without `--no-sandbox`, and left no orphan process. The accepted synthetic
receipt is stored outside the repositories at
`qualification-v3/receipts/synthetic-smoke-v3.json`; its SHA-256 is
`98D0BCDA88BB6A6514AD85DD597F7284A7EF383B02484FD2BDDD0A13075F5869`.

This gate authorizes the preregistered holdout procedure. It does not qualify
the Skill. It is a synthetic one-artifact, two-viewport infrastructure test and
makes no product-effect, human-preference, interaction, accessibility, or
production-readiness claim. The isolation is application-level and does not
claim strict operating-system egress isolation or packet-level proof.

## Qualification-v3 holdout attempt 1

The first authorized holdout attempt stopped after 6 of 150 source executions.
The source-only stage completed, but the external renderer wrapper failed to
parse every model response before rendering. The partial attempt is
infrastructure-invalid and contributes zero product evidence and zero human
reviews. No review packet was produced.

The custodian AES-256-GCM-encrypted the quarantine, verified it, removed the
plaintext staging, and kept the remaining holdout sealed. The attempt receipt
SHA-256 is
`A65B8F1AC51D6FEB1BEB41FC596851EE4B32137D9980CBB37668F376C7A655F2`.
The encrypted quarantine archive SHA-256 is
`5C55D472996C7885DA2D7B04A0781A60F47D8E63539ACB42C25DA46A148959E2`.
A new holdout run requires a parser-specific synthetic gate and separate
authorization.

The defect was a missing closing parenthesis in the PowerShell
`CreateDirectory(...)` call, so the wrapper failed with
`System.Management.Automation.ParseException` before it parsed any model
response. The correction added only that parenthesis. Synthetic revision 7
then passed 15 of 15 artifact-parser cases, the existing 13 of 13 negative
security cases, and both renders. It accepts exactly one complete HTML or SVG
artifact block and fails closed on missing or ambiguous blocks. The receipt
SHA-256 is
`493AEA6D4EBE5F262DDCF0B213E5EEE78BE669C7519944F5AA17DD4E9D100BD3`.
This is parser and infrastructure evidence only.

## Qualification-v3 holdout attempt 2

The second authorized holdout attempt also stopped after 6 of 150 source
executions. Before the first browser launch, the revision-7 integrity check
correctly rejected the case-specific manifest: it resolved the hashed
determinism shim relative to the private case input directory, but staging had
not copied the shim there. The attempt produced zero accepted renders, zero
product evidence, zero human reviews, and no review packet.

The custodian encrypted and verified the quarantine and removed plaintext
staging. The attempt receipt SHA-256 is
`D3FA814B9E00821F77565DA0050DBF3AC2585D5A7A3FC8F6B8C63E2446DB1043`.
The encrypted quarantine archive SHA-256 is
`B9434EF4CEA43461592C8A30F1949C768E1F2F296FDC0C99BBAA7BAA9F766BFA`.
A new holdout run requires a case-private staging and integrity smoke plus
separate authorization.

Synthetic revision 8 materialized the exact hashed shim as
`.renderer/deterministic-shim.js` inside each complete declared case-input
graph before ACL freeze. It resolved every manifest path against that documented
root and verified canonical path, reparse state, and hash without weakening the
integrity gate. The smoke passed 8 of 8 renderer-input cases, 15 of 15 parser
cases, 13 of 13 security cases, and both case-private renders. Input and all 888
renderer-font hashes remained identical before and after rendering. The receipt
SHA-256 is
`5F9BF60CB53595C5F7DE4E2B63E6B2866B18381EEA4B68E96B025372C8C92E1B`.
This is still synthetic infrastructure evidence only.

## Qualification-v3 holdout attempt 3

The third attempt passed its first real checkpoint with 6 of 6 case-private
render runs and 12 of 12 intended/alternate PNGs. It later stopped at 12 of 150
status records: 11 jobs completed, one returned `Selected model is at
capacity`, and three workspaces were incomplete at immediate shutdown. The
frozen no-retry, whole-attempt contract invalidated the entire attempt even
though the provider failure occurred before a model response. It therefore
contributes zero product evidence and no human reviews.

The custodian encrypted and verified the quarantine and removed plaintext
staging. The attempt receipt SHA-256 is
`536AFD6184A150F0AD582836921BCC6C0DA09AA78C0699307C56F488F41EDC36`.
The encrypted quarantine archive SHA-256 is
`059C6A559A04F18B6BBF27973533EA76F1AB9A718DC3FE7BE8E2EAA460DAA57E`.

No further 150-job restart is authorized under the whole-attempt rule. A new
contract must use early real canaries, small immutable shards, per-job receipts,
and a predeclared same-job continuation rule for transport failures that occur
before any model response. Completed jobs may be retained only after an
independent review confirms that the new rule cannot introduce outcome-based
retry or arm selection.

These repairs change infrastructure configuration, not task content, Gold,
Skill wording, comparator scope, or evaluation claims. Every rejected batch
remains quarantined and cannot be recovered as product evidence.
