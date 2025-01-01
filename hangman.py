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
# - add more words

# param == words list
def random_word(param):

    # returns random word from list passed through in main() below
    return random.choice(param)


# param_1 == words list, param_2 == dashed_word
def show_dashes(param_1, param_2):

    # shows characters in word as underscores w/ correct amount 
    for _ in random_word(param_1):
        param_2 += "_" 
    print(f"Can you guess the word?: {param_2}")


def letter_guess(param):

    # asks user for letter guess
    param = input("Enter letter guess: ").lower()
    print(f"You guessed: {param}")

def show_correct_letters():
    pass

def show_hangman():
    pass

def show_full_answer():
    pass

# helps allow file to run from other files w/out repeats
def main():

    # stores list of words for game - [5, 4, 2, 3, 8]
    words = ["lunch", "knee", "it", "fly", "lollipop"]

    # stores word as dashes e.g. "_ _ _"
    dashed_word = ""

    # displays full dashes/hidden word
    show_dashes(words, dashed_word)
    
    # stores user's letter guess
    user_guess = ""
    letter_guess(user_guess)

# allows file to run from other files w/out repeats
if __name__ == "__main__":
    main()
