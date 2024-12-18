# For Loops

# lists -> '[ ... ]'
foods = ["chips", "pizza", "chocolate", "cake"]
for food in foods:
    print(food)

clothes = ["t-shirt", "shoes", "scarf", "jacket", "socks", "jumper"]
for clothing in clothes:
    print(clothing)



print(" --- next --- ")



# strings
name = "vivian"
for letter in name:
    print(letter)

counter = "12345"
for count in counter:
    print(count)
print("GO!!!")



print(" --- next --- ")



# using 'range()'
for y in range(0, 11, 2):
    print(y)

for y in range(11):
    print(y)

for x in range(1, 11):
    print(x)

for x in reversed(range(1, 11)):
    print(x)



print(" --- next --- ")



# using 'continue'
numbers = "0123456789"
for number in numbers:
    if number == "7":
        continue
    else:
        print(number)

number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in number_list:
    if number % 2 != 0:
        continue
    else:
        print(number)



print(" --- next --- ")



# using 'break'
word = "inconsequential"
for letter in word:
    if letter == "q":
        break
    else:
        print(letter)

find_key = ["grass", 10, "blue", 8.21, True, "key", -63, False]
for key in find_key:
    if key == "key":
        break
    else:
        print(key)
