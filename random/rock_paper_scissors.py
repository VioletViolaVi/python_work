# Rock Paper Scissors

import random

# user vs computer rock, paper, scissors game
all_options = ["rock", "paper", "scissors"]

# keeping score
user_score = 0
computer_score = 0

# start num for while loop
counter = 0

# plays game 5 times
while counter < 5:

    # gets choices made from user and computer
    user_choice = input("choose: rock, paper or scissors: ").lower()
    
    # to only accept rock, paper or scissors
    while not user_choice == "rock" and not user_choice == "paper" and not user_choice == "scissors":
            user_choice = input("you can only choose from: rock, paper or scissors: ").lower()

    # picks rock, paper or scissors from list
    computer_choice = random.choice(all_options)

    if user_choice == computer_choice:
        print("DRAW!")

    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("you win! rock beats scissors!")
            user_score += 1
        else:
            print("you lose! paper beats rock!")
            computer_score += 1

    elif user_choice == "paper":
        if computer_choice == "rock":
            print("you win! paper beats rock!")
            user_score += 1
        else:
            print("you lose! scissors beats paper!")
            computer_score += 1

    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("you win! scissors beats paper!")
            user_score += 1
        else:
            print("you lose! rock beats scissors!")
            computer_score += 1

    else:
        print("error 😶")

    # increase counter to make while loop statement false after 5 iterations
    counter += 1

print("------")
print("Scores")
print(f"your score: {user_score} computer's score: {computer_score}")

# stores bigger score
higher_score = max(user_score, computer_score)

# states who wins
if higher_score == user_score and higher_score == computer_score:
    print(f"it's a tie!")

elif higher_score == user_score:
    print(f"you are the winner!")

elif higher_score == computer_score:
    print(f"computer is the winner!")

else:
    print("error 😶")
