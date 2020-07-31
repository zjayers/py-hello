numbers = [1, 2]

# Index Error Exception
try:
    print(numbers[3])  # Throws an index error
except IndexError:
    print("Index does not exist")

# Value Error Example with Else Block
try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as error:
    print("You didn't enter a valid age!")
    print(error)
    print(type(error))
else:
    print("No exceptions were thrown!")
finally:
    file.close()

# Method 2 For File Opening
try:
    with open("app.py") as file, open('dictionary.py') as target:
        print("File Opened")

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as error:
    print("You didn't enter a valid age!")
    print(error)
    print(type(error))
else:
    print("No exceptions were thrown!")


# Custom Exception Messages - NOT GOOD PRACTICE
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less!")
    return age * 10


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# Timing
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less!")
    return age * 10


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

print('Bad Handling Time: ', timeit(code1, number=10000))

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return age * 10

if calculate_xfactor(-1) == None:
    pass
"""

print('Good Handling Time: ', timeit(code2, number=10000))
