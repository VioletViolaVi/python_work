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