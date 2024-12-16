# # Logical Operators: and | or | not

# # Going Clubbing
# age = 16
# has_id = False

# # Getting inside club
# if age >= 18 and has_id:
#     print("You can go into the club!🍻🍸")
# elif age >= 18 and not has_id:
#     print("You need id to prove you're of age! 🪪")
# elif age < 18 and has_id:
#     print("You are not old enough to enter!")
# else:
#     print("You're not old enough and/or you don't have id!")



# print(" --- new examples --- ")



# # Shop availability
# fruit = "apples"

# if fruit == "apples" or fruit == "cherries" or fruit == "bananas":
#     print(f"Yes, we still have {fruit} in stock.")
# else:
#     print(f"Sorry, we're all out of {fruit}.")


# veg = "sweet peppers"
# has_enough_money = True

# if veg == "cabbage" or veg == "lettuce" or veg == "sweetcorn" or veg == "carrots":
#     print(f"We still have {veg} in stock")
#     if not has_enough_money:
#         print(f"You cannot afford to buy the {veg}")
#     else:
#         print(f"You can buy the {veg}. That'll be £46.97 please! 💷")
# else:
#     print(f"Sorry, we're all out of {veg}.")


# Shopping list
meat = "beef"
drink = "lemonade"
ice_cream = "vanilla"

if (meat == "beef" or meat == "chicken") and (drink == "coffee" or drink == "lemonade" ) and (ice_cream == "vanilla" or ice_cream == "chocolate"):
    print("You have all the items on my shopping list!")
else:
    print("You don't have all the items on my shopping list!")
