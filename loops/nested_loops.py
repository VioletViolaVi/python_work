# Nested Loops

for outer in range(0, 3):
    for inner in range(0, 3):   
        print("inner", end=" ")        
    print("outer")



print(" --- new ---")



# from vid
for x in range(0, 10):
    print(x, end="")
print()

# print 3x
for x in range(0, 10):
    for y in range(0, 3):
        print(y, end="")

# print 3x on own lines
for x in range(0, 3):
    for y in range(0, 10):
        print(y, end="")
    print()