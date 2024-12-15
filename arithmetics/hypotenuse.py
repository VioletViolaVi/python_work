# Right Angled Triangle Hypotenuse

import math

opposite = float(input("Enter numerical opposite value: "))

adjacent = float(input("Enter numerical adjacent value: "))

hypotenuse = math.sqrt( pow(opposite, 2) + pow(adjacent, 2) )

print(f"The hypotenuse of this triangle is {hypotenuse}")