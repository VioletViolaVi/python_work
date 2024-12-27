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
