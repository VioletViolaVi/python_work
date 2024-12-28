# Variable Scope

# Notes:
# - variables defined w/ in local scope would not be accessible by other code outside it
# - scoping occurs in specific order of operations (FOR LOCATING VARIABLES)
#   - local -> enclosed -> global -> built in
#       - built in scope
#           - refers to accessing variables/functions/methods etc. that already exist in python
#           - e.g. print(), len(), range(), etc.


# functions w/ local scope as variables have been defined inside functions
def function_1():
    # local scope
    func_1 = 10
    print(func_1)

def function_2():
    # local scope
    func_2 = 5
    print(func_2)

function_1()
function_2()


print(" --- new --- ")


# 'nested' function/function inside another function - still using local scope
def outer_func():
    # will not be shown as the variable with the same name is found in the same local scope and as the 'print()' using it
    fave_colour = "green"
    def inner_func():
        # will be used & shown as 'print()' is w/ in same scope as 'fave_colour' variable it's using
        fave_colour = "purple"
        print(f"fav colour is: {fave_colour}")

# both functions needs to be called as seen below, in order to see output from 'print()'   
    inner_func()
outer_func()

print()

# enclosed scoping w/ function in function - now using enclosed scope
def outer_func():    
    fave_colour = "green" # enclosed scope
    def inner_func():
        # as there's no 'fave_colour' variable in this function (local scope) & this function is inside another function, the outer function is looked into to find if there's a 'fave_colour' variable fo use, otherwise, error.
        print(f"fav colour is: {fave_colour}") 
    inner_func()
outer_func()


print(" --- new --- ")


# global scoping
def function_3():
    # this 'func_1' doesn't refer to the variable written in the 1st function at top of page as that variable is local
    print(func_1)

# this is the 'func_1' variable 'function_3()' refers to as this variable has global scoping
func_1 = 3
function_3() # note the function had to be called after the global variable above had been declared and assigned, otherwise error!
