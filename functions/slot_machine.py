# Slot Machine

import random

# functions ----------------------------------------------------------------------------------------------------------------------------


print("Wanna play? 🎰")

# dict containing all slot machine icons
icons = {
    1: "🍋",
    2: "🍏",
    3: "🍉",
}

# stores fruits gotten when slot machine is pulled
slot_result = []

# to check if 3 in a row occurs
def slot_machine():

    # start counter to change in while loop to help prevent infinite loop
    counter = 0
    
    # helps ensures loop stops running after 3 times 
    while counter < 3:

        # get random whole number between 1 and 3 inclusively
        random_num = random.randint(1, 3)

        # get random icon from dict
        random_icon = icons.get(random_num)

        # randomly puts 3 icons in list 1 by 1
        slot_result.append(random_icon)

        # increases counter to avoid infinite loop
        counter += 1

    return slot_result

print(slot_machine())


# functions ----------------------------------------------------------------------------------------------------------------------------


# helps stops this file running automatically if this file is used in another file via imports 
def main():
    pass

# stops this file running automatically if this file is used in another file via imports
if __name__ == "__main__":
    main()
