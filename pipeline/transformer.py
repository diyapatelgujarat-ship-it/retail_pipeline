def filter_active_transactions(records: list, min_revenue: float = 0.0) -> list:
    """Filters transactions using list comprehensions and filter()."""
    return list(filter(lambda r: r.revenue > min_revenue, records))

def apply_discount_to_tier(records: list, target_tier: str, discount_pct: float) -> list:
    """Applies a functional transformation mapping records to new values immutably."""
    return list(map(
        lambda r: type(r)(
            transaction_id=r.transaction_id,
            branch_id=r.branch_id,
            date=r.date,
            customer_tier=r.customer_tier,
            item_count=r.item_count,
            revenue=round(r.revenue * (1 - discount_pct), 2) if r.customer_tier == target_tier else r.revenue,
            store=r.store
        ),
        records
    ))

def extract_high_value_ids(records: list, threshold: float) -> list:
    """List comprehension returning IDs of high-value transactions."""
    return [r.transaction_id for r in records if r.revenue >= threshold]