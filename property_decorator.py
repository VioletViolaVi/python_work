# Property Decorator

# Notes:

# @property decorator enables the ability to define a method as a property
# @property decorator makes respective part of code able to be accessed/treated as if it's an attribute 
# additional logic can be added using the @property decorator
    #   - additional logic can be added when reading, writing & deleting attributes
# @property methods provides the following when working w/ attributes:
    #   - getter method -> to read
    #   - setter method -> to write
    #   - deleter method -> to delete


# standard class
class Human:

    # standard constructor/magic/dunder method
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

# standard object creation
human = Human(name="Bob", age=29, weight=56.31, height=6.47)

# standard printing of values from attribute variables
print(human.name)
print(human.age)
print(human.weight)
print(human.height)
