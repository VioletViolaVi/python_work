# Module

# Notes
    # - putting the name of a module in help() function shows everything contained in the module
    # - can use alias when importing modules
    #    - 'import math' becomes 'import math as m', 'm' would be used instead of 'math' e.g. 'm.random()', 'm.pi()'
    #    - alias could be useful if module name is really long
    # - 

# # shows full list of modules
# print(help("modules"))

# # shows all features present in math module
# print(help("math"))

# different ways to import modules
import math
print(math.ceil(9.1))

# uses alias
import math as m 
print(m.ceil(9.1))

# directly noting what from math module is to be used
from math import pi, ceil

# didn't need to use dot notation
print(pi)
print(ceil(9.1))
