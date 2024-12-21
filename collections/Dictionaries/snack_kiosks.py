# Cinema Snack Kiosks / Snack Bars

# - users select food they want & get told total price

# food keys, price values
snack_menu = {
    "popcorn" : 1.99,
    "hot dogs" : 7.05,
    "chips" : 4.28,
    "chicken nuggets" : 8.10,
    "water" : 0.75,
    "strawberry milkshake" : 6.19,
    "banana smoothie" : 2.00,
    "lemonade" : 3.03,
}

# user's shopping basket
basket = []
prices = []
total = 0

# user enters what they want
user_request = input("Welcome to the snack bar. Press 'C' to continue: ").lower()
print(user_request)

while user_request == "c":
    # displays snack menu
    for snack, price in snack_menu.items():
        print(" --- --- ")
        print(f"Snack: {snack.title()}", end=", ")
        print(f"Price: £{price:.2f}")
    print()

    # asks user what they want
    user_request = input("What would you like to buy? Select from above menu ('x' to quit): ").lower()
    # puts what they want in basket
    basket = basket.append(user_request)