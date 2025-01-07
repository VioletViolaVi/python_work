# Magic Methods

# Notes:

# magic methods aka dunder methods
# these are are methods that start & end with double underscores
    # - e.g. '__init__' like the ones used in constructor previously
# usually used inside classes
# these methods are automatically called by python's built in operations e.g. 'print()' function, '==' operator, '>=' operator, '<' operator, etc.
    # when python operators are used on object, it becomes possible to customise the behaviour of said object 


# standard class
class Song:
    
    # this constructor is a 'magic method' aka 'dunder method'
        # double underscores before & after 'init' makes it a magic/dunder method
    def __init__(self, title, singer, sales):
        self.title = title
        self.singer = singer
