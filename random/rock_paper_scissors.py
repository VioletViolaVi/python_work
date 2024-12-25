# Rock Paper Scissors

import random

# user vs computer rock, paper, scissors game
all_options = ["r", "p", "s"]

# keeping score
user_score = 0
computer_score = 0

# start num for while loop
counter = 0

# greets user
print("Hi! Lets Play! 🪨   🗞️   ✂️")
print("===============================")

# plays game 5 times
while counter < 5:

    # gets choices made from user and computer
    user_choice = input("Choose, letters only -> rock (R), paper (P) or scissors (S): ").lower()
    print("===============================")
    
    # to only accept rock, paper or scissors
    while not user_choice == "r" and not user_choice == "p" and not user_choice == "s":
            user_choice = input("You can only choose from: rock (R), paper (P) or scissors (S): ").lower()
            print("===============================")

    # picks rock, paper or scissors from list
    computer_choice = random.choice(all_options)

    if user_choice == computer_choice:
        print("DRAW!")
        print("===============================")

    elif user_choice == "r":
        if computer_choice == "s":
            print("You win! rock beats scissors!")
            print("===============================")
            user_score += 1
        else:
            print("You lose! paper beats rock!")
            print("===============================")
            computer_score += 1

    elif user_choice == "p":
        if computer_choice == "r":
            print("You win! paper beats rock!")
            print("===============================")
            user_score += 1
        else:
            print("You lose! scissors beats paper!")
            print("===============================")
            computer_score += 1

    elif user_choice == "s":
        if computer_choice == "p":
            print("You win! scissors beats paper!")
            print("===============================")
            user_score += 1
        else:
            print("You lose! rock beats scissors!")
            print("===============================")
            computer_score += 1

    else:
        print("Error 😶")

    # increase counter to make while loop statement false after 5 iterations
    counter += 1


print("Scores")
print("------")
print(f"Your score: {user_score}")
print(f"Computer's score: {computer_score}")

# stores bigger score
higher_score = max(user_score, computer_score)

# states who wins
if higher_score == user_score and higher_score == computer_score:
    print(f"It's a tie! 😑  👔  😐")

elif higher_score == user_score:
    print(f"You are the winner! 🥇  😁  🙌")

elif higher_score == computer_score:
    print(f"Computer is the winner! 🤖  🖥️   😈")

else:
    print("Error!!! 😶")
