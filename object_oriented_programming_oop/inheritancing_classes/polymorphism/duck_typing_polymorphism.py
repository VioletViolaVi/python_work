# Polymorphism - Duck Typing

# Notes:

# duck typing
    # - another way to achieve polymorphism (the other way is inheritance)
    # - an unrelated object of class can be treated the same way as other classes that are children to a separate class
        # - the unrelated class will take on more forms, its own & the other classes it can copy, despite not being related to them
        # - MUST HAVE same attributed and/or methods in the children & parent classes to achieve this
        # - examples of equal treatment:
            # 1) can use the unrelated class w/ the actual children classes in a for loop iterating over a [list] w/out an error
            # 2) a class can use methods and/or attributes from a class that's NOT its parent, as long as this class has same methods and/or attributes


# create classes

# parent class
class Rooms():
    pass

# child class
class Bathroom(Rooms):
    pass

# child class
class Bedroom(Rooms):
    pass

# NOT ONE OF THE CHILD CLASSES!!!
class Limo():
    pass