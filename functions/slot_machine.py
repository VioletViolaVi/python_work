# Slot Machine

import random, time

# functions ----------------------------------------------------------------------------------------------------------------------------


# to produce 3 different fruit icons
def slot_machine(fruit_icons, slot_result):

    # start counter to change in while loop to help prevent infinite loop
    counter = 0
    
    # helps ensures loop stops running after 3 times 
    while counter < 3:

        # get random whole number between 1 and 3 inclusively
        random_num = random.randint(1, 3)

        # get random fruit icon from dict
        random_icon = fruit_icons.get(random_num)

        # randomly puts 3 fruit icons in list 1 by 1
        slot_result.append(random_icon)

        # takes longer time to show fruit icons 1 @ a time - like a real slot machine
        time.sleep(1)

        match counter:
            # during 1st while loop iteration, display only 1st fruit icon
            case 0:
                print(slot_result[0])

            # during 2nd while loop iteration, display 1st & 2nd fruit icons
            case 1:
                print(f"{slot_result[0]}  {slot_result[1]}") 

            # during 3rd/last while loop iteration, display 1st, 2nd & 3rd fruit icons   
            case 2:
                print(f"{slot_result[0]}  {slot_result[1]}  {slot_result[2]}")  

            # if this is seen, something else has gone wrong!!!
            case _:
                print("Error!!! 💀 ")
    
        # increases counter to avoid infinite loop
        counter += 1

    # returns 3 different fruit icons in list
    return slot_result


# checks if the 3 fruit icons are the same i.e. checks if there's a jackpot
def jackpot(fruit_icons, slot_result):

    # the current 3 fruit icons gotten by user
    current_fruit_list = slot_machine(fruit_icons, slot_result)

    # converts current fruit icon list into a {set} which will remove any duplicates if present
    fruit_icons_set = set( current_fruit_list )

    # gets length of the {set} of fruit icons
    set_fruit_icons_len = len( fruit_icons_set )

    # checks if the length of the {set} fruit icons is the same as 1
    if set_fruit_icons_len == 1:

        # occurs if set only contains 1 fruit icon as duplicates are not allowed - the other 2 would have been the same therefore, jackpot!
        return "Jackpot!"
    else:

        # occurs if there's only 2 duplicates or all 3 are different as set would take in more than 1 fruit icon if they're not all the same
        return "not a jackpot"


# functions ----------------------------------------------------------------------------------------------------------------------------


# continuous play ----------------------------------------------------------------------------------------------------------------------------


# helps stops this file running automatically if this file is used in another file via imports 
def main():
    
    # helps make game continuous until user wants to stop playing
    is_playing = True

    # keeps track of game round number
    game_round_num = 0

    # helps make game continuous until user wants to stop playing - makes condition falsy
    while is_playing:
        
        # speaks to user
        print("---------                 ")
        print("   🎰 Lets Gamble? 🎰   ")
        print("                 ---------")
        print()

        # increases game round number by 1 before first/next round starts
        game_round_num += 1
        
        # shows which round user is on
        print(f"Round {game_round_num} 🏁🏇🚩")

        # dict containing all slot machine icons
        fruit_icons = {
            1: "🍋",
            2: "🍏",
            3: "🍉",
        }

        # stores fruits gotten when slot machine is pulled
        slot_result = []

        # informs user if the get a jackpot or not
        print(jackpot(fruit_icons, slot_result))

        # asks if user wants to keep playing
        user_request = input("Keep playing? 🎮 : Yes (Y) | No (N): ").lower()

        # stops users from entering any other key other than y or n
        while not user_request == "y" and not user_request == "n":
            user_request = input("Please only choose between Yes (Y) | No (N): ").lower()

        # stops game if user says yes
        match user_request:
            case "n":
                is_playing = False
                print("Thanks for playing! Goodbye! ⛳ ")
            case "y":
                is_playing = True
            case _:
                print("Error!!! 💀 ")


# continuous play ----------------------------------------------------------------------------------------------------------------------------


# running from this file ----------------------------------------------------------------------------------------------------------------------------

# stops this file running automatically if this file is used in another file via imports
if __name__ == "__main__":
    main()


# running from this file ----------------------------------------------------------------------------------------------------------------------------


# to do:
# - user starts off w/ money sum then is to lose money per play
# - user is to win money for jackpot
# - could allow user to win small amounts for 2 same fruit icons
# - state how much user won/lost