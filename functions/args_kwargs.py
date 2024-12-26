# Arguments (*args) and Keyword Arguments (**kwargs)

# Notes
    # - *args and **kwargs are used when you want to accommodate for any number of arguments, at any time, to be passed through function when it's
    # - 'args' and 'kwargs' don't have to be used but they are convention among developers
        # - '*' and '**' are what's important to add in 'def python_func()' brackets
            # - e.g. *test, **test_dict, *example, **example_dict, etc.
    # - '*' stores arguments in tuple
    # - '**' stores arguments in dictionaries
    #
    # Error example for *args:
    #
    # def add_nums_error(num1, num2):
    #     return num1 + num2
    #   -----------------------    
    # print( add_nums_error(2,2,2) ) --> w/ out '*' putting more than 2 arguments when calling function leads to error


# *args
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


# list out foods
# '*foods' used as any parameter/placeholder name can be used w/ '*'
def foods(*foods):
    # iterates throughout *foods tuple
    for num in range(len(foods)):
        # avoids printing out 0. first
        print(f"{num+1}. {foods[num]}")

foods("pizza", "burger", "pie", "chips", "soup", "curry", "rice")


print()
print("------ new ------")


# *kwargs 
# printing out addresses
def produce_address(**kwargs):
    print()
    print(f"*kwargs: {kwargs}")
    print()
    print(f"key: {kwargs.keys()}, value: {kwargs.values()}")
    print()

    for key, value in kwargs.items():
        print(f"{key}: {value}")

produce_address(building_num=1, 
                street="Test Street", 
                city="Test City", 
                country="UK", 
                post_code="ab1 cd2")

produce_address(building_num=789, 
                street="Jam Lane", 
                city="Tower City",
                county="Ham-shire",
                country="UK", 
                post_code="ef5 h98",)

produce_address(flat_num="66a", 
                street="Filler Road", 
                city="Goldstone",
                post_code="HJ5 N34",)


print()
print("------ new ------")


# printing out capital cities
def capital_cities(**capitals):
    print(f"**capitals: {capitals}")

    # produce sentences using keys, values
    for key, value in capitals.items():
        print()
        print(f"The capital of the {key.capitalize() if not key == 'uk' else key.upper()} is {value}.")
        print()

capital_cities(uk="London",
               china="Beijing",
               japan="Tokyo",
               ghana="Accra",
               )

capital_cities(uk="London",
               japan="Tokyo",
               ghana="Accra",
               )

capital_cities(ghana="Accra",
               china="Beijing",
               )

