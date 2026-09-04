---
format_version: 1
id: ADR-0021
status: accepted
created: 2026-09-02
accepted: 2026-09-02
scope: architecture/expert-boundaries
---

# Use hard owners, soft observers, and a non-owning communication record

## Decision

Keep expert edges soft for observation and interdisciplinary effect, but hard
for canonical mutation, authority and proof. One parent cause has one owner.
Other experts may append attributed observations or conflicts and hand them to
that owner; they may not silently change the decision or claim its proof.

Use a compact non-owning Communication record in Core:

`job | sender/authority | audience/context/prior knowledge |
interpretation/action | supported proposition/evidence | modal relation |
misreading/consequence | protected content | field owner/status/source version |
proof target | unknowns`.

Only the canonical field owner updates decision/status. A governing source-
version change invalidates affected fields until rechecked. Unresolved
conflicts propagate as unresolved. Do not add a universal Communication leaf.

Admit a specialist only when it has an independent parent cause, contrast
route, owned state, distinct proof, stop boundary and material applied token
value. Otherwise keep the concern as a local observation or record field.

## Problem

Graphic-design disciplines overlap perceptually, but vague shared ownership
causes duplicate routing, contradictory mutation and unsupported proof claims.
Completely isolated modules lose the cross-domain effects needed for good
design. A universal Communication expert would load on nearly every task and
repeat Brief, Concept and craft knowledge.

## Drivers

- Typography, space, image, meaning, medium and interaction affect one another.
- Authority, rights, facts, standards and receiver proof cannot be negotiated
  as aesthetic preference.
- Progressive loading requires independent leaves without hidden sibling reads.
- Boundary-object research supports a stable shared representation with local
  specialist interpretations rather than erased ownership.

## Considered alternatives

- Give every overlap to both experts. Rejected because mutation and proof become
  ambiguous.
- Make experts completely isolated. Rejected because cross-domain effects and
  causal handoffs disappear.
- Add a general Communication Design leaf. Rejected because its route and token
  value are not independently discriminative.

## Consequences

- Brief owns the supplied problem and gates; Concept owns the organising
  mechanism; craft and medium leaves own their local systems.
- Observers can detect but cannot repair another owner's parent cause.
- The shared record is a coordination object, not evidence of consensus or
  successful communication.
- `requires` and `conflicts` remain empty; Core selects leaves directly.

## Confirmation

Near-neighbour fixtures must route the parent cause to exactly one owner while
permitting owner-attributed observations. Tests invalidate a record after a
source-version change and preserve unresolved disagreement. No task routes a
leaf from the topic word `communication` alone.

## Revisit when

A repeatedly co-loaded pair cannot exchange a compact record without losing
decisive information or a supposedly soft overlap proves to have a distinct
parent cause and proof contract.

