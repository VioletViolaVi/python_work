# Slot Machine

import random

# functions ----------------------------------------------------------------------------------------------------------------------------



# to check if 3 in a row occurs
def slot_machine(fruit_icons, slot_result):

    # start counter to change in while loop to help prevent infinite loop
    counter = 0
    
    # helps ensures loop stops running after 3 times 
    while counter < 3:

        # get random whole number between 1 and 3 inclusively
        random_num = random.randint(1, 3)

        # get random icon from dict
        random_icon = fruit_icons.get(random_num)

        # randomly puts 3 fruit icons in list 1 by 1
        slot_result.append(random_icon)

        # increases counter to avoid infinite loop
        counter += 1

    # returns 3 different fruit icons in list
    return slot_result


# functions ----------------------------------------------------------------------------------------------------------------------------


# helps stops this file running automatically if this file is used in another file via imports 
def main():

    # speaks to user
    print("Wanna play? 🎰 ")
    print("  --- --- ---  ")

    # dict containing all slot machine icons
    fruit_icons = {
        1: "🍋",
        2: "🍏",
        3: "🍉",
    }

    # stores fruits gotten when slot machine is pulled
    slot_result = []

    # calls function, passes through fruit icon dict & slot machine result list, respectively
    print(slot_machine(fruit_icons, slot_result))


# stops this file running automatically if this file is used in another file via imports
if __name__ == "__main__":
    main()
