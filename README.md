# Date Adder

A simple command-line utility to add time intervals (days, weeks, months, years) to a specific date or today's date.

## Features
- Add days, weeks, months, or years to a date.
- Supports ISO 8601 format (YYYY-MM-DD).
- Defaults to today's date if none is provided.

## Usage

```bash
python date_adder.py --date 2024-01-01 --days 10
# Output: 2024-01-11

python date_adder.py --weeks 2
# Output: [Today's date + 14 days]
```

## Testing
Run tests using pytest:
```bash
pytest
```
