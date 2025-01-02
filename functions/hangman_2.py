# Hangman Game

import random

# functions

# shows correct hangman art based on num of wrong guesses dict key
def display_hangman_art(hangman_art, wrong_guess_total):

    # uses assigned num, from app() below, to find respective key in hangman_art dict to produce its correct art value
    for code_line in hangman_art[wrong_guess_total]:
        print(code_line)

# shows [list] of dashes for letters to guess
def display_dashes(dashes):
    print(" ".join(dashes)) # .join() being used as dashes variable is a [list]

# shows correct answer when game is won or lost
def display_answer(correct_word):
    print(correct_word) 

# to contain main body of code
def app():

    # different hangman states - {num of wrong guesses: art}
    hangman_art = {
        0 : ("   ", 
            "   ", 
            "   "),

        1 : (" O ", 
            "   ", 
            "   "),

        2 : (" O ", 
            " | ", 
            "   "),

        3 : (" O ", 
            "/| ", 
            "   "),

        4 : (" O ", 
            "/|\\", 
            "   "),

        5 : (" O ", 
            "/|\\", 
            "/  "),

        6 : (" O ", 
            "/|\\", 
            "/ \\")
    }    

    # stores words for game
    words = ["lunch", "knee", "it", "fly", "lollipop"]    

    # gets random word from [words] list above
    correct_word =  random.choice(words)
    
    # produces same num of dashes as there are in word to guess
    #   - needs to NOT BE A STRING as items need to be reassigned (to swap dashes for correct letters)
    #   - reassignment of characters in strings is not possible as strings are immutable
    dashes = [" _ "] * len(correct_word)

    # stores num of incorrect guesses made so correct hangman art can be shown
    wrong_guess_total = 0

    # stores all letters guessed by user, wrong or not
    all_user_guesses = ""

    # to turn game on and off once game has been won/lost
    is_playing = True

    # print(f"correct_word: {correct_word}")
    # print(f"dashes: {dashes}")    
    # print(f"user_guess: {user_guess}")
    
    # runs the game
    while is_playing:

        # calls function to show respective hangman art based on number of wrong guesses
        display_hangman_art(hangman_art, wrong_guess_total)

        # calls function to show respective num of dashes based on the length of the random word gotten
        display_dashes(dashes)

        # stores letter user entered
        user_guess = input("Guess a letter: ").lower()

        # switches dashes for letters when guessed correctly by user
        if user_guess in correct_word:
            for index_num in range( len(correct_word) ):
                if correct_word[index_num] == user_guess:
                    dashes[index_num] = user_guess
                    print(f"dashes[index_num]: {dashes[index_num]}")
                    print(f"dashes: {dashes}")


# app() function gets called only when this code is ran directly
if __name__ == "__main__":
    app()
