---
format_version: 1
id: ADR-0059
status: accepted
created: 2026-09-05
accepted: 2026-09-05
scope: project/package-size
---

# Remove package size guidelines

## Decision

The user explicitly requested complete removal of size guidelines on 2026-09-05. Remove package, Core, index, module and common-load size targets, ceilings, leaf-count allowances and their warnings from current runtime metadata, authoring tools, tests and current guidance. Actual resource measurements may remain descriptive. This specific package-size choice replaces the advisory treatment of size in ADR-0032; its separate resource accounting and execution-integrity provisions remain applicable.

## Problem

Advisory thresholds still impose maintenance work and suggest preferred document lengths without demonstrating design quality.

## Drivers

Complete practical guidance and preserve factual evaluation records under the user's explicit choice.

## Considered alternatives

Increasing thresholds or retaining warnings would preserve the guidelines the user requested removing. Removing historical measurements would destroy evidence and is unnecessary.

## Consequences

Current package validation checks structure and evidence without judging instruction length. Preserve historical protocols, results and provider-enforced technical or spending controls. No installation or publication is authorized by this change.

## Confirmation

Current metadata and tooling contain no operative size thresholds; expanded valid content and common loads validate without size warnings, while malformed routes and references still fail.

## Revisit when

The user explicitly requests a new size policy or a real provider constraint requires a bounded execution setting.
