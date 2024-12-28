# Variable Scope

# Notes:
# - variables defined w/ in local scope would not be accessible by other code outside it
# - 
# - 

# functions w/ local scope as variables have been defined inside functions
def function_1():
    func_1 = 10
    print(func_1)

def function_2():
    func_2 = 5
    print(func_2)

function_1()
function_2()
