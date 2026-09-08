import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "evaluation" / "plan-0017"
spec = importlib.util.spec_from_file_location("visual_proof", ROOT / "validate_visual_proof.py")
visual_proof = importlib.util.module_from_spec(spec)
spec.loader.exec_module(visual_proof)


def merge(target, update):
    for key, value in update.items():
        if isinstance(value, dict) and isinstance(target.get(key), dict):
            merge(target[key], value)
        else:
            target[key] = value


class VisualProofCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = json.loads((ROOT / "proof-coverage-fixtures.json").read_text(encoding="utf-8"))

    def test_status_fixtures(self):
        for case in self.fixtures["cases"]:
            with self.subTest(case=case["id"]):
                records = []
                for name in case["records"]:
                    self.assertEqual(name, "base")
                    record = copy.deepcopy(self.fixtures["base_record"])
                    merge(record, case.get("overrides", {}))
                    records.append(record)
                result = visual_proof.evaluate_bundle({"required_relations": case["required_relations"], "records": records})
                self.assertEqual(case["expected"], result["status"], result)

    def test_extracts_only_fenced_proof_records(self):
        record = self.fixtures["base_record"]
        response = "Commentary outside evidence.\n```json\n" + json.dumps({"records": [record]}) + "\n```\nMore prose."
        self.assertEqual([record], visual_proof.extract_records(response))

    def test_unfenced_claim_is_not_extracted(self):
        self.assertEqual([], visual_proof.extract_records(json.dumps(self.fixtures["base_record"])))

    def test_frozen_known_proofs_are_fully_bound(self):
        bundle = json.loads((ROOT / "known-proof-records.json").read_text(encoding="utf-8"))
        result = visual_proof.evaluate_bundle(bundle)
        self.assertEqual([], result["issues"], result)
        self.assertEqual("fail", result["status"])


if __name__ == "__main__":
    unittest.main()
