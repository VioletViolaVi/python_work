# Banking App

# user is greeted to their bank account
print("Welcome to your bank account. How can we help you?")
print(" ------ ")

# ---------------------------------------------------------------------------------------------------------------------------------------------- #
# functions

# updates user's option choices
def change_option():
        # asks user what they want to do next
        user_request = input("What would you like to do now? Enter number, 1) Deposit money, 2) Withdraw money, 3) Check balance, 4) Exit: ")
        print(" ------ ")
        return user_request

# ---------------------------------------------------------------------------------------------------------------------------------------------- #

# user picks which action they want to take
user_request =  input("Enter number, 1) Deposit money, 2) Withdraw money, 3) Check balance, 4) Exit: ") # returns strings!
print(" ------ ")
# helps user leave banking process
is_banking = True

# starts current balance amount as 100 (£)
current_balance = 100

# keeps user w/ in process as they have not quit
while is_banking:

    # keeps asking user to enter valid option until they enter a valid option
    # if users pick from outside of provided options
    while not user_request == "1" and not user_request == "2" and not user_request == "3" and not user_request == "4": # uses strings not numbers!
        user_request = input("Invalid option! Enter positive number, 1) Deposit money, 2) Withdraw money, 3) Check balance, 4) Exit: ")
        print(" ------ ")
        
    # user wants to deposit money into bank - keeps going until they choose a different option
    while user_request == "1": # uses string not number!
        
        # placed out of the while loop for the try/except section so users wont keep seeing this message when invalid entry occurs
        deposit_amount_str = input("Please enter amount you want to deposit: £ ")

        # continuously ensures to stop any input with '-' in front e.g. negative numbers -> this code is specifically made for these
        while deposit_amount_str[0] == "-":
            print(" ------ ")
            deposit_amount_str = input("Invalid option! Please enter a positive numerical amount: £ ")

        # keeps user in this try/except area until a valid entry in entered
        while True:

            # handles ValueError if user enters non numbers as deposit amount
            try:

                # converts string inputted amount into float number
                deposit_amount =  float(deposit_amount_str)

                # stops negative numbers coming through
                while deposit_amount < 0:
                    deposit_amount = float(input("Please enter an amount greater than 0: £ "))
                    print(" ------ ")                

                # stores the addition of deposit amount to current amount in account
                current_balance += deposit_amount

                # displays new balance after deposit
                print(" ------ ")
                print(f"Your new bank balance after deposit is £{current_balance:.2f}")

                # asks user what they want to do next
                print(" ------ ")
                user_request = change_option()                   

                # allows user to leave this try/except area once a valid number has been entered, so rest of code can work
                break

            # stops output from 'crashing'
            except ValueError:
                # shows readable message asking for number input instead
                print(" ------ ")
                deposit_amount_str = input("Invalid option! Please enter a positive numerical amount: £ ")

    # user wants to withdraw money from account
    while user_request == "2": # uses string not number!

        # gives user chance to change option if there's £0 in their bank account
        while current_balance == float(0) and user_request == "2":
            print(f"Your current balance: £{current_balance:.2f}")
            user_request = input("You have no funds left! Where to now? Enter number, 1) Deposit money, 2) Withdraw money, 3) Check balance, 4) Exit: ")
            print(" ------ ")
                   
        # stops rest of this while loop code being read if there's no money left to withdraw and user picks new option
        if current_balance != float(0):

            # placed out of the while loop for the try/except section so users wont keep seeing this message when invalid entry occurs
            withdrawal_amount_str = input("Please enter amount you want to withdraw: £ ")

            # continuously ensures to stop any input with '-' in front e.g. negative numbers -> this code is specifically made for these
            while withdrawal_amount_str[0] == "-":
                print(" ------ ")
                withdrawal_amount_str = input("Invalid option! Please enter a positive numerical amount: £ ")           
       
            # keeps user in this try/except area until a valid entry in entered
            while True:
                
                # handles ValueError if user enters non numbers as deposit amount
                try:

                    # asks user for amount of money they want to withdraw
                    withdrawal_amount =  float(withdrawal_amount_str)

                    # continuously checks if user has enough money to withdraw in 1st place
                    while withdrawal_amount > current_balance:
                        print(" ------ ")
                        print(f"Your current balance: £{current_balance:.2f}")
                        withdrawal_amount = float(input("You don't have enough funds! Enter a lower amount: £ "))
                        print(" ------ ")
                        
                        # stops negative numbers coming through
                        if withdrawal_amount < 0:
                            withdrawal_amount = float(input("Please enter an amount greater than 0: £ "))
                            print(" ------ ")
                                            
                    # calculates current amount left in account once money is taken
                    current_balance -= withdrawal_amount

                    # displays new balance after withdrawal
                    print(" ------ ")
                    print(f"Your new bank balance after withdrawal is £{current_balance:.2f}")

                    # asks user what they want to do next
                    print(" ------ ")
                    user_request = change_option()                    

                    # allows user to leave this try/except area once a valid number has been entered, so rest of code can work
                    break                

                # stops output from 'crashing'
                except ValueError:
                    # shows readable message asking for number input instead
                    print(" ------ ")
                    withdrawal_amount_str = input("Invalid option! Please enter a positive numerical amount: £ ") 

    # user wants to check bank balance
    while user_request == "3": # uses string not number!

        # displays current bank balance to user
        print(f"Your current bank balance is £{current_balance:.2f}")

        # asks user what they want to do next
        print(" ------ ")
        user_request = change_option()

    # user wants to leave
    if user_request == "4": # uses string not number!
        print("Thank you for banking with us! Bye!")
        is_banking = False
