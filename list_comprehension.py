# List Comprehension

# Notes:
    # - 
    # - 
    # -

# iterating to double numbers from 1-10 inclusively
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled = []
for num in range(1,11):
    num *= 2
    doubled.append(num)
print(original)
print(doubled)

print()

# same for loop as above but written w/ 1 line of code
doubled = [num*2 for num in range(1, 11)]
print(doubled)

