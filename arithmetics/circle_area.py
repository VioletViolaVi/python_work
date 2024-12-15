# Circle Area

import math

radius = 3

squared_radius = radius ** 2

circle_area = math.pi * squared_radius

print(circle_area)



print("--- user input version ---")



user_radius = float(input("Enter numerical value for radius: "))

user_squared_radius = user_radius ** 2

user_circle_area = math.pi * user_squared_radius

print(round(user_circle_area, 2))
