# Cinema Snack Kiosk / Snack Bar

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

# --------------------------------------------------------------------------------------------------------------------------------------------- #

# calculates total cost of items
pennies = 0 # get pennies
for price in prices:
    total += price
    if total < 1:
         pennies = total * 100

print()
print(" -- Checkout -- ")
print()

# user leaves w/out picking snacks
if basket == [] and total == 0:
    print("Thank you for visiting. Goodbye!")

# user gets receipt for buying snacks
else:
    # designs receipt
    print("=====================")
    print("      Your Bill      ")
    print("========== ==========")
    print()

    # creates list of unique snacks
    unique_list = list(set(basket)) # -> turns to a: 'list' then 'set' then 'list' again

    # iterates through newly made list(), made from set(), that no longer contains duplicates
    for snack_item in unique_list:

        # gets quantity of respective snack
        snack_quantity = basket.count(snack_item)

        # gets price of respective snack
        snack_item_price = snack_menu.get(snack_item)

        # snack price & amount of the respective snacks selected multiplied together
        total_price = snack_quantity * snack_item_price

        # formats display of snack count quantity, single price cost & multi price cost
        print(f"{snack_quantity}x {snack_item.title()} - £{total_price:.2f}")

        # only shows single price when multiples of the same snack is bought
        if snack_quantity > 1:
            print(f"                  (£{snack_menu.get(snack_item):.2f})")

    print()

    if total < 1:
        # displays full total using pence (e.g. 15p)
        print(f"Your Total: {int(pennies)}p")   
    else:
        # displays full total using £ sign
        print(f"Your Total: £{round(total, 2):.2f}") # avoids long decimal numbers   
    print("========= =========")
