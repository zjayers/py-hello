# Lists
letters = ["a", "b", "c"]

# List of Lists
listOfLists = [[0, 1], [2, 3]]

# Create list of 100 zeroes
zeros = [0] * 100

# Create list from iterable
print(list(range(20)))
print(list("Hello World"))

# Index Access
print(letters[0])  # item at index
print(letters[-1])  # reverse access
print(letters[0:3])  # slice
print(letters[::2])  # step
print(letters[::-1])  # reverse order

# Unpacking Lists
first, second, third = letters

# Unpack & packing
first, *other = letters
*other, last = letters

# Looping over lists
for letter in letters:
    print(letter)

# Unpack to get index
for index, letter in enumerate(letters):  # Get index
    print(index, letter)

# Adding & Removing Items
letters.append("d")
letters.insert(0, "prepended")
letters.pop()
letters.pop(0)  # Remove item at location
letters.remove("d")  # Remove first occurrence
del letters[0:3]

letters.clear()  # Remove everything from a list

# Find index of given object
print(letters.index("a"))

if "z" in letters:
    print(letters.index("z"))

# Get number of occurrences
letters.count("z")

# Sorting
letters.sort()
letters.sort(reverse=True)

sorted(letters)
sorted(letters, reverse=True)

# Advanced Sorting
items = [
    ("Product1", 10),
    ("Product2", 15),
    ("Product3", 9),
    ("Product4", 2),
]


def sort_item(item: tuple):
    return item[1]


items.sort(key=sort_item)

