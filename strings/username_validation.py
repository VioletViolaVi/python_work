# Username Validation Exercise

# username rules:
# - 12 characters max
# - no spaces
# - no digits

rules = input("Pick a username ( 12 char max | no spaces | no digits )")
username = input("Please enter a valid username: ")

check_char_len = len(username) # needs to be 12 or less
check_spaces = username.find(" ") # needs to be -1
check_only_letters = username.isalpha() # needs to be True

print(f"check_char_len: {check_char_len} (needs to be 12 or less)")
print(f"check_spaces: {check_spaces} (needs to be -1)")
print(f"check_only_letters: {check_only_letters} (needs to be True)")

if check_char_len <= 12:
    if check_spaces == -1:
        if check_only_letters:
            print("Yeah! You have a valid username! 🎊 🥳 🙌")
        else:
            print("Username must have no digits!")
    else:
        print("Username must have no spaces!")
else:
    print("Username must have no more than 12 characters!")
