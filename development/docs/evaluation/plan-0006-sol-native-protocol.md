# SOL native execution fallback

Protocol P6-focused-v1/P6-sol-native-v1 is frozen before native outputs on
2026-09-04 under ADR-0057. It changes the executor, not task inputs, candidate
bytes or acceptance. Both arms of C4, C5A, C5B, C6 and C7 use fresh
gpt-5.6-sol/high native subagents without conversation history. Each receives
only its own neutral workspace, the identical transport instruction and the
frozen task. Generation is read-only; the host materialises returned source
and supplies actual render feedback. C6 deliberately receives no render.
No other arm, findings, acceptance expectations or package-change history are
supplied to generators. C1-C3 are not repeated.

The documented CLI attempt is retained at
`C:/Users/benja/AppData/Local/Temp/design-plan6-sol-v1-20260904/cases/C4/baseline/attempt-1`.
Its thread 01a06b4f-3ecd-7f73-94e3-e112d95d8657 returned no source because
workspace reads were rejected by host policy. Exit code zero describes the
completed transport, not a successful case. This is unverified infrastructure
failure, not a Skill failure. The policy is not weakened and the attempt is
not silently replaced by a passing receipt.

The native host retains its own developer instructions and tool catalogue.
This is therefore a matched native-execution stratum, not an assertion of a
clean CLI catalogue or genuine implicit Skill discovery. Workers are scoped
to their own package/input tree. Any outside reads or extra Skill activation
must be disclosed and assessed for pair comparability. Actual trace evidence
is distinguished from a worker's read-path report. Host activation remains a
separate lane; explicit package instructions cannot pass it.

Generated freeze and per-file input/package hashes are at
`C:/Users/benja/AppData/Local/Temp/design-plan6-sol-native-v1-20260904/freeze.json`.
Use new labelled artifacts and proof directories. Preserve original outputs,
failures and unfavourable judgments. The separate blinded reviewer receives
anonymous outputs and actual evidence, not this arm assignment or prior
findings. Corrections require affected-case rechecks only.
