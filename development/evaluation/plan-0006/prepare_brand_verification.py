"""Append anonymised corrected evidence without changing the blind originals."""
import json
from pathlib import Path
import shutil

ROOT = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-sol-native-v1-20260904')
mapping = json.loads((ROOT / 'brand-blind-assignment.json').read_text(encoding='utf-8'))
bundle = Path(mapping['bundle'])
for arm in ['A', 'B']:
    source = ROOT / mapping[arm]
    dest = bundle / arm / 'v3'
    if dest.exists(): raise ValueError('Refusing to overwrite v3 evidence')
    dest.mkdir()
    shutil.copyfile(source / 'artifact-v3.html', dest / 'artifact.html')
    for old, new in [('proof-3', 'proof'), ('proof-palette-3', 'palette')]:
        target = dest / new
        target.mkdir()
        for item in (source / old).iterdir():
            if item.suffix == '.json':
                data = json.loads(item.read_text(encoding='utf-8'))
                data.pop('source', None)
                (target / item.name).write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
            else: shutil.copyfile(item, target / item.name)
shutil.copyfile(ROOT / 'reviews/brand-r1/review.md', bundle / 'prior-review.md')
print(json.dumps({'bundle': str(bundle), 'appended': ['A/v3', 'B/v3', 'prior-review.md']}))
