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
    
    # this code runs when error occurs, more specifically when input is not a number e.g. string got entered instead
    except ValueError:
        print()
        print("That's not a number! 😠")
        
        # stops while loop here & makes user start again from while loop beginning
        continue

    # this code is used as a last resort as using it as the only exception rule is bad practice
    # 'Exception' covers all possible errors
        #   - using this therefore will not inform users on what specifically went wrong, which is bad practice
    except Exception:
        print()
        print("Something has gone wrong! - we don't know what, this exception is too generic! 😭")
        
        # stops while loop here & makes user start again from while loop beginning
        continue
