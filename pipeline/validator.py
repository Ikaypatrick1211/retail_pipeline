from datetime import datetime
from pipeline.schema import TransactionRecord


def validate_records(rows):
    """Check every row. Returns the good records and a list of reasons for bad rows."""
    clean = []
    rejected = []

    for row in rows:
        branch_id = row["branch_id"].strip()
        tier = row["customer_tier"].strip().title()

        if branch_id == "":
            rejected.append("missing branch ID")
            continue

        if tier not in ("Gold", "Silver", "Bronze"):
            rejected.append("invalid customer tier")
            continue

        try:
            date = datetime.strptime(row["transaction_date"], "%Y-%m-%d").date()
            items = int(row["item_count"])
            revenue = float(row["revenue"])
        except ValueError:
            rejected.append("bad date or number")
            continue

        if items < 0 or revenue < 0:
            rejected.append("negative item count or revenue")
            continue

        clean.append(TransactionRecord(branch_id, date, tier, items, revenue))

    return clean, rejected