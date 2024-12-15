# Circle Circumference

import math

radius = 3

circumference = 2 * math.pi * radius

print(circumference)
print(round(circumference, 2))



print("--- user input version ---")



user_radius = float(input("Enter a numerical radius value: "))
print(user_radius)

user_circumference = round(2 * math.pi * user_radius, 2)
print(f"The circumference of your circle, with the radius of '{user_radius}cm' is '{user_circumference}cm2'! :D")
