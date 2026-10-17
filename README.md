# Retail Pipeline

Reads retail transactions from a CSV file, removes bad rows, and prints a summary of sales and data quality.

## How to run

Open a terminal in this folder and run:

```
python3 main.py
```

To use a different file:

```
python3 main.py path/to/file.csv
```

To run the tests:

```
python3 -m unittest discover -v
```

No installs are needed. The project uses only Python's built-in modules.

## Your CSV needs these columns

`branch_id, transaction_date, customer_tier, item_count, revenue`

- Dates look like `2026-01-05`.
- Tiers must be Gold, Silver or Bronze.

A sample file is included at `data/transactions.csv`.

## What you get

A summary showing you rows read, clean and rejected rows, total sales, the top branch, sales by customer tier, and the reason each bad row was rejected.

## Files

- `main.py` runs everything
- `pipeline/schema.py` has the TransactionRecord and Branch classes
- `pipeline/validator.py` checks each row
- `pipeline/transformer.py` does the calculations
- `pipeline/reporter.py` prints the summary
- `tests/` has the unit tests