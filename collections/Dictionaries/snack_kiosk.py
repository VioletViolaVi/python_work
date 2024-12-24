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

# helps toggle ability for user to be done with removing snacks & return to the 'snack selection' stage
done_with_removing = False

# any key pressed, except "x".lower(), moves user to 1st if code block
greeting = input("Welcome to the snack bar. Press 'X' to leave: ").lower()
if greeting != "x":
    # displays snack menu
    print("=================")
    print("       Menu      ")
    print("      ------     ")
    print("   Snack   Price ")
    print("=================")
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

            user_snack_order = input("What else do what you want to order. Press 'X' to leave, 'R' to remove: ").lower()

        # snack not in dictionary, keeps running until snack in dictionary chosen
        while snack_menu.get(user_snack_order) == None:
                    
                    # helps allow users to exit
                    if user_snack_order == "x":
                        break

                    # helps allow users to remove snacks
                    if user_snack_order == "r":

                        # to remove snacks from basket if user changes their mind & user is not trying to end process of removing snacks
                        while user_snack_order == "r" and not done_with_removing:

                            # when basket is empty i.e. nothing else to remove
                            if basket == []:
                                print("Your current basket is empty")
                                # give user chance to buy anew
                                user_snack_order = input("Order more? Enter what you want to order. Press 'X' to leave: ").lower()
                                
                                # helps allow users to exit after 'order more' stage
                                if user_snack_order == "x":
                                    break

                                # stops non available snacks being added after 'order more' stage
                                while snack_menu.get(user_snack_order) == None:
                                    user_snack_order = input("Please only choose from our menu above. Press 'X' to leave: ").lower()
                                
                                # prevents 'basket' list being empty so "# opportunity to change snack if basket == []..." below code doesn't happen
                                basket.append(user_snack_order)
                                prices.append(snack_menu.get(user_snack_order))
                                print(f"Your current basket: {basket}")
                                print("-------- --------")
                                break
                            
                            # for removing snacks from basket
                            print(f"Your current basket: {basket}")
                            remove_snack = input("Enter snack you wish to remove. Press 'D' for Done: ").lower()
                            print("-------- --------")

                            # user wants to end process of removing snacks
                            if remove_snack == "d":
                                # helps stop while loop from asking user to enter snack again for removal, as they are done with this
                                done_with_removing = True
                                break
                                           
                            # checks if snack is present to be removed
                            if remove_snack in basket:                                 
                                # to keep removing snacks & their respective price from prices list
                                basket.remove(remove_snack)
                                prices.remove(snack_menu.get(remove_snack))

                                # messages for user to keep them informed                                
                                print(f"You removed: {remove_snack.title()}")

                            # prevents "d" being interpreted as 'snack not in basket'
                            # helps break while loop as user is done with removing snacks
                            elif done_with_removing:
                                break 

                            else:
                                # if user enters snack not in basket
                                print("Sorry, that snack is not in your basket.")                       

                    # helps user exit after removing all items
                    if user_snack_order == "x":
                        break

                    # opportunity to change snack
                    if basket == []:     
                        user_snack_order = input("Sorry, that's not available. Enter a different order. Press 'X' to leave: ").lower()
                    
                    # prevents "d" being interpreted as item in 'basket' list, so 'sorry' message below does not show
                    elif done_with_removing:

                        # resets to default value so user can be done w/ removing snacks at any stage at any number of times
                        done_with_removing = False

                        # give user chance to continue selecting snacks after being done with removing
                        user_snack_order = input("Anything else you want to order? Enter what you want to order. Press 'X' to leave: ").lower()
                        print(f"Your current basket: {basket}")
                        print("-------- --------")
                        
                        # helps break while loop as user is done with removing snacks                    
                        break                         

                    # changed from 'else' to 'elif' to stop users seeing this message after ordering more for empty basket (code: 'Order more?...')
                    elif not user_snack_order in basket:
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

    # designs original/1st receipt (b4 any duplicates)
    print()
    print("====================================")
    print("            Your Receipt            ")
    print("====================================")
    print()    

    # helps create duplicate receipt on request
    duplicate_receipt = False

    # helps stop outputting more receipts after duplicate
    stop_duplicate_receipt = False

    # ----------------------------------------------------------------------------------------------------
    while not duplicate_receipt:
        
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

        # only allows below question to show if duplicate has not been given already
        if stop_duplicate_receipt:
            print("Thank you for buying snacks from us. Goodbye!")
            break

        # ask user if they need duplicate receipt
        duplicate_receipt_response = input("Do you need a duplicate receipt? Enter 'Y' for Yes or 'N' for No): ").lower()

        # makes user pick between 'Y' or 'N' only
        while duplicate_receipt_response != "y" and duplicate_receipt_response != "n":
            duplicate_receipt_response = input("Do you need a duplicate receipt? Please only choose between 'Y' for Yes or 'N' for No: ").lower()

        # user sees goodbye message, not needing duplicate receipt
        if duplicate_receipt_response == "n":
            print("Thank you for buying snacks from us. Goodbye!")
            
            # prevents infinite loop of this receipt continuously outputting, only outputs once to begin w/
            duplicate_receipt = True
        
        # repeats while loop to show same receipt
        elif duplicate_receipt_response == "y":
            # designs duplicate receipt
            print()
            print("====================================")
            print("       Your Duplicate Receipt       ")
            print("====================================")
            print()

            # helps stop question asking if user needs duplicate receipt
            # helps stop another receipt be given after duplicate
            stop_duplicate_receipt = True    
    # ----------------------------------------------------------------------------------------------------
