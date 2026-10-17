from pipeline.schema import Branch


def print_report(clean, rejected):
    """Work out the business numbers and print them."""
    if len(clean) == 0:
        print("No clean records to report on.")
        return

    total_rows = len(clean) + len(rejected)
    gross_sales = sum(r.revenue for r in clean)
    retention = len(clean) / total_rows * 100

    # Put each record into a Branch object, then find the best branch
    branches = {}
    for r in clean:
        if r.branch_id not in branches:
            branches[r.branch_id] = Branch(r.branch_id)
        branches[r.branch_id].add_transaction(r)
    top = max(branches.values(), key=lambda b: b.total_revenue)

    # Count and total the sales for each customer tier
    tier_count = {}
    tier_sales = {}
    for r in clean:
        tier_count[r.customer_tier] = tier_count.get(r.customer_tier, 0) + 1
        tier_sales[r.customer_tier] = tier_sales.get(r.customer_tier, 0) + r.revenue

    print("===== RETAIL PIPELINE SUMMARY =====")
    print(f"Rows read:          {total_rows}")
    print(f"Clean rows:         {len(clean)}")
    print(f"Rejected rows:      {len(rejected)}")
    print(f"Retention rate:     {retention:.1f}%")
    print(f"Total gross sales:  ${gross_sales:,.2f}")
    print(f"Top branch:         {top.branch_id} (${top.total_revenue:,.2f})")

    print("\nCustomer tiers:")
    for tier in sorted(tier_sales):
        print(f"  {tier}: {tier_count[tier]} sales, ${tier_sales[tier]:,.2f}")

    print("\nRejected rows:")
    for reason in rejected:
        print("  -", reason)