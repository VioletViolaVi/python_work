# Decorator

# Notes:

# decorator is a function that extends the behaviour of another function 
# decorators don't make changes to the original base function they are added to 
# base functions are passed through decorator function as an argument/value


# creating a decorator
# use this format for creating decorators
# pass through base function in brackets '(...)' as the argument/value
def add_sugar(func_param):

    # inner function required to stop decorator from outputting contents of base function, w/out the base function making the call
        #   -  the '@add_sugar' decorator will cause print statements to be outputted in terminal despite 'bake_cake()' not being called
    def layer():

        # function being passed through as the argument/value gets called inside inner function
        print()
        print("Add sugar! 🍚")
        func_param()
    
    # returns entire function
    # 'layer' NOT 'layer()' as TypeError occurs
        #   - TypeError: 'NoneType' object is not callable
    return layer


# creating more decorators
def add_butter(func_param):
    def inner_layer():
        print()
        print("Add butter! 🧈")
        func_param()
    return inner_layer

def add_eggs(func_param):
    def inner_layer():
        print()
        print("Add eggs! 🍳")
        func_param()
    return inner_layer

def add_flour(func_param):
    def inner_func():
        print()
        print("Add flour! 💐")
        func_param()
    return inner_func

def add_milk(func_param):
    def inner_func():
        print()
        print("Add milk! 🥛")
        func_param()
    return inner_func


# decorator added on code line above base function
# makes its function above run
# this decorator makes no changes to the base function below, it merely extends it
@add_sugar
# more than 1 decorator can be added
@add_butter
@add_eggs
@add_flour
@add_milk
# base function
def bake_cake():
    print()
    print("The cake is baked! 🍰")

bake_cake()