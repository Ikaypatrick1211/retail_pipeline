import math
from datetime import datetime
from pipeline.schema import TransactionRecord


def validate_records(rows):
    """Check every row. Returns the good records and a list of reasons for bad rows."""
    clean = []
    rejected = []

    # Row 1 of the file is the header, so data starts on row 2
    for row_num, row in enumerate(rows, start=2):
        branch_id = (row.get("branch_id") or "").strip()
        tier = (row.get("customer_tier") or "").strip().title()

        if branch_id == "":
            rejected.append(f"row {row_num}: missing branch ID")
            continue

        if tier not in ("Gold", "Silver", "Bronze"):
            rejected.append(f"row {row_num}: invalid customer tier")
            continue

        try:
            date = datetime.strptime(row.get("transaction_date") or "", "%Y-%m-%d").date()
            items = int(row.get("item_count") or "")
            revenue = float(row.get("revenue") or "")
        except ValueError:
            rejected.append(f"row {row_num}: bad date or number")
            continue

        if not math.isfinite(revenue):
            rejected.append(f"row {row_num}: bad date or number")
            continue

        if items < 0 or revenue < 0:
            rejected.append(f"row {row_num}: negative item count or revenue")
            continue

        clean.append(TransactionRecord(branch_id, date, tier, items, revenue))

    return clean, rejected
