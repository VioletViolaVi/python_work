# Multithreading

# Notes
# - multithreading is used to perform multiple tasks at the same time (think of this as multitasking)
# - multithreading is good for input output tasks
    # - examples included reading files, fetching data from APIs
        # - any activity that will take time to do & it is unknown when these activities will be completed
# - the 'threading' module is to be imported to carry out multithreading

# allows use of multithreading in python
import threading

# functions to emulate watching movie @ home
# eating popcorn
def popcorn_eating():
    print()
    print("You've finished eating the popcorn!")

# watching movie
def movie_watching():
    print()
    print("Movie ended!")

# microwaving the popcorn
def microwaving_popcorn():
    print()
    print("Microwave popcorn ready!")

