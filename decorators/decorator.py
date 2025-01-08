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
    # *args & **kwargs used to allow for any number of values to be passed through this function, when called
    # this is where parameters are placed if base function is called whilst passing value(s) through
    def layer(*args, **kwargs):

        # function being passed through as the argument/value gets called inside inner function
        print()
        print("Add sugar! 🍚")

        # *args & **kwargs used to allow for any number of values to be passed through this function, when called
        # this is where parameters are placed if base function is called whilst passing value(s) through
        func_param(*args, **kwargs)
    
    # returns entire function
    # 'layer' NOT 'layer()' as TypeError occurs
        #   - TypeError: 'NoneType' object is not callable
    return layer


# creating more decorators
def add_butter(func_param):
    
    # *args & **kwargs used to allow for any number of values to be passed through this function, when called
    # this is where parameters are placed if base function is called whilst passing value(s) through
    def inner_layer(*args, **kwargs):
        print()
        print("Add butter! 🧈")

        # *args & **kwargs used to allow for any number of values to be passed through this function, when called
        # this is where parameters are placed if base function is called whilst passing value(s) through
        func_param(*args, **kwargs)
    return inner_layer

def add_eggs(func_param):

    # *args & **kwargs used to allow for any number of values to be passed through this function, when called
    # this is where parameters are placed if base function is called whilst passing value(s) through    
    def inner_layer(*args, **kwargs):
        print()
        print("Add eggs! 🍳")

        # *args & **kwargs used to allow for any number of values to be passed through this function, when called
        # this is where parameters are placed if base function is called whilst passing value(s) through        
        func_param(*args, **kwargs)
    return inner_layer

def add_flour(func_param):

    # *args & **kwargs used to allow for any number of values to be passed through this function, when called
    # this is where parameters are placed if base function is called whilst passing value(s) through   
    def inner_func(*args, **kwargs):
        print()
        print("Add flour! 💐")

        # *args & **kwargs used to allow for any number of values to be passed through this function, when called
        # this is where parameters are placed if base function is called whilst passing value(s) through           
        func_param(*args, **kwargs)
    return inner_func

def add_milk(func_param):

    # *args & **kwargs used to allow for any number of values to be passed through this function, when called
    # this is where parameters are placed if base function is called whilst passing value(s) through     
    def inner_func(*args, **kwargs):
        print()
        print("Add milk! 🥛")

        # *args & **kwargs used to allow for any number of values to be passed through this function, when called
        # this is where parameters are placed if base function is called whilst passing value(s) through        
        func_param(*args, **kwargs)
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
def bake_cake(cake_type):
    print()
    print("The cake is baked! 🍰")
    print()
    print(f"The type of cake baked is {cake_type}! 🥕")

# if base function gets called w/ value passed through, parameter/placeholders will need to be put in decorator functions (see above)
bake_cake("carrot")
