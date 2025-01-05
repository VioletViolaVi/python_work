# Super Function - super()

# Notes:

# super()
    # - it's a function
    # - used in child classes
    # - calls attributes/methods from parent class into child classes
    # - extends functionality of inherited methods
        # - e.g. putting 'super()' in a (grand) child class's method

# child class == subclass
# parent class == superclass

# best practice to write constructor code once then reuse it by allowing other classes to inherit attributes from it
    # - super() helps achieve this


# parent class containing all common attributes from other classes below
class Shape:
    def __init__(self, sides, colour, is_filled_in):
        self.sides = sides
        self.colour = colour
        self.is_filled_in = is_filled_in


# shape classes - turned into child classes

# inheriting from 'Shape' class
class Triangle(Shape):
    
    # constructor
    def __init__(self, sides, colour, is_filled_in, height, breadth):
        super().__init__(sides, colour, is_filled_in)
        self.height = height
        self.breadth = breadth


# inheriting from 'Shape' class
class Square(Shape):
    
    # constructor
    def __init__(self, sides, colour, is_filled_in, height, width):
        super().__init__(sides, colour, is_filled_in)
        self.height = height
        self.width = width


# inheriting from 'Shape' class
class Circle(Shape):
    
    # constructor
    def __init__(self, sides, colour, is_filled_in, pi, radius):
        super().__init__(sides, colour, is_filled_in)
        self.pi = pi
        self.radius = radius


# inheriting from 'Shape' class
class Rectangle(Shape):
    
    # constructor
    def __init__(self, sides, colour, is_filled_in, height, width):
        super().__init__(sides, colour, is_filled_in)
        self.height = height
        self.width = width

