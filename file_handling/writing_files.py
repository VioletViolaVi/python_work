# Writing Files

# Notes: (see below)


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
    print(f"{file_path} has been created.")


print(" --- next --- ")


# output '.txt' file to laptop home (outside of vs code)

# outputs data
txt_data_2 = "This should be seen on the landing page of this laptop."

# stores file name
    #   - uses an absolute file path
file_path_2 = "C:/Users/vivia/OneDrive/Desktop/test_2.txt"

# using try/except to avoid 'FileExistsError' if 'x' mode is used when file already exists
try:
    # creates file
    with open(file=file_path_2, mode="w") as file:

        # writes 'file'
        file.write(txt_data_2)

        # shows in terminal when file is written
        print(f"So, '{file_path_2}' has been created on the landing page of this laptop.")

# this block of code will run if 'x' mode is used in 'with', when file had already been created
except FileExistsError:
    print("The file you're trying to create already exists! Stop it! 🛑")
