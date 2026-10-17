import unittest
from datetime import date

from pipeline.schema import TransactionRecord
from pipeline.validator import validate_records
from pipeline.transformer import get_active

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

    def test_negative_revenue_is_rejected(self):
        clean, rejected = validate_records([dict(GOOD_ROW, revenue="-50")])
        self.assertEqual(len(clean), 0)
        self.assertEqual(rejected, ["negative item count or revenue"])

    def test_missing_branch_is_rejected(self):
        clean, rejected = validate_records([dict(GOOD_ROW, branch_id="")])
        self.assertEqual(rejected, ["missing branch ID"])

    def test_active_filter_drops_zero_revenue(self):
        records = [
            TransactionRecord("BR01", date(2026, 1, 5), "Gold", 4, 200.0),
            TransactionRecord("BR02", date(2026, 1, 6), "Silver", 0, 0.0),
        ]
        self.assertEqual(len(get_active(records)), 1) 

if __name__ == "__main__":
    unittest.main()