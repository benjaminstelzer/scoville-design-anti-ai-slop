"""Freeze only representative cases affected by the five record-scope fixes."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
ROOT=Path('C:/Users/benja/AppData/Local/Temp/design-plan6-sol-native-v1-20260904')
BUILD=Path('C:/Users/benja/AppData/Local/Temp/design-plan6-record-scope-r1-20260904/candidate')
original=json.loads((ROOT/'freeze.json').read_text(encoding='utf-8'))
new=json.loads((REPO/'docs/evaluation/plan-0006-record-scope-build.json').read_text(encoding='utf-8'))
old=json.loads((REPO/'docs/evaluation/plan-0006-tested-build.json').read_text(encoding='utf-8'))
before={f['path']:f['sha256'] for f in old['runtime']['files']}
after={f['path']:f['sha256'] for f in new['runtime']['files']}
changed=sorted(k for k in after if after[k]!=before.get(k))
expected=sorted('references/'+name+'.md' for name in ['colour-and-reproduction','imagery-and-art-direction','brand-and-visual-systems','logo-and-identity-mark-design','packaging-graphics-and-sku-systems'])
if changed!=expected or before.keys()!=after.keys(): raise ValueError('Unexpected runtime change')
freeze_path=ROOT/'freeze-record-scope-r1.json'
if freeze_path.exists() or any((ROOT/label).exists() for label in ['N13','N14']): raise ValueError('Refusing overwrite')
frozen={k:v for k,v in original.items() if k not in ['sessions','prior_attempt','fallback_reason','frozen_at','version']}
frozen.update(version='P6-record-scope-r1/P6-sol-native-v1',frozen_at=datetime.now(timezone.utc).isoformat(),changed_files=changed,
    purpose='Representative affected-record regression after a confirmed R02 omission, not a search for a better visual score. Retain old candidate outcomes and unchanged baselines. C5A covers Packaging/Colour; C8 covers Brand/Mark/Imagery/Colour. No full holdout or unchanged-family rerun.',sessions={})
frozen['packages']['candidate']=new['runtime']
for label,source_label,case in [('N13','N08','C5A'),('N14','N12','C8')]:
    work=ROOT/label
    work.mkdir()
    shutil.copytree(BUILD,work/'skill')
    shutil.copytree(ROOT/source_label/'inputs',work/'inputs')
    shutil.copyfile(ROOT/source_label/'prompt.txt',work/'prompt.txt')
    frozen['sessions'][label]={'case':case,'arm':'candidate','prior_candidate':source_label,
        'inputs':{p.relative_to(work).as_posix():hashlib.sha256(p.read_bytes()).hexdigest().upper() for p in [work/'prompt.txt',*sorted((work/'inputs').rglob('*'))] if p.is_file()},
        'package':{p.relative_to(work/'skill').as_posix():hashlib.sha256(p.read_bytes()).hexdigest().upper() for p in sorted((work/'skill').rglob('*')) if p.is_file()}}
freeze_path.write_text(json.dumps(frozen,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'freeze':str(freeze_path),'changed':changed,'candidate_manifest':new['runtime']['manifest_sha256']}))
