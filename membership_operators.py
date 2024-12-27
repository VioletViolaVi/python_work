# Membership Operators

# practicing 'not in' membership operator
# letter guessing game, user needs to enter letter that's present to be right
answer = "apple"

# greeting for user
print("Can you guess the word?")
# stores user's guess
user_letter_guess = input("Guess a letter in the word: ").lower()

# characters, including '', not part of "apple" produce truthy output
if user_letter_guess not in answer or user_letter_guess == "":
    print(f"No. '{user_letter_guess}' is not in the word!")

# only characters in "apple" produce falsy output
else:
    print(f"Yes. '{user_letter_guess}' is in the word!")


print(" --- new ---")


# practicing 'in' membership operator
# guess the number
correct_num_list = [8]

# user sees game instructions & enters number guess
print("Can you guess the correct number?")
user_num_guess = int(input("Guess the correct number!: "))

# if entered input is the number is in list above, user is correct otherwise they'll be told they're wrong
if user_num_guess in correct_num_list:
    print(f"Yes. '{user_letter_guess}' was the correct number!")
else:
    print("No! You are wrong!")


print(" --- new ---")


# using sets to practice 'in' and 'not in'
# set of sports
sports = {"tennis", "basketball", "football", "rugby", "swimming"}

# using 'in' membership operator w/ if else
if "rock climbing" in sports:
    print(f"This sport is in the set.")
else:
    print("This sport is not in the set.")

print()

# using 'not in' membership operator w/ if else
if "rugby" not in sports:
    print("This sport is not in the set.")
else:
    print(f"This sport is in the set.")


print(" --- new ---")


# using dictionaries to practice 'in' and 'not in' membership operators
colours_dict = {
    "red": "primary",
    "orange": "secondary",
    "yellow": "primary",
    "green": "primary",
    "purple": "secondary"
}

# iterates through dictionary values to find "primary"
if "primary" in colours_dict.values():
    print("This is in the dictionary")
else:
    print("This is not in the dictionary")

print()

# iterates through dictionary keys to find "blue"
if "blue" not in colours_dict:
    print("This is not in the dictionary")
else:
    print("This is in the dictionary")


print(" --- new ---")


# using 'in' to check if email's valid i.e. contains '@' / '.'
email = "fakeemail@fake.com"

if "@" in email and "." in email:
    print("this is a valid email address")
else:
    print("this is an invalid email address")

print()

# using 'not in' to check if email's valid i.e. contains '@' / '.'
email_2 = "fakeemail@fakecom"

if "@" not in email_2 and "." not in email_2:
    print("this is a valid email address")
else:
    print("this is an invalid email address")
