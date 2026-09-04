---
format_version: 1
id: ADR-0016
status: accepted
created: 2026-09-02
accepted: 2026-09-02
scope: content/typography-priority
---

# Prioritize Latin typography with a multiscript safety floor

## Decision

Make professional Latin typography and typesetting the primary V1 typography
depth. Keep non-Latin and vertical writing systems as a bounded safety and
routing floor rather than a broad specialist curriculum.

The floor must:

- detect the supplied language, script, direction, and required repertoire;
- require a font and renderer that support shaping, marks, fallback, line
  breaking, and direction for that script;
- prohibit silent transfer of Latin tracking, casing, italic, hyphenation,
  justification, word-spacing, or line-break assumptions;
- render the actual supplied text and flag unsupported glyphs or layout drift;
- require native-reader or script-specific authority when quality, meaning,
  safety, or publication consequence is material.

## Problem

Comprehensive writing-system instruction is large, highly language-specific,
and still cannot replace native-reader or font-engineering review. It would
consume context away from the user's primary need: excellent general graphic
design and Latin typography.

## Drivers

- Typography, spacing, hierarchy, negative space, and composition are the
  highest-priority adoption criteria.
- Exact coverage matters more than token count, but coverage must match the
  intended V1 scope.
- A compact safety floor prevents confident misuse without claiming broad
  multiscript expertise.

## Considered alternatives

- Ship a full writing-systems leaf. This is useful future work but exceeds the
  current priority and still needs domain reviewers.
- Ignore non-Latin scripts. This permits harmful Latin-default behavior.
- Treat every script with one generic rule. This hides material differences.

## Consequences

- Typography research goes deepest on Latin family selection and combination,
  type roles, hierarchy, measure, leading, spacing, alignment, justification,
  microtypography, page breaks, numerals, optical sizes, fallback drift,
  licensing, and screen/print proof.
- Non-Latin additions remain basic gates and escalation instructions unless a
  future Decision elevates a specific script or language.
- The successor package makes no native-reader, multiscript typesetting, or
  global writing-system competence claim.

## Confirmation

Open Terra tests must cover professional Latin generation, critique, and
repair. A small multilingual safety case must show detection, no Latin-default
misapplication, actual-font/render checks, and honest escalation; it does not
qualify the script's typography.

## Revisit when

Users request sustained work in a named non-Latin script and suitable sources,
fonts, fixtures, and native reviewers are available.
