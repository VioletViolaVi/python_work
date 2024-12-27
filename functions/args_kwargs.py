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


print()
print("------ new ------")


# shopkeeper inventory
def shop_inventory(**inventory):
    print(f"inventory: {inventory}")
    print()
    
    # gets values from dictionary & stores in list
    values = []
    for key_name in inventory:
        values.append(inventory[key_name])
    
    print(f"values: {values}")
    print()

    # uses values of dictionary to complete formatted string sentence
    return f"{values[0].title()} is priced at £{float(values[1]):.2f}. It has sold {values[2]} units and still has {values[3]} units left."
    

print(shop_inventory(product_name="birds eye chicken breast",
               price=4.89,
               products_sold=110,
               products_left=90,))
    

print(shop_inventory(product_name="duck curry & lamb hotpot soup",
               price=89.41,
               products_sold=23,
               products_left=177,))
    

print(shop_inventory(product_name="cream vanilla and frosted sticky coffee sorbet",
               price=19.70,
               products_sold=154,
               products_left=46,))


print()
print("------ new ------")


# using both *args & **kwargs
# generate billing addresses
def billing_address(*args, **kwargs):

    # iterates through values in tuple
    for item in args:
        print(item)
    print()
    # iterates through keys in dictionary to get values
    for value in kwargs.values():
        print(value)
    print()

    # '\' at end & front helps stop line of code being too long, output same as if it were to stay on same line
    return f"Address:\n{args[0]} {args[1]} {args[2]} {args[3]}\
    \
    \n{kwargs.get('house_num') if kwargs.get('house_num') != None else kwargs.get('apt_num')} {kwargs.get('street_name')}\
    \
    \n{kwargs.get('town')}\n{kwargs.get('post_code')}"


print(billing_address("Mrs", "Jane", "Ann", "Doe",
                house_num=101,
                street_name="Garden Street",
                town="Utopia",
                post_code="GH1 6DW"))
print()


print(billing_address("Mr", "Dave", "Luke", "Smith",
                house_num=89,
                street_name="Hopes St.",
                town="Arcane Falls",
                post_code="AB4 8PL"))
print()


print(billing_address("Ms", "Hallie", "Susan", "Robinson",
                apt_num="Apt. 50c",
                street_name="Crystal Cove",
                town="Cascade Meadows",
                post_code="XZ3 0BC"))
print()


print(billing_address("Miss", "Kathy", "Wendy", "Hilton",
                house_num=781,
                street_name="Ember Hollow",
                town="Enchanted Glade",
                post_code="FJ7 5OP"))
