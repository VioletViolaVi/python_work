# Multiple Inheritance & Multilevel Inheritance

# Notes:
# multiple inheritance
    # - occurs when child class inherits from more than 1 parent class
    # - syntax structure: 
        # - class name_of_child_class(name_of_parent_class, name_of_parent_class_2, name_of_parent_class_3):

# multilevel inheritance
    # - occurs when parent class inherits from another parent class
        # - child class of parent class, inheriting from the other parent class, will also inherit methods/attributes from the (grand) parent class
            # - child class: C, child's parent class: B, parent class of the child's parent class: A
                # - C inherits from B, C also inherits from A because B inherits from A & C inherits everything from B


# parent class -------------------------------------------------

# prey class
class Prey():
    
    # method for Prey() class
    def run(self):
        print("This animal prey needs to run or it'll get eaten!")

# predator class
class Predator():
    
    # method for Predator() class
    def hunt(self):
        print("This animal predator hunts for its food!")


# child class --------------------------------------------------

# killer whale class - sharks eat penguins - top of food chain so is prey to no animal
class Killer_Whale(Predator):
    pass

# penguin class - penguins eat fish - penguins get eaten by sharks
class Penguin(Prey, Predator):
    pass

# fish class - fish eat other fish - fish gets eaten by penguins & sharks
class Fish(Prey, Predator):
    pass


# accessing methods from parent classes from child classes

# create objects from child classes
killer_whale = Killer_Whale()
penguin = Penguin()
fish = Fish()