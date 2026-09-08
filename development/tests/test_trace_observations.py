import base64
import hashlib
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('trace_observations', Path(__file__).parents[1] / 'evaluation/plan-0017/trace_observations.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def event(kind, **payload):
    return {'type': 'response_item', 'payload': {'type': kind, **payload}}


class TraceObservations(unittest.TestCase):
    def test_actual_image_bytes_and_missing_forwarded_image(self):
        data = b'fixture payload, not a rendered image claim'
        es = [event('custom_tool_call', call_id='a', input='await tools.view_image({path:"C:/case/a.png"});'),
              event('custom_tool_call_output', call_id='a', output=[{'type':'input_image', 'image_url':'data:image/png;base64,'+base64.b64encode(data).decode()}]),
              event('custom_tool_call', call_id='b', input='await tools.view_image({path:"C:/case/unseen.png"});'),
              event('custom_tool_call_output', call_id='b', output='file produced, no image forwarded')]
        got = module.observe(es)['received_image_calls']
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0]['received_image_sha256'], [hashlib.sha256(data).hexdigest()])
        self.assertEqual(got[0]['literal_requested_paths'], ['C:/case/a.png'])

    def test_dynamic_path_or_incomplete_batch_remains_unverified(self):
        es = [event('custom_tool_call', call_id='a', input='await tools.view_image({path: candidate});'),
              event('custom_tool_call_output', call_id='a', output=[{'type':'input_image', 'image_url':'https://example.invalid/image.png'}])]
        got = module.observe(es)['received_image_calls'][0]
        self.assertEqual(got['path_pairing'], 'unverified')
        self.assertEqual(got['received_image_sha256'], [None])

    def test_reference_is_not_a_note_patch(self):
        es = [event('custom_tool_call', call_id='a', input='await tools.exec_command({cmd:"Get-Content notes.md"});')]
        self.assertIsNone(module.observe(es)['first_note_patch_candidate_index'])

    def test_literal_patch_order_is_a_candidate_only(self):
        es = [event('custom_tool_call', call_id='n', input='await tools.exec_command({cmd:"node inspect.cjs"});'),
              event('custom_tool_call', call_id='p', input='await tools.apply_patch("*** Begin Patch\\n*** Add File: C:/case/review-notes.md\\n+Map\\n*** End Patch");')]
        got = module.observe(es)
        self.assertEqual(got['first_node_execution_candidate_index'], 0)
        self.assertEqual(got['first_note_patch_candidate_index'], 1)
        self.assertIn('not proof', got['ceiling'])


if __name__ == '__main__':
    unittest.main()
