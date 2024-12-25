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
        # add to total
        total += rand_dice_side
        
        # 'one' side
        print("+-------+")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("+-------+")

        print(f"You rolled {rand_dice_side}")
    elif rand_dice_side == 2:
        # add to total
        total += rand_dice_side

        # 'two' side
        print("+-------+")
        print("| O     |")
        print("|       |")
        print("|     O |")
        print("+-------+")

        print(f"You rolled {rand_dice_side}")
    elif rand_dice_side == 3:
        # add to total
        total += rand_dice_side
        
        # 'three' side
        print("+-------+")
        print("| O     |")
        print("|   O   |")
        print("|     O |")
        print("+-------+")

        print(f"You rolled {rand_dice_side}")
    elif rand_dice_side == 4:
        # add to total
        total += rand_dice_side
        
        # 'four' side
        print("+-------+")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print("+-------+")

        print(f"You rolled {rand_dice_side}")
    elif rand_dice_side == 5:
        # add to total
        total += rand_dice_side
        
        # 'five' side
        print("+-------+")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("+-------+")

        print(f"You rolled {rand_dice_side}")
    elif rand_dice_side == 6:
        # add to total
        total += rand_dice_side
        
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

    # keeps track of number of dice rolled
    dice_quantity += 1

    # displays number of dice rolled as game is played
    print(f"Number of dice rolled: {dice_quantity}")
    print("===============================")

    # displays total as game is played
    print(f"Your current dice total is: {total}")
    print("===============================")

# displays final total at end of game
print(f"Your final dice total is: {total}")
print("===============================")
