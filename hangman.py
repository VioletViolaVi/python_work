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

# param_1 == words list, param_2 == chosen_word
def random_word(param_1, param_2):

    # randomly chosen word stored in variable
    param_2 += random.choice(param_1)

    # returns random word from list passed through in main() below
    return param_2


# param_1 == dashed_word, param_2 == chosen_word
def show_dashes(param_1, param_2):

    # shows characters in word as underscores w/ correct amount
    for _ in param_2:
        print(_) # shows word being used - remove @ end
        param_1 += "_" 
    print(f"Can you guess the word?: {param_1}")


# param == user_guess ("")
def letter_guess(param):

    # asks user for letter guess
    param += input("Enter letter guess: ").lower()
    print(f"You guessed: {param}")

    # returns letter inputted by user
    return param

# param_1 == user_guess (""), param_2 == chosen_word
def show_correct_letters(param_1, param_2):

    # display letter if present in word
    if param_2.find(param_1) == -1:
        print("letter not in word")
    elif param_2.find(param_1) != -1:
        print("letter is in word")
    else:
        print("Error!")


    print(f"diff func, word: {param_2}")
    print(f"diff func, letter: {param_1}")
    print(f"param_2.find(param_1): {param_2.find(param_1)}")


def show_hangman():
    pass

def show_full_answer():
    pass

# helps allow file to run from other files w/out repeats
def main():

    # stores list of words for game - [5, 4, 2, 3, 8]
    words = ["lunch", "knee", "it", "fly", "lollipop"]

    # stores chosen random word
    chosen_word = ""
    chosen_word = random_word(words, chosen_word)

    # stores word as dashes e.g. "_ _ _"
    dashed_word = ""

    # displays full dashes/hidden word
    show_dashes(dashed_word, chosen_word)
    
    # stores user's letter guess
    user_guess = ""
    user_guess = letter_guess(user_guess)

    # # responsible for getting user's guess
    # letter_guess(user_guess)

    # responsible for showing if user guess is in word
    show_correct_letters(user_guess, chosen_word)
    
    

# allows file to run from other files w/out repeats
if __name__ == "__main__":
    main()
