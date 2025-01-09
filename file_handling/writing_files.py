# Writing Files

# Notes:
# - 


# to output data
txt_data = "This is a string to be seen in a .txt document."

# stores name of file, incl. extension
    #   - file path chosen below is a relative file path
file_path = "test.txt"

# to create a file
# features of code below:
    # 'with' is a statement used to wrap blocks of code for execution
    # 'with' statement will close file once code is done using it
        # - prevents need to manually close files
        # - important to close files once done w/ them being opened to avoid unexpected behaviours occurring
    # 'w' means write
with open(file_path, "w") as file:
    pass
