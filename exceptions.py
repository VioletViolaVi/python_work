# Exceptions

# Notes

# exceptions are events that interrupt regular flow of programs
# some types of exceptions include (there's a lot more 📜):
    #   - ArithmeticError
    #   - IndentationError
    #   - ValueError
    #   - ZeroDivisionError
    #   - AttributeError
    #   - etc.
# try/except/finally blocks are created to handle exception errors
    #   - 'try' portions run when code doesn't produce an error
    #   - 'except' portions run when code causes an error
    #   - 'finally' portions always run regardless of whether the 'try' or 'except' portions ran


# allows user to keep entering input when prompted until they give valid input that doesn't throw an error
keep_running = True
while keep_running:
    # try/except/finally block
    # this code is executed when no errors occur
    try:
        print()

        # considered dangerous code as it comes from users, who could write anything & have program throw errors
            #   - hence input cleaning is needed
        user_input = int(input("Enter a number to divide by 5: "))
        print()

        # divide whatever the input is (converted to an int by this point) by 5
        end_result = user_input / 5

        # format result in string
        print(f"Calculation: {user_input} (your number) / 5 = {int(end_result)}")

        # put end to while loop running again
        keep_running = False
