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



# logging in
username = "user1"
password = "pass1"

entered_username = input("Please enter your username: ")
entered_password = input("Please enter your password: ")

while entered_password != password or entered_username != username:
    print("You have entered the wrong username and/or password")
    entered_username = input("Please try again. Enter your username: ")
    entered_password = input("Please try again. Enter your password: ")



print(" --- next --- ")



# logging in - broken down for more while loop practice (probs not good idea irl 🙃🤣😅😂😆😁)
correct_name = "user3"
correct_password = "abc123"

login_name = input("Enter your login name: ")
while not login_name == correct_name:
    print("Wrong login name. Try again: ")
    login_name = input("Enter your login name: ")

login_password = input("Enter your login password: ")
while not login_password == correct_password:
        print("Wrong login password. Try again: ")
        login_password = input("Enter your login password: ")

print("passed")



print(" --- next --- ")



# entering blanks

name = input("Please enter your name: ")

while name == "":
     print("You did not enter your name!")
     name = input("Please enter your name: ")
print(f"Hello {name}!👋")



print(" --- next --- ")



# checking age
age = int(input("Enter your age: "))
while age < 18:
    print("You are not old enough to enter!🛑")
    age = int(input("Enter your age: "))

while age >= 18:
    print("You are old enough to enter!🥂")
    break



print(" --- next --- ")



# guessing game

num = 17
guess = int(input("Guess the number!: "))

print(f"num: {num}")
print(f"guess: {guess}")
while guess != num:
    print("You got it wrong!")
    guess = int(input("Guess the number! (Hint: between 1 and 20 inclusively 😉) : "))

print("You got it right!")



print(" --- next --- ")



# quit option
colour = input("Enter a colour ('x' to leave): ").lower()

while not colour == "x":
    print(f"You entered: {colour}")
    colour = input("Enter a NEW colour ('x' to leave): ").lower()

print("You have left the game!👋")



print(" --- next --- ")



# number range
number = int(input("Pick number from 1 to 10 (inclusively): "))

while not 1 <= number <= 10:
    print(f"'{number}' is not in range!")
    number = int(input("Pick number from 1 to 10 (inclusively): "))

print(f"Your number is {number}")
