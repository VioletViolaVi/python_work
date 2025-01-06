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

# Notes (again):
# - below, classes have been made
    # - 1 parent, 2 children, 1 separate/unrelated to anybody!
# - 'Bathroom(Rooms)' & 'Bedroom(Rooms)' will inherit the attribute from the 'Rooms()' class, 'Limo()' will not

# parent class
class Rooms():
    is_occupied = True

# child class
class Bathroom(Rooms):
    
    def sit(self):
        print("You are sitting in a bathtub in the bathroom. 🛀")

# child class
class Bedroom(Rooms):
    
    def sit(self):
        print("You are sitting on the bed in the bedroom. 🛌")

# NOT ONE OF THE CHILD CLASSES!!!
class Limo():
    
    def seats(self):
        print("You are sitting on a seat in the limo. 🚘")


# Notes (again... again):
# iterating through '[Bathroom(), Bedroom()]':
    # - this will NOT cause an 'AttributeError' as objects are from classes that can use the same 'sit()' method via parent class inheritance
# iterating through '[Bathroom(), Bedroom(), Limo()]':
    # - this WILL cause an 'AttributeError' as 'Limo()' doesn't have access to the 'sit()' method, it's NOT a child class

# creates list of objects

# will NOT cause an 'AttributeError'
rooms = [Bathroom(), Bedroom()]

# WILL cause an 'AttributeError'
rooms = [Bathroom(), Bedroom(), Limo()] # 'Limo()' doesn't have access to the 'sit()' method

# iterates through list
for room in rooms:
    print()
    room.sit()
