# Shopping Cart Exercise - (lists, sets, tuples)

foods = []
prices = []
total = 0

print(f"foods start: {foods}")
print(f"prices start: {prices}")

# in case user quits straight away    
user_request_food = input("What food would you like to buy? ('x' to quit): ").lower()
if user_request_food != "x".lower():
    user_request_price = float(input(f"What's the price of {user_request_food}? (£): "))

while not user_request_food == "x":
    # put food & price in lists above
    foods.append(user_request_food)
    prices.append(user_request_price)

    # asks users again
    user_request_food = input("What food would you like to buy? ('x' to quit): ").lower()
    if user_request_food != "x".lower():
        user_request_price = float(input(f"What's the price of {user_request_food}? (£): "))

print(f"foods end: {foods}")
print(f"prices end: {prices}")


print(f" --- shopping basket --- ")
for food in foods:
    print(food)

print(f" --- checkout total --- ")
for price in prices:
    total += price
    print(price)

print(f"Your total shopping cost is £{round(total, 2)}")
