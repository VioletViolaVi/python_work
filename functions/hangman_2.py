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

x = 0
while x <= 6:
    for line in hangman_art[x]:
        print(line)
    x += 1
