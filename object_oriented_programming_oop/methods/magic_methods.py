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
    # makes object display a string instead of a memory address, when printed out using 'print()'
        # - this is the act of customising the behaviour of the 'print()' function showing a memory address
    def __str__(self):

        # must be a STRING value for '__str__(self)' otherwise a TypeError will occur
        return f"Song name: {self.title} | Music genre: {self.genre} | Artist/Band: {self.recording_artist} | Number of sales: {self.sales:,}"
    
    # another magic/dunder method
        # - this magic/dunder method checks if values are equal to each other
    # this magic/dunder methods defines behaviour for the '==' operator
        # '==' needs to be present in order to use this (see below in print statement)
    # other_value represents the other value passed through when this function is used
        # - it can be named anything, - just be consistent, as usual
    def __eq__(self, other_song_value):

        # checks values of the 'self.sales' attribute value for both objects passed through print() function e.g. 'print(song_1 == song_3)'
        return self.sales == other_song_value.sales
    

    # another magic/dunder method
    # this magic method is needed otherwise a TypeError is thrown if you attempt 'print(song_2 < song_3)'
        # - error goes on to say: " '<' not supported between instances of 'Song' and 'Song' "
        # error is due to not being able to use '<' on objects
    # checks if 1 value is less than the other
        # '<' needs to be present in order to use this (see below in print statement)
    def __lt__(self, other_value):

        # returns boolean value True/False
        return self.sales < other_value.sales
    

    # another magic/dunder method
    # 'print(song_2 > song_3)' w/out this magic method will cause output to be 'False' every time, regardless on whether it's correct or not
    # checks if 1 value is greater than the other
        # '>' needs to be present in order to use this (see below in print statement)
    def __gt__(self, other_value):

        # returns boolean value True/False
        return self.sales > other_value.sales


# create objects from class
song_1 = Song(title="Manager of your nightmares", genre="Pop Ballad", recording_artist="FrontRoad Guys", sales=500000)
song_2 = Song(title="Get ready for the jellies", genre="Rock", recording_artist="The Jellies", sales=175000)
song_3 = Song(title="Let it stop", genre="Jazz", recording_artist="Nene Moore", sales=986300)

# this is the same as song_2 - for testing purposes '__eq__(self)' (see below)
song_4 = Song(title="Get ready for the jellies", genre="Rock", recording_artist="The Jellies", sales=175000)


# using the 'print()' function alone like this will get a memory address
# a magic method can be used to customise this 'song_1' object as 'print()' is a built in python operation that is being used on the object
    # - e.g. '__str__' would make 'print(song_1)' show the formatted string (not memory address) w/out need to make an instance method like b4
print()
print(song_1)
print(song_2)
print(song_3)


# using '==' in 'print()' function, along with the '__eq__' magic/dunder method to check if values are equal to each other
# shows False as sales amounts are not the same
print()
print(f"(same sales) song_1 same as song_3: {song_1 == song_3}")

# shows True as sales amounts are the same
# use of '==' needed here in order to see results of '__eq__' magic method
print(f"(same sales) song_2 same as song_4: {song_2 == song_4}")


# using '<' (less than)  in 'print()' function, along with the '__lt__' magic/dunder method to check if 1 value is less than the other
    # - focusses on sales amount (see '__lt__' magic method)
print()
print(f"(less sales) song_2 less than song_3: {song_2 < song_3}") # True
print(f"(less sales) song_3 less than song_1: {song_3 < song_1}") # False
print(f"(less sales) song_4 less than song_2: {song_4 < song_2}") # False


# using '>' (greater than)  in 'print()' function, along with the '__gt__' magic/dunder method to check if 1 value is greater than the other
    # - focusses on sales amount (see '__gt__' magic method)
# w/out '__gt__' magic method created, all these print statements will print 'False' whether that's correct or not
    # - therefore, ensure to include '__gt__' magic method
print()
print(f"(greater sales) song_4 greater than song_4: {song_4 > song_4}") # False
print(f"(greater sales) song_3 greater than song_2: {song_3 > song_2}") # True
print(f"(greater sales) song_1 greater than song_2: {song_1 > song_2}") # True
