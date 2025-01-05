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
    pass

# predator class
class Predator():
    pass


# child class --------------------------------------------------

# killer whales class - sharks eat penguins
class Killer_Whales():
    pass

# penguins class - penguins eat fish, penguins get eaten by sharks
class Penguins():
    pass


# fish class - fish eat other fish, fish gets eaten by penguins & sharks
class Fish():
    pass

