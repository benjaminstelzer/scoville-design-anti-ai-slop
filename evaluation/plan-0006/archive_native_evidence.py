"""Copy completed, explicitly selected evidence into a new hash-verified archive."""
import hashlib
import json
from pathlib import Path
import shutil

TEMP = Path('C:/Users/benja/AppData/Local/Temp')
BASE = Path('Z:/Projekts/AI/scoville-design-eval-local')
OUT = BASE / 'plan-0006-native-completion-20260904'
SOURCES = {
    'native': TEMP / 'design-plan6-sol-native-v1-20260904',
    'blind-original': TEMP / 'design-plan6-sol-neutral-8bf7',
    'blind-brand': TEMP / 'design-plan6-brand-neutral-d052',
    'blind-record-scope': TEMP / 'design-plan6-scope-neutral-e107',
    'fidelity': TEMP / 'design-plan6-sol-fidelity-20260904',
    'cli-failed-attempt': TEMP / 'design-plan6-sol-v1-20260904/cases/C4/baseline/attempt-1',
}
if OUT.exists() or not OUT.resolve().is_relative_to(BASE.resolve()):
    raise ValueError('Archive must be a new child of the explicit evaluation directory')
files = []
for name, source in SOURCES.items():
    for path in sorted(source.rglob('*')):
        if path.is_symlink(): raise ValueError('Unexpected symlink')
        if path.is_file():
            if path.name.lower() in ['auth.json', '.credentials.json', 'credentials.json', 'config.toml']:
                raise ValueError('Refusing authentication/configuration material')
            files.append((path, Path(name) / path.relative_to(source)))
OUT.mkdir()
manifest = []
for source, relative in files:
    before = source.read_bytes()
    target = OUT / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    after = target.read_bytes()
    if before != after or source.read_bytes() != before:
        raise ValueError('Evidence changed during archive: ' + str(source))
    manifest.append({'path': relative.as_posix(), 'bytes': len(after), 'sha256': hashlib.sha256(after).hexdigest().upper()})
receipt = {'archive': str(OUT), 'source_trees': {k:str(v) for k,v in SOURCES.items()}, 'files': manifest, 'file_count': len(manifest), 'authentication_files': 0, 'limit': 'Completed local development evidence, not qualification or publication.'}
(OUT / 'archive-manifest.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps({k:v for k,v in receipt.items() if k != 'files'}))
