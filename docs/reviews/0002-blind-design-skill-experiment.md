# Blind ten-point design-skill experiment

Date: 2026-09-01  
Status: completed  
Models: fresh GPT-5.6 SOL XHigh; fresh Claude Fable 5.1 High

## Protocol

Both models received the same general question without project context and
were instructed not to use files, tools, or web research:

> Design an Agent Skill that gives the user a professional designer able to
> create, evaluate, and improve designs and graphics. What are the ten most
> important things it must contain or master? Return exactly ten German points,
> at most 100 words each.

SOL ran in a fresh no-history subagent. Fable ran as a fresh, customization-off
read-only consultation from a temporary working directory. Fable's reported
backend model field was empty; the wrapper requested `claude-fable-5-1` with
high effort and reported USD 0.169054 cost.

## Independent answer map

| Area | SOL | Fable 5.1 | Existing Plan |
| --- | --- | --- | --- |
| Brief, audience, purpose, context | explicit | explicit | covered |
| Visual strategy and subject fit | explicit | through context/layout | covered |
| Composition and formal foundations | explicit | explicit | covered |
| Typography | explicit | explicit | covered with stronger evidence limits |
| Colour and contrast | explicit | explicit | covered with medium/reproduction scope |
| Imagery and graphic production | explicit | indirect via artifact creation | covered |
| Systems, brand, consistency | explicit | explicit | covered |
| Accessibility and intended context | explicit | explicit | covered with observation boundaries |
| Critique, prioritization, iteration | explicit | explicit | covered |
| Technical production and handoff | explicit | partial | covered |
| Actual editable artifact creation | implied through creation | explicit | strengthen in Plan |
| Executable style fluency/anti-cliché | explicit only as anti-cliché imagery | absent | covered more deeply by user requirement |
| Rule exceptions and evidence honesty | absent | absent | covered |
| Provenance/licensing | explicit in type/assets | absent | covered |
| Multiscript/culture/representation | partial language scope | absent | covered |
| Optional Design/UI ownership | absent | absent | covered |

## New or strengthened item

The only material addition is an explicit artifact-output gate: design work
must produce a real editable artifact through the appropriate format/tool
owner and inspect a render. Advice, a design-system description, or an image
prompt alone is not sufficient when the user requested an artifact.

## Rejected universalizations

The Fable answer mentioned the golden ratio, fixed-unit spacing systems,
generic serif/sans/monospace fit, and always-on WCAG/UI checks. These are useful
possible tools or scoped requirements, not universal graphic-design laws. The
existing rule taxonomy, applicability checks, and observation boundary remain
stronger than adopting them literally.

## Conclusion

The blind answers strongly corroborate the Plan's practical coverage and add no
new top-level expert domain. They support the application-first priorities and
justify strengthening real artifact production. They do not validate visual
quality, model parity, or market leadership and do not replace source-grounded
research or outcome testing.
