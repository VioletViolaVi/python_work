# Sentence Encryption

import string

# original order of characters as string
original_chars = string.printable

# reversed order of characters as string
mixed_up_chars = original_chars[::-1]

# user enters message to be encrypted
message = input("Enter a sentence: ")

# shows new encrypted message
encrypt_message = ""

# encrypt user message
for character in message:

    # gets index number of inputted character from index location of letter in mixed_up_chars string
    encrypt_letter_num_index = original_chars.index(character)
    print(f"encrypt_letter_num_index for OG: {encrypt_letter_num_index}")

    # puts letter gotten from mixed_up_chars string in empty string above
    encrypt_message += mixed_up_chars[encrypt_letter_num_index]
    print(f"encrypt_message: {encrypt_message}")

# shows encrypted message
print(f"encrypt_message: {encrypt_message}")
