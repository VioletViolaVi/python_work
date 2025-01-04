# Inheritance

# Notes:

# 

# parent class -------------------------------------------------------------------------------------------------------------------
class Animal:

    # constructor
    def __init__(self, name, is_alive, animal_type):
        self.name = name
        self.is_alive = is_alive
        self.animal_type = animal_type

    # methods
    def eating(self):
        return f"{self.name} the {self.animal_type}, is eating."

    def sleeping(self):
        return f"{self.name} the {self.animal_type}, is sleeping."

# creating an object then assigning the object to a variable
animal_obj_1 = Animal("Daffy", True, "generic animal")
animal_obj_2 = Animal("Bugs", False, "generic animal")
print()
print(f"{animal_obj_1.animal_type.capitalize()} 1's name is: {animal_obj_1.name}")
print(f"Is {animal_obj_1.animal_type} 1 dead or alive?: {'Alive! 😊' if animal_obj_1.is_alive else 'Dead! 😢'}")
print()
print(f"{animal_obj_2.animal_type.capitalize()} 2's name is: {animal_obj_2.name}")
print(f"Is {animal_obj_2.animal_type} 2 dead or alive?: {'Alive! 😊' if animal_obj_2.is_alive else 'Dead! 😢'}")
print()
print(" ------------------------------------------------------------------------------------------------------------------- ")
print()

# ------------------------------------------------------------------------------------------------------------------- parent class

# creating child classes that inherit from parent class

# dog child/sub class
class Dog(Animal):

    # methods
    def speak(self):
        return "Woof! 🐶"


# cat child/sub class
class Cat(Animal):

    # methods
    def speak(self):
        return "Meow! 😺"


# pig child/sub class
class Pig(Animal):

    # methods
    def speak(self):
        return "Oink! 🐷"

# creating objects from child/sub classes
# dog object
dog = Dog("Clifford", True, "dog")

# cat object
cat = Cat("Tom", False, "cat")

# pig object
pig = Pig("Miss Piggy", True, "pig")
