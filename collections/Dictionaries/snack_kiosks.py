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
    print("-------- --------")
    print("  Snack   Price  ")
    print("-------- --------")
    for snack, price in snack_menu.items():
        print(f"{snack.title()}", end=",  ")
        print(f"£{price:.2f}")
    print()

    # asks user what they want 
    user_request = input("A) Select from above menu what you want to buy ('x' to quit): ").lower()

    # purchasing snacks
    while not user_request == "x".lower():
        # # asks user what they want 
        # user_request = input("A) Select from above menu what you want to buy ('x' to quit): ").lower()
        # user enters item not on menu
        if snack_menu.get(user_request) == None:
            user_request = input("B) Sorry, that's not available. Select from above menu what you want to buy ('x' to quit): ").lower()
            while snack_menu.get(user_request) == None: # i.e. user is STILL entering an item not in the dictionary at this point
                user_request = input("C) Sorry, that's not available. Select from above menu what you want to buy ('x' to quit): ").lower()
        else:
            # asks user what they want 
            user_request = input("D) Select from above menu what you want to buy ('x' to quit): ").lower()
            # puts what they want in basket        
            basket.append(user_request)
            # get respective snack prices stored
            prices.append(snack_menu.get(user_request))

    # stops .pop() on empty lists, only 'pops' on lists with items inside
    if not basket == [] and not prices == []:
        basket.pop() # removes 'x' from list when user stops shopping
        prices.pop() # removes 'None' from list when user stops shopping
    
    # adds all prices
    for price in prices:
        total += price
        print(f"price: {price}")
        print(f"total: {total}")

print(f"basket: {basket}") # delete later
print(f"prices: {prices}") # delete later

# display purchases & cost
print(" ------ Checkout ------  ")
if basket == [] and total == 0: # user fails to enter 'c'.lower()
    print("You did not buy anything.")
else:
    print(f"Your basket: {basket}")
    print(f"Your Total: £{round(total, 2)}") # avoids long decimal numbers

# - ensure u can quit at any stage!