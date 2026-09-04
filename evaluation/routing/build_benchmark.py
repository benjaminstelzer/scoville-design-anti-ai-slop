#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


SKILL = ".agents/skills/scoville-design-anti-ai-slop/SKILL.md"
MODULES = [
    "brief-and-concept",
    "composition-and-layout",
    "typography-and-writing-systems",
    "colour-and-reproduction",
    "imagery-and-art-direction",
    "information-and-data",
    "brand-and-visual-systems",
    "ui-and-interaction-design",
    "motion-and-sequence",
    "media-production-and-handoff",
    "critique-and-validation",
    "culture-ethics-and-provenance",
    "sources-and-attribution",
    "style-direction",
]


def reference(module_id: str) -> str:
    return f".agents/skills/scoville-design-anti-ai-slop/references/{module_id}.md"


def item(case_id: str, task: str, selected: list[str]) -> dict:
    brief = "brief/task-context.md"
    selected_reads = [reference(module_id) for module_id in selected]
    required = [SKILL, *selected_reads]
    phases = [[SKILL]]
    if selected_reads:
        phases.append(selected_reads)
    forbidden = [reference(module_id) for module_id in MODULES if module_id not in selected]
    forbidden.append(brief)
    return {
        "id": case_id,
        "task_type": "design_routing_probe",
        "prediction": {
            "task_text": (
                "Routing-only probe. Read only the applicable Scoville Design experts. "
                "Do not create an artifact. " + task +
                " Return only the exact contracted JSON."
            ),
            "files": {brief: "No additional task context. The complete probe is in the user prompt.\n"},
            "output_contract": (
                "Return exactly one JSON object with keys status and selected_modules. "
                "status must be ok. selected_modules must be an array containing only the "
                "applicable canonical module IDs in direct-index order."
            ),
            "skill_activation": "explicit",
        },
        "scoring": {
            "expected": {"status": "ok", "selected_modules": selected},
            "required_file_reads": required,
            "forbidden_file_reads": forbidden,
            "exact_once_file_reads": required,
            "required_read_phases": phases,
            "required_command_patterns": [],
            "forbidden_command_patterns": [
                "curl|wget|Invoke-WebRequest|Set-Content|Remove-Item|apply_patch"
            ],
            "max_shell_calls": len(required),
        },
    }


TRAIN = [
    ("route-train-core", "Classify a simple visual-design request whose brief is already complete and needs no specialist judgment.", []),
    ("route-train-brief", "Resolve an ambiguous campaign brief into distinct concept territories and select one before making.", ["brief-and-concept"]),
    ("route-train-layout", "Judge a dense poster hierarchy, spacing system, and intentional off-grid title.", ["composition-and-layout"]),
    ("route-train-type", "Audit typesetting, font fallback, and Arabic plus Latin script requirements.", ["typography-and-writing-systems"]),
    ("route-train-colour", "Define colour roles and verify web contrast plus CMYK proof boundaries.", ["colour-and-reproduction"]),
    ("route-train-imagery", "Art-direct one abstract still-life hero image with generated-image edits and responsive crops; people, documentary, identity, and motion or sequence work are out of scope.", ["imagery-and-art-direction"]),
    ("route-train-data", "Given verified values and a fixed approved type system, choose the encoding and uncertainty treatment for a public budget chart.", ["information-and-data"]),
    ("route-train-brand", "Define invariants, controlled variation, touchpoints, and governance for a visual identity system.", ["brand-and-visual-systems"]),
    ("route-train-ui", "Redesign a clinic appointment workflow and its responsive/error/loading states without implementing code.", ["ui-and-interaction-design"]),
    ("route-train-motion", "Storyboard a timed title sequence and define its reduced-motion and static equivalents.", ["motion-and-sequence"]),
]

VAL = [
    ("route-val-production", "Prepare an editable SVG and PDF handoff with syntax validation, exact render proof, and vendor unknowns.", ["media-production-and-handoff"]),
    ("route-val-critique", "Perform a deep generic-cliche critique and validate a before/after repair.", ["critique-and-validation"]),
    ("route-val-culture", "Review cultural authority, participant consent, privacy, AI provenance, and IP risk for campaign imagery.", ["culture-ethics-and-provenance"]),
    ("route-val-sources", "Audit licenses, attribution, source IDs, and current-fact verification for external reference material.", ["sources-and-attribution"]),
    ("route-val-style", "Compile a named historical style into a contemporary medium; a separate deep critique is not requested.", ["style-direction"]),
    ("route-val-mixed-poster", "Create a typographically led historical-style poster with a deliberate grid exception.", ["composition-and-layout", "typography-and-writing-systems", "style-direction"]),
    ("route-val-mixed-data", "Create an editable projected data story and prove content fit in its rendered slide.", ["composition-and-layout", "information-and-data", "media-production-and-handoff"]),
    ("route-val-mixed-ui", "Define a localized UI workflow, its typography/fallback behavior, and a render-ready Design-to-UI handoff.", ["typography-and-writing-systems", "ui-and-interaction-design", "media-production-and-handoff"]),
]

TEST = [
    (
        "route-test-multilingual-packaging",
        "Define and hand off a multilingual food-packaging identity across a small label: script-aware typography, colour roles and print constraints, brand invariants, cultural review, and editable production proof are all required; no separate image art direction is requested.",
        [
            "typography-and-writing-systems",
            "colour-and-reproduction",
            "brand-and-visual-systems",
            "media-production-and-handoff",
            "culture-ethics-and-provenance",
        ],
    ),
    (
        "route-test-wayfinding-system",
        "Create an accessible exhibition wayfinding family whose spatial hierarchy, bilingual type, pictorial landmark treatment, and information encoding work across signs and a map.",
        [
            "composition-and-layout",
            "typography-and-writing-systems",
            "imagery-and-art-direction",
            "information-and-data",
        ],
    ),
    (
        "route-test-retro-web-repair",
        "Repair a cliched retro-neon campaign page while preserving recognizability: diagnose generic style choices, rebuild the composition and colour logic, and validate the before/after result; implementation code is out of scope.",
        [
            "composition-and-layout",
            "colour-and-reproduction",
            "critique-and-validation",
            "style-direction",
        ],
    ),
    (
        "route-test-annual-report-system",
        "Turn an unresolved annual-report brief into a repeatable editorial system with verified charts, deliberate image roles, and an editable print plus screen handoff.",
        [
            "brief-and-concept",
            "composition-and-layout",
            "imagery-and-art-direction",
            "information-and-data",
            "media-production-and-handoff",
        ],
    ),
]


def write_items(root: Path, split: str, cases: list[tuple[str, str, list[str]]]) -> None:
    path = root / split / "items.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps([item(*case) for case in cases], indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> int:
    root = Path(__file__).resolve().parent / "benchmark"
    write_items(root, "train", TRAIN)
    write_items(root, "val", VAL)
    write_items(root, "test", TEST)
    print(f"wrote routing benchmark: train={len(TRAIN)} val={len(VAL)} test={len(TEST)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
