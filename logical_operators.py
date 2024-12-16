# Logical Operators: and | or | not

# Going Clubbing
age = -26
has_id = False

# Getting inside club
if age >= 18 and has_id:
    print("You can go into the club!🍻🍸")
elif age >= 18 and not has_id:
    print("You need id to prove you're of age! 🪪")
elif age < 18 and has_id:
    print("You are not old enough to enter!")
else:
    print("Something has gone wrong! 🤯🫨 😱😲")

