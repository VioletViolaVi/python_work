# script_1.py

# Notes
#   - from this file, when ran, output produces -> script_1.py __name__ == __main__


# shows in output when code is ran from this file
# __name__    becomes    __main__
print(f"script_1.py __name__ == {__name__}")

print()

# simple function made, for printing 'hello world' so script_2.py can be checked to see if the file runs it
def simple_func():
    print("Hello World!")

# - controls if script_2.py will be able to run this function from this file or if it can only run the called function from the called function written in its own file
#   - code below will not allow script_2.py from running the function from this file
if __name__ == "__main__": # this is asking if you are running the file directly, if yes = truthy, if no = falsy
    simple_func()  
