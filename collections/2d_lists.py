# 2D (Dimensional) Lists

desserts = ["jelly", "ice-cream", "custard", "cake", "muffins", "brownies"]
mains = ["Vine Tomato & Basil Soup", "Pan-fried Scallops", "New Potato Salad", "Braised Beef Cheek", "Butternut Squash & Pepper Curry"]
drinks = ["water", "juice", "coffee", "tea", "lemonade", "milkshake", "smoothie"]

# 2d list
restaurant = [desserts, mains, drinks]

print(f"restaurant: {restaurant}")
print(restaurant[2][4])

# change 1st item in 1st list
restaurant[0][0] = "Raspberry and Pistachio Mango Mousse"
print(restaurant[0])
