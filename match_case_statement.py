# Match Case Statements

# Notes
    # - match case statements are alternatives to using lots of elif statements
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


print()


# finding days of week using match case statements
def find_day(day):
    match day:
        case "Monday":
            print(f"It's {day}!")
        case "Tuesday":
            print(f"It's {day}!")
        case "Wednesday":
            print(f"It's {day}!")
        case "Thursday":
            print(f"It's {day}!")
        case "Friday":
            print(f"It's {day}!")
        case "Saturday":
            print(f"It's {day}!")
        case "Sunday":
            print(f"It's {day}!")
        # ' _ ' is a wildcard 
        # this case occurs if there's no matching cases from above
        case _:
            print("Error!")
find_day(day)


print(" --- next --- ")


# finds out which are weekends
user_input = input("Is it a weekend? Enter a day: ").capitalize()

def is_weekend(user_input):
    match user_input:
        case "Monday":
            print("No. This is a weekday.")
        case "Tuesday":
            print("No. This is a weekday.")
        case "Wednesday":
            print("No. This is a weekday.")
        case "Thursday":
            print("No. This is a weekday.")
        case "Friday":
            print("No. This is a weekday.")
        case "Saturday":
            print("Yes. This is a weekend.")
        case "Sunday":
            print("Yes. This is a weekend.")
        case _:
            print("Error!")
is_weekend(user_input)

print()

# condensed match case statement for is_weekend() above
def is_weekend(user_input):
    match user_input:
        # '|' is the or operator
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print("No. This is a weekday.")
        case "Saturday" | "Sunday":
            print("Yes. This is a weekend.")
        case _:
            print("Error!")
is_weekend(user_input)
