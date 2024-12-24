# Random Number Guessing Game

import random

# random number to guess
correct_num = random.randint(1, 6)

# get number guess from user between 1 and 5
user_guess = int(input("Guess the number between 1 and 5 (inclusively): "))


print(f"user_guess: {user_guess}")
print(f"correct_num: {correct_num}")
