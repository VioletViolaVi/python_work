# Sets

# Notes:
    # - sets 'print() out' differently each time '@ random'
    # - items in sets cannot be edited i.e. reassigned
    # - sets are unordered (probs 'cause/why they print out differently)
    # - sets cannot have more than 1 of the same item (lists can)
        # - {"eggs", "eggs", "bacon", "beans"} would NOT be allowed
        # - .count() for counting multiple of the same item in a set would probs not be useful

weathers = {"sunny", "rainy", "clear", "snowy", "icy", "dry", "wet", "wet"}
print(weathers) # wont show 'wet' twice (items cannot be repeated)
print(dir(weathers)) # shows usable methods 
print(help(weathers)) # provides help list



print(" --- new --- ")



# set length
print(len(weathers))

# 'in' operator
print("mango" in weathers)
print("rainy" in weathers)

# adding to sets
weathers.add("thunder")
print(weathers)

# removing specific items from sets
weathers.remove("clear")
print(weathers)

# removing any item sets
print(weathers)
weathers.pop()
print(weathers)

# clear all set items
print(weathers)
weathers.clear()
print(weathers)
