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


