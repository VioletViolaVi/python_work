# File Detection

# Notes

# os module needs to be imported to give python a way to interact with the operating system
    #   - os means 'operating system'
# relative file path
    #   - this path states how to get to the file from your current directory (the file location you are currently working from e.g. THIS '.py' file)
# absolute file path 
    #   - this states how to access the file from the root of the file system

# need to import to be able to detect files
import os

# variable contains string that matches the real file path of the 'test_file.txt' file
# add folder in file path as file is in folder
file_path = "file_handling/test_file.txt"

# finds out if file exists in director
print(os.path.exists(file_path)) # True
if os.path.exists(file_path):
    print("Yes this file exists.")
else:
    print("No this file does not exists.")
