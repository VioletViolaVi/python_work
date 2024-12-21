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
    print(" Snack   Price   ")
    print(" ------  ------  ")
    for snack, price in snack_menu.items():
        print(f"{snack.title()}", end=",  ")
        print(f"£{price:.2f}")
    print()

    while not user_request == "x".lower():
        # asks user what they want
        user_request = input("What would you like to buy? Select from above menu ('x' to quit): ").lower()
        # puts what they want in basket
        basket.append(user_request)
    basket.pop() # removes 'x' from list when user stops shopping

print(f"basket: {basket}")