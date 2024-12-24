# Random Number Guessing Game

import random

# numbers for guess range
start_range = 1
end_range = 10

# random number to guess
correct_num = random.randint(start_range, end_range) # both numbers i.e. 'start_range' and 'end_range' are included in range!!!
print(f"correct_num: {correct_num}")

# get number guess from user between 'start_range' and 'end_range'
user_guess = int(input(f"Guess the number between {start_range} and {end_range} (inclusively): "))

# prevent number being out of range of 'start_range' and 'end_range'
while user_guess < start_range or user_guess > end_range:
    user_guess = int(input(f"Number out of range! Guess the number between {start_range} and {end_range} (inclusively): "))

# user keeps trying to guess correct num
while not user_guess == correct_num:

    # prevent number being out of range of {start_range} and {end_range} after at least 1 guess made
    while user_guess < start_range or user_guess > end_range:
        user_guess = int(input(f"Not accepted! Out of range! Guess the number between {start_range} and {end_range} (inclusively): "))

    # informing user how far off they're WRONG guess is
    if user_guess > correct_num:
        user_guess = int(input(f"It's lower than that! Guess the number between {start_range} and {end_range} (inclusively): "))
    elif user_guess < correct_num:
        user_guess = int(input(f"It's higher than that! Guess the number between {start_range} and {end_range} (inclusively): "))
    else:
        print("Error! 🫠")

# user guesses correct number
if user_guess == correct_num:
    print("Well done! You guessed correctly! 🥳")
