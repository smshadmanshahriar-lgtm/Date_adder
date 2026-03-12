from datetime import datetime
from date_adder import add_months, add_years

def test_add_months():
    start = datetime(2024, 1, 31)
    # Adding 1 month to Jan 31st 2024 (leap year) -> Feb 29th
    assert add_months(start, 1).strftime("%Y-%m-%d") == "2024-02-29"
    
    start = datetime(2023, 1, 31)
    # Adding 1 month to Jan 31st 2023 (non-leap year) -> Feb 28th
    assert add_months(start, 1).strftime("%Y-%m-%d") == "2023-02-28"

def test_add_years():
    start = datetime(2024, 2, 29)
    # Adding 1 year to Feb 29th 2024 -> Feb 28th 2025
    assert add_years(start, 1).strftime("%Y-%m-%d") == "2025-02-28"
    
    start = datetime(2024, 1, 1)
    assert add_years(start, 1).strftime("%Y-%m-%d") == "2025-01-01"

if __name__ == "__main__":
    # Simple manual run
    test_add_months()
    test_add_years()
    print("Tests passed!")
