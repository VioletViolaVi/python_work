# Rock Paper Scissors

import random

# user vs computer rock, paper, scissors game
all_options = ["r", "p", "s"]

# keeping score
user_score = 0
computer_score = 0

# start num for while loop
counter = 0

# controls if game playing is infinite or not
is_still_playing = True

# greets user
print("Hi! Lets Play! 🪨   🗞️   ✂️")
print("===============================")

# makes game playing infinite until user leaves
while is_still_playing:

    # ----------------------------------------------------------------------------------------------------------------------------------------
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
                print("You win! Rock beats scissors!")
                print("===============================")
                user_score += 1
            else:
                print("You lose! Paper beats rock!")
                print("===============================")
                computer_score += 1

        elif user_choice == "p":
            if computer_choice == "r":
                print("You win! Paper beats rock!")
                print("===============================")
                user_score += 1
            else:
                print("You lose! Scissors beats paper!")
                print("===============================")
                computer_score += 1

        elif user_choice == "s":
            if computer_choice == "p":
                print("You win! Scissors beats paper!")
                print("===============================")
                user_score += 1
            else:
                print("You lose! Rock beats scissors!")
                print("===============================")
                computer_score += 1

        else:
            print("Error  😶")

        # increase counter to make while loop statement false after 5 iterations
        counter += 1
    # ----------------------------------------------------------------------------------------------------------------------------------------

    print("Scores  🏆  🥇  🥈  🥉  🏆")
    print("------")
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")
    print("------")

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

    # asks if user wants to play again
    print("------")
    play_again = input("Play again? Yes (Y) or No (N): ").lower()
    print("===============================")

    # prevents anything but "y" or "n" being accepted to play on or leave
    while not play_again == "y" and not play_again == "n":
        play_again = input("(Y) or No (N) Only. Play again? Yes (Y) or No (N): ").lower()
        print("===============================")

    # continues or ends game based on user response
    if play_again == "y":
        # plays game again
        is_still_playing = True
    else:
        # stops infinite game playing
        is_still_playing = False
        print("See you next time!👋")
        break
