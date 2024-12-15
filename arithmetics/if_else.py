# If / Elif / Else Statements

user_age = int(input("How old are you?: "))

if user_age >= 18:
    print("You are old enough to drink beer!")
else:
    print("You are NOT old enough to drink beer!")



print(" --- new example --- ")



user_meal = input("Do you prefer pizza or spaghetti?: ")

if user_meal == "pizza":
    print("You selected PIZZA")
elif user_meal == "spaghetti":
    print("You selected SPAGHETTI")
else:
    print("You DID NOT choose between pizza or spaghetti!")



print(" --- new example --- ")



user_topping = input("Pick a pizza topping (pepperoni, ham, spinach, bacon, onions, extra cheese): ")

if user_topping == "pepperoni":
    print("You added pepperoni to your pizza")
elif user_topping == "ham":
    print("You added ham to your pizza")
elif user_topping == "spinach":
    print("You added spinach to your pizza")
elif user_topping == "bacon":
    print("You added bacon to your pizza")
elif user_topping == "onions":
    print("You added onions to your pizza")
elif user_topping == "extra cheese":
    print("You added extra cheese to your pizza")
else:
    print("You must pick from the provided options!")



print(" --- new example --- ")



user_name = input("What is your name?: ")

if user_name != "":
    print(f"Hello {user_name}! Nice to meet you!")
else:
    print("Why don't you want to tell me your name?")



print(" --- new example --- ")



is_thirsty = False

if is_thirsty:
    print("Drink some water!")
else:
    print("DON'T drink some water!")



print(" --- new example --- ")



user_is_happy = True

if user_is_happy:
    print("Yay! You are happy!")
else:
    print("Oh no! You are sad!")



print(" --- new example --- ")



user_is_thirsty = input("True or False, are you thirsty?: ")

if user_is_thirsty == "True":
    user_is_thirsty = True
    if user_is_thirsty:
        print("Drink some water!")
    else:
        print("DON'T drink some water!")
elif user_is_thirsty == "False":
    user_is_thirsty = False
    if user_is_thirsty:
        print("Drink some water!")
    else:
        print("DON'T drink some water!")
else:
    print("You did not pick between 'True' or 'False'!!!")
