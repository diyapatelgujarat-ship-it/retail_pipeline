from collections import Counter

class PipelineReporter:
    """Aggregates and formats terminal outputs for executive review."""
    def __init__(self, raw_count: int, clean_records: list):
        self.raw_count = raw_count
        self.clean_records = clean_records

    def compute_metrics(self) -> dict:
        total_gross_sales = sum(r.revenue for r in self.clean_records)
        retention_rate = (len(self.clean_records) / self.raw_count * 100) if self.raw_count > 0 else 0.0
        
        branch_sales = Counter()
        for r in self.clean_records:
            branch_sales[r.branch_id] += r.revenue
        
        top_branch = branch_sales.most_common(1)[0][0] if branch_sales else "N/A"
        tier_counts = Counter(r.customer_tier for r in self.clean_records)

        return {
            "total_gross_sales": round(total_gross_sales, 2),
            "retention_rate": round(retention_rate, 2),
            "clean_count": len(self.clean_records),
            "dropped_count": self.raw_count - len(self.clean_records),
            "top_branch": top_branch,
            "branch_sales": dict(branch_sales),
            "tier_breakdown": dict(tier_counts)
        }

    def print_terminal_summary(self):
        metrics = self.compute_metrics()
        print("\n" + "="*60)
        print("     EXECUTIVE RETAIL DATA PIPELINE — SUMMARY REPORT")
        print("="*60)
        print(f" Total Raw Records Processed : {self.raw_count}")
        print(f" Clean Records Retained      : {metrics['clean_count']} ({metrics['retention_rate']}%)")
        print(f" Malformed Records Dropped   : {metrics['dropped_count']}")
        print(f" Total Gross Sales           : ${metrics['total_gross_sales']:,.2f}")
        print(f" Top-Performing Branch       : {metrics['top_branch']}")
        print("-" * 60)
        print(" Customer Tier Breakdown:")
        for tier, count in metrics['tier_breakdown'].items():
            print(f"   - {tier}: {count} transactions")
        print("="*60 + "\n")