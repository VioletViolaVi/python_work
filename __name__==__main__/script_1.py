# script_1.py

# Notes
#   - from this file, when ran, output produces -> script_1.py __name__ == __main__


# shows in output when code is ran from this file
# __name__ becomes __main__
print(f"script_1.py __name__ == {__name__}")

print()

# simple function made, for printing 'hello world' so script_2.py can be checked to see if the file runs it
def simple_func():
    print("Hello World!")
simple_func()
