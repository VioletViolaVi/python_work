# Lists

names = ["vivian", "bella", "steve", "mike", "traci", "duke"]
foods = ["pizza", "burger", "pie", "chips", "soup"]
weathers = ["sunny", "rainy", "clear"]
animals = ["mouse", "dog", "fish", "cat", "donkey", "flamingo"]

# lists printed out
print(names)
print(foods)
print(weathers)
print(animals)

# locate items in lists
print(names[3])
print(foods[1])
print(weathers[2])
print(animals[4])

# lists slicing
print(names[3:])
print(foods[0::2])
print(weathers[0:2])
print(animals[-1:-6:-1])



print(" --- next ---")



# for loops
for name in names:
    print(name)

print()

for food in foods:
    print(food)

print()

for weather in weathers:
    print(weather)

print()

for animal in animals:
    print(animal, end=", ")

