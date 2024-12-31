# Sentence Encryption

import string

# stores all different characters available
chars = string.printable

# converts chars "string" into [list]
chars_list = list(chars)

# creates copy of chars [list]
chars_list_copy = chars_list.copy()

print(chars)
print(chars_list)
print(chars_list_copy)
