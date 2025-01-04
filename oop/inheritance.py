# Inheritance

# Notes:

# 

# parent class
class Animal:

    # constructor
    def __init__(self, name, is_alive):
        self.name = name
        self.is_alive = is_alive

    # methods
    def eating(self):
        return f"The {self.name} is eating."

    def sleeping(self):
        return f"The {self.name} is sleeping."

# creating an object then assigning the object to a variable
animal_obj_1 = Animal("Daffy", True)
animal_obj_2 = Animal("Bugs", False)
print()
print(f"Animal 1's name is: {animal_obj_1.name}")
print(f"Is animal 1 dead or alive?: {'Alive! 😊' if animal_obj_1.is_alive else 'Dead! 😢'}")
print()
print(f"Animal 2's name is: {animal_obj_2.name}")
print(f"Is animal 2 dead or alive?: {'Alive! 😊' if animal_obj_2.is_alive else 'Dead! 😢'}")


