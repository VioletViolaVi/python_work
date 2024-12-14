# Shopping Basket

item = input("What would you like to purchase?: ")

item_quantity = int(input("How many would you like to buy?: "))

price = float(input("How much is each item?: "))

total = item_quantity * price

if item_quantity > 1:
    print(f"The total cost for {item_quantity} {item}s is £{total} please.")
else:
    print(f"The total cost for {item_quantity} {item} is £{total} please.")
