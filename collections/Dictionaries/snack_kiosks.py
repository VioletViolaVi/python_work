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
user_request = input("1) Welcome to the snack bar. Press 'C' to continue: ").lower()

if user_request == "c".lower():
    # displays snack menu
    print("-------- --------")
    print("  Snack   Price  ")
    print("-------- --------")
    for snack, price in snack_menu.items():
        print(f"{snack.title()}", end=",  ")
        print(f"£{price:.2f}")
    print()

    print("-------- --------")
    user_snack_order = input("2) Enter what you want to order. Press 'X' to leave: ").lower()

    # continuous checking for if entered snack is available or not to be added
    while snack_menu.get(user_snack_order) != None or snack_menu.get(user_snack_order) == None:
        # helps prevents infinite loop when exiting further down
        if user_snack_order == "x":
            break

        # snack is present in dictionary
        while snack_menu.get(user_snack_order) != None:
            basket.append(user_snack_order)
            print(f"This entered item is available & has been put in basket list: {user_snack_order}")
            print(f"basket list so far: {basket}")
            user_snack_order = input("3) What else do what you want to order. Press 'X' to leave: ").lower()

        # snack not in dictionary, keeps running until snack in dictionary chosen
        while snack_menu.get(user_snack_order) == None:
                    # helps allow users to exit
                    if user_snack_order == "x":
                        print("can you see this (X)? ")
                        break
                         
                    user_snack_order = input("4) Sorry, that's not available. Enter a different order. Press 'X' to leave: ").lower()
                    print(f"REASSIGN user snack order: {user_snack_order}")




# display purchases & cost
print(" ------ Checkout ------  ")
if basket == [] and total == 0: # user fails to enter 'c'.lower()
    print("You did not buy anything.")
else:
    print(f"Your basket: {basket}")
    print(f"Your Total: £{round(total, 2)}") # avoids long decimal numbers

# - ensure u can quit at any stage!
# - ensure items are added at any stage!