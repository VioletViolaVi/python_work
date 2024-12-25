# Dice Game

import random

# 'one' side
print("+-------+")
print("|       |")
print("|   O   |")
print("|       |")
print("+-------+")

# 'two' side
print("+-------+")
print("| O     |")
print("|       |")
print("|     O |")
print("+-------+")

# 'three' side
print("+-------+")
print("| O     |")
print("|   O   |")
print("|     O |")
print("+-------+")

# 'four' side
print("+-------+")
print("| O   O |")
print("|       |")
print("| O   O |")
print("+-------+")

# 'five' side
print("+-------+")
print("| O   O |")
print("|   O   |")
print("| O   O |")
print("+-------+")

# 'six' side
print("+-------+")
print("| O   O |")
print("| O   O |")
print("| O   O |")
print("+-------+")

# counts number of dice used
dice_quantity = 0

# stores total dice numbers add up to
total = 0

# gets random side of dice
rand_dice_side = random.randint(1,6)
print(f"rand_dice_side: {rand_dice_side}")


