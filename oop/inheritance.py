# Inheritance

# Notes:

# inheritance allows a class to inherit attributes & methods from another class
# inheritance:
    # - makes code reusable
    # - makes code extensive

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

# formatting strings using attributes from parent class
print(f"The {dog.animal_type}'s name is {dog.name}. The {dog.animal_type} is {'Alive! 😊' if dog.is_alive else 'Dead! 😢'}")
print(f"The {cat.animal_type}'s name is {cat.name}. The {cat.animal_type} is {'Alive! 😊' if cat.is_alive else 'Dead! 😢'}")
print(f"The {pig.animal_type}'s name is {pig.name}. The {pig.animal_type} is {'Alive! 😊' if pig.is_alive else 'Dead! 😢'}")
print()

# formatting strings using methods for own respective child/sub classes
print(f"What sound the {dog.animal_type} say? {dog.speak()}!")
print(f"What sound the {cat.animal_type} say? {cat.speak()}!")
print(f"What sound the {pig.animal_type} say? {pig.speak()}!")
print()

# formatting strings using methods from parent class
print(f"{dog.eating()} 🍴")
print(f"{cat.eating()} 🍴")
print(f"{pig.eating()} 🍴")
print()
print(f"{dog.sleeping()} 💤")
print(f"{cat.sleeping()} 💤")
print(f"{pig.sleeping()} 💤")
