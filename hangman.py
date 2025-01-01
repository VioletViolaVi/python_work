# Hangman

import random

# todo - basics:
# - show dashes
# - show correct letters
# - show parts of hangman when wrong letters
# - game over & correct word
# todo - additions:
# - scores
# - continuous play
# - greeting & goodbye

def random_word(words_param):
    return random.choice(words_param)

def show_dashes():
    pass

def show_correct_letters():
    pass

def show_hangman():
    pass

def show_full_answer():
    pass

# helps allow file to run from other files w/out repeats
def main():

    # stores list of words for game
    words = ["lunch", "knee", "town", "fly", "lollipop"]

    # selects random word from list
    print(random_word(words))
    pass

# allows file to run from other files w/out repeats
if __name__ == "__main__":
    main()
