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
print(" --- next --- ")
print()


# creates time object
# 'time()' takes in hours, minutes & seconds as values
time = datetime.time(18, 36, 20)

print(f"time: {time}")


print()
print(" --- next --- ")
print()


# gets what the time is right now
# output includes hours, minutes & seconds
# 'datetime.datetime' -> calls the 'datetime' class from the 'datetime' module
right_now = datetime.datetime.now()

print(f"right_now: {right_now}")

# format appearance of string stored in teh 'right_now' module
# 'strftime()' is a method that gets called on the object made from the 'datetime' class in 'datetime' module ('datetime.datetime')
    # use formatters, written as strings, in brackets of method 'strftime( ... )'
        # can view 'datetime' module's documentation to find more string formatters
right_now_formatted = right_now.strftime("%H:%M:%S | %d-%m-%Y")

print()
print(f"right_now_formatted: {right_now_formatted}")


print()
print(" --- next --- ")
print()


# checking if date & time, being compared w/, has passed the current date & time

# date & time being compared with
# # 'datetime.datetime()' datetime method called on datetime module
# 'datetime()' needs both date & time passed through
# 'datetime()' -> separate values by commas
target_datetime = datetime.datetime(3000, 12, 25, 17, 0, 1)

# current date & time
# 'now()' -> gets what the date & time is right now
current_datetime = datetime.datetime.now()

print(f"target_datetime: {target_datetime}")
print()

print(f"current_datetime: {current_datetime}")
print()


