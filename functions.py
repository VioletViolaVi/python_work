# Functions

# happy birthday song
def happy_birthday_song():
    print("happy birthday to u")
    print("u live in a zoo")
    print("u look like a monkey")
    print("and u smell like one too!")
    print()

happy_birthday_song()
happy_birthday_song()

# say hello world
def hello_world():
    print("Hello World! 👋")
    print()

hello_world()
hello_world()
hello_world()
hello_world()


print("------ new ------")
print()


# passing arguments through functions
def greeting(name):
    print(f"Hello. My name is {name}.")

greeting("Helen")

def age(age):
    print(f"I'm {age} years old.")

age("19")

def fav_food(food):
    print(f"My favourite food is {food}.")

fav_food("chips")

# passing multiple arguments through functions
def self_bio(name, age, fav_food):
    print(f"Hello. My name is {name}. I'm {age} years old. My favourite food to eat is {fav_food}.")

self_bio("Helen", "19", "chips")
self_bio("Matt", "21", "fish")
self_bio("Sam", "31", "eggs")


print("------ new ------")
print()


# display invoice
def display_invoice(account_holder, amount, due_date):
    print(f"Hello {account_holder}. You owe £{amount}. Your due to pay this by {due_date}.")

display_invoice("Mr Smith", "3031.53", "21st November 2022")
display_invoice("Mrs Adams", "25.11", "2nd April 2023")
display_invoice("Miss Lyon", "46.90", "15th March 2023")


print("------ new ------")
print()


# using return statements
def add_more_nums(num1, num2, num3):
    return num1 + num2 + num3
print("should be fifteen: ", end=" ")
print(add_more_nums(5, 5, 5))

def add_nums(num1, num2):
    return num1 + num2
print("should be six: ", end=" ")
print(add_nums(5, 1))

def subtract_nums(num1, num2):
    return num1 - num2
print("should be three: ", end=" ")
print(subtract_nums(5, 2,))

def multiply_nums(num1, num2):
    return num1 * num2
print("should be ten: ", end=" ")
print(multiply_nums(5, 2,))

def divide_nums(num1, num2):
    return num1 / num2
print("should be two point five: ", end=" ")
print(divide_nums(5, 2,))


print("------ new ------")
print()


# creating full names using return statements
def creating_full_names(fname, lname):
    # return f"{fname} {lname}"
    return fname + " " + lname

print(creating_full_names("Billy", "Johns"))
print(creating_full_names("Tracy", "Beaker"))
print(creating_full_names("Clover", "Lee"))

# using variables to store called functions
def create_cities(name1, name2):
    capitalised_name1 = name1.capitalize()
    capitalised_name2 = name2.capitalize()

    return capitalised_name1 + " " + capitalised_name2

capitalised_city1 = create_cities("hiGH", "strEeT")
print(capitalised_city1)

capitalised_city2 = create_cities("wOkan", "dA")
print(capitalised_city2)

capitalised_city3 = create_cities("tOwNs", "viLlE")
print(capitalised_city3)

print("------ new ------")
print()
# 
