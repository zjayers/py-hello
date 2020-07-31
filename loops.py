# For Loops
# Strings
for x in "Python":
    print(x)

# List
for x in ['a', 'b', 'c']:
    print(x)

# Range
for x in range(0, 10, 2):  # Start, End, Step
    print(x)

#  For Else
names = ["John", "Mary"]

for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not Found")

# While Loops
guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
else:
    pass
