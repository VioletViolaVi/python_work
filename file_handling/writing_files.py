# Writing Files

# imported to work w/ json file (@ bottom)
import json

# to output data
txt_data = "This is a string to be seen in a '.txt' document."

# stores name of file, including extension
    #   - file path chosen below is a relative file path
file_path = "file_handling/test.txt"

# to create a file
# features of code below:
    # 'with' is a statement used to wrap blocks of code for execution
    # 'with' statement will close file once code is done using it
        # - prevents need to manually close files
        # - important to close files once done w/ them being opened to avoid unexpected behaviours occurring
            # - it's good practice
    # 'open()' function returns file object
        # -  1st parameter/placeholder in 'open()' function is for the file path (file)
        # -  2nd parameter/placeholder in 'open()' function is the mode
            #   types of modes:
                #   - 'w' means write
                    #   - will create new file from scratch
                    #   - can also overwrite same file
                #   - 'x' means also means write but will only do so if the file doesn't exist already otherwise an error will be thrown (FileExistsError)
                #   - 'a' means to append file
                #   - 'r' means read
    # 'as' keyword is used to give with statement a name to be know as within the code
        # - example below means file object output given out by the 'with' statement will be called 'file'
with open(file=file_path, mode="w") as file:

    # to write to 'file'
    # actual '.txt' file of 'file_handling/test.txt' was made & can be found in VS Code's Explorer (left hand side)
    # written string from 'txt_data' variable can also be seen in this '.txt' file
    file.write(txt_data)

    # confirmation message
    print()
    print(f"(from desktop) [created/written] file location: '{file_path}'")


print()
print(" --- next --- ")
print()


# output '.txt' file to laptop home (outside of vs code)

# stores "string" data
txt_data_2 = "This should be seen on the landing page of this laptop."

# stores file name
    #   - uses an absolute file path
file_path_2 = "C:/Users/vivia/OneDrive/Desktop/test_2.txt"

# using try/except to avoid 'FileExistsError' if 'x' mode is used when file already exists
try:
    # creates file
    with open(file=file_path_2, mode="a") as file:

        # writes 'file'
        # adds new line after string is printed in '.txt' file
        file.write(txt_data_2 + "\n")

        # shows in terminal when file is written
        print(f"(from desktop) file location: '{file_path_2}'")

# this block of code will run if 'x' mode is used in 'with', when file had already been created
except FileExistsError:
    print("The file you're trying to create already exists! Stop it! 🛑")


print()
print(" --- next --- ")
print()


# working with collections whilst file handling

# stores [list] data
spies = ["Sam", "Clover", "Alex"]

# stores file name
file_path_3 = "C:/Users/vivia/OneDrive/Desktop/test_3.txt"

# creates file
with open(file=file_path_3, mode="w") as file:

    # writes 'file'
    # to write over [list], the [list] must be iterated over via a loop
        #   - CANNOT put in the brackets of the 'write()' method the [list] directly
            #   - i.e. 'file.write(spies)' is wrong
    for spy in spies:

        # 'spy' is a string each now that can go in the brackets of the 'write()' method
        # '\n' or ' ' (space bar) stops strings from being shown on '.txt' file squashed together
        file.write(spy + " ")

    # shows in terminal when file is written
    print(f"(from desktop) json file: '{spies}' file location: '{file_path_3}'")


print()
print(" --- next --- ")
print()


# working with '.json' files for file handling
# '.json' files are made up of 'key:value' pairs

# stores {dictionary} data
spies_colours = {
    "Sam": "green", 
    "Clover": "red", 
    "Alex": "yellow"
    }

# stores file name
# file extension changed to '.json' (no longer '.txt')
file_path_4 = "C:/Users/vivia/OneDrive/Desktop/test_4.json"

# creates file
with open(file=file_path_4, mode="w") as file:

    # uses imported json module
    # 'dump()' method converts dictionaries to json string for outputting data
        #   - takes in json data as value inside its brackets
            #   - 'spies_colours' is the dictionary in this case (see above)
        #   - also takes in 2nd argument/value of 'file' from 'with' statement
        #   - 'TypeError' is thrown if 2 arguments/values are not passed through
    json.dump(spies_colours, file)

    # print statement appears in terminal once file is written (& on desktop)
    print(f"(from desktop) json file: '{spies_colours}' file location: '{file_path_4}'")
