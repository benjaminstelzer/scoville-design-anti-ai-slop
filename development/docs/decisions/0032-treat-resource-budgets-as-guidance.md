---
format_version: 1
id: ADR-0032
status: accepted
created: 2026-09-03
accepted: 2026-09-03
scope: project/resource-budgets
---

# Treat resource budgets as guidance

## Decision

Accepted from the user's explicit instruction on 2026-09-03: token, context,
cost and provider-call budgets in this project are planning guidelines rather
than absolute product-quality or execution limits. Exceeding one does not by
itself fail a package, Work Item or qualification lane when the additional
resource use is necessary, proportionate and recorded.

This does not turn non-budget controls into guidelines. Authorization
boundaries, immutable evidence, frozen model and reasoning settings,
arm-parity rules, terminal-on-model-response semantics, outcome-retry bans,
source and ownership constraints, safety controls and publication or release
prohibitions remain binding unless the user changes them explicitly.

Existing budgets remain useful for preflight, comparison and detecting
unbounded work. Prefer the smallest sufficient payload and stop unnecessary
calls, but do not trade away professional depth, valid evidence or a correct
repair merely to stay below a numeric guideline.

## Problem

Earlier Decisions and Work Items sometimes use token, call and cost ceilings
as hard admission gates. The user clarified that these numbers are guidance
and do not outweigh the goal of fully developing and qualifying the Skill.
Leaving them as automatic failure conditions would misrepresent current
authority and could stop useful work for accounting rather than product risk.

## Drivers

- Complete the Skill to the required quality and evidence standard.
- Keep resource use visible without letting estimates replace judgment.
- Preserve strict execution integrity and authorization boundaries.
- Avoid expanding prompts or calls without a concrete quality or evidence need.

## Considered alternatives

- Keep every historic numeric ceiling absolute. Rejected because it conflicts
  with the user's explicit clarification.
- Remove all resource accounting. Rejected because measured usage remains
  useful for planning, parity and later release claims.
- Treat every numeric control as advisory. Rejected because parity counts,
  retry limits and security invariants are protocol and safety controls rather
  than resource budgets.

## Consequences

- Budget-only validator findings are recorded and judged proportionately
  instead of automatically blocking progress.
- Resource overruns require a short factual reason and exact observed usage.
- Existing evidence remains unchanged; this Decision governs subsequent
  interpretation and work.
- No new authorization for sealed calls, installation, publication, commit,
  push, tag or release is created.

## Confirmation

Future Plan and evaluation records distinguish advisory resource estimates
from binding protocol, evidence, safety and authorization controls and report
actual usage without claiming that a budget overrun is automatically a product
failure.

## Revisit when

The user reinstates a hard cost or token stop, a provider enforces a technical
limit, or arm parity requires a common binding maximum.
