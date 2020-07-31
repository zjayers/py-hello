numbers = [1,1,2,3,3,4]
first = set(numbers)
print(first)

second = {1, 6}
second.add(5)
second.remove(5)

# Add Sets Together
print(first | second)

# Intersection of Two Sets
print(first & second)

# Difference between two sets
print(first - second)

# Symmetric Difference
print(first ^ second)

# Check if in set
if 1 in first:
    print('yes')