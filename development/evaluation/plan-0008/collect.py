"""Collect new receipts and check preservation without altering old evidence."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
DEV=HERE.parents[1]
REPO=DEV.parent
OUT=REPO.parent/'output'
sys.path.insert(0,str(DEV/'scripts'))
from build_package_manifest import build

def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest().upper()
new=OUT/'design-plan8-supplements'
old=read(DEV/'docs/evaluation/plan-0007-trial-receipts.json')
verified=[]
for trial in old['trials']:
 p=Path(trial['receipt_path'])
 assert digest(p)==trial['receipt_sha256']
 assert digest(p.parent/'answer.json')==trial['answer_sha256']
 assert digest(p.parent/'prompt.txt')==trial['prompt_sha256']
 for name,sha in trial['artifacts'].items(): assert digest(p.parent/name)==sha
 verified.append({'case':trial['case'],'arm':trial['arm'],'artifacts':len(trial['artifacts'])})
frozen=read(OUT/'design-plan7-trials/freeze.json')
for rel,sha in frozen['runtime_baseline'].items(): assert digest(OUT/'design-plan7-baseline-runtime'/rel)==sha
for rel,sha in frozen['source_baseline'].items(): assert digest(OUT/'design-plan7-trials/source-baseline'/rel)==sha
assert digest(DEV/'evaluation/plan-0007/protocol.json')==frozen['protocol_sha256']
assert digest(DEV/'evaluation/plan-0007/run_cases.py')==frozen['runner_sha256']
plan6=DEV/'docs/plans/0006-implement-fable-design-improvements.md'
head=subprocess.check_output(['git','show','HEAD:'+plan6.relative_to(REPO).as_posix()],cwd=REPO).decode('utf-8')
def w4(s): return s.split('### W-004',1)[1].split('### W-005',1)[0]
assert w4(head)==w4(plan6.read_text(encoding='utf-8'))

supplements=read(OUT/'playwright/design-plan8/supplements-receipt.json')
for artifact in supplements['artifacts']:
 assert digest(Path(artifact['path'])).lower()==artifact['sha256']
 if 'maps' in artifact:
  for m in artifact['maps']:
   features={f['id']:f['attrs'] for f in m['features']}
   assert features['brook']['d']=='M 10 25 C 30 5, 55 45, 90 25'
   assert features['orchard']['points']=='12,52 45,52 45,85 12,85'
   assert features['meadow']['points']=='61,53 66,53 66,90 61,90'
   assert (features['depot']['cx'],features['depot']['cy'])==('80','78')
   assert all('transform' not in f for f in features.values())
 if 'actualFonts' in artifact:
  assert all(font['familyName']=='Georgia' for node in artifact['actualFonts'] for font in node['fonts'])
motion=read(OUT/'playwright/design-plan8/motion-receipt.json')
assert digest(Path(motion['derivative']['source'])).lower()==motion['derivative']['source_sha256']
assert digest(Path(motion['derivative']['destination'])).lower()==motion['derivative']['sha256']
build_receipt=read(DEV/'docs/evaluation/plan-0008-final-build.json')
assert build(REPO/'scoville-design-anti-ai-slop')==build_receipt['source']
assert build(OUT/'design-plan8-final-runtime')==build_receipt['runtime']
trials=[read(new/case/arm/'receipt.json') for case,arm in [('PG-02S','baseline'),('PG-02S','candidate'),('PG-08S','candidate')]]
for t in trials:
 assert t['exit_code']==0
 assert 'capture_error' not in t
 if t['arm']=='candidate':
  for rel,sha in t['source_hashes'].items(): assert digest(REPO/'scoville-design-anti-ai-slop'/rel)==sha
record={'scope':'Three new frozen model calls, six rendered artifacts and six Motion state observations; no improvement, audience, GIS or automatic routing claim.',
 'freeze_sha256':digest(new/'freeze.json'),'trials':trials,
 'render_receipt':{'path':str(OUT/'playwright/design-plan8/supplements-receipt.json'),'sha256':digest(OUT/'playwright/design-plan8/supplements-receipt.json')},
 'motion_receipt':{'path':str(OUT/'playwright/design-plan8/motion-receipt.json'),'sha256':digest(OUT/'playwright/design-plan8/motion-receipt.json')},
 'preserved_plan7_trials':verified,'original_baseline_and_source_freeze_unchanged':True,'original_protocol_and_runner_unchanged':True,'plan6_w004_unchanged':True,
 'exact_supplement_geometry_and_georgia_verified':True,'candidate_exposure_matches_current_source':True,'source_and_runtime_match_build_receipt':True}
dest=DEV/'docs/evaluation/plan-0008-receipts.json'
with dest.open('x',encoding='utf-8',newline='\n') as f: json.dump(record,f,indent=2);f.write('\n')
print(json.dumps({'new_trials':len(trials),'preserved_original_trials':len(verified),'preserved_original_artifacts':sum(x['artifacts'] for x in verified),'source_runtime_manifest':build_receipt['runtime']['manifest_sha256']}))
