import csv
import sys

from pipeline.validator import validate_records
from pipeline.transformer import get_active, get_net_margins
from pipeline.reporter import print_report


def main():
    path = "data/transactions.csv"
    if len(sys.argv) > 1:
        path = sys.argv[1]

    try:
        with open(path, newline="") as f:
            rows = list(csv.DictReader(f))
    except FileNotFoundError:
        print("Could not find the file:", path)
        sys.exit(1)

    clean, rejected = validate_records(rows)
    print_report(clean, rejected)

    active = get_active(clean)
    print(f"\nActive sales:           {len(active)}")
    print(f"Total net margin:       ${sum(get_net_margins(active)):,.2f}")


if __name__ == "__main__":
    main()