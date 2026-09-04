# W-005 ADR-0042 public routing-boundary stress

Date: 2026-09-03  
Status: passed with two preserved infrastructure/benchmark adjudications  
Decisions: ADR-0042 through ADR-0044

## Purpose

This source-cleared public sequence tests the fixed-media routing rule introduced
by ADR-0042:

1. open reproduction and delivery work must add Editorial, Colour and Media
   Production;
2. settled reproduction and delivery must not add Colour or Media Production;
3. delivery-only work must load Media Production without reopening Editorial or
   Colour.

The three cases ran sequentially with one Terra High transport call each, no
outcome retry and no sealed content or call.

## Results

| Case | Authenticated route | Forbidden reads | Result |
| --- | --- | ---: | --- |
| 1: open production | Editorial, Colour, Media Production (3/3) | 0 | pass on immutable replay |
| 2: settled production | Editorial, Composition, Typography, Information Design (4/4) | 0 | pass on immutable replay |
| 3: delivery only | Media Production (1/1) | 0 | pass |

All three terminal reports aligned exactly with authenticated staged-file reads,
all response contracts passed, and all requested artifacts existed. Aggregate
transport evidence is three calls, zero retries and zero sealed calls.

## Preserved adjudications

Case 1 initially scored zero authenticated reads because the canonical extractor
did not understand a literal filename array joined to the exact staged references
root. ADR-0043 added a strict output-authenticated form and adversarial rejection;
the immutable raw evidence then passed 3/3 without another model call.

Case 2 initially failed its original Editorial-only Gold after four authenticated
reads. ADR-0044 preserves that result and Gold. Direct owner inspection showed the
brief also left reading hierarchy, grouping, type hierarchy and a two-page
timetable open, which materially route to Composition, Typography and Information
Design. A versioned corrected Gold retains Colour and Media Production as the
negative boundary. Immutable replay passed 4/4 with zero forbidden reads and no
additional model call.

The final Case 3 diagnostic command returned nonzero only because it appended
`git status` in a non-repository workspace. The expert read completed at zero,
the artifact existed, the terminal response and usage were present, and every
scoring check passed. This ancillary diagnostic failure is not product evidence.

## Validation and hashes

- Canonical route-provenance tests: 18 of 18 passed.
- Case 1 replay receipt:
  `B18DEB28243BB8E7DFE1807E3FA4533959EFE65870F4B35E241DADB91DC8D725`
- Case 2 original failed receipt:
  `BE9283431994624EB7297B59F8C34F64798F78B8605DEDA7267DE6279C390A3C`
- Case 2 corrected-Gold replay receipt:
  `987782A9EB431495E4CADA19816B95D7F17CC47B65E5DE870FAC04AED5B90242`
- Case 3 receipt:
  `3B83BBC457A3AD0379F3411CB35F54399C290580E0DA7F937A3654F0AA2B4163`
- Case 3 raw events:
  `865773E1D16357386DF228E99542B72C48A7A93AEB8BB4E0C774C2F8BEA1F020`
- Case 3 artifact:
  `C59BB635289DCC89782B4D79D7F37806F8B89F5FAF116B65C14B4B629C1CE100`
- Final route extractor:
  `220A78B43BB2FE526F5D9E9ED8366A56ECCD15A87A9B6981906D4A68D1423D68`
- Final route-provenance tests:
  `575024E247D1C10BA9921CC4091F46ECDFC61901C5D477AA6B3DF502729B5E83`
- Case 3 execution descriptor:
  `324E6EAF3E2E5ECE90B8DFAFAB2BEB3719773A25BB9CA4CA54EEC5A9BE5BC972`

## Claim limit and next gate

The public sequence supports the ADR-0042 routing boundaries and removes the
public behavioral blocker to a fresh sealed generation. It does not rehabilitate
failed qualification-v6, qualify the product by itself, or authorize a new
sealed execution. A v7 suite requires fresh zero-call custody receipts and a
separate hash-bound execution authorization before any unseal or provider call.
Publication, installation, commit, push, tag and release remain unauthorized.
