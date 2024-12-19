# Interest Amount Calculator

# formula: interest amount = start balance * interest rate * time
instruction = input("Let's work out your interest rate.")

start_balance = float(input("Enter your start balance: "))
while start_balance < 0:
    print("Please enter a valid start balance.")
    start_balance = float(input("Enter your start balance: "))

interest_rate = float(input("Enter your interest rate: "))
while interest_rate < 0:
    print("Please enter a valid interest rate.")
    interest_rate = float(input("Enter your interest rate: "))

time = int(input("Enter the amount of time in years: "))
while time < 0:
    print("Please enter a valid amount of time in years.")
    time = int(input("Enter the amount of time in years: "))

interest_amount = start_balance * interest_rate * time
print(f"Your interest amount is: £{interest_amount:.2f}")
