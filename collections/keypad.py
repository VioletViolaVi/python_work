# Keypad

# Create following via 2D lists:
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # * 0 #

# LISTS
# create row lists
row_1 = ["1", "2", "3"]
row_2 = ["4", "5", "6"]
row_3 = ["7", "8", "9"]
row_4 = ["*", "0", "#"]

# create list containing all rows
keypad = [row_1, row_2, row_3, row_4]

# print individually
for row in keypad:
    for btn in row:
        print(btn, end=" ")
    print()

print()
print(" --- list above tuple below --- ")
print()

# TUPLES
# create row tuples
row_1 = ("1", "2", "3")
row_2 = ("4", "5", "6")
row_3 = ("7", "8", "9")
row_4 = ("*", "0", "#")

# create tuples containing all rows
keypad = (row_1, row_2, row_3, row_4)

# print individually
for row in keypad:
    for btn in row:
        print(btn, end=" ")
    print()
