# Reading Files - '.txt', '.json', 'csv'

# ----------------------------------- '.txt'file
# absolute file path
file_path = "C:/Users/vivia/OneDrive/Desktop/test_1.txt"

# using try/except exceptions
try:
    # 'with' is a statement
    # 'with' wraps block of code w/in a context manager
    # 'with' will close a file after being opened
        # good practice to close files that have been opened
            # if file is not closed, it could cause unexpected behaviour
    # 'open()' function takes 2 arguments
        # file path & mode
    # 'open()' function returns a file object
        # 'file' is the name this 'open()' function has been given
        # 'file' is now a file object
    # 'r' is for reading files
    with open(file=file_path, mode="r") as file:
        
        # 'read()' method will read the file object (file)
            # reading 'file' object will return 1 long string
                # this long string is stored in this variable
        long_str_container = file.read()

        # display this long string
        print()
        print(long_str_container)

# 'FileNotFoundError' occurs when file cannot be found (according to the entered file path in the string)
except FileNotFoundError:
    print()
    print("This file cannot be found!")

# 'PermissionError' occurs when user doesn't have permission to view the file
except PermissionError:
    print()
    print("You do not have permission to read this file!")
