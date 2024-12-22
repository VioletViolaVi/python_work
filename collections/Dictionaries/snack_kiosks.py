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

# any key pressed, except "x".lower(), moves user to 1st if code block
greeting = input("Welcome to the snack bar. Press 'X' to leave: ").lower()
if greeting != "x":
    # displays snack menu
    print("-------- --------")
    print("  Snack   Price  ")
    print("-------- --------")
    for snack, price in snack_menu.items():
        print(f"{snack.title()}", end=",  ")
        print(f"£{price:.2f}")
    print()

    print("-------- --------")
    user_snack_order = input("Enter what you want to order. Press 'X' to leave: ").lower()

    # continuous checking for if entered snack is available or not to be added
    while snack_menu.get(user_snack_order) != None or snack_menu.get(user_snack_order) == None:

        # helps prevents infinite loop when exiting further down
        if user_snack_order == "x":
            break

        # snack is present in dictionary
        while snack_menu.get(user_snack_order) != None:

            # add snacks to list
            basket.append(user_snack_order)
            # add snack prices to list
            prices.append(snack_menu.get(user_snack_order))

            user_snack_order = input("What else do what you want to order. Press 'X' to leave: ").lower()

        # snack not in dictionary, keeps running until snack in dictionary chosen
        while snack_menu.get(user_snack_order) == None:
                    
                    # helps allow users to exit
                    if user_snack_order == "x":
                        break

                    # opportunity to change snack     
                    user_snack_order = input("Sorry, that's not available. Enter a different order. Press 'X' to leave: ").lower()

# calculates total cost of items
for price in prices:
     total += price

# display purchases & cost
print(" ------ Checkout ------  ")
if basket == [] and total == 0:
    # user leaves w/out picking snacks
    print("Thank you for visiting. Goodbye!")
else:
    # user picks snacks, now needs to pay
    print(f"Your Basket: {basket}")
    print(f"Your Total: £{round(total, 2)}") # avoids long decimal numbers
