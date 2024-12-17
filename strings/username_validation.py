# Username Validation Exercise

# username rules:
# - 12 characters max
# - no spaces
# - no digits

rules = input("Pick a username ( 12 char max | no spaces | no digits ): ")
username = input("Please enter a valid username: ")

check_char_len = len(username) # needs to be 12 or less
check_spaces = username.find(" ") # needs to be -1
check_digits = username.isdigit() # needs to be False

print(f"check_char_len: {check_char_len}")
print(f"check_spaces: {check_spaces}")
print(f"check_digits: {check_digits}")
