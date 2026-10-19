from datetime import datetime
from pipeline.schema import TransactionRecord, StoreLocation

def validate_and_parse_record(raw_record: dict, valid_branches: dict) -> TransactionRecord:
    """
    Validates schema integrity, performs type coercion, and flags malformed data.
    Raises ValueError if critical fields are invalid.
    """
    try:
        required_keys = ["transaction_id", "branch_id", "date", "customer_tier", "item_count", "revenue"]
        for key in required_keys:
            if key not in raw_record or raw_record[key] is None:
                raise ValueError(f"Missing mandatory field: {key}")

        tx_id = str(raw_record["transaction_id"]).strip()
        branch_id = str(raw_record["branch_id"]).strip()
        
        if branch_id not in valid_branches:
            raise ValueError(f"Unknown branch ID: {branch_id}")

        parsed_date = datetime.strptime(str(raw_record["date"]).strip(), "%Y-%m-%d").strftime("%Y-%m-%d")
        
        tier = str(raw_record["customer_tier"]).strip().upper()
        if tier not in ["STANDARD", "SILVER", "GOLD", "PLATINUM"]:
            tier = "STANDARD"

        item_count = int(raw_record["item_count"])
        if item_count < 0:
            raise ValueError("Item count cannot be negative.")

        revenue = float(raw_record["revenue"])
        if revenue < 0:
            raise ValueError("Revenue cannot be negative.")

        store_obj = valid_branches.get(branch_id)

        return TransactionRecord(
            transaction_id=tx_id,
            branch_id=branch_id,
            date=parsed_date,
            customer_tier=tier,
            item_count=item_count,
            revenue=revenue,
            store=store_obj
        )

    except (ValueError, TypeError) as e:
        raise ValueError(f"Malformed Record {raw_record.get('transaction_id', 'UNKNOWN')}: {str(e)}")