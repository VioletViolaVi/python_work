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

    print("-------- --------")
    user_snack_order = input("Enter what you want to order (Press 'X' to leave): ").lower()
   
    if not user_snack_order == "x":
        print(f"entered item: {user_snack_order}") 
        for snack_key in snack_menu.keys():
            print(f"dict item: {snack_key}")  
            if user_snack_order == snack_key:
                print("This item is available")
                basket.append(snack_key)
                print(f"snack key put in list: {snack_key}")
                print(f"basket list: {basket}")
                break
            # else:
            #     input("Sorry, that's not available. Enter what you want to order: ").lower()


    
    
    
    
    

    




# display purchases & cost
print(" ------ Checkout ------  ")
if basket == [] and total == 0: # user fails to enter 'c'.lower()
    print("You did not buy anything.")
else:
    print(f"Your basket: {basket}")
    print(f"Your Total: £{round(total, 2)}") # avoids long decimal numbers

# - ensure u can quit at any stage!
# - ensure items are added at any stage!