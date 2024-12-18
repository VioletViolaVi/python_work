# While Loops

# asking for name
name = input("Please enter ur name: ")

while name == "":
    print("You did not enter your name!")
    name = input("Please enter ur name: ")

print(f"Hello {name.title()}! 👋")



print(" --- next --- ")



# asking for age
age = input("Enter ur age: ")

while not age.isdigit():
    print("You did not enter a valid age!")
    age = input("Enter ur valid age: ")

print(f"You are {age}yrs old!")



print(" --- next --- ")



#
