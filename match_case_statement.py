# Match Case Statements

# Notes
    # - 
    # - 


# finding days of week using if/elif/else
day = input("What day is it today?: ").capitalize()

def find_day(day):
    if day == "Monday":
        print(f"It's {day}!")
    elif day == "Tuesday":
        print(f"It's {day}!")
    elif day == "Wednesday":
        print(f"It's {day}!")
    elif day == "Thursday":
        print(f"It's {day}!")
    elif day == "Friday":
        print(f"It's {day}!")
    elif day == "Saturday":
        print(f"It's {day}!")
    elif day == "Sunday":
        print(f"It's {day}!")
    else:
        print("Error!")

find_day(day)