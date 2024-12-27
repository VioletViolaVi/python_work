# Iterables

# list of colours
colours = ["red", "green", "yellow", "orange", "purple"]

# give single items being printed out readable names
for colour in colours:
    print(f"colour: {colour}")

print()

# prints list backwards
for colour in reversed(colours):
    print(f"colour: {colour}", end=" ][ ")
print()


print(" -- new -- ")


# tuple of drinks
drinks = ("water", "lemonade", "tea", "coffee", "juice")

for drink in drinks:
    print(drink)


print(" -- new -- ")


# set of fruits
fruits = {"orange", "apple", "pear", "mango", "coconut"}

for fruit in fruits:
    print(fruit)

print()

# set of vegetables
vegetables = {"sweetcorn", "cucumber", "carrot", "tomato", "peas"}

for vegetable in vegetables:
    print(vegetable)


print(" -- new -- ")


# iterating through strings
song = "We built this city on rock and roll!"

for char in song:
    print(char)

print()

song_2 = "And this christmas, will be, very special christmas, for me!!!"

for char_2 in song_2:
    print(char_2, end="/ ")



