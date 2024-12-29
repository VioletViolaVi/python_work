# Banking App (function focussed)

# stores users' selected option
print("Choose option: 1-4")
user_input = input("1. Check balance, 2. Make deposit, 3. Withdraw money, 4. Exit: ")

# stores users' current amount of money they have
user_balance = 100

# functions ----------------------------------------------------------------------------------------------------------------------------

# helps prevent code running when this file is ran from different file's server
def main():
    # checks balance
    def check_balance():
        message = f"Your current balance is {user_balance:.2f}"
        return message

    # deposits in balance (adds to balance)
    def to_deposit():
        deposit_amount = float(input("How much do you want to deposit into your account?: £ "))
        user_balance += deposit_amount
        return user_balance

    # withdraws from balance
    def withdraws_from_balance():
        withdrawal_amount = float(input("How much do you want to withdraw from your account?: £ "))
        user_balance -= withdrawal_amount
        return user_balance

    # leaves banking app
    def leaves_bank_app():
        print("Thank you for banking with us. Goodbye.")

# functions ----------------------------------------------------------------------------------------------------------------------------

# so functions in this file don't have to be run from this file's server
if __name__ == "__main__":
    main()
