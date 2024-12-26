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


# passing arguments through functions
def greeting(name):
    print(f"Hello. My name is {name}")

greeting("Helen")

def age(age):
    print(f"I'm {age} years old")

age("19")

def fav_food(food):
    print(f"My favourite food is {food}")

fav_food("chips")

# passing multiple arguments through functions
def self_bio(name, age, fav_food):
    print(f"Hello. My name is {name}. I'm {age} years old. My favourite food to eat is {fav_food}")

self_bio("Helen", "19", "chips")
