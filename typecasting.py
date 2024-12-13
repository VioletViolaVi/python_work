# Typecasting

name = "Vivian"
age = 30
pay = 11.44
is_hungry = False

print(type(name))
print(type(age))
print(type(pay))
print(type(is_hungry))

print(" --------- After changing type --------- ")

print(f"'30' integer changed into float: {float(age)}")

pay_type_change = int(pay)
print(f"'11.44' float changed into integer: {pay_type_change}")

age_type_change = str(age)
print(f"'30' integer changed into string: {age_type_change}")
print(f"'30 age' should be a string type here: {type(age_type_change)}")

# print(age_type_change + 1) --------- this produces an error as u cannot concatenate a string and integer

name_type_change = bool(name)
print(f"'Vivian' string changed into boolean: {name_type_change}")
