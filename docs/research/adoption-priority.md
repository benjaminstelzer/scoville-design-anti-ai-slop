# Adoption priority for external Skill mechanisms

Date: 2026-09-02  
Status: W-011 comparison criterion

## Priority order

External mechanisms are valuable first when they improve:

1. typography and typesetting quality;
2. spacing logic and spatial rhythm;
3. negative space, hierarchy, grouping, and reading order;
4. subject-specific, interesting composition without template mannerisms;
5. responsive preservation or medium translation of those relationships;
6. other specialist depth after the visual foundation is sound.

Popularity or feature count never outranks these priorities.

Typography comparison gives primary depth to Latin scripts. Non-Latin Skills
are relevant only to the V1 safety floor unless a candidate offers a compact
mechanism for detection, supported rendering, prevention of Latin-default
misuse, and honest native-reader escalation.

## Typography comparison questions

- Does the Skill assign typographic roles before selecting families?
- Does it show how to combine families through compatible or deliberately
  contrasting proportion, x-height, stroke, terminals, rhythm, voice, script
  coverage, optical sizes, and available weights/styles?
- Does it treat serif display plus sans body as one possible mechanism rather
  than a universal pairing recipe?
- Does it diagnose and repair kerning, tracking, word spacing, leading,
  measure, paragraph rhythm, alignment, justification, hyphenation, line and
  page breaks, punctuation, numerals, and fallback drift?
- Does it evaluate the actual language, writing system, copy, size, distance,
  renderer, and medium?
- Do examples or tests visibly support the claimed type quality?

## Spacing and composition comparison questions

- Are spacing decisions based on relationship and consequence rather than one
  universal scale?
- Are within-group, between-group, section, edge, and sequence spaces clearly
  distinguished?
- Does negative space separate, pace, frame, direct, or intensify, rather than
  serving as a generic request for more emptiness?
- Can the Skill diagnose uniform spacing, arbitrary cards, false alignment,
  weak grouping, tangents, trapped gaps, edge tension, overcrowding, and
  decorative whitespace?
- Does it create focal hierarchy, counterstructure, asymmetry, overlap,
  cropping, rhythm, or controlled density when the concept benefits, while
  keeping communication legible?
- Does responsive work recompose relationships instead of shrinking one
  desktop arrangement?
- Do examples show several subjects and media, or only one fashionable page
  pattern?

## Adoption rule

Adopt mechanisms, never prose or unexplained recipes. A mechanism must name:

- the design problem it solves;
- observable inputs and failure signatures;
- the decision or repair move;
- what should remain unchanged;
- the context where it applies;
- the exception and compensating structure;
- the render or human evidence that could disprove it.

Reject fixed font counts, universal family pairings, unexplained spacing
scales, mandatory white space, universal grids, style bans, or example quality
presented as general proof.

## Architecture question

W-011 must decide whether spacing and rhythm remain inside composition and
typography or justify a directly routed `spacing-and-rhythm` leaf. Split only
if spacing tasks have independent signals and the leaf avoids duplicating
layout hierarchy, typesetting, or UI token implementation. Design owns spacing
relationships and the system definition; Scoville UI implements supported
tokens and responsive mechanics when active.
