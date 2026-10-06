import json
import unittest
from scripts.validate_fixture import ROOT, load_rows, summarize

class FixtureTests(unittest.TestCase):
    def setUp(self):
        self.rows = load_rows()
        self.result = summarize(self.rows)

    def test_expected(self):
        expected = json.loads((ROOT / "data/expected-summary.json").read_text())
        self.assertEqual(self.result, expected)

    def test_count(self):
        self.assertEqual(self.result["total_data_rows"], 8)

    def test_status(self):
        self.assertEqual(sum(self.result["booking_status_counts"].values()), 8)
        self.assertEqual(self.result["successful_booking_count"], 5)

    def test_empty(self):
        with self.assertRaises(ValueError):
            summarize([])

    def test_non_numeric(self):
        self.rows[0]["Booking Value"] = "invalid"
        with self.assertRaises(ValueError):
            summarize(self.rows)

    def test_non_finite(self):
        self.rows[0]["Booking Value"] = "NaN"
        with self.assertRaises(ValueError):
            summarize(self.rows)

    def test_duplicate(self):
        self.rows[1]["Booking ID"] = self.rows[0]["Booking ID"]
        with self.assertRaises(ValueError):
            summarize(self.rows)

if __name__ == "__main__":
    unittest.main()
