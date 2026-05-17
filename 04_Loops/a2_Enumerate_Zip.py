# ======================================
# enumerate() in Python
# ======================================

# enumerate() is used when we want:
# 1. Index
# 2. Value
# together while looping


fruits = ["Apple", "Banana", "Mango"]

print("Using enumerate()")

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
# 0 Apple
# 1 Banana
# 2 Mango


# --------------------------------------
# enumerate() with custom starting index
# --------------------------------------

print("\nCustom Starting Index")

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Output:
# 1 Apple
# 2 Banana
# 3 Mango


# ======================================
# zip() in Python
# ======================================

# zip() combines multiple iterables
# element by element


names = ["Mohan", "Rahul", "Aman"]
marks = [85, 90, 78]

print("\nUsing zip()")

for name, mark in zip(names, marks):
    print(name, mark)

# Output:
# Mohan 85
# Rahul 90
# Aman 78


# ======================================
# zip() with 3 Lists
# ======================================

cities = ["Delhi", "Mumbai", "Pune"]

print("\nzip() with 3 lists")

for name, mark, city in zip(names, marks, cities):
    print(name, mark, city)

# ======================================
# Convert zip Object to List
# ======================================

result = list(zip(names, marks))

print("\nConverted zip to list")

print(result)

# Output:
# [('Mohan', 85), ('Rahul', 90), ('Aman', 78)]


# ======================================
# Important Note About zip()
# ======================================

# zip() stops at shortest iterable


list1 = [1, 2, 3, 4]
list2 = ["A", "B"]

print("\nzip() stops at shortest list")

for x, y in zip(list1, list2):
    print(x, y)

# Output:
# 1 A
# 2 B


# ======================================
# Real-Life Example
# ======================================

subjects = ["Math", "Science", "English"]
scores = [95, 88, 91]

print("\nStudent Report Card")

for index, (subject, score) in enumerate(zip(subjects, scores), start=1):
    print(f"{index}. {subject} --> {score}")
