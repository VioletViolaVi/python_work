# enables the use of dates and times using this computer's system clock
import datetime

# creates date object
# 'datetime' -> module
# 'date()' -> method
# inside method values:
    # - (year, month, day) -> '(2025, 12, 25)'
date = datetime.date(2025, 12, 25)

print(f"date: {date}")
