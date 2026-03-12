import argparse
from datetime import datetime, timedelta

def add_months(start_date, months):
    month = start_date.month - 1 + months
    year = start_date.year + month // 12
    month = month % 12 + 1
    day = min(start_date.day, [31,
        29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28,
        31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month-1])
    return datetime(year, month, day)

def add_years(start_date, years):
    try:
        return start_date.replace(year=start_date.year + years)
    except ValueError:
        # Handling Feb 29 for non-leap years
        return start_date.replace(year=start_date.year + years, day=28)

def main():
    parser = argparse.ArgumentParser(description="Add time intervals to a date.")
    parser.add_argument("--date", type=str, help="Initial date in YYYY-MM-DD format (default: today)")
    parser.add_argument("--days", type=int, default=0, help="Days to add")
    parser.add_argument("--weeks", type=int, default=0, help="Weeks to add")
    parser.add_argument("--months", type=int, default=0, help="Months to add")
    parser.add_argument("--years", type=int, default=0, help="Years to add")

    args = parser.parse_args()

    if args.date:
        start_date = datetime.strptime(args.date, "%Y-%m-%d")
    else:
        start_date = datetime.now()

    # Add intervals
    new_date = start_date + timedelta(days=args.days + (args.weeks * 7))
    
    if args.months:
        new_date = add_months(new_date, args.months)
    
    if args.years:
        new_date = add_years(new_date, args.years)

    print(new_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    main()
