import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "evaluation" / "plan-0017"
spec = importlib.util.spec_from_file_location("blind_analysis", ROOT / "analyze_blind_results.py")
blind_analysis = importlib.util.module_from_spec(spec)
spec.loader.exec_module(blind_analysis)


class BlindResultAnalysisTests(unittest.TestCase):
    def test_missing_user_rank_is_not_imputed(self):
        user = "## First\nBild 1: Rang 1\n"
        key = {"tasks": [{"id": "01", "image_1": "skill", "image_2": "no-skill"}]}
        manifest = {"briefs": [{"id": "01", "output_type": "test"}]}
        root = "| 01 First | 2 | 1 | review |"
        result = blind_analysis.analyse(user, key, manifest, root)
        self.assertEqual(0, result["user_complete_tasks"])
        self.assertEqual({"skill": 1}, result["records"][0]["user"]["condition_ranks"])

    def test_complete_pair_maps_conditions_and_agreement(self):
        user = "## First\nBild 1: Rang 2\nBild 2: Rang 1\n"
        key = {"tasks": [{"id": "01", "image_1": "no-skill", "image_2": "skill"}]}
        manifest = {"briefs": [{"id": "01", "output_type": "test"}]}
        root = "| 01 First | 2 | 1 | review |"
        result = blind_analysis.analyse(user, key, manifest, root)
        self.assertEqual(1, result["user_skill_wins"])
        self.assertEqual(1, result["root_skill_wins"])
        self.assertEqual(1, result["same_winner_count"])


if __name__ == "__main__":
    unittest.main()
