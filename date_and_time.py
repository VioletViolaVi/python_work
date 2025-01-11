# enables the use of dates and times using this computer's system clock
import datetime

# creates date object
# 'datetime' -> module
# 'date()' -> method
# inside method values:
    # - (year, month, day) -> '(2025, 12, 25)'
date = datetime.date(2025, 12, 25)

print()
print(f"date: {date}")


print()
print(" --- next --- ")
print()


# gets whatever date is now
# returns date object that displays today's date
today_date = datetime.date.today()

print(f"today_date: {today_date}")
print()

