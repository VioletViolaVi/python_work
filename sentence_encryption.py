# Sentence Encryption

import string, random

# stores all different characters available
chars = string.printable

# converts chars "string" into [list]
chars_list = list(chars)

# creates copy of chars [list]
chars_list_copy = chars_list.copy()

# to shuffle copy of chars list
random.shuffle(chars_list_copy)

# stores shuffled characters
shuffled_chars_list_copy = chars_list_copy

# get sentence from user to encrypt
user_sentence = input("Enter a sentence to encrypt: ")

# stores encrypted message
encrypted_sentence = ""

# replace each user sentence character with character from [shuffled_chars_list_copy list]
for char in user_sentence:

    # gets random number for selecting random char from shuffled list
    # uses length of [shuffled_chars_list_copy list] for passed number value
    rand_num = random.randint( 0, ( len(shuffled_chars_list_copy) - 1 ) )

    # stores random character from [shuffled_chars_list_copy list] for every character entered in user sentence
    encrypted_sentence += shuffled_chars_list_copy[rand_num]
    
    print(f"char: {char} | encrypted_sentence: {encrypted_sentence}")

print(f"The final encrypted message: {encrypted_sentence}")
