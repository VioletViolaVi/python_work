# Age Converting Calculator via Conditional Statements

input("Hi, lets find out how old you are! (hit enter)")

user_age = int(input("How old are you?: "))

frequency = input("Select Frequency -> (Minutes, Hours, Days, Weeks, Months, Years): ").lower()

if frequency == "minutes":
    new_age = user_age * 525600
    print(f"You are {new_age} {frequency} old!")
elif frequency == "hours":
    new_age = user_age * 8760
    print(f"You are {new_age} {frequency} old!")
elif frequency == "days":
    new_age = user_age * 365
    print(f"You are {new_age} {frequency} old!")
elif frequency == "weeks":
    new_age = user_age * 52
    print(f"You are {new_age} {frequency} old!")
elif frequency == "months":
    new_age = user_age * 12
    print(f"You are {new_age} {frequency} old!")
elif frequency == "years":
    new_age = user_age * 1
    print(f"You are {new_age} {frequency} old!")
else:
    print("ERROR!!! Invalid age or frequency! ERROR!!!")
