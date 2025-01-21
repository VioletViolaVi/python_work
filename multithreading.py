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
# value using in function when called will be passed through in place of this parameter
def movie_watching(move_title):
    time.sleep(10)
    print()
    print(f"{move_title} movie ended!")

# microwaving the popcorn
def microwaving_popcorn():
    time.sleep(3)
    print()
    print("Microwave popcorn ready!")

# calling all functions
    # -  without multithreading, these functions get called in order of being called (see below)
        # - current order: 'You've finished eating the popcorn!' -> 'Microwave popcorn ready!' -> 'Movie ended!'
            # - this is because the functions are currently running on the same 'python thread'
            # - this order is 'out of step' for real world scenario so multithreading can help
# popcorn_eating()
# movie_watching()
# microwaving_popcorn()

# makes all functions start running at the same time
    # - using multithreading here print statements appear in different order
        # - 'Microwave popcorn ready!' -> 'You've finished eating the popcorn!' -> 'Movie ended!'
task_1 = threading.Thread(target=popcorn_eating)
task_1.start()

# str argument will be passed through respective function
task_2 = threading.Thread(target=movie_watching("Death by Rose")) # shout out to project 3 😉
task_2.start()

task_3 = threading.Thread(target=microwaving_popcorn)
task_3.start()

# to show before any threading begins
print()
print("Lets watch a movie! 🎥 🍿 🎬")

# makes last print statement (see below) appear after all threading has completed / all threads have been joined
task_1.join()
task_2.join()
task_3.join()

# to show after all threading has been completed
print()
print("Clean up time! 🫧 🧹 🧼")
