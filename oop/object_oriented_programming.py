# Object Oriented Programming

# Notes:

# objects:
# - these are a bundle of related attributes & methods
#   - e.g. car, person, book, mobile, etc. (any 'noun' thing really)
# - 'constructors' are required to construct objects

# attributes:
# - these are similar to variables
# - they describe what object has

# methods:
# - they are functions inside the object
# - these functions belong to the object

# classes:
# - they are used to make many objects
# - they are a type of blueprint used to design layout & structure of an object
# - they are used to design the attributes & methods of an object
#   - what do the objects have (attributes) and what do the objects do (methods)

# (Car class relocated to separate file)

# imports only the 'Car' class from the 'car_class.py' file
#   - from car_class import Car

# imports everything from 'car_class.py' file
#   - need to use '.' to call specific part of file u want to use i.e. car_class.Car()
import car_class

# constructing Car objects
# 'self' is already provided
    # - if u try to use 'self' a TypeError gets thrown
car_1 = car_class.Car("limo", 2025, "blue", True)
car_2 = car_class.Car("jeep", 2026, "orange", False)
car_3 = car_class.Car("mercedes", 2027, "pink", True)

# this prints memory address of where car_1 object is located, see below:
    # - <__main__.Car object at 0x0000026A63E3B190>
print(car_1)
print(car_2)
print(car_3)

# to get the attributes located at the object's (car_1) memory address
# the dot '.' used, just b4 the attribute, is called the 'attribute access operator'
print(car_1.model)
print(car_1.year)
print(car_1.colour)
print(car_1.for_sale)
print()
print(car_2.model)
print(car_2.year)
print(car_2.colour)
print(car_2.for_sale)
print()
print(car_3.model)
print(car_3.year)
print(car_3.colour)
print(car_3.for_sale)
print()

# invoking the 'def drive(self)' method from the 'Car' class

# mini notes:
    # {- has a problem w/ calling method w/ no values passed through due to 'self' in 'def drive(self)'
    #  - left empty string in place as result, correct output was still produced tho. ¯\_(ツ)_/¯}

# the reason u had this problem {see above} is because u called the methods directly on the 'Car' class
# u need to call methods on the OBJECTS/INSTANCES of the class not on the class itself
# disregard {note above} - however, it's been left for future reference, in case this happens again

# calling methods on objects made from the class
car_1.driving()
car_1.stop_driving()
car_1.describe()
print()
car_2.driving()
car_2.stop_driving()
car_2.describe()
print()
car_3.driving()
car_3.stop_driving()
car_3.describe()
