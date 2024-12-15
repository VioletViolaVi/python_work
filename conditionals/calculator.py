# Calculator via Conditional Statements

operator = input("Select an operator ( + | - | / | * ): ")
num_1 = float(input("Enter 1st value: "))
num_2 = float(input("Enter 2nd value: "))
answer = 0

if operator == "+":
    answer = num_1 + num_2
    print(f"{num_1} + {num_2} = {answer}")
elif operator == "-":
    answer = num_1 - num_2
    print(f"{num_1} - {num_2} = {answer}")
elif operator == "/":
    answer = num_1 / num_2
    print(f"{num_1} / {num_2} = {answer}")
elif operator == "*":
    answer = num_1 * num_2
    print(f"{num_1} * {num_2} = {answer}")
else:
    print("Error! Error! Error!")
