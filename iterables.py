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
