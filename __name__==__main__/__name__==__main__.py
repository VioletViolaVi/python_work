# __name__ == "__main__"

# Notes
# __name__ == "__main__" means the .py it's in can be imported into other files or it can run on its own
    # - functions & methods in .py files that contain the __name__ == "__main__" can be used w/ out running the main block of code in the file when the conditional statement is used i.e. if __name__ == "__main__":

# examples when you'd want to import functions/methods from .py files w/ out their main function body running:
    # - importing modules like math, random, time, os, etc.
        # - if not, outputs like what the help() produces will be created i.e. the full help page
            # - this way help pages can be made to run only if they are being ran directly

# __name__ == "__main__" 
    # - helps avoid unintentional execution of code
    # - makes code more modular
    # - makes code more readable
    # - leaves no global variables 

# provided list of attributes available
print(dir())

# prints out __main__
print(__name__)
