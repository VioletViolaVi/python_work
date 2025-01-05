# Super Function - super()

# Notes:

# child class == subclass
# parent class == superclass

# best practice to write constructor code once then reuse it by allowing other classes to inherit attributes from it
    # - super() helps achieve this

# super()
    # - it's a function
    # - used in child classes
    # - calls attributes/methods from parent class into child classes
    # - extends functionality of inherited methods
        # - e.g. putting 'super()' in a (grand) child class's method

# extending functionality
    # - 'super()' is used to extend functionality from parent class to the child class
        # - e.g., parent class has 'def eats(self)...', child class has 'def eats(self)...'
            # - put 'super()' in child's 'def eats(self)...' method

# method overriding
    # - if a child class inherits a method from the parent class, whilst holding a method with the same name in its own class, the child's method will be outputted and override the parent's method
        # - e.g., parent class has 'def describe(self)...', child class has 'def describe(self)...'
            # - the 'def describe(self)...' in the child class will be outputted 
                # - NOT the one in the parent class


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
        print(f"(from parent class) This shape has {self.sides} side{'s' if self.sides > 1 else ''}, it's colour is {self.colour} and it's {'filled' if self.is_filled_in else 'empty'}.")


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
    
    # method
    # this method will be produce in output, not 'describe()' from parent class
    def describe(self):
        print(f"(from its own class) This shape has a height of {self.height}cm and a breadth of {self.breadth}cm.")

        # extends functionality from parent class to this child class
        # allows this child class to use the '.describe()' method from the parent
        # handy to use this as both the parent and child class have methods with the same name
            # - as a result, extending functionality like this allows developers to use both methods w/out any of them getting overridden
        super().describe()


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

# using 'describe()' method child class inherited from parent class
# when 'super().describe()' is inside the 'describe()' method, both print statements from the parent & child classes are displayed
    # - can help avoid method overriding
triangle.describe()
print()

# square
print(" --------------------- square --------------------- ")
print(square.sides)
print(square.colour)
print(square.is_filled_in)
print(square.height)
print(square.width)
print()

# using 'describe()' method child class inherited from parent class
square.describe()
print()

# circle
print(" --------------------- circle --------------------- ")
print(circle.sides)
print(circle.colour)
print(circle.is_filled_in)
print(circle.pi)
print(circle.radius)
print()

# using 'describe()' method child class inherited from parent class
circle.describe()
print()


# rectangle
print(" --------------------- rectangle --------------------- ")
print(rectangle.sides)
print(rectangle.colour)
print(rectangle.is_filled_in)
print(rectangle.height)
print(rectangle.width)
print()

# using 'describe()' method child class inherited from parent class
rectangle.describe()
print()
