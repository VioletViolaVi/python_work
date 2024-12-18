# # While Loops

# # asking for name
# name = input("Please enter ur name: ")

# while name == "":
#     print("You did not enter your name!")
#     name = input("Please enter ur name: ")

# print(f"Hello {name.title()}! 👋")



# print(" --- next --- ")



# # asking for age
# age = input("Enter ur age: ")

# while not age.isdigit():
#     print("You did not enter a valid age!")
#     age = input("Enter ur valid age: ")

# print(f"You are {age}yrs old!")



# print(" --- next --- ")



# logging in
username = "user1"
password = "pass1"

entered_username = input("Please enter your username: ")
entered_password = input("Please enter your password: ")

while entered_password != password or entered_username != username:
    print("You have entered the wrong username and/or password")
    entered_username = input("Please try again. Enter your username: ")
    entered_password = input("Please try again. Enter your password: ")
    