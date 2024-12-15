# Circle Area

import math

radius = 3

squared_radius = radius ** 2

circle_area = math.pi * squared_radius

print(circle_area)



print("--- user input version ---")



user_radius = float(input("Enter numerical value for radius: "))

print(f"user_radius: {user_radius}")

user_squared_radius = user_radius ** 2

print(f"user_squared_radius: {user_squared_radius}")

user_circle_area = math.pi * user_squared_radius

print(f"user_circle_area: {user_circle_area}")

print(round(user_circle_area, 2))



print("--- (shorter) user input version ---")



entered_radius = float(input("Enter numerical value for radius: "))

entered_circle_area = math.pi * pow(entered_radius, 2)

print(f"entered_radius: {entered_radius}")

print(f"entered_circle_area: {entered_circle_area}")

print(round(entered_circle_area, 2))
