# Class Variables

# Notes:

# class variables are variables shared among all instances/objects made from the same class

# instance variables:
    # - these are defined INSIDE a constructor
    # - each object has their own of these variables

# class variables:
    # - these are defined OUTSIDE a constructor
    # - these can share their data with all objects made from the same class
        # - these are shared by all objects created by the same respective class
    # - when calling/getting values of class variables, use the (.) 'attribute access operator' on the class name, not on its objects


# class of Student made
class Student:

    # class variable
    grad_year = 2025

    # keeps track of how many student objects have been created
    student_total = 0

    # constructor

    # when Student object is created, this constructor gets automatically called
    # constructor code will always be executed when object is instantiated
        # - i.e. when object is made, this constructor code will run
    def __init__(self, name_param, age_param):

        # 'self.' is to refer to object currently being worked w/
        # attributes = values
            # - think of attributes here as the same/similar to variables u've written in other coding files a bunch of times b4
        self.name = name_param
        self.age = age_param

        # increases student total by 1 every time object is instantiated/made
            # - to make changes to class variable i.e. 'student_total', replace 'self' keyword w/ class name 'Student'
                # - 'self.student_total' becomes 'Student.student_total'
        Student.student_total += 1

# Student objects created below
student_1 = Student("Milo", 24)
student_2 = Student("Fizz", 23)
student_3 = Student("Jake", 22)
student_4 = Student("Bella", 25)

# get values by calling their variables (attributes) - using constructor attributes
print(student_1.name)
print(student_1.age)
print()
print(student_2.name)
print(student_2.age)
print()
print(student_3.name)
print(student_3.age)
print()
print(student_4.name)
print(student_4.age)
print()

# getting value of class attribute - below in print() statements work however...

# below is NOT good practice of getting the value of a class variable 
    # - as code is not clear on if '.grad_year' is a class variable or attribute variable
    # - '.grad_year' looks like it could be an attribute variable in the constructor - however, it's not!
    # - still works, but NOT good practice
print(student_1.grad_year)
print(student_2.grad_year)
print(student_3.grad_year)
print(student_4.grad_year)
print()

# below is good practice in getting value of class variable 
    # - as it's clear '.grad_year' is a class variable since it's attached to Student (the class) 
    # - writing like this helps w/ clarity & readability
print(Student.grad_year)
print()

# shows value of 'student_total' class variable
    # - all show 4 as 4 objects were made w/ the constructor
print(Student.student_total)
print(student_1.student_total)
print(student_2.student_total)
print(student_3.student_total)
print(student_4.student_total)
