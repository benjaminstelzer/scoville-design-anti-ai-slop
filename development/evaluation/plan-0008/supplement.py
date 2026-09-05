"""Separately frozen coverage supplements; original trials are never modified."""
import argparse
import copy
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('original_runner',HERE.parent/'plan-0007/run_cases.py')
runner=importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
original_out=runner.OUT
runner.OUT=original_out.parent/'design-plan8-supplements'
paragraph='A repaired object keeps more than its material. It carries the marks of ordinary use, the decisions of its makers, and the patience of the people who kept it working. The archive records these traces without pretending that every object tells the same story.'
cases=[{
 'id':'PG-02S','tier':'paired','modules':['typography-and-typesetting'],
 'reason':'PG-02 exercised family substitution only, not the separately required coupled measure/leading comparison.',
 'task':f'''Create main.html as a typesetting comparison using actual installed Georgia, 18px regular throughout. Show three separately labelled specimens, each containing EXACTLY TWO paragraphs, each paragraph exactly: {paragraph}
Specimen original: text measure 648px and line-height 29px. Specimen narrower: text measure 432px, still 18px/29px. Specimen selected: choose a suitable line-height at 432px and the unchanged 18px size after considering the narrower comparison. Keeping 29px is allowed if reasoned. Keep all three specimens visible in the document; specify their measured CSS settings and explain the line-return/leading decision without claiming to have rendered or user-tested it. Use data-specimen="original", "narrower", "selected" on the text containers; labels and explanations must be outside those containers. No tracking or font-family substitution. control.html is a legitimate single-paragraph specimen using the same exact paragraph, Georgia 18px/29px at 648px, with a reason to retain this setting for a wide reading panel. These numerical values are supplied fixture conditions, not universal typography rules.''',
 'checks':['two exact paragraphs per main specimen','same actual font and 18px size','648 to 432 measure with constant leading comparison','explicit final leading decision','original visible alongside alternatives','legitimate unchanged wide control']
},{
 'id':'PG-08S','tier':'candidate','modules':['cartography-and-spatial-data'],
 'reason':'PG-08 covered point labels only; audit row 09 also requires practical line and area distinctions.',
 'task':'''Create main.html with two maps at exactly 600px and 300px square, same full extent x=0..100 rightwards and y=0..100 downwards (fictional drawing coordinates, no CRS or jurisdiction). The supplied geometry is authoritative for this fictional exercise and must be identical in both maps: Willow Brook is line M 10 25 C 30 5, 55 45, 90 25; Orchard is polygon points 12,52 45,52 45,85 12,85; Long Meadow is narrow polygon points 61,53 66,53 66,90 61,90; Depot is point 80,78. Use SVG viewBox="0 0 100 100" and unchanged source geometry with data-feature="brook", "orchard", "meadow", "depot" respectively. All four exact names are mandatory and must stay visibly associated at both sizes. Choose and explain distinct line, area and point label strategies; compare a line-following or aligned label against a clearly associated horizontal alternative, and interior area placement against a callout when the narrow polygon cannot fit a label. Preserve features; label paths or callout lines may differ from source geometry but must be distinct, not replace or distort it. Supply an accessible exact geometry table or description. control.html is a legitimate name/type lookup table with all four names, types and exact source coordinates, for the different question "which feature is a line, area or point?" Do not invent spatial values, projection, terrain, official authority, audience tests or GIS certification. Explain the reason for the different placement at each size without claiming prior render inspection.''',
 'checks':['identical authoritative geometry at two sizes','line area point strategies','readable line alternative and narrow-area callout','mandatory name association','accessible exact geometry','non-map control','no geographic authority claim']
}]

def freeze():
 original=json.loads((original_out/'freeze.json').read_text(encoding='utf-8'))
 frozen=copy.deepcopy(original)
 frozen.update(version='PG-8-supplement-v1',frozen_at=runner.now(),cases=cases,
  prompts={c['id']:original['protocol']['artifact_contract']+'\n\nUSER TASK\n'+c['task'] for c in cases},
  revision_of=str(original_out/'freeze.json'),original_freeze_sha256=runner.digest(original_out/'freeze.json'),
  supplement_runner_sha256=runner.digest(Path(__file__)),source_before_supplement=runner.manifest(runner.SOURCE))
 runner.OUT.mkdir(exist_ok=False)
 runner.save(runner.OUT/'freeze.json',frozen)
 runner.save(runner.OUT/'schema.json',runner.SCHEMA)
 runner.save(HERE/'freeze-receipt.json',{'path':str(runner.OUT/'freeze.json'),'sha256':runner.digest(runner.OUT/'freeze.json'),'frozen_at':frozen['frozen_at'],'cases':cases,'model':original['protocol']['model'],'effort':original['protocol']['effort']})
 print('Frozen '+str(runner.OUT))

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('action',choices=['freeze','run']);parser.add_argument('--case');parser.add_argument('--arm',choices=['baseline','candidate']);args=parser.parse_args()
 if args.action=='freeze': freeze()
 else:
  frozen=json.loads((runner.OUT/'freeze.json').read_text(encoding='utf-8'))
  assert runner.digest(Path(__file__))==frozen['supplement_runner_sha256']
  runner.run(args.case,args.arm)
