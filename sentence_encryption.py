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

print(f"chars: {chars}")
print()
print(f"chars_list: {chars_list}")
print()
print(f"chars_list_copy: {chars_list_copy}")
print()
print(f"shuffled chars_list_copy: {shuffled_chars_list_copy}")
