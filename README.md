# Retail Pipeline

It reads retail transaction records from a CSV file, removes any bad rows, and prints
a summary of sales and data quality.

## How to run

1. Open a terminal in the `retail_pipeline` folder.
2. Activate the virtual environment: `source .venv/bin/activate`
3. Run the program:

```
   python main.py
```

   To use a different file: `python main.py path/to/file.csv`

4. Run the tests: `python -m unittest discover -v`

## Your CSV needs to have these columns

`branch_id, transaction_date, customer_tier, item_count, revenue`

Dates must look like this: `2026-01-05`. 
Tiers must be Gold, Silver or Bronze.

## Files

- `main.py` runs everything
- `pipeline/schema.py` has the TransactionRecord and Branch classes
- `pipeline/validator.py` checks each row
- `pipeline/transformer.py` does the calculations
- `pipeline/reporter.py` prints the summary
- `tests/` has the unit tests