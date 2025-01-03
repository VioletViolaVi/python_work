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
