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
        print(f"True/False - The bathtub is occupied: {self.is_occupied}.")

# child class
class Bedroom(Rooms):
    
    def sit(self):
        print("You are sitting on the bed in the bedroom. 🛌")
        print(f"True/False - The bedroom is occupied: {self.is_occupied}.")

# NOT ONE OF THE CHILD CLASSES!!!
class Limo():

    # adding the same attribute variable 'is_occupied' as the one in 'Room()' class above, enables this class to get access
        # adding this helps this 'Limo()' class meet the minimum necessary requirements to be considered & treated as a child of the 'Room()' class
            # - it's still NOT a child of the 'Room()' class!!!
            # - polymorphism has still occurred
    is_occupied = True
    
    # method name as 'def seat(self)' is different to 'def sit(self)' causing 'Limo()' class to not work in for loop below
    def seat(self):
        print("1, You are sitting on a seat in the limo. 🚘")

    # renaming it to 'def sit(self)' will enable the 'Limo()' class to work in the for loop
        # - this is the case despite not being a sibling of the other classes
        # - this class has the minimum number of methods to be considered & treated as one of the child classes
            # - polymorphism has still occurred
    # looks like a duck, quacks like a duck, it'll be treated like a duck (duck typing)
    def sit(self):
        print("2, You are sitting on a seat in the limo. 🚘")

        # causes 'AttributeError' as attribute variable 'is_occupied' comes from the 'Room()' class, which is NOT accessible by this class
        print(f"True/False - The limo is occupied: {self.is_occupied}.")


# Notes (again... again):
# iterating through '[Bathroom(), Bedroom()]':
    # - this will NOT cause an 'AttributeError' as objects are from classes that can use the same 'sit()' method via parent class inheritance
# iterating through '[Bathroom(), Bedroom(), Limo()]':
    # - this WILL cause an 'AttributeError' as 'Limo()' doesn't have access to the 'sit()' method, it's NOT a child class

# creates list of objects

# will NOT cause an 'AttributeError' - as long as 'Limo()' is 'def seat(self)'
rooms = [Bathroom(), Bedroom()]

# WILL cause an 'AttributeError' - as long as 'Limo()' is 'def seat(self)'
# 'Limo()' doesn't have access to the 'sit()' method
rooms = [Bathroom(), Bedroom(), Limo()]

# iterates through list
for room in rooms:
    print()
    room.sit()
    print()
    room.is_occupied
