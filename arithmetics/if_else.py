# If Else Statements

user_age = int(input("How old are you?: "))

if user_age >= 18:
    print("You are old enough to drink beer!")
else:
    print("You are NOT old enough to drink beer!")



print(" --- new example --- ")


user_topping = input("Do you prefer pizza or spaghetti?: ")

if user_topping == "pizza":
    print("You selected PIZZA")
elif user_topping == "spaghetti":
    print("You selected SPAGHETTI")
else:
    print("You DID NOT choose between pizza or spaghetti!")
