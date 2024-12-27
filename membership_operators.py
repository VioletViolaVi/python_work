# Membership Operators

# word guessing game

# word user needs to guess right
answer = "apple"

# greeting for user
print("Can you guess the word?")
# stores user's guess
user_letter_guess = input("Guess a letter in the word: ").lower()

if user_letter_guess not in answer or user_letter_guess == "":
    print(f"No. '{user_letter_guess}' is not in the word!")
else:
    print(f"Yes. '{user_letter_guess}' is in the word!")
