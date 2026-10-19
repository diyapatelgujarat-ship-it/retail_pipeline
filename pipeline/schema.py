class StoreLocation:
    """Encapsulates branch metadata and tax rates."""
    def __init__(self, branch_id: str, region: str, tax_rate: float):
        self.branch_id = branch_id
        self.region = region
        self.tax_rate = tax_rate

    def __repr__(self):
        return f"StoreLocation(id={self.branch_id}, region={self.region}, tax={self.tax_rate})"


class TransactionRecord:
    """Encapsulates validated operational transaction attributes."""
    def __init__(self, transaction_id: str, branch_id: str, date: str, 
                 customer_tier: str, item_count: int, revenue: float, store: StoreLocation = None):
        self.transaction_id = transaction_id
        self.branch_id = branch_id
        self.date = date
        self.customer_tier = customer_tier
        self.item_count = item_count
        self.revenue = revenue
        self.store = store  # Interaction between TransactionRecord and StoreLocation

    def calculate_net_revenue(self) -> float:
        """Computes revenue after accounting for store tax rate if available."""
        tax = self.store.tax_rate if self.store else 0.05
        return round(self.revenue * (1 - tax), 2)

    def to_dict(self) -> dict:
        return {
            "transaction_id": self.transaction_id,
            "branch_id": self.branch_id,
            "date": self.date,
            "customer_tier": self.customer_tier,
            "item_count": self.item_count,
            "revenue": self.revenue,
            "net_revenue": self.calculate_net_revenue()
        }

    def __repr__(self):
        return f"TransactionRecord(id={self.transaction_id}, branch={self.branch_id}, rev={self.revenue})"