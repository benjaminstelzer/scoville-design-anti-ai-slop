"""Freeze anonymous actual initial artifacts for the two R02 retests."""
import hashlib
import json
from pathlib import Path
import secrets
import shutil

ROOT = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-sol-native-v1-20260904')
OUT = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-scope-neutral-e107')
if OUT.exists(): raise ValueError('Refusing to overwrite review evidence')
OUT.mkdir()
protocol = json.loads((Path(__file__).parent / 'protocol-v1.json').read_text(encoding='utf-8'))
cases = {c['id']: c for c in protocol['cases']}
brand = json.loads((Path(__file__).parent / 'protocol-brand-v1.json').read_text(encoding='utf-8'))

def copy_anonymous(source, destination):
    destination.mkdir()
    for item in source.iterdir():
        target = destination / item.name
        if item.is_dir(): copy_anonymous(item, target)
        elif item.suffix == '.json':
            data = json.loads(item.read_text(encoding='utf-8'))
            if isinstance(data, dict): data.pop('source', None)
            target.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
        else: shutil.copyfile(item, target)

assignment = {}
for case, labels in [('C5A', ['N07', 'N13']), ('C8', ['N11', 'N14'])]:
    task = OUT / case
    task.mkdir()
    # Extract raw task content from the already neutral task, never worker instructions.
    prior = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-sol-neutral-8bf7/C5A/task.txt') if case == 'C5A' else Path('C:/Users/benja/AppData/Local/Temp/design-plan6-brand-neutral-d052/task.txt')
    shutil.copyfile(prior, task / 'task.txt')
    copy_anonymous(ROOT / labels[0] / 'inputs', task / 'inputs')
    secrets.SystemRandom().shuffle(labels)
    assignment[case] = {}
    for arm, label in zip(['A', 'B'], labels):
        dest = task / arm
        dest.mkdir()
        shutil.copyfile(ROOT / label / 'artifact.html', dest / 'artifact.html')
        copy_anonymous(ROOT / label / 'proof-1', dest / 'proof')
        assignment[case][arm] = {'label': label, 'artifact_sha256': hashlib.sha256((dest / 'artifact.html').read_bytes()).hexdigest().upper()}
    (task / 'evidence-scope.txt').write_text('Actual initial source proposals and host renders. Identities, packages, read disclosures and previous findings are withheld. Compare only the supplied task and evidence; do not infer general quality or production approval.\n', encoding='utf-8')
(ROOT / 'record-scope-blind-assignment.json').write_text(json.dumps({'bundle': str(OUT), 'assignment': assignment}, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'bundle': str(OUT), 'cases': list(assignment)}))
