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
