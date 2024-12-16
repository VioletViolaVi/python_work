# Measurement Converter via Conditional Statements

input("Hi, lets convert your height! - press enter to continue")

user_height = float(input("Enter your height: "))

user_unit_choice = input("Select unit measurement ('mm', 'cm', 'm'): ").lower()

# converting from mm
if user_unit_choice == "mm":
    user_conversion_choice = input("Select unit to convert to ('cm' or 'm'): ").lower()

    # mm --> cm / m / error
    if user_conversion_choice == "cm":
        result = user_height / 10
        print(f"Your {user_height}{user_unit_choice} height is {result}{user_conversion_choice}!")
    elif user_conversion_choice == "m":
        result = user_height / 1000
        print(f"Your {user_height}{user_unit_choice} height is {result}{user_conversion_choice}!")
    else:
        print("You did not pick between 'cm' or 'm'!")

# converting from cm
elif user_unit_choice == "cm":
    user_conversion_choice = input("Select unit to convert to ('mm' or 'm'): ").lower()

    # cm --> mm / m / error
    if user_conversion_choice == "mm":
        result = user_height * 10
        print(f"Your {user_height}{user_unit_choice} height is {result}{user_conversion_choice}!")
    elif user_conversion_choice == "m":
        result = user_height / 100
        print(f"Your {user_height}{user_unit_choice} height is {result}{user_conversion_choice}!")
    else:
        print("You did not pick between 'mm' or 'm'!")

# converting from m
elif user_unit_choice == "m":
    user_conversion_choice = input("Select unit to convert to ('mm' or 'cm'): ").lower()

    # m --> mm / cm / error
    if user_conversion_choice == "mm":
        result = user_height * 1000
        print(f"Your {user_height}{user_unit_choice} height is {result}{user_conversion_choice}!")
    elif user_conversion_choice == "cm":
        result = user_height * 100
        print(f"Your {user_height}{user_unit_choice} height is {result}{user_conversion_choice}!")
    else:
        print("You did not pick between 'mm' or 'cm'!")

# mm, cm or m not entered
else:
    print("You did not pick between 'mm', 'cm' or 'm'!")
