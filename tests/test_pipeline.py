import io
import unittest
from contextlib import redirect_stdout
from datetime import date

from pipeline.schema import TransactionRecord
from pipeline.validator import validate_records
from pipeline.transformer import get_active
from pipeline.reporter import print_report

GOOD_ROW = {
    "branch_id": "BR01",
    "transaction_date": "2026-01-05",
    "customer_tier": "gold",
    "item_count": "4",
    "revenue": "210.50",
}


class TestPipeline(unittest.TestCase):
    def test_good_row_is_accepted(self):
        clean, rejected = validate_records([GOOD_ROW])
        self.assertEqual(len(clean), 1)
        self.assertEqual(clean[0].customer_tier, "Gold")

    def test_short_row_is_rejected_not_crashed(self):
        # csv.DictReader fills missing columns with None
        row = dict(GOOD_ROW, customer_tier=None, item_count=None, revenue=None)
        clean, rejected = validate_records([row])
        self.assertEqual(rejected, ["row 2: invalid customer tier"])

    def test_active_filter_drops_zero_revenue(self):
        records = [
            TransactionRecord("BR01", date(2026, 1, 5), "Gold", 4, 200.0),
            TransactionRecord("BR02", date(2026, 1, 6), "Silver", 0, 0.0),
        ]
        self.assertEqual(len(get_active(records)), 1)

    def test_report_shows_top_branch(self):
        records = [
            TransactionRecord("BR01", date(2026, 1, 5), "Gold", 4, 100.0),
            TransactionRecord("BR02", date(2026, 1, 6), "Silver", 2, 300.0),
        ]
        out = io.StringIO()
        with redirect_stdout(out):
            print_report(records, [])
        self.assertIn("Top branch:         BR02 ($300.00)", out.getvalue())


if __name__ == "__main__":
    unittest.main()
