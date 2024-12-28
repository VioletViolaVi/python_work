# Banking App

# user is greeted to their bank account
print("Welcome to your bank account. How can we help you?")
print(" ------ ")

# user picks which action they want to take
user_request =  input("Enter number 1) Deposit money, 2) Withdraw money, 3) Check balance, 4) Exit: ") # returns strings!
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
        user_request = input("Invalid option! Enter number 1) Deposit money, 2) Withdraw money, 3) Check balance, 4) Exit: ")
        print(" ------ ")

    # displays current bank balance
    print(f"Your current bank balance is £{current_balance:.2f}")
    print(" ------ ")
        
    # user wants to deposit money into bank - keeps going until they choose a different option
    while user_request == "1": # uses string not number!

        # converts string inputted amount into float number
        deposit_amount =  float(input("Please enter amount you want to deposit: £ "))

        # stores the addition of deposit amount to current amount in account
        current_balance += deposit_amount

        # displays new balance after deposit
        print(" ------ ")
        print(f"Your new bank balance after deposit is £{current_balance:.2f}")
        print(" ------ ")

        # asks user what they want to do next
        user_request = input("What would you like to do next? Enter number 1) Deposit money, 2) Withdraw money, 3) Check balance, 4) Exit: ")
        print(" ------ ")

    # user wants to withdraw money from account
    while user_request == "2":

        # asks user for amount of money they want to withdraw
        withdrawal_amount =  float(input("Please enter amount you want to withdraw: £ "))
        
        # calculates current amount left in account once money is taken
        current_balance -= withdrawal_amount

        # displays new balance after withdrawal
        print(" ------ ")
        print(f"Your new bank balance after withdrawal is £{current_balance:.2f}")
        print(" ------ ")

        # asks user what they want to do next
        user_request = input("What would you like to do next? Enter number 1) Deposit money, 2) Withdraw money, 3) Check balance, 4) Exit: ")
        print(" ------ ")






