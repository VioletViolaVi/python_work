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

    # constructor - child classes underneath will inherit attribute variables from here
    def __init__(self, sides, colour, is_filled_in):
        self.sides = sides
        self.colour = colour
        self.is_filled_in = is_filled_in
    
    # method - child classes underneath will inherit this method so they'd be able to call it
    # ensure to add 'self' in '()' so attributes written in 'print()' are recognised
    def describe(self):
        print(f"This shape has {self.sides} sides, it's colour is {self.colour} and it's {'filled in' if self.is_filled_in else 'empty'}.")


# shape classes - turned into child classes

# inheriting from 'Shape' class
class Triangle(Shape):
    
    # constructor
    def __init__(self, sides, colour, is_filled_in, height, breadth):
        
        # inherits from parent class so its attribute variables can be accessible in this child class
        super().__init__(sides, colour, is_filled_in)
        
        # attribute variables unique to this child class
        self.height = height
        self.breadth = breadth


# inheriting from 'Shape' class
class Square(Shape):
    
    # constructor
    def __init__(self, sides, colour, is_filled_in, height, width):
        
        # inherits from parent class so its attribute variables can be accessible in this child class
        super().__init__(sides, colour, is_filled_in)
        
        # attribute variables unique to this child class
        self.height = height
        self.width = width


# inheriting from 'Shape' class
class Circle(Shape):
    
    # constructor
    def __init__(self, sides, colour, is_filled_in, pi, radius):
        
        # inherits from parent class so its attribute variables can be accessible in this child class
        super().__init__(sides, colour, is_filled_in)
        
        # attribute variables unique to this child class
        self.pi = pi
        self.radius = radius


# inheriting from 'Shape' class
class Rectangle(Shape):
    
    # constructor
    def __init__(self, sides, colour, is_filled_in, height, width):
        
        # inherits from parent class so its attribute variables can be accessible in this child class
        super().__init__(sides, colour, is_filled_in)
        
        # attribute variables unique to this child class
        self.height = height
        self.width = width


# creates objects
triangle= Triangle(sides=3, colour="yellow", is_filled_in=True, height=10, breadth=5)

square= Square(sides=4, colour="orange", is_filled_in=False, height=5, width=5)

circle= Circle(sides=1, colour="pink", is_filled_in=True, pi=3.14, radius=5)

rectangle= Rectangle(sides=4, colour="green", is_filled_in=False, height=10, width=5)

print()

# triangle
print(" --------------------- triangle --------------------- ")
print(triangle.sides)
print(triangle.colour)
print(triangle.is_filled_in)
print(triangle.height)
print(triangle.breadth)
print()

# square
print(" --------------------- square --------------------- ")
print(square.sides)
print(square.colour)
print(square.is_filled_in)
print(square.height)
print(square.width)
print()

# circle
print(" --------------------- circle --------------------- ")
print(circle.sides)
print(circle.colour)
print(circle.is_filled_in)
print(circle.pi)
print(circle.radius)
print()


# rectangle
print(" --------------------- rectangle --------------------- ")
print(rectangle.sides)
print(rectangle.colour)
print(rectangle.is_filled_in)
print(rectangle.height)
print(rectangle.width)
print()
