"""Prepare anonymous artifacts only; assignment stays outside reviewer tree."""
import hashlib
import json
from pathlib import Path
import re
import secrets
import shutil

HERE = Path(__file__).resolve().parent
ROOT = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-sol-native-v1-20260904')
BLIND = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-sol-neutral-8bf7')
if BLIND.exists(): raise ValueError('Refusing to overwrite blind bundle')
BLIND.mkdir()
protocol = json.loads((HERE / 'protocol-v1.json').read_text(encoding='utf-8'))
case_map = {c['id']:c for c in protocol['cases']}
assignment = {}

def anonymous_copy(source, destination):
    destination.mkdir(parents=True, exist_ok=False)
    for item in source.iterdir():
        target = destination / item.name
        if item.is_dir(): anonymous_copy(item, target)
        elif item.suffix == '.json':
            payload = json.loads(item.read_text(encoding='utf-8'))
            if isinstance(payload, dict): payload.pop('source', None)
            target.write_text(json.dumps(payload, indent=2)+'\n', encoding='utf-8')
        else: shutil.copyfile(item, target)

def task_notes(label, case):
    notes = json.loads((ROOT / label / 'capture-1/answer.json').read_text(encoding='utf-8'))['notes']
    if case == 'C7':
        notes = re.split(r'\n\nRead disclosure|\n\nFiles read wholly', notes)[0]
    elif case == 'C6':
        notes = re.split(r' Files read (?:wholly|completely)', notes)[0]
    elif case == 'C5B':
        notes = re.split(r'\nFiles actually read| Loaded the supplied scoville-design-anti-ai-slop package only', notes)[0]
    return notes

for case, labels in [('C4',['N01','N02']),('C5A',['N07','N08']),('C5B',['N09','N10']),('C6',['N03','N04']),('C7',['N05','N06'])]:
    task_dir = BLIND / case
    task_dir.mkdir()
    (task_dir / 'task.txt').write_text(case_map[case]['prompt']+'\n', encoding='utf-8')
    anonymous_copy(ROOT / labels[0] / 'inputs', task_dir / 'inputs')
    secrets.SystemRandom().shuffle(labels)
    assignment[case] = {}
    for arm, label in zip(['A','B'],labels):
        work, out = ROOT / label, task_dir / arm
        out.mkdir()
        artifact = 'artifact-v2.html' if label == 'N02' else 'artifact.html'
        proofs = 'proof-2' if label == 'N02' else 'proof-1'
        assignment[case][arm] = {'native_label':label, 'source_version':artifact, 'proofs':proofs}
        if case != 'C7':
            shutil.copyfile(work / artifact, out / 'artifact.html')
            assignment[case][arm]['artifact_sha256'] = hashlib.sha256((out/'artifact.html').read_bytes()).hexdigest().upper()
        if case not in ['C6','C7']:
            anonymous_copy(work / proofs, out / 'proof')
        if case in ['C5B','C6','C7']:
            (out / 'task-response.txt').write_text(task_notes(label,case)+'\n',encoding='utf-8')
    (task_dir/'evidence-scope.txt').write_text('Only the task, input material and actual returned source/proofs are supplied. Author/model/package identities, generation-read disclosures and prior review findings are withheld. The host rendered any supplied output screenshots in Chromium. Source-only and critique cases intentionally have no new rendered output. Do not infer performance beyond actual evidence.\n',encoding='utf-8')
(ROOT / 'blind-assignment-v1.json').write_text(json.dumps({'bundle':str(BLIND),'assignment':assignment},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'bundle':str(BLIND),'cases':list(assignment)}))
