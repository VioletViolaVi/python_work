# String Functions & Methods

# len()
username = input("Enter your name: ") # Jane Doe used
print(len(username))



print(" --- next --- ")



# .find() / .rfind()
j_index = username.find('J')
a_index = username.rfind('A') # .rfind() -> last occurrence
n_index = username.find('N')
e_index = username.rfind('e') # .rfind() -> last occurrence
space_index = username.find(' ')
d_index = username.find('d')
o_index = username.find('o')

print(f"J => {j_index}")
print(f"a => {a_index}")
print(f"n => {n_index}")
print(f"e => {e_index}")
print(f"' ' => {space_index}")
print(f"D => {d_index}")
print(f"o => {o_index}")



print(" --- next --- ")



# Capitalisation
lowered_username = input("Enter your name: ") # john doe used
capitalize_method = lowered_username.capitalize()
title_method = lowered_username.title()

print(f"lowered_username: {lowered_username}")
print(f"capitalize_method: {capitalize_method}")
print(f"title_method: {title_method}")



print(" --- next --- ")



# Upper / Lower
whisper = input("What do you want to whisper?: ").lower()
shout = input("What do you want to shout?: ").upper()

print(whisper)
print(shout)



print(" --- next --- ")


# Number / Alphabet Presence
is_digit_present = "123"
is_digit_present_2 = "i have 5 eggs"

print(is_digit_present.isdigit())
print(is_digit_present_2.isdigit())

is_alphabet_present = "123"
is_alphabet_present_2 = "i have 5 eggs"
is_alphabet_present_3 = "i have five eggs"
is_alphabet_present_4 = "ihavefiveeggs"
is_alphabet_present_5 = "iHaveFiveEggs"

print(is_alphabet_present.isalpha())
print(is_alphabet_present_2.isalpha())
print(is_alphabet_present_3.isalpha())
print(is_alphabet_present_4.isalpha())
print(is_alphabet_present_5.isalpha())



print(" --- next --- ")

