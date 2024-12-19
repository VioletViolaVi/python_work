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



print(" --- next ---")



# all diff. methods (using food python list)
print(dir(foods))

# index
print(foods.index("pie"))

# inset
foods.insert(2,"bacon")
print(foods)

# pop
foods.pop()
print(foods)
foods.pop(2)
print(foods)

# remove
foods.remove("pizza")
print(foods)

# reverse
foods.reverse()
print(foods)

# sort
foods.sort()
print(foods)
foods.sort(reverse=True)
print(foods)

# append -> adds ONE item/elements
foods.append(["cake", "chocolate"])
foods.append("turkey")
for food in foods:
    print(food)
print(foods)

# extend -> adds multiple items/elements
foods.extend("soup") # - adds 's', 'o', 'u', 'p' NOT soup
foods.extend(["chicken", "jelly"])
print(foods)

# count: number of times item/element appears in list
print(foods.count("soup"))

# copy
foods.copy()
for food in foods:
    print(food)

# remove all items/elements
foods.clear()
print(foods)
