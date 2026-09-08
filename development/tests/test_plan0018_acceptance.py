import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from PIL import Image

spec = importlib.util.spec_from_file_location('v18', Path(__file__).parents[1] / 'evaluation/plan-0018/validate_run.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class FinalEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root/'source.svg').write_text('<svg/>')
        Image.new('RGB', (20,20), 'white').save(self.root/'final.png')
        final = {'source':'source.svg','render':'final.png','source_hash':v.digest(self.root/'source.svg'),
                 'render_hash':v.digest(self.root/'final.png'),'viewport':[20,20]}
        binding = {k:final[k] for k in ('source_hash','render_hash','viewport')}
        metric = dict(binding, region='inner-panel', status='pass', support='supported', method='declared inset', observed=[2,2,2,2])
        (self.root/'metric.json').write_text(json.dumps(metric))
        record = {'relation':{'id':'r','objects':['label'],'region_or_anchor':'inner-panel','intent':'fit','target':2,'owner':'composition'},
                  'artifact':binding,
                  'visual':{'status':'pass','region':'inner-panel','view_receipt':dict(binding,region='inner-panel',path='final.png',sha256=final['render_hash'])},
                  'measurement':{'status':'pass','support':'supported','receipt':dict(binding,region='inner-panel',path='metric.json',sha256=v.digest(self.root/'metric.json'))},
                  'verdict':{'status':'pass'}}
        self.bundle = {'final':final, 'records':[record]}

    def check(self, bundle=None, expected=None):
        return v.validate_run(self.root, bundle or self.bundle, ['r'] if expected is None else expected)

    def test_clean_and_reasoned_exception(self):
        self.assertTrue(self.check()['qualified'])
        self.bundle['records'][0]['exception'] = dict(purpose='expressive route',gain='hierarchy',protected_floors='legible',counterstructure='shared family',cost='density',falsifier='collision',evidence='independently viewed final')
        self.assertTrue(self.check()['qualified'])

    def test_invalid_acceptance_paths(self):
        def mutate(kind, b):
            r=b['records'][0]
            if kind=='missing': b['records']=[]
            if kind=='duplicate': b['records'].append(copy.deepcopy(r))
            if kind=='hash': b['final'].pop('render_hash')
            if kind=='nonexistent': r['visual']['view_receipt']['path']='missing.png'
            if kind=='stale': r['artifact']['render_hash']='0'*64
            if kind=='region': r['measurement']['receipt']['region']='canvas'
            if kind=='unsupported': r['measurement']['support']='unsupported'
            if kind=='contradiction': r['visual']['status']='fail'
            if kind=='exception': r['exception']={'purpose':'looks good'}
            if kind=='third-pass-failure': b['renders']=4; r['visual']['status']='fail'; r['measurement']['status']='fail'; r['verdict']['status']='fail'
            if kind=='neighbour': b['required_relations']=[] # executor cannot omit evaluator relation
            if kind=='wrong-file-version': (self.root/'metric.json').write_text('{}')
        for kind in ['missing','duplicate','hash','nonexistent','stale','region','unsupported','contradiction','exception','third-pass-failure','neighbour','wrong-file-version']:
            with self.subTest(kind=kind):
                b=copy.deepcopy(self.bundle); mutate(kind,b)
                self.assertFalse(self.check(b, ['r','neighbour'] if kind=='neighbour' else ['r'])['qualified'])

    def test_empty_expected_not_a_pass(self):
        self.assertFalse(self.check(expected=[])['qualified'])

    def test_nonapplicable_optional_concern_does_not_invalidate_required_pass(self):
        extra=copy.deepcopy(self.bundle['records'][0]);extra['relation']['id']='print-trim'
        extra['visual']['status']=extra['measurement']['status']=extra['verdict']['status']='not-applicable'
        extra['verdict']['reason']='Digital card, no print delivery requested.'
        self.bundle['records'].append(extra)
        self.assertTrue(self.check()['qualified'])
        extra['verdict'].pop('reason')
        self.assertFalse(self.check()['qualified'])

    def test_actual_crop_binding(self):
        Image.open(self.root/'final.png').crop((1,1,10,10)).save(self.root/'crop.png')
        receipt=self.bundle['records'][0]['visual']['view_receipt']
        receipt.update(path='crop.png',sha256=v.digest(self.root/'crop.png'),crop_box=[1,1,10,10])
        self.assertTrue(self.check()['qualified'])
        Image.new('RGB',(9,9),'black').save(self.root/'crop.png')
        receipt['sha256']=v.digest(self.root/'crop.png')
        self.assertFalse(self.check()['qualified'])

if __name__=='__main__': unittest.main()
