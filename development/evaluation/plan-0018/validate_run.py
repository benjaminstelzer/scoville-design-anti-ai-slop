"""Evaluator-owned receipt integrity around the unchanged PLAN-0017 proof matrix.

This checks files and claims, never whether an image was actually viewed or
whether its design judgment is right. Those require the independent review.
Expected relations are an evaluator argument, not a generator inventory.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import re

spec = importlib.util.spec_from_file_location('previous_matrix', Path(__file__).parents[1] / 'plan-0017/validate_visual_proof.py')
matrix = importlib.util.module_from_spec(spec)
spec.loader.exec_module(matrix)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate_run(root, bundle, expected):
    root = Path(root).resolve()
    issues = []
    def issue(code, rid='run'):
        issues.append({'relation': rid, 'code': code})
    def file(name, claimed, rid):
        if not isinstance(name, str) or not name:
            issue('missing-file', rid); return None
        path = (root / name).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            issue('nonexistent-or-outside-file', rid); return None
        if not isinstance(claimed, str) or not re.fullmatch('[0-9a-f]{64}', claimed):
            issue('missing-or-invalid-hash', rid); return None
        if digest(path) != claimed:
            issue('file-hash-mismatch', rid); return None
        return path

    if not expected or len(set(expected)) != len(expected):
        issue('empty-or-duplicate-expected')
    records = bundle.get('records', [])
    if not isinstance(records, list):
        records = []; issue('invalid-records')
    ids = [r.get('relation', {}).get('id') for r in records]
    if not ids or len(ids) != len(set(ids)):
        issue('empty-or-duplicate-inventory')
    for rid in expected:
        if ids.count(rid) != 1:
            issue('missing-critical-relation', rid)
    final = bundle.get('final', {})
    source = file(final.get('source'), final.get('source_hash'), 'final-source')
    render = file(final.get('render'), final.get('render_hash'), 'final-render')
    viewport = final.get('viewport')
    if not isinstance(viewport, list) or len(viewport) != 2 or not all(isinstance(v, int) and v > 0 for v in viewport):
        issue('invalid-viewport')
    elif render:
        from PIL import Image
        try:
            with Image.open(render) as img:
                if list(img.size) != viewport:
                    issue('render-viewport-mismatch')
        except OSError:
            issue('invalid-render')
    keys = ('source_hash', 'render_hash', 'viewport')
    for record in records:
        relation = record.get('relation', {})
        rid = relation.get('id', '<missing>')
        artifact = record.get('artifact', {})
        if any(artifact.get(k) != final.get(k) for k in keys):
            issue('not-final-artifact', rid)
        for lane, receipt_key in [('visual', 'view_receipt'), ('measurement', 'receipt')]:
            claim = record.get(lane, {})
            if claim.get('status') not in ('pass', 'fail'):
                continue
            receipt = claim.get(receipt_key, {})
            if any(receipt.get(k) != final.get(k) for k in keys):
                issue('stale-receipt', rid)
            if receipt.get('region') != relation.get('region_or_anchor'):
                issue('receipt-wrong-region', rid)
            path = file(receipt.get('path'), receipt.get('sha256'), rid)
            if not path:
                continue
            if lane == 'visual' and render:
                if path != render:
                    from PIL import Image
                    box = receipt.get('crop_box')
                    try:
                        if not isinstance(box, list) or len(box) != 4:
                            raise ValueError()
                        parent = Image.open(render).convert('RGBA')
                        crop = Image.open(path).convert('RGBA')
                        if not (0 <= box[0] < box[2] <= parent.width and 0 <= box[1] < box[3] <= parent.height):
                            raise ValueError()
                        target = parent.crop(box)
                        if crop.size != target.size or crop.tobytes() != target.tobytes():
                            raise ValueError()
                    except (OSError, ValueError, TypeError):
                        issue('crop-not-from-final', rid)
            elif lane == 'measurement':
                try:
                    metric = json.loads(path.read_text(encoding='utf-8'))
                    if any(metric.get(k) != final.get(k) for k in keys) or metric.get('region') != relation.get('region_or_anchor'):
                        issue('metric-file-unbound', rid)
                    if metric.get('status') != claim.get('status') or metric.get('support') != claim.get('support'):
                        issue('metric-file-contradiction', rid)
                    if 'observed' not in metric or not metric.get('method'):
                        issue('metric-file-empty', rid)
                    if 'provenance' in metric:
                        provenance = metric['provenance']
                        file(provenance.get('path'), provenance.get('sha256'), rid)
                except (ValueError, OSError):
                    issue('invalid-metric-file', rid)
        exception = record.get('exception')
        if exception is not None:
            fields = ('purpose', 'gain', 'protected_floors', 'counterstructure', 'cost', 'falsifier', 'evidence')
            if not isinstance(exception, dict) or not all(exception.get(k) for k in fields):
                issue('invalid-exception', rid)
        if record.get('verdict', {}).get('status') == 'not-applicable' and rid in expected:
            issue('critical-relation-dismissed', rid)
        elif record.get('verdict', {}).get('status') == 'not-applicable' and not record.get('verdict', {}).get('reason'):
            issue('unjustified-nonapplicability', rid)

    result = matrix.evaluate_bundle({'required_relations': list(expected), 'records': records})
    issues.extend(result['issues'])
    status = result['status']
    if not issues and expected and all(result['effective'].get(rid) == 'pass' for rid in expected) and all(value in ('pass', 'not-applicable') for value in result['effective'].values()):
        status = 'pass'
    if issues and status == 'pass':
        status = 'unverified'
    return {'status': status, 'qualified': status == 'pass' and not issues,
            'effective': result['effective'], 'issues': issues,
            'limit': 'Integrity only; independent actual image inspection required.'}
