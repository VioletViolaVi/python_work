# Arguments (*args) and Keyword Arguments (**kwargs)

# Notes
    # - *args and **kwargs are used when you want to accommodate for any number of arguments, at any time, to be passed through function when it's
    # - 'args' and 'kwargs' don't have to be used but they are convention among developers
        # - '*' and '**' are what's important to add in 'def python_func()' brackets
            # - e.g. *test, **test_dict, *example, **example_dict, etc.
    # - '*' stores arguments in tuple
    # - '**' stores arguments in dictionaries
    # Example:
    #
    # def add_nums_error(num1, num2):
    #     return num1 + num2
    #   -----------------------    
    # print( add_nums_error(2,2,2) ) --> w/ out '*' putting more than 2 arguments when calling function leads to error


 # corrected code for adding values
def add_nums_corrected(*args):
    print(f"'*args' tuple: {args}") # e.g. (2, 2, 2, 2)
    print(f"'*args' length: {len(args)}") # e.g. 4

    total = 0
    # iterates through length of tuple i.e. *args
    for num in range( len(args) ):
        # gets values in tuple i.e. *args via indexing
        total += args[num]
        print(f"for loop totals: {total}")
    return total

# print out return value from function
    # - value is all arguments added via for loop in function, throughout length of tuple
print(f"total: {add_nums_corrected(2,2,2,2)}")


print()
print("------ new ------")


# taking school register
def school_register(*args):
    print("The following is the school register:")
    # concatenate 'student' strings into names variable
    names = ""
    # keeps iterating for length of *args tuple
    for tuple_item_index in range(len(args)):
        names += f"{args[tuple_item_index]} - present ✔️ \n" # 'student' strings 
    return names

    # # prints out names via iteration
    # for tuple_item_index in range(len(args)):
    #     print(f"{args[tuple_item_index]} - present ✔️")    

students = school_register("Milo", "Jake", "Fizz", "Bella", "Max", "Judy")
print(students)
# for print() commented out in function above
# school_register("Milo", "Jake", "Fizz", "Bella", "Max", "Judy")


print()
print("------ new ------")


