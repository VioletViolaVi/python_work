# Shopping Cart Exercise - (lists, sets, tuples)

foods = []
prices = []
total = 0

print(f"start: {foods}")

user_request = input("What food would you like to buy? ('x' to quit): ").lower()

while not user_request == "x":
    foods.append(user_request)
    user_request = input("What food would you like to buy? ('x' to quit): ").lower()
print(f"end: {foods}")
