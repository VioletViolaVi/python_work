# Random Number Guessing Game

import random

# ends game
done_playing = False

# start number for guess range
start_range = 1

# varied end numbers for game difficulty
official_end_range = 0
easy_end_range = 10
mid_end_range = 50
hard_end_range = 100

while not done_playing:
    # user chooses game difficulty
    user_difficulty = input(f"Choose level difficulty - easy (E), medium (M), hard (H): ").lower()

    # prevents anything but "e", "m" or "h" being accepted as level difficulty
    while not user_difficulty == "e" and not user_difficulty == "m" and not user_difficulty == "h":
        print("--------------------------------------")
        user_difficulty = input("Choose 'E', 'M' or 'H' only. Choose level difficulty - easy (E), medium (M), hard (H): ").lower()
    
    # change game difficulty
    if user_difficulty == "e":
        official_end_range = easy_end_range
    elif user_difficulty == "m":
        official_end_range = mid_end_range
    elif user_difficulty == "h":
        official_end_range = hard_end_range

    # random number to guess
    # both numbers i.e. 'start_range' and 'official_end_range' are included in range!!!
    correct_num = random.randint(start_range, official_end_range)

    # get number guess from user between 'start_range' and 'official_end_range'
    print("--------------------------------------")    
    # starts off with taking user input as a string
    user_str_guess = input(f"Guess the number between {start_range} and {official_end_range} (inclusively): ")
    print("--------------------------------------")

    # ensures user guess is a number, otherwise user will not be able to move on to next stage, respective to where they are in game
    while True:
        # if user input is NOT a number (-ve / +ve) the except block will run to catch 'ValueError' so project can keep moving w/out stopping
        try: 
            # changes string to integer
            user_guess = int(user_str_guess)

            # prevent number being out of range of 'start_range' and 'official_end_range'
            while user_guess < start_range or user_guess > official_end_range:
                user_guess = int(input(f"Number out of range! Guess the number between {start_range} and {official_end_range} (inclusively): "))
                print("--------------------------------------")

            # user keeps trying to guess correct num
            while not user_guess == correct_num:

                # prevent number being out of range of {start_range} and {official_end_range} after at least 1 guess made
                while user_guess < start_range or user_guess > official_end_range:
                    user_guess = int(input(f"Not accepted! Out of range! Guess the number between {start_range} and {official_end_range} (inclusively): "))
                    print("--------------------------------------")

                # informing user how far off their WRONG guess is
                if user_guess > correct_num:
                    user_guess = int(input(f"It's lower than that! Guess the number between {start_range} and {official_end_range} (inclusively): "))
                    print("--------------------------------------")         
            
                # informing user how far off their WRONG guess is
                elif user_guess < correct_num:
                    user_guess = int(input(f"It's higher than that! Guess the number between {start_range} and {official_end_range} (inclusively): "))
                    print("--------------------------------------")

            # user entered valid input i.e. (-ve / +ve) number, so loop stops & user can move on to rest of code
            break

        # 'catches' error when user input is not a number (-ve / +ve)
        except ValueError: 
            # user given another chance to change entered data
            user_str_guess = input(f"Cannot accept! Pick a number between {start_range} and {official_end_range} (inclusively): ")
            print("--------------------------------------")

    # user guesses correct number
    if user_guess == correct_num:
        print("Well done! You guessed correctly! 🥳")
        print("--------------------------------------")
        
        # asks if user wants to play again
        play_again = input("Play again? Enter yes (Y), no (N): ").lower()
        print("--------------------------------------")

        # prevents anything but "y" or "n" being accepted to play on or leave
        while not play_again == "y" and not play_again == "n":
            play_again = input("Choose 'Y' or 'N' only. Play again? Enter yes (Y), no (N): ").lower()
            print("--------------------------------------")

        # continues or ends game based on user response
        if play_again == "y":
            done_playing = False
        else:
            done_playing = True
            print("See you next time!👋")
            break
