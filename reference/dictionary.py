from sys import getsizeof

point = {"x": 1, "y": 2}
point = dict(x=1, y=2)

# Get values
x = point['x']
point['x'] = 10

# Adding Keys
point['z'] = 20

# Avoiding Non Existent Key Error
a = point.get("a")  # return None if key doesnt exist
a = point.get("a", 0)  # Return 0 if key doesnt exist

# Remove Items
del point['x']

# Looping over dicts
for key in point:
    print(key, point[key])

for key, value in point.items():
    print(key, value)

#  Comprehensions
values = []
for x in range(5):
    values.append(x * 2)

#  COMP
# [expression for item in items]
values = [x * 2 for x in range(5)] # Return as List
values = {x * 2 for x in range(5)}  # Return as Set
values = {x: x * 2 for x in range(5)}  # Return as Dictionary

# Return as Generator Object <Tuple>
values = (x * 2 for x in range(100000))
print("generator:", getsizeof(values))