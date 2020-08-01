age = 22

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

if age == 22:
    pass

# Logical Operators
name = "Zach"

if not name.strip():
    print("Name is empty")

#  Longform
if age >= 18 and age < 65:
    print("Not Retired")

#  Shorthand
if 18 <= age < 65:
    print("Not Retired")

#  Ternary Operators
message = "Eligible" if age >= 18 else "Not Eligible"
