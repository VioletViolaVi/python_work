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
    return param_1


# param == user_guess ("")
def letter_guess(param):

    # asks user for letter guess
    param += input("Enter letter guess: ").lower()
    print(f"You guessed: {param}")

    # returns letter inputted by user
    return param

# param_1 == user_guess (""), param_2 == chosen_word, param_3 == dashed_word, param_4 == word_reveal
def show_correct_letters(param_1, param_2, param_3, param_4):

    # display letter if present in word
    if param_2.find(param_1) == -1:
        # displays dashes if letter is not in word
        print(f"Wrong: {param_3}")
    elif param_2.find(param_1) != -1:
        print(f"Correct:", end=" ")
        
        # displays letter if in word, otherwise leaves dashes
        for char in param_2:
            if char == param_1:
                print(char , end=" ")
            else:
                print("_", end=" ")
        # return param_4
    else:
        print("Error!")


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
    dashed_word = show_dashes(dashed_word, chosen_word)
    print(f"Can you guess the word?: {dashed_word}")
    
    # stores user's letter guess
    user_guess = ""
    user_guess = letter_guess(user_guess)

    # shows correct letters as user guesses them
    word_reveal = ""

    # responsible for showing letters if user's guess is in word
    word_reveal = show_correct_letters(user_guess, chosen_word, dashed_word, word_reveal)


# ____________________________________________________________________________________________________________________________ #
# allows file to run from other files w/out repeats
if __name__ == "__main__":
    main()
