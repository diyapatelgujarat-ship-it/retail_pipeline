import unittest
from pipeline.schema import StoreLocation, TransactionRecord
from pipeline.validator import validate_and_parse_record
from pipeline.transformer import filter_active_transactions

class TestRetailPipeline(unittest.TestCase):
    
    def setUp(self):
        self.stores = {"BR_01": StoreLocation("BR_01", "North", 0.10)}

    def test_schema_and_net_revenue(self):
        store = self.stores["BR_01"]
        record = TransactionRecord("T001", "BR_01", "2026-06-01", "GOLD", 2, 200.0, store)
        self.assertEqual(record.calculate_net_revenue(), 180.0)

    def test_validator_rejects_malformed_data(self):
        bad_record = {"transaction_id": "T999", "branch_id": "BR_99", "date": "2026-06-01", "customer_tier": "GOLD", "item_count": 1, "revenue": 100.0}
        with self.assertRaises(ValueError):
            validate_and_parse_record(bad_record, self.stores)

    def test_functional_filter(self):
        r1 = TransactionRecord("T1", "BR_01", "2026-06-01", "STANDARD", 1, 50.0)
        r2 = TransactionRecord("T2", "BR_01", "2026-06-01", "STANDARD", 1, 0.0)
        filtered = filter_active_transactions([r1, r2], min_revenue=0.0)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].transaction_id, "T1")

if __name__ == "__main__":
    unittest.main()
    