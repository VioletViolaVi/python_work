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
rand_dice_side = random.randint(1, 6)
print(f"rand_dice_side: {rand_dice_side}")

# specific conditions for specific dice sides
if rand_dice_side == 1:
    print(f"You rolled {rand_dice_side}")
elif rand_dice_side == 2:
    print(f"You rolled {rand_dice_side}")
elif rand_dice_side == 3:
    print(f"You rolled {rand_dice_side}")
elif rand_dice_side == 4:
    print(f"You rolled {rand_dice_side}")
elif rand_dice_side == 5:
    print(f"You rolled {rand_dice_side}")
elif rand_dice_side == 6:
    print(f"You rolled {rand_dice_side}")
else:
    print("Error!")


