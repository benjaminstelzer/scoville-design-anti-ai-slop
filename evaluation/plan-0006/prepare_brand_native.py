"""Freeze only the uncovered Brand extension; never rewrite the original freeze."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil

HERE = Path(__file__).resolve().parent
ROOT = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-sol-native-v1-20260904')
original = json.loads((ROOT / 'freeze.json').read_text(encoding='utf-8'))
protocol = json.loads((HERE / 'protocol-brand-v1.json').read_text(encoding='utf-8'))
freeze_path = ROOT / 'freeze-brand-v1.json'
if freeze_path.exists() or any((ROOT / label).exists() for label in ['N11','N12']):
    raise ValueError('Refusing to overwrite extension')
frozen = {k:v for k,v in original.items() if k not in ['sessions', 'prior_attempt', 'fallback_reason', 'frozen_at', 'version']}
frozen.update(version=protocol['version'], frozen_at=datetime.now(timezone.utc).isoformat(), protocol_sha256=hashlib.sha256((HERE / 'protocol-brand-v1.json').read_bytes()).hexdigest().upper(), sessions={})
for label, package, arm in [('N11','N01','baseline'),('N12','N02','candidate')]:
    work = ROOT / label
    work.mkdir()
    shutil.copytree(ROOT / package / 'skill', work / 'skill')
    (work / 'inputs').mkdir()
    shutil.copyfile(HERE / 'inputs/facts.txt', work / 'inputs/facts.txt')
    prompt = 'Use the installed-form design package in skill/SKILL.md for this task, reading only the actual linked modules you need. Work only with files inside this workspace.\n\n' + protocol['case']['prompt'] + '\n\nYou have read-only file tools. Return proposed source for the authorised host to materialise, not a claim of already edited files. Output one JSON object only, with files (array of {path, content}, a single artifact.html for source tasks; empty for critique) and notes (a string containing the concise task response and limits). No code fences. Do not render by assertion. The host will return actual rendered evidence where available.\n'
    (work / 'prompt.txt').write_text(prompt, encoding='utf-8')
    frozen['sessions'][label] = {'case':'C8','arm':arm,
        'inputs': {p.relative_to(work).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest().upper() for p in [work/'prompt.txt',work/'inputs/facts.txt']},
        'package': {p.relative_to(work/'skill').as_posix(): hashlib.sha256(p.read_bytes()).hexdigest().upper() for p in sorted((work/'skill').rglob('*')) if p.is_file()}}
freeze_path.write_text(json.dumps(frozen,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'freeze':str(freeze_path),'sessions':list(frozen['sessions'])}))
