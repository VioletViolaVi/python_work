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

        # 'self.' is used as it's referring to the class's attributes being used
        print(f"You are driving the {self.colour} {self.model.title()}!")

    # 'self' is added & will already be provided
    def stop_driving(self):

        # 'self.' is used as it's referring to the class's attributes being used
        print(f"You stopped the {self.colour} {self.model.title()} driving!")

    # method for describing the different cars
    def describe(self):

        # 'self.' is used as it's referring to the class's attributes being used
        print(f"""What you're looking at right here is the new '{self.year} {self.colour.capitalize()} {self.model.title()}' make. {"Fortunately, it's" if self.for_sale else "Unfortunately, it's not"} for sale!""")