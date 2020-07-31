numbers = [1, 2, 3]
print(*numbers)

values = [*range(5), *"Hello"]

values2 = [*values, *values]

# Unpack Dictionaries
dict = {"x": 1}
dict2 = {"x": 1, "y": 2}
combinedDicts = {**dict, **dict2, "z": 1}
