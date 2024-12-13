# input()

user_name = input("Enter username: ")
user_height = int(input("Enter your height in cm: "))

print(f"user_height is type: {type(user_height)}")
increased_user_height = user_height + 5

print(f"Welcome back: {user_name}!")
print(f"You are {user_height}cm tall!")
print(f"5cm more and you will be {increased_user_height}cm tall!")
