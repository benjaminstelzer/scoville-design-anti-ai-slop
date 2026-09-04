---
format_version: 1
id: ADR-0056
status: accepted
created: 2026-09-04
accepted: 2026-09-04
scope: design/reviewer-contingency
---

# Use SOL for interim reviews

## Decision

Use fresh context-free gpt-5.6-sol subagent sessions for reviews while Fable is
unavailable, as explicitly selected by the user on 2026-09-04. Keep blinded
artifact comparison separate from installed-package and proposal-fidelity
review. SOL may recommend corrections for authorised host implementation and
verify separately versioned renders. Preserve the original outcomes.

## Problem

The Claude provider returned HTTP 429 with a session-limit reset of 11:10
Europe/Berlin. It interrupted C4 candidate generation and the revised isolated
host-activation attempt. This is an external provider limit, not a project
token budget or a demonstrated Skill defect. The user then asked to continue
without Fable and use a SOL agent in an extra session for reviews until Fable
returns.

## Drivers

- Continue useful independent review rather than silently retry a provider limit.
- Preserve the requested model and equal conditions for each generation pair.
- Keep initial artefacts and unfavourable findings available for comparison.
- Do not infer installation, publication or broader model-substitution authority.

## Considered alternatives

- Wait for every review until Fable returns: preserves the original reviewer
  but delays independent checks the user explicitly wants to continue.
- Silently substitute SOL for all generation and review: faster but confounds
  the frozen comparison and exceeds the specifically named review substitution.
- Selected: SOL reviews now; retain Fable-generated paired artefacts unchanged,
  identify any review-driven host corrections separately, and leave unexecuted
  generation and genuine activation lanes visibly open.

## Consequences

SOL verdicts are attributed to their actual reviewer, never to the retained
Fable session. The user's temporary review substitution does not erase the
remaining Fable final-review requirement or authorise mixed-model generation
pairs. Authorised local implementation and deterministic checks can continue.
PLAN-0006 W-004 has already started. Format-version-1 therefore forbids changing
its authored Decisions list or Acceptance; this supplementary decision is
discoverable through execution evidence, not an invented canonical WI link.

## Confirmation

Retain the separate reviewer task identifiers, package or anonymised artifact
hashes, complete findings, limits and any correction-version receipts. Recheck
only affected outputs after real corrections. A static clean review is not
proof of design improvement or host activation.

## Revisit when

Fable becomes available, the user explicitly authorises another execution
model for remaining paired cases, or a review shows a material scope or
evidence conflict requiring a new choice.
