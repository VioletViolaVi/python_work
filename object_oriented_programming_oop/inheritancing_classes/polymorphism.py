# Polymorphism

# Notes

# polymorphism 
    # - means to have many forms/faces
    # - poly: many
    # - morph: form

# objects can take 1 of many forms

# 2 ways to make polymorphism happen 
    # - inheritance 
    # - duck typing


# imports the abstract base class (ABC) module
from abc import ABC, abstractmethod

# parent class
class Shape(ABC):

    # constructor
    def __init__(self, name, sides, length):
        self.name = name
        self.sides = sides
        self.length = length
        self.perimeter = length * sides

    def how_many_sides(self):
        return f"A {self.name} has {self.sides} sides."

    # uses the abc module to make this function abstract
    # method is undefined & needs to be overridden by its children classes
    @abstractmethod
    def calculate_perimeter(self):
        pass


# child classes
# as all of these classes inherit the 'Shape()' class, they take 2 forms, this is Polymorphism
    # - form 1 -> as they exist as themselves
    # - form 2 -> their parent class
class Pentagon(Shape):
    
    # is overriding 'calculate_perimeter()' method from its parent being inherited from
    def calculate_perimeter(self):
        return f"The perimeter of {self.name} is {self.perimeter}cm at {self.length}cm per side."

class Hexagon(Shape):
    
    # is overriding 'calculate_perimeter()' method from its parent being inherited from
    def calculate_perimeter(self):
        return f"The perimeter of {self.name} is {self.perimeter}cm at {self.length}cm per side."

class Nonagon(Shape):
    
    # is overriding 'calculate_perimeter()' method from its parent being inherited from
    def calculate_perimeter(self):
        return f"The perimeter of {self.name} is {self.perimeter}cm at {self.length}cm per side."

class Decagon(Shape):
    
    # is overriding 'calculate_perimeter()' method from its parent being inherited from
    def calculate_perimeter(self):
        return f"The perimeter of {self.name} is {self.perimeter}cm at {self.length}cm per side."


# unrelated class to 'Shape()'
class Pancake():
    # constructor
    def __init__(self, flavour):
        self.flavour = flavour


# objects made from classes
# due to polymorphism, these objects take the form of their own respective classes & their parent class

# its forms are:
    # - form 1 -> 'Pentagon()', form 2 -> 'Shape()'
    # this is NOT a Hexagon(), Nonagon() or Decagon()
pentagon = Pentagon(name="pentagon", sides=5, length=5)

# its forms are:
    # - form 1 -> 'Hexagon()', form 2 -> 'Shape()'
    # this is NOT a Pentagon(), Nonagon() or Decagon()
hexagon = Hexagon(name="hexagon", sides=6, length=5)

# its forms are:
    # - form 1 -> 'Nonagon()', form 2 -> 'Shape()'
    # this is NOT a Pentagon(), Hexagon() or Decagon()
nonagon = Nonagon(name="nonagon", sides=9, length=5)

# its forms are:
    # - form 1 -> 'Decagon()', form 2 -> 'Shape()'
    # this is NOT a Pentagon(), Hexagon() or Nonagon()
decagon = Decagon(name="decagon", sides=10, length=5)

# creates pancake object from 'Pancake()' class
pancake = Pancake(flavour="plain")



# list of objects instantiated from child classes, inheriting from parent class

# same as below:
    # - shape_list = [Pentagon(), Hexagon(), Nonagon(), Decagon()]
# if an object, that is not inheriting from the parent class, is added to this list an error will occur 
    # - error would be as a result of not being able to access the methods/attributes from the parent class as no inheritance is occurring 
        # - 'AttributeError: '[name of class]' object has no attribute '[name of method]''
shape_list = [pentagon, hexagon, nonagon, decagon, pancake]

# looping through objects list to use parent class method on each object - as they're all inheriting the method from the parent class
# these child classes where able to use the 'how_many_sides()' method from the parent class due to polymorphism
    # - the 'how_many_sides()' method is in the parent class which is being inherited by the child classes
for shape in shape_list:
    print()
    print(shape.how_many_sides())
    print(shape.calculate_perimeter())
