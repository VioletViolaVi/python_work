# Dice Game

import random

# counts number of dice used
dice_quantity = 0

# stores total dice numbers add up to
total = 0

# gets random side of dice
rand_dice_side = random.randint(1, 6)
print(f"rand_dice_side: {rand_dice_side}")

# specific conditions for specific dice sides
if rand_dice_side == 1:
    # 'one' side
    print("+-------+")
    print("|       |")
    print("|   O   |")
    print("|       |")
    print("+-------+")

    print(f"You rolled {rand_dice_side}")
elif rand_dice_side == 2:
    # 'two' side
    print("+-------+")
    print("| O     |")
    print("|       |")
    print("|     O |")
    print("+-------+")

    print(f"You rolled {rand_dice_side}")
elif rand_dice_side == 3:
    # 'three' side
    print("+-------+")
    print("| O     |")
    print("|   O   |")
    print("|     O |")
    print("+-------+")

    print(f"You rolled {rand_dice_side}")
elif rand_dice_side == 4:
    # 'four' side
    print("+-------+")
    print("| O   O |")
    print("|       |")
    print("| O   O |")
    print("+-------+")

    print(f"You rolled {rand_dice_side}")
elif rand_dice_side == 5:
    # 'five' side
    print("+-------+")
    print("| O   O |")
    print("|   O   |")
    print("| O   O |")
    print("+-------+")

    print(f"You rolled {rand_dice_side}")
elif rand_dice_side == 6:
    # 'six' side
    print("+-------+")
    print("| O   O |")
    print("| O   O |")
    print("| O   O |")
    print("+-------+")

    print(f"You rolled {rand_dice_side}")
else:
    print("Error!")


