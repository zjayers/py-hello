items = [
    ("Product1", 10),
    ("Product2", 15),
    ("Product3", 9),
    ("Product4", 2),
]

#  Sorting
items.sort(key=lambda item: item[1])

# Mapping
pricesAsMap = map(lambda item: item[1], items)
for item in pricesAsMap:
    print(item)

pricesAsList = list(map(lambda item: item[1], items))
print(pricesAsList)

# Comprehension
prices = [item[1] for item in items]

# Filtering
filteredAsFilter = filter(lambda item: item[1] >= 10, items)
for item in filteredAsFilter:
    print(item)

filterASList = list(map(lambda item: item[1] >= 10, items))

# Comprehension
prices = [item for item in items if item[1] >= 10]

# Zipping
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(zip(list1, list2))  # Returns Zip Object
print(list(zip("abc", list1, list2)))
