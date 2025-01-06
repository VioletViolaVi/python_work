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

# instance methods
    # - these are methods that BELONG to the objects that will be instantiated/created from the class
    # - these are the methods that use 'self' in their brackets
    # - these methods require to be called on objects of a class as they cannot be called directly on the class
