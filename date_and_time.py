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


print()
print(" --- next --- ")
print()


# creates time object
# 'time()' takes in hours, minutes & seconds as values
time = datetime.time(18, 36, 20)

print(f"time: {time}")
print()


print()
print(" --- next --- ")
print()


# gets what the time is right now
# output includes hours, minutes & seconds
# 'datetime.datetime' -> calls the 'datetime' class from the 'datetime' module
right_now = datetime.datetime.now()

print(f"right_now: {right_now}")
print()


