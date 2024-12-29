# Banking App (function focussed)

# stores users' selected option
print("Choose option: 1-4")
user_input = input("1. Check balance, 2. Make deposit, 3. Withdraw money, 4. Exit: ")
print(" ------ ")

# stores users' current amount of money they have
user_balance_global_scope = 100

# functions ----------------------------------------------------------------------------------------------------------------------------

# checks balance
def check_balance():

    # displays message to user regarding what their current balance is
    message = f"Your current balance is £{user_balance_global_scope:.2f}"

    # returns full message from above - needs printing in match case statements below
    return message


# deposits in balance (adds to balance)
def to_deposit(user_balance_local_scope): # passes parameter for argument value to be passed through

    # takes in user's deposit amount as a decimal & stores in variable
    deposit_amount = float(input("How much do you want to deposit into your account?: £ "))

    # adds inputted deposit amount into parameter
    user_balance_local_scope += deposit_amount

    # stores message informing user of current balance using parameter, after deposit input has been added to it
    current_balance = f"Your current balance is £{user_balance_local_scope:.2f}"

    # returns full message from above - needs printing in match case statements below
    return current_balance


# withdraws from balance
def withdraws_from_balance(user_balance_local_scope):

    # stores user's requested amount for withdrawal
    withdrawal_amount = float(input("How much do you want to withdraw from your account?: £ "))

    # removes withdrawal amount inputted by user from parameter representing user's current balance 
    #   - parameter gets replaced with argument value when function is called
    user_balance_local_scope -= withdrawal_amount
    
    # stores message informing user of current balance using parameter, after withdrawal input has been subtracted from it
    current_balance = f"Your current balance is £{user_balance_local_scope:.2f}"

    return current_balance


# leaves banking app
def leaves_bank_app():
    
    # stores message to say bye to user when they leave
    goodbye_message = "Thank you for banking with us. Goodbye."

    # returns full message from above - needs printing in match case statements below
    return goodbye_message


# functions ----------------------------------------------------------------------------------------------------------------------------

# helps prevent code running when this file is ran from different file's server
# will only run on other files when imported & then called instead of automatically 
def main():
    # controls what users see based on option they choose
    match user_input:
        case "1":
            print(check_balance())
        case "2":
            print(to_deposit(user_balance_global_scope))
        case "3":
            print(withdraws_from_balance(user_balance_global_scope))
        case "4":
            print(leaves_bank_app())
        case _:
            print("Error!")

# so functions in this file don't have to be run from this file's server
if __name__ == "__main__":
    main()
