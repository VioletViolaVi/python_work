# Object Oriented Programming

# Notes:

# objects:
# - these are a bundle of related attributes & methods
#   - e.g. car, person, book, mobile, etc. (any 'noun' thing really)
# - 'constructors' are required to construct objects

# attributes:
# - these are similar to variables
# - they describe what object has

# methods:
# - they are functions inside the object
# - these functions belong to the object

# classes:
# - they are used to make many objects
# - they are a type of blueprint used to design layout & structure of an object
# - they are used to design the attributes & methods of an object
#   - what do the objects have (attributes) and what do the objects do (methods)


# creating objects using classes
# class of Car
class Car:

    # this is a constructor, it is need to create objects
    # in brackets, parameters are being passed through, they'll be replaced w/ real values passed through when object is being created
    def __init__(self, model, year, colour, for_sale):

        # assigning passed through values to objects (the part starting with 'self.')
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

# constructing Car objects
# 'self' is already provided
    # - if u try to use 'self' a TypeError gets thrown
car_1 = Car("limo", 2025, "blue", True)

# this prints memory address of where car_1 object is located, see below:
    # - <__main__.Car object at 0x0000026A63E3B190>
print(car_1)

# to get the attributes located at the object's (car_1) memory address
# the dot '.' used, just b4 the attribute, is called the attribute access operator
print(car_1.model)
print(car_1.year)
print(car_1.colour)
print(car_1.for_sale)