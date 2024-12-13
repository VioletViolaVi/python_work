# Calculate area of a rectangle (length * breadth)

user_length = float((input("please enter the length: ")))
user_breadth = float(input("please enter the breadth: "))

rect_area = user_length * user_breadth

print(f"The area of your rectangle is: {rect_area}cm2")


print("----- checks below ----- ")
print(f"user_length is: {user_length}")
print(f"user_length TYPE is: {type(user_length)}")

print(f"user_breadth is: {user_breadth}")
print(f"user_breadth TYPE is: {type(user_breadth)}")
