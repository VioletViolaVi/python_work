# Cinema Snack Kiosks / Snack Bars

# - users select food they want & get told total price

# food keys, price values
snack_menu = {
    "popcorn" : 1.99,
    "chips" : 4.28,
    "hot dogs" : 7.05,
    "chicken nuggets" : 8.10,
    "strawberry milkshake" : 6.19,
    "banana smoothie" : 2.00,
    "water" : 0.75,
    "lemonade" : 3.03,
}

# user's shopping basket
basket = []
prices = []
total = 0

# user enters what they want
user_request = input("Welcome to the snack bar. Press 'C' to continue: ").lower()

if user_request == "c".lower():
    # displays snack menu
    print("  Snack   Price  ")
    print("-------- --------")
    for snack, price in snack_menu.items():
        print(f"{snack.title()}", end=",  ")
        print(f"£{price:.2f}")
    print()

    while not user_request == "x".lower():        
        user_request = input("What would you like to buy? Select from above menu ('x' to quit): ").lower() # asks user what they want       
        basket.append(user_request) # puts what they want in basket        
        prices.append(snack_menu.get(user_request)) # get respective prices stored

    basket.pop() # removes 'x' from list when user stops shopping
    prices.pop() # removes 'None' from list when user stops shopping
    print(f"prices: {prices}")

# display purchases & cost
print(" ------ Checkout ------  ")
if basket == [] and total == 0:
    print("You did not buy anything.")
else:
    print(f"Your basket: {basket}")
    print(f"Your Total: £{total}")