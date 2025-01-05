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


# shape classes
class triangle:
    
    # constructor
    def __init__(self, sides, colour, is_filled_in, height, breadth):
        self.sides = sides
        self.colour = colour
        self.is_filled_in = is_filled_in
        self.height = height
        self.breadth = breadth


class square:
    
    # constructor
    def __init__(self, sides, colour, is_filled_in, height, width):
        self.sides = sides
        self.colour = colour
        self.is_filled_in = is_filled_in
        self.height = height
        self.width = width


class circle:
    
    # constructor
    def __init__(self, sides, colour, is_filled_in, pi, radius):
        self.sides = sides
        self.colour = colour
        self.is_filled_in = is_filled_in
        self.pi = pi
        self.radius = radius


class rectangle:
    
    # constructor
    def __init__(self, sides, colour, is_filled_in, height, width):
        self.sides = sides
        self.colour = colour
        self.is_filled_in = is_filled_in
        self.height = height
        self.width = width

