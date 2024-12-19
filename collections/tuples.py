# Tuples

# Notes:
    # -
    # -
    # -
    # -

animals = ("mouse", "dog", "fish", "cat", "donkey", "donkey", "donkey", "flamingo")

print(animals)
print(len(animals)) # tuple length
print("cat" in animals) # shows 'True'
print("shoes" in animals) # shows 'False'
print(dir(animals)) # '.count()' & '.index()' the only methods
print(help(animals)) # get help



print(" --- new --- ")



# find index in tuples
print(animals.index("donkey"))
print(animals.index("flamingo"))

# states how frequently item appears
print(animals.count("donkey"))
print(animals.count("mouse"))
print(animals.count("fish"))



print(" --- new --- ")



# for loops
for animal in animals:
    print(animal, end=", ")
