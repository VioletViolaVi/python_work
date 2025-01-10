# Reading Files - '.txt', '.json', 'csv'

# needed to use methods from json module to read '.json' files
# need to import csv module to read csv files
import json, csv

# ----------------------------------- '.txt'file
# absolute file path for '.txt' file
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

        # displays this long string
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


print()
print(" --- new --- ")
print()


# absolute file path for '.json' file
file_path = "C:/Users/vivia/OneDrive/Desktop/test_2.json"

# using try/except exceptions
try:
    with open(file=file_path, mode="r") as file:
        
        # to read contents of a '.json' file
        container = json.load(file)

        # displays '.json' file contents
        print()
        print(container)

        # to access values from'.json' file using keys
        print()
        print(container["Clover"]) # red
        print(container["Alex"]) # yellow
        print(container["Sam"]) # green

# 'FileNotFoundError' occurs when '.json' file cannot be found (according to the entered file path in the string)
except FileNotFoundError:
    print()
    print("This file cannot be found!")

# 'PermissionError' occurs when user doesn't have permission to view the '.json' file
except PermissionError:
    print()
    print("You do not have permission to read this file!")


print()
print(" --- new --- ")
print()


# reading '.csv' files
file_path = "C:/Users/vivia/OneDrive/Desktop/test_3.csv"

# using try/except exceptions
try:
    with open(file=file_path, mode="r") as file:
        
        # 'reader()' method reads csv file
            # this results to a memory address being saved in variable
        file_content = csv.reader(file)

        # displays content of csv file
        # csv files need to be read line by line
            # all data in inside a collection that needs to be iterated over
        print()
        print(file_content)
        print()

        # iterating through collection to avoid getting memory address & get values instead
        for line in file_content:
            # indexing e.g. 'print(line[1])' can be used to get specific columns
            print(line)

# 'FileNotFoundError' occurs when '.csv' file cannot be found (according to the entered file path in the string above)
except FileNotFoundError:
    print()
    print("This file cannot be found!")

# 'PermissionError' occurs when user doesn't have permission to view the '.csv' file
except PermissionError:
    print()
    print("You do not have permission to read this file!")
