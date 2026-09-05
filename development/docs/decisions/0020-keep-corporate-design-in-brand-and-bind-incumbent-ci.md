---
format_version: 1
id: ADR-0020
status: accepted
created: 2026-09-02
accepted: 2026-09-02
scope: architecture/corporate-design-ci
---

# Keep Corporate Design in Brand and bind incumbent CI

## Decision

Keep Corporate Design and corporate visual-identity creation, application,
audit, evolution, documentation and governance in
`brand-and-visual-systems`. Do not create a duplicate Corporate Design leaf.

Resolve one package mode from `generate`, `critique`, `repair`, or
`style-direction`, then a separate Brand operation from `create`, `apply`,
`audit`, `evolve`, or `document`, and an incumbent relation from `conform`,
`authorised change`, `no applicable incumbent`, or `unresolved`.

`No applicable incumbent` requires an explicit owner statement or recorded
authority check. Missing files are not evidence. Unknown currency, authority,
scope, or equal-rank contradiction is `unresolved` and blocks non-provisional
identity mutation. A current mandatory CI outranks an aesthetically preferable
alternative unless an authorised exception changes its scope.

Corporate Identity is broader than Design. Purpose, strategy, behaviour,
culture, naming and verbal identity are authorised inputs; they do not route
Design unless a corporate-design or visual-system decision is open.

## Problem

The existing Brand leaf owns much of visual identity but cannot reliably apply
an incumbent CI without source precedence, contradiction, exception and proof
state. Adding a second Corporate Design leaf would duplicate the same system
owner, while routing generic Corporate Identity would overclaim strategy and
organisational authority.

## Drivers

- Greenfield visual identity and incumbent conformance need different freedom.
- One canonical visual-system decision needs one owner.
- CI sources can be missing, stale, contradictory or scoped differently.
- Scoville UI must implement the current framework/design system strictly when
  active without becoming its visual author.

## Considered alternatives

- Add a Corporate Design leaf. Rejected because it duplicates Brand ownership.
- Treat `conform` as a fifth package mode. Rejected because conformance can
  constrain generation, critique, repair or style direction.
- Treat absent manuals as no incumbent identity. Rejected because absence is
  not authority.
- Let Design define Corporate Identity strategy. Rejected as a materially
  broader organisational discipline.

## Consequences

- Brand receives an authority/version/scope/rule/variation/exception/proof
  contract and explicit architecture/co-branding logic.
- A local craft owner repairs a valid rule's application; Brand repairs a
  faulty or contradictory visual-system rule under authority.
- UI retains standalone Greenfield fallback when Design is absent. With Design
  active, Design defines/judges and UI implements/proves mechanics.

## Confirmation

Route fixtures distinguish corporate visual identity from strategy-only,
behaviour-only, naming-only and verbal-identity work. Terra cases separately
exercise Greenfield creation, mandatory conformance and unresolved conflicting
sources without granting false approval.

## Revisit when

Applied evidence shows Brand cannot remain independently routable at its token
ceiling or a distinct Corporate Design parent cause appears that does not share
visual-identity governance.

