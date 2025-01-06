# Static Methods

# Notes:

# static methods
    # - these are methods that belong to the class
    # - these do not belong to objects/instances of the class
    # - these methods DO NOT use 'self' in their brackets as they belong to the class NOT the object/instance
    # - the '@staticmethod' decorator needs to be added just above the method, as part of its syntax
    # - these methods wont have access to attributes/data within constructors
    # - these methods are called directly on methods
        # - you don't make an object 1st then call the method like you would for instance methods
    # - best to use these for general utility functions w/in a class

# instance methods
    # - these are methods that BELONG to the objects that will be instantiated/created from the class
    # - these are the methods that use 'self' in their brackets
    # - these methods require to be called on objects of a class as they cannot be called directly on the class


# class
class Employee:

    # constructor
    def __init__(self, name, job_role):

        # attributes
        self.name = name
        self.job_role = job_role

    # instance method
        # this is an instance method as it requires use of attributes from constructor
        # all objects made from this class will have access the their own 'bio()' instance method
    def bio(self):
        print()
        print(f"Name: {self.name}, Job Role: {self.job_role}")
    
    # static method
    # '@staticmethod' decorator needs to be added 1st
    @staticmethod
    # no 'self' needs to be added in brackets as this is NOT an instance method, it is static!!!
    # you can still pass through parameters/placeholders in brackets for values later
    # this static method does not have nor need access to attributes in constructor
        # - therefore, creating objects will not be needed
            # - static methods are called directly on class i.e. 'Employee.salary("...")'
    def salary(pay):
        print()
        print(f"The salary of this employee is £{pay}.")


# calling a INSTANCE method

# make an object 1st then call instance method
# values passed through in brackets of class to make the object
employee = Employee(name="Bob", job_role="The Builder")

# instance method attached to object 
employee.bio()

# instance method can also be written as below:
Employee(name="Bob", job_role="The Builder"). bio()


# calling a STATIC method

# no object is required to be made
# static method is called directly on class
# value is passed through brackets of method being called
Employee.salary("56,000")
