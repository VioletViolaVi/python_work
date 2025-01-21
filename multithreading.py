# Multithreading

# Notes
# - multithreading is used to perform multiple tasks at the same time (think of this as multitasking)
# - multithreading is good for input output tasks
    # - examples included reading files, fetching data from APIs
        # - any activity that will take time to do & it is unknown when these activities will be completed
# - the 'threading' module is to be imported to carry out multithreading

# 'threading': allows use of multithreading in python
# 'time': used to delay outputs from functions below
import threading, time

# functions to emulate watching movie @ home
# eating popcorn
def popcorn_eating():
    time.sleep(7)
    print()
    print("You've finished eating the popcorn!")

# watching movie
def movie_watching():
    time.sleep(10)
    print()
    print("Movie ended!")

# microwaving the popcorn
def microwaving_popcorn():
    time.sleep(3)
    print()
    print("Microwave popcorn ready!")

# calling all functions
    # -  without multithreading, these functions get called in order of there appearance
        # - this order is 'out of step' for real world scenario so multithreading can help
popcorn_eating()
movie_watching()
microwaving_popcorn()