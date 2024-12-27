# List Comprehension

# Notes:
    # - every output in this .py file is in a list
        # - list comprehensions can reduce for loops (and if conditions when added) to 1 line of code
            # - whatever the result, it will be outputted in a list, [ ... ]
    # - for loops can be written w/ 1 line of code
        # - structure: [ 'expression' '1st for loop line' ] *don't include quotations tho.
    # - if condition can be added in single line written for loops
        # - structure: [ 'expression' '1st for loop line' 'if' ] *don't include quotations tho. 
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


print(" --- new --- ")


# iterate triple the numbers via single for loop
tripled = [ number * 3 for number in range(1, 11) ]
print(original)
print(tripled)


print(" --- new --- ")


# iterate the square of numbers via single for loop
squared = [ number **2 for number in range(1, 11) ]
print(original)
print(squared)


print(" --- new --- ")


# iterate over strings via single for loop
test_str = "this is a test"

result = [ string.upper() for string in test_str ]
print(result)


print(" --- new --- ")


# iterate over strings via single for loop
fruits = ["orange", "apple", "pear", "mango", "coconut"]

fruit_output = [ fruit.capitalize() for fruit in fruits ]
print(fruit_output)

print()

# take 1st letter of each list's string & place in new list
first_letter_fruits = [ fruit[0] for fruit in fruits ]
print(first_letter_fruits)


print(" --- new --- ")


# using if conditions in list comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# put all even numbers in this list
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

print()

# put all odd numbers in this list
odd_nums = [num for num in numbers if num % 2 != 0]
print(odd_nums)


print(" --- new --- ")


# put all +ve numbers in new list
all_numbers = [-1, 2, -3, 4, -5]

# the 'num' before the for loop means it's being returned (like what the return statement does)
positive_nums = [ num for num in all_numbers if num > 0 ]
print(positive_nums)

print()

# put all -ve numbers in new list
negative_nums = [ num for num in all_numbers if num < 0 ]
print(negative_nums)
