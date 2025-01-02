# Hangman Game

import random

# stores words for game
words = ["lunch", "knee", "it", "fly", "lollipop"]

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

# functions

# shows correct hangman art based on num of wrong guesses dict key
def display_hangman_art(incorrect_guess_num):
    pass

# shows [list] of dashes for letters to guess
def display_dashes(dashes):
    pass

# shows correct answer when game is won or lost
def display_answer(correct_word):
    pass

# to contain main body of code
def app():
    
    # gets random word from [words] list above
    correct_word =  random.choice(words)
    
    # produces same num of dashes as there are in word to guess
    dashes = " _ " * len(correct_word)

    # stores num of incorrect guesses made so correct hangman art can be shown
    incorrect_guess_num = 0

    # stores all letters guessed by user, wrong or not
    all_user_guesses = ""

    # to turn game on and off once game has been won/lost
    is_playing = True



    print(f"correct_word: {correct_word}")
    print(f"dashes: {dashes}")

# app() function gets called only when this code is ran directly
if __name__ == "__main__":
    app()
