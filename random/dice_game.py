# Dice Game

import random

# counts number of dice used
dice_quantity = 0

# stores total dice numbers add up to
total = 0


# helps control number of plays per round
game_round = 0

# lets user role dice 4 times
while game_round < 4:

    # user is to submit empty string
    user_input = input("Press enter to roll dice 🎲: ")
    print("===============================")
    
    # when users don't enter empty strings
    while not user_input == "":
        user_input = input("Just press enter to roll dice 🎲: ")
        print("===============================")
    
    # gets random side of dice
    rand_dice_side = random.randint(1, 6) # inside loop allows for different num each time
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

    # increases counter so while loop can end
    game_round += 1
