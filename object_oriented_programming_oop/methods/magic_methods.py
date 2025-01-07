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
    # '__init__' gets automatically called when the 'Song' class is called
    def __init__(self, title, genre, recording_artist, sales):
        self.title = title
        self.genre = genre
        self.recording_artist = recording_artist
        self.sales = sales

    # a different type of magic/dunder method
    # makes object display a formatted string instead of a memory address, when printed out using 'print()'
    def __str__(self):

        # must be a STRING value for '__str__(self)' otherwise a TypeError will occur
        return f"Song name: {self.title} | Music genre: {self.genre} | Artist/Band: {self.recording_artist} | Number of sales: {self.sales:,}"

# create objects from class
song_1 = Song(title="Manager of your dreams", genre="Pop Ballad", recording_artist="FrontRoad Guys", sales=500000)

# using the 'print()' function alone like this will get a memory address
# a magic method can be used to customise this 'song_1' object as 'print()' is a built in python operation that is being used on the object
    # - e.g. '__str__' would make 'print(song_1)' show the formatted string (not memory address) w/out need to make an instance method like b4
print()
print(song_1)
