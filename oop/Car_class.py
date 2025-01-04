# Car class - placed in own file


# creating objects using classes
# class of Car
class Car:

    # this is a constructor, it is need to create objects
    # in brackets, parameters are being passed through, they'll be replaced w/ real values passed through when object is being created
    def __init__(self, model, year, colour, for_sale):

        # assigning passed through values to objects (the part starting with 'self.')
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    # methods
    # 'self' is added & will already be provided
    def driving(self):
        print("You are driving the car!")

    def stop_driving(self):
        print("You stopped the car from driving!")
