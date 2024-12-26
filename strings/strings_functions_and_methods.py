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

print("vIviAN vIviAN".title()) # Vivian Vivian
print("vIviAN vIviAN".capitalize()) # Vivian vivian

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



# .count()
alliteration = "Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked"

picked_count = alliteration.count("picked")
print(f"picked: {picked_count}")

peter_count = alliteration.count("Peter")
print(f"Peter: {peter_count}")

pick_count = alliteration.count("pick")
print(f"pick: {pick_count}")

pe_count = alliteration.count("pe") # case sensitive
print(f"pe: {pe_count}")

Pe_count = alliteration.count("Pe") # case sensitive
print(f"CAPITAL 'P'!!! (Pe): {Pe_count}")



print(" --- next --- ")



# .replace()
login_greeting = "Hello User 👋"
bella = login_greeting.replace("User", "Bella")
steve = login_greeting.replace("User", "Steve")
pat = login_greeting.replace("User", "Pat")
cathy = login_greeting.replace("User", "Cathy")

print(f"Default login: {login_greeting}")
print(f"Bella logs in: {bella}")
print(f"Steve logs in: {steve}")
print(f"Pat logs in: {pat}")
print(f"Cathy logs in: {cathy}")

# using input()
default_greeting = "Hello user!"
entered_username = input("Please enter your name: ")
dynamic_greeting = default_greeting.replace("user", entered_username)
print(f"Dynamic Greeting: {dynamic_greeting}")
