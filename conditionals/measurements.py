# Measurement Converter via Conditional Statements

input("Hi, lets convert your height! - press enter to continue")

user_height = float(input("Enter your height: "))

user_unit_choice = input("Select unit measurement ('mm', 'cm', 'm'): ").lower()

if user_unit_choice == "mm":
    user_conversion_choice = input("Select unit to convert to ('cm' or 'm'): ").lower()
    if user_conversion_choice == "cm":
        result = user_height / 10
        print(f"Your {user_height}{user_unit_choice} height is {result}{user_conversion_choice}!")
    elif user_conversion_choice == "m":
        result = user_height / 1000
        print(f"Your {user_height}{user_unit_choice} height is {result}{user_conversion_choice}!")
    else:
        print("You did not pick between 'cm' or 'm'!!!")









