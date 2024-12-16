# Short Hand Operators (Ternary Operators / Conditional Expressions)

# mine
if True: print("This is truthy!")



print(" --- next --- ")



# outside/inside print()
print("5 is bigger than 10") if 5 > 10 else print("5 is NOT bigger than 10")

print("15 is bigger than 10" if 15 > 10 else "15 is NOT bigger than 10") # following vid structure

num = 5
print("+ve" if num > 0 else "-ve")

print("+ve") if num > 0 else print("-ve")



print(" --- next --- ")



# Odd or Even?
num = 141

print("Odd number" if not num % 2 == 0 else "Even number")
print("Odd number") if not num % 2 == 0 else print("Even number")



print(" --- next --- ")



# w/ variables

# highest/lowest number
num_1 = 150
num_2 = 600

highest_num =  num_1 if num_1 > num_2 else num_2
print("highest_num: " + str(highest_num))

lowest_num =  num_1 if num_1 < num_2 else num_2
print(f"lowest_num: {lowest_num}")



print(" --- next example --- ")



# drinking age
age = 28

can_drink = True if age >= 18 else False
print(f"can_drink: {can_drink}")

response = "Here's your beer 🍺" if can_drink else "I can't serve you alcohol!"
print(response)



print(" --- next example --- ")



# login greeting
username = "Bella"

login_greeting = "username not entered" if username == "" else f"Hello {username}"

print(login_greeting)



print(" --- next example --- ")



# cooking turkey
oven_temp = 35
hours = 65

is_cooked = True if 20 <= oven_temp <= 35 and 8 <= hours <= 15 else False
print(f"is_cooked: {is_cooked}")

conclusion = "Ready to eat! 🍗" if is_cooked else "Throw it away! 🤮 🤢"
print(conclusion)



print(" --- next example --- ")



# admin or guest?
user = "admin"
is_admin = True if user == "admin" else False
print(is_admin)

user = "guest"
is_admin = True if user == "admin" else False
print(is_admin)
