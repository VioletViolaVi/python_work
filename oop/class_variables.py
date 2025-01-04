# Class Variables

# Notes:

# - class variables are variables shared among all instances/objects made from the same class

# instance variables:
    # - these are defined INSIDE a constructor
    # - each object has their own of these variables

# class variables:
    # - these are defined OUTSIDE a constructor
    # - these can share their data with all objects made from the same class


# class of Student made
class Student:

    # constructor
    # when Student object is created, this constructor gets automatically called
    def __init__(self, name_param, age_param):

        # 'self.' is to refer to object currently being worked w/
        # attributes = values
            # - think of attributes here as the same/similar to variables u've written in other coding files a bunch of times b4
        self.name = name_param
        self.age = age_param

