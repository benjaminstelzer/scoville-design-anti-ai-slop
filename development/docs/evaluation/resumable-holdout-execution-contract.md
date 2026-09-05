# Resumable holdout execution contract

Date: 2026-09-02  
Status: accepted infrastructure amendment under ADR-0013  
Scope: execution only; case content, arms, Gold, rubrics, packages, and
human-review rules remain frozen. ADR-0014 changes the next execution suite's
model target to `gpt-5.6-terra` at `high` before that suite is frozen.

## Non-negotiable boundary

The custodian remains the only actor that can read holdout prompts, fixtures,
Gold, raw model responses, artifacts, or scores. Parent and implementer receive
only blinded infrastructure classes, aggregate progress, hashes, and final
permitted reports.

No completed output may be retried because it is malformed, incomplete,
unattractive, unparseable, unrenderable, low-scoring, or inconsistent. Once any
model response exists, that job ID is terminal and all downstream failures are
part of its result.

## Execution order

1. Freeze the new execution-suite version, ordered blinded job IDs, blocked
   randomization, retry allowlist, backoff, receipts, and cost ceiling before
   any unseal.
2. Run synthetic fixtures for every materially different runner, output, parser,
   renderer, scorer, and arm-materialization path.
3. Run exactly one preregistered sealed canary for each materially different
   end-to-end path. The canary counts in the final schedule.
4. Evaluate the canary automatically and armblind. Report only infrastructure
   pass/fail and a predeclared error class. No person sees its task, arm,
   response, artifact, score, or Gold before the rest of the schedule.
5. If every canary passes, execute one shard at a time. A shard is the smallest
   complete arm-balanced randomization block, normally one blinded
   case-by-repetition block across every arm assigned to it.
6. Commit and verify every attempt or terminal job receipt before leasing the
   next shard.

No more than one shard may be active. A failed infrastructure invariant stops
before another shard is leased.

## Job state machine

Permitted job states are:

- `pending`: no attempt leased;
- `leased`: one attempt owns the idempotent job lock;
- `transport_retryable`: an allowlisted failure occurred before any model
  response and the fixed attempt budget remains;
- `terminal_result`: a model response exists, regardless of downstream result;
- `infrastructure_unresolved`: retry budget exhausted or failure class is not
  safely retryable;
- `corrupt`: receipt, hash chain, lock, or duplicate terminal output conflicts.

Only `pending` and `transport_retryable` may execute. `terminal_result` can
never execute again. `infrastructure_unresolved` keeps the qualification
incomplete. `corrupt` stops the suite.

## Transport retry

A retry requires all of:

- an allowlisted provider or transport status captured structurally, not only
  by matching free text;
- no response bytes, response event, completion tokens, artifact, or terminal
  model result;
- the identical blinded job ID, case, arm, repetition, seed, model, reasoning,
  prompt, fixture, package, harness, and limits;
- a valid immutable receipt for every earlier attempt;
- a retry decision made without case content, arm identity, scores, or other
  outcomes.

Initial allowlist: provider capacity rejection, provider rate-limit rejection,
and connection failure before request acceptance or response. Authentication,
configuration, model-not-found, ambiguous partial response, local parser,
renderer, scorer, timeout after response start, and unknown failures are not
retryable.

Maximum attempts per job: three total. Backoff after the first retryable
failure is at least 10 minutes; after the second it is at least 60 minutes.
Retry order follows the frozen blinded queue and cannot prioritize an arm or
case. Exhaustion produces `infrastructure_unresolved`, not omission.

## Atomic resume and receipts

Every attempt receipt records:

- schema, execution-suite, run, shard, blinded job, and attempt IDs;
- blinded case, arm, and repetition IDs plus seed and frozen order position;
- exact model, reasoning, CLI, Skill/control, prompt, fixture, benchmark,
  harness, parser, renderer, scorer, and renderer-font hashes;
- start/end timestamps, provider request ID, process and transport status,
  response-present flag, and token usage;
- raw trace/log, source, asset graph, artifact, parse, request log, render, PNG,
  score, and invariant hashes when present;
- terminal state and structured retry eligibility reason;
- hashes of every previous attempt receipt for the job;
- append-only hash-chain or authenticated binding plus atomic commit timestamp.

Write to a same-volume temporary path, flush, hash, authenticate, and rename to
the final receipt atomically. Resume verifies the entire chain before leasing
work. A valid terminal receipt prevents a new lease. Duplicate or conflicting
terminal receipts are corruption, not a latest-result choice.

## Qualification and claim boundary

Aggregate product scoring and human-review packet preparation begin only after
all preregistered jobs are terminal and all receipts verify. A partial suite
may report infrastructure progress and terminal counts only. It cannot silently
drop unresolved jobs, average complete cases, or claim qualification.

This amendment reduces wasted calls. It does not reduce the frozen evidence
requirement, expose holdout content, change a comparison arm, or permit an
outcome-based retry.
