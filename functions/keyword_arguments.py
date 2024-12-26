# Keyword Arguments

# self introduction
def self_intro(greeting, first_name, last_name, fav_colour):
    print()
    return f"{greeting}! My name is {first_name} {last_name} and my favourite colour is {fav_colour}."

# prints correctly as normal
print(self_intro("Good Morning", "Jane", "Doe", "green"))
# prints in exact order below, making sentence weird 😂
print(self_intro("Jane", "green", "Good Morning", "Doe"))
# using keyword arguments in exact order below, sentence stops being weird, returns to being normal 😭
print(self_intro(first_name="Jane", fav_colour="green", greeting="Good Morning", last_name="Doe"))


print()
print("------ new ------")


# shopping purchase
def shopping(quantity=5, item="apple", cost=3.2):
    if int(quantity) == 1:
        print()
        return f"I bought {int(quantity)} {item} that cost £{float(cost):.2f} each."
    else:
        print()
        return f"I bought {int(quantity)} {item}s that cost £{float(cost):.2f} each."

# uses keyword arguments
shopping_order_1 = shopping(24, "pear", 4.13)
print(shopping_order_1)

shopping_order_2 = shopping(1, "banana")
print(shopping_order_2)

# keyword argument usage is helpful here as there's only 1 argument passed in called function
    # - arguments passed in called function are ORDERED!!!
    # - 'shopping("computers")' means "computers" will be passed through the function where 'quantity' is placed 
        # - i.e. int("computers") -> ERROR!!!
    # - once called function's brackets contain keywords assigned to values, where in order they are written becomes irrelevant
shopping_order_3 = shopping(cost=60.7, item="computers")
print(shopping_order_3)


print()
print("------ new ------")


# using end="" & sep=""
for num in range(1, 11):
    print(num, end=",")
print()

print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", sep=",")


print()
print("------ new ------")


# 
