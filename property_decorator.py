# Property Decorator

# Notes:

# @property decorator enables the ability to define a method as a property
# @property decorator makes respective part of code able to be accessed/treated as if it's an attribute
    #   - e.g. when @property method is created, the name of the method can be called w/out its brackets
        #   - 'human.weight' instead of 'human.weight()' (see print statements below)
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
        # adding the '_' tells you & other developers reading this code that the attributes are to be protected/private
            # - these '_' attributes should not be used/accessed outside the class
            # - the '_' attributes are internal
            # - getter methods are used instead to get these attributes to use their values
        self._name = name
        self._age = age
        self._weight = weight
        self._height = height
    
    # ------------------- using the @property decorator to add in additional logic -------------------
    # (this is just 1 example below) use @property decorator to add 1 digit after the decimal point & unit measurements e.g. cm, g, kg, etc.
    
    # 4x getter methods
    @property
    def name(self):

        # using additional logic
        # using @property for getters
            # - '_' need to be added to attribute variable names here also or a RecursionError will occur
                #   - e.g.: RecursionError: maximum recursion depth exceeded
        return f"Mr {self._name}"

    @property
    def age(self):

        # using additional logic
        # using @property for getters
            # - '_' need to be added to attribute variable names here also or a RecursionError will occur
                #   - e.g.: RecursionError: maximum recursion depth exceeded
        return f"{self._age}yrs old"

    @property
    def weight(self):

        # using additional logic
        # using @property for getters
            # - '_' need to be added to attribute variable names here also or a RecursionError will occur
                #   - e.g.: RecursionError: maximum recursion depth exceeded
        return f"{self._weight}kg"

    @property
    def height(self):

        # using additional logic
        # using @property for getters
            # - '_' need to be added to attribute variable names here also or a RecursionError will occur
                #   - e.g.: RecursionError: maximum recursion depth exceeded
        return f"{self._height}m"


    # 4x setter methods
    @age.setter
    def age(self, new_age):
        if self._age > 18:
            print()
            print("You are of drinking age!")
        else:
            self.name = new_age
            print()
            print(f"You are too young to drink at {new_age}yrs old!")


# standard object creation
human = Human(name="Bob", age=29, weight=56.31, height=6.47)

# standard printing of values from attribute variables
    # values w/out getter, setter, deleter:
        #   - Bob
        #   - 29
        #   - 56.31
        #   - 6.47

# using @property decorator stops the previous 'standard' values from showing
# they now contain the additional logic that was added to their respective methods e.g. 'yrs old', 'Mr', etc.
    # values w/ getter:
        #   - Mr Bob
        #   - 29yrs old
        #   - 56.31kg
        #   - 6.47m

# makes if condition code execute & print out statement in method under @name.setter
human.age = 16

print()
print(human.name)
print(human.age) 
print(human.weight)
print(human.height)
