# Short hand Operators

# mine
if True: print("This is truthy!")



print(" --- next --- ")


# in/out print()
print("5 is bigger than 10") if 5 > 10 else print("5 is NOT bigger than 10")

print("15 is bigger than 10" if 15 > 10 else "15 is NOT bigger than 10") # following vid structure

num = 5
print("+ve" if num > 0 else "-ve")



print(" --- next --- ")



# Odd or Even?
num = 141

print("Odd number" if not num % 2 == 0 else "Even number")
print("Odd number") if not num % 2 == 0 else print("Even number")



print(" --- next --- ")



# w/ variables
num_1 = 150
num_2 = 600

highest_num =  num_1 if num_1 > num_2 else num_2
print("highest_num: " + str(highest_num))

lowest_num =  num_1 if num_1 < num_2 else num_2
print(f"lowest_num: {lowest_num}")


print(" --- next example --- ")


age = 28

can_drink = True if age >= 18 else False
print(f"can_drink: {can_drink}")

response = "Here's your beer 🍺" if can_drink else "I can't serve you alcohol!"
print(response)


print(" --- next example --- ")
