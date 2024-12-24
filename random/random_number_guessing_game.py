# Random Number Guessing Game

import random

# random number to guess
correct_num = random.randint(1, 5) # both numbers (1, 5) are included!!!
print(f"0) correct_num: {correct_num}")

# get number guess from user between 1 and 5
user_guess = int(input("Guess the number between 1 and 5 (inclusively): "))

# prevent number being out of range of 1 and 5
while user_guess < 1 or user_guess > 5:
    user_guess = int(input("Number out of range! Guess the number between 1 and 5 (inclusively): "))


print(f"1) user_guess: {user_guess}")
print(f"1) correct_num: {correct_num}")

# user keeps trying to guess correct num
while not user_guess == correct_num:

    # prevent number being out of range of 1 and 5 after at least 1 guess made
    while user_guess < 1 or user_guess > 5:
        user_guess = int(input("Not accepted! Out of range! Guess the number between 1 and 5 (inclusively): "))

    # informing user how far off they're WRONG guess is
    if user_guess > correct_num:
        user_guess = int(input("Wrong! Too high! Guess the number between 1 and 5 (inclusively): "))
    elif user_guess < correct_num:
        user_guess = int(input("Wrong! Too low! Guess the number between 1 and 5 (inclusively): "))
    else:
        print("Error! 🫠")

    print(f"2) user_guess: {user_guess}")
    print(f"2) correct_num: {correct_num}")

# user guesses correct number
if user_guess == correct_num:
    print("Well done! You guessed correctly! 🥳")
    print(f"3) user_guess: {user_guess}")
    print(f"3) correct_num: {correct_num}")
