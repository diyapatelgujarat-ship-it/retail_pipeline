import sys
from pipeline.schema import StoreLocation
from pipeline.validator import validate_and_parse_record
from pipeline.transformer import filter_active_transactions, apply_discount_to_tier
from pipeline.reporter import PipelineReporter

def run_pipeline():
    stores = {
        "BR_01": StoreLocation("BR_01", "North", 0.08),
        "BR_02": StoreLocation("BR_02", "South", 0.05),
        "BR_03": StoreLocation("BR_03", "East", 0.06),
    }

    raw_data = [
        {"transaction_id": "T101", "branch_id": "BR_01", "date": "2026-06-01", "customer_tier": "GOLD", "item_count": 3, "revenue": 450.50},
        {"transaction_id": "T102", "branch_id": "BR_02", "date": "2026-06-01", "customer_tier": "STANDARD", "item_count": 1, "revenue": 89.99},
        {"transaction_id": "T103", "branch_id": "BR_INVALID", "date": "2026-06-02", "customer_tier": "SILVER", "item_count": 2, "revenue": 150.00},
        {"transaction_id": "T104", "branch_id": "BR_03", "date": "INVALID_DATE", "customer_tier": "PLATINUM", "item_count": 5, "revenue": 1200.00},
        {"transaction_id": "T105", "branch_id": "BR_01", "date": "2026-06-02", "customer_tier": "GOLD", "item_count": 4, "revenue": -50.00},
        {"transaction_id": "T106", "branch_id": "BR_02", "date": "2026-06-03", "customer_tier": "PLATINUM", "item_count": 2, "revenue": 340.00},
    ]

    print(f"[*] Starting ingestion of {len(raw_data)} raw operational records...")

    clean_records = []
    for raw in raw_data:
        try:
            valid_record = validate_and_parse_record(raw, stores)
            clean_records.append(valid_record)
        except ValueError as err:
            print(f"[!] Validation Warning: {err}")

    transformed_records = apply_discount_to_tier(clean_records, "PLATINUM", 0.10)
    final_records = filter_active_transactions(transformed_records, min_revenue=0.0)

    reporter = PipelineReporter(raw_count=len(raw_data), clean_records=final_records)
    reporter.print_terminal_summary()

if __name__ == "__main__":
    run_pipeline()