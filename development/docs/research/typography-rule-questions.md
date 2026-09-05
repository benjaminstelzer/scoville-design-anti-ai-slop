# Typography rule questions

Date: 2026-09-02  
Status: mandatory W-011 typography audit input

V1 priority: professional Latin typography and typesetting. Non-Latin and
vertical systems receive the bounded safety floor in ADR-0016, not an
exhaustive curriculum.

## Typeface combination

The typography audit must derive source-backed decision rules for:

- role compatibility: display, body, annotation, navigation, data, code,
  caption, action, and fallback;
- formal relationship: x-height, cap height, width, proportion, stroke contrast,
  terminals, counters, apertures, stress, rhythm, texture, and typographic
  colour;
- useful contrast versus accidental near-similarity;
- historical, cultural, and tonal coherence versus deliberate tension;
- weight, width, optical-size, italic, small-cap, numeral, punctuation, and
  language/script repertoire;
- metric compatibility when faces share a line, table, component, or fallback
  chain;
- rendering quality, variable-font behavior, licensing, embedding, web/app use,
  and performance;
- hierarchy that remains clear when colour and decoration are removed.

The result must explain how to compare candidate families using real text at
final size and medium. It must not reduce pairing to serif plus sans, similarity
scores, historical genre labels, or a list of fashionable combinations.

## Number of families

Determine what established sources support about family count and classify it
correctly:

- one family or superfamily may cover a complete system when its roles,
  weights, widths, optical sizes, and language support are sufficient;
- add a second family only when it supplies a distinct function, voice, or
  contrast the first cannot provide cleanly;
- add a third or further family only for a separately legible role whose value
  exceeds the added hierarchy, licensing, loading, rendering, and governance
  cost;
- count families separately from styles, weights, widths, variable axes,
  symbol fonts, code faces, and functional fallbacks;
- test whether removing one family preserves meaning and character; if so, the
  extra family may be decorative redundancy;
- test whether two families are so similar that the difference appears
  accidental, or so unrelated that they create competing voices.

If sources support a common one-, two-, or three-family range, state it as a
contextual convention or starting heuristic with its medium and exception,
not as a universal maximum. Posters, editorial systems, vernacular work,
historical quotation, multilingual systems, data/code interfaces, and
experimental display work may justify different counts when hierarchy and
coherence remain controlled.

## Typesetting rules to resolve

- character differentiation and repertoire;
- kerning versus tracking versus word spacing;
- optical versus mathematical spacing;
- contextual measure and return sweep;
- leading, line-box behavior, paragraph rhythm, baseline relationships;
- alignment, rag quality, justification, hyphenation, rivers, ladders, runts,
  widows/orphans, headings and page/column breaks;
- real quotation marks, apostrophes, dashes, ellipses, spaces, ligatures,
  fractions, ordinals, tabular/lining/oldstyle figures, superscripts, small caps,
  language-specific punctuation and casing;
- fallback substitution and metric drift;
- basic multiscript detection, supported shaping/direction/fallback/render
  requirements, prohibition of Latin-default transfer, and native-reader
  escalation per ADR-0016;
- screen zoom/reflow/text-spacing resilience and print/PDF/font proof.

For every topic, record rule strength, source, scope, failure signature, likely
cause, smallest repair, allowed exception, and final verification view.
