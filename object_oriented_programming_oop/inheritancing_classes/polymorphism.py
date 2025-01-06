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


# parent class
class Shape():
    pass

# child classes
# as all of these classes inherit the 'Shape()' class, they take 2 forms, this is Polymorphism
    # - form 1 -> as they exist as themselves
    # - form 2 -> their parent class
class Pentagon(Shape):
    pass

class Hexagon(Shape):
    pass

class Nonagon(Shape):
    pass

class Decagon(Shape):
    pass


# objects made from classes
# due to polymorphism, these objects take the form of their own respective classes & their parent class

# its forms are:
    # - form 1 -> 'Pentagon()', form 2 -> 'Shape()'
    # this is NOT a Hexagon(), Nonagon() or Decagon()
pentagon = Pentagon()

# its forms are:
    # - form 1 -> 'Hexagon()', form 2 -> 'Shape()'
    # this is NOT a Pentagon(), Nonagon() or Decagon()
hexagon = Hexagon()

# its forms are:
    # - form 1 -> 'Nonagon()', form 2 -> 'Shape()'
    # this is NOT a Pentagon(), Hexagon() or Decagon()
nonagon = Nonagon()

# its forms are:
    # - form 1 -> 'Decagon()', form 2 -> 'Shape()'
    # this is NOT a Pentagon(), Hexagon() or Nonagon()
decagon = Decagon()


# list of objects instantiated from child classes, inheriting from parent class

# same as below:
    # - shape_list = [Pentagon(), Hexagon(), Nonagon(), Decagon()]
shapes_list = [pentagon, hexagon, nonagon, decagon]
