# Cinema Snack Kiosk / Snack Bar

# Notes:
    # - users select food they want & get told total price
    # - unique_list = list(set(basket))*
        #  - *can work as just a set i.e. set(basket)
        #  - *list() still good to wrap set(), in case user wants a duplicate receipt, snacks would print same order

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

# --------------------------------------------------------------------------------------------------------------------------------------------- #

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

            print(f"basket after adding, after removing: {basket}") # delete later!!!
            user_snack_order = input("What else do what you want to order. Press 'X' to leave, 'R' to remove: ").lower()

        # snack not in dictionary, keeps running until snack in dictionary chosen
        while snack_menu.get(user_snack_order) == None:
                    
                    # helps allow users to exit
                    if user_snack_order == "x":
                        break

                    # helps allow users to remove snacks
                    if user_snack_order == "r":
                        # to remove snacks from basket if user changes their mind
                        while user_snack_order == "r":

                            # when basket is empty i.e. nothing else to remove
                            if basket == []:
                                print("Your current basket is empty")
                                # give user chance to buy anew
                                user_snack_order = input("Order more? Enter what you want to order. Press 'X' to leave: ").lower() # error continues w/ 'x'
                                break
                            
                            # for removing snacks from basket
                            print(f"Your current basket: {basket}")
                            remove_snack = input("Enter snack you wish to remove. Press 'D' for Done: ").lower() # NEXT HERE FIX 'D' OPTION
                            print("-------- --------")

                            # checks if snack is present to be removed
                            if remove_snack in basket:                                 
                                # to keep removing snacks & their respective price from prices list
                                basket.remove(remove_snack)
                                prices.remove(snack_menu.get(remove_snack))

                                # messages for user to keep them informed                                
                                print(f"You removed: {remove_snack.title()}")

                            else:
                                # if user enters snack not in basket
                                print("Sorry, that snack is not in your basket.")                                
                    
                    # opportunity to change snack
                    if basket == []:     
                        user_snack_order = input("Sorry, that's not available. Enter a different order. Press 'X' to leave: ").lower()
                    else:
                        user_snack_order = input("Sorry, that's not available. Enter a different order. Press 'X' to leave, 'R' to remove: ").lower()
                    
                    # helps user pick snacks from beginning after removing all snacks
                    if basket == []:
                        break       

# --------------------------------------------------------------------------------------------------------------------------------------------- #

# calculates total cost of items
pennies = 0 # get pennies
for price in prices:
    total += price
    if total < 1:
         pennies = total * 100

# user leaves w/out picking snacks
if basket == [] and total == 0:
    print()
    print("Thank you for visiting. Goodbye!")

# user gets receipt for buying snacks
else:

    # at checkout
    print()
    print(" -- Checkout -- ")
    print()

    # designs receipt
    print("====================================")
    print("            Your Receipt            ")
    print("====================================")
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

        # used for multi purchases
        if snack_quantity > 1:
            # only shows single price when multiples of the same snack bought
            print(f"                    (£{snack_menu.get(snack_item):.2f})") # displays price for 1 snack

        # adds line space below single bought snacks only
        if snack_quantity == 1:
             print()

    print()

    if total < 1:
        # displays full total using pence (e.g. 15p)
        print(f"Your Total: {int(pennies)}p")   
    else:
        # displays full total using £ sign
        print(f"Your Total: £{round(total, 2):.2f}") # avoids long decimal numbers   
    print("====================================")
