# script_2.py

# Notes
#   - from this file, when ran, output produces -> script_1.py __name__ == script_1
#       - script_1 is written instead of __name__ as code is being ran from this file not script_1.py


import script_1 # prints out hello world in output when this part is ran

# uses function from script_1.py file that was imported to this file
script_1.simple_func() # also prints out hello world in output when this part is ran

# - at this point, output shows hello world twice

# - at this point the code below is in script_1.py
# if __name__ == "__main__":
#     simple_func()  

# the code above in script_1.py makes this file only run hello world once as the condition in script_1.py has not been met for this file to run it
