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
def display_man(wrong_guesses):
    pass

# shows [list] of dashes for letters to guess
def display_hint(hint):
    pass

# shows correct answer when game is won or lost
def display_answer(answer):
    pass

# to contain main body of code
def app():
    pass

# app() function gets called only when this code is ran directly
if __name__ == "__main__":
    app()
