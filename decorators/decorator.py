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
    def layer():

        # function being passed through as the argument/value gets called inside inner function
        print()
        print("Add sugar!🍚")
        func_param()
    
    # returns entire function
    # 'layer' NOT 'layer()' as TypeError occurs
        #   - TypeError: 'NoneType' object is not callable
    return layer

# decorator added on code line above base function
# makes its function above run
# this decorator makes no changes to the base function below, it merely extends it
@add_sugar
# base function
def bake_cake():
    print()
    print("The cake is baked! 🍰")

bake_cake()