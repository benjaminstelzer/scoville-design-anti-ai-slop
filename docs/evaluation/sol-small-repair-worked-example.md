# Small repair: illustrative workflow

This is a constructed development example, not an executed test or evidence of
visual improvement. It is excluded from the installed Skill and reviewer input.

## Fixed task and input

The user supplies an accepted HTML event poster and asks to reduce only the
excessive tracking of its Latin title. Keep text, font, size, colour, placement
and footer unchanged. Deliver the edited HTML. Only source tools are available.

Relevant source before:

```css
.event-title { font-size: 48px; letter-spacing: 0.30em; }
```

## Minimal decision and action

- Mode: repair. Authority: title tracking only.
- Owner: Typography. No open concept, brand, general composition or production
  decision; no additional expert is selected merely because this is a poster.
- Candidate source repair: change `letter-spacing` to `0.03em`. This is an
  illustrative candidate, not a universal tracking value or verified best fit.
- Preserve every other declaration and supplied content. Check the diff for
  the single authorized change; do not refactor unrelated CSS.

## Proof and stopping state

Inspect the source diff to establish scope, not appearance. Without a renderer,
the honest handoff is: source tracking changed, visual result unverified.
Do not say that fit or optical quality passed. The remaining check is the title
and its affected surrounding region at intended size in the target renderer.
If that check later exposes a collision caused by the repair, adjust the
authorized tracking or report that a different change needs permission.

## Intentionally omitted

No audience study, full brief inventory, alternative concept, font-engineering
review, new branding, all-module load, unrelated footer repair, release dossier,
or comparison report is needed. No missing renderer is represented as a pass.
The working notes above are shown only to explain the example; they are not
mandatory deliverables for the corresponding user task.
