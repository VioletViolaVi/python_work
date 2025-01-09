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
# folder needs to be included inside file path as .txt file is in folder
relative_file_path = "file_handling/test_file.txt"

# finds out if file exists in directory
if os.path.exists(relative_file_path):
    print("Yes this file exists.")
else:
    print("No this file does not exists.")

print(os.path.exists(relative_file_path)) # True
print()


# for absolute file paths
# this file path is for a .txt doc 'stored' as this laptop's windows screen (w/ the sims game icons)
absolute_file_path = "C:/Users/vivia/OneDrive/Desktop/hello/outer_test"

# finds out if file exists in directory
if os.path.exists(absolute_file_path):
    print("Yes this file exists.")
    print()

    # to check if file is really a file & not a directory (folder)
    if os.path.isfile(absolute_file_path):
       
       # the file path value put in the variable will determine if it a file or folder NOT where the file is located
        #   - i.e., if u put file in folder but you write the path all the way up to the file name, os.path.isfile() will see this as a file
            #   - the file name in the path is where you stopped, not the folder
                #   - '...... /hello/outer_test' - > file!!!  '...... /hello' - > folder!!!
                    #   - all depends on how much you write in path
       print("Yes. This is a file, not a folder.")
    else:
        print("No. This is a directory.")
else:
    print("No this file does not exists.")

print(os.path.exists(absolute_file_path)) # True
