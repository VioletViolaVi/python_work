# Random Number Guessing Game

import random

# random number to guess
correct_num = random.randint(1, 5) # both numbers (1, 5) are included!!!

# get number guess from user between 1 and 5
user_guess = int(input("Guess the number between 1 and 5 (inclusively): "))

# prevent number being out of range of 1 and 5
while user_guess < 1 or user_guess > 5:
    user_guess = int(input("Number out of range! Guess the number between 1 and 5 (inclusively): "))

# user keeps trying to guess correct num
while not user_guess == correct_num:

    # prevent number being out of range of 1 and 5 after at least 1 guess made
    while user_guess < 1 or user_guess > 5:
        user_guess = int(input("Not accepted! Out of range! Guess the number between 1 and 5 (inclusively): "))

    # informing user how far off they're WRONG guess is
    if user_guess > correct_num:
        user_guess = int(input("It's lower than that! Guess the number between 1 and 5 (inclusively): "))
    elif user_guess < correct_num:
        user_guess = int(input("It's higher than that! Guess the number between 1 and 5 (inclusively): "))
    else:
        print("Error! 🫠")

# user guesses correct number
if user_guess == correct_num:
    print("Well done! You guessed correctly! 🥳")
