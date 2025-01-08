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

        # '_' need to be added to attribute variable names otherwise AttributeError will throw
        #   - e.g.: AttributeError: property 'age' of 'Human' object has no setter
        self._name = name
        self._age = age
        self._weight = weight
        self._height = height
    
    # ------------------- using the @property decorator to add in additional logic -------------------
    # (this is just 1 example below) use @property decorator to add 1 digit after the decimal point & unit measurements e.g. cm, g, kg, etc.
    
    # 4x methods made
    @property
    def name(self):

        # using additional logic
        return f"Mr {self.name}"

    @property  
    def age(self):

        # using additional logic
        return f"{self.age}yrs old"

    @property    
    def weight(self):

        # using additional logic
        return f"{self.weight}kg"

    @property    
    def height(self):
        
        # using additional logic
        return f"{self.height}m"


# standard object creation
human = Human(name="Bob", age=29, weight=56.31, height=6.47)

# standard printing of values from attribute variables
print(human.name) # Bob (w/out getter, setter, deleter)
print(human.age) # 29 (w/out getter, setter, deleter)
print(human.weight) # 56.31 (w/out getter, setter, deleter)
print(human.height) # 6.47 (w/out getter, setter, deleter)
