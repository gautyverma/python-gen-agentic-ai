# ======================================
# Comprehensions in Python
# ======================================

# Comprehension provides a short and
# clean way to create:
#
# 1. Lists
# 2. Dictionaries
# 3. Sets


print("--------------------------------------")
print("List Comprehension Basics")

# Normal Way
numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)

# List Comprehension Way
numbers = [i for i in range(5)]

print(numbers)

# Output:
# [0, 1, 2, 3, 4]


print("--------------------------------------")
print("List Comprehension with Condition")

# Even numbers only
even_numbers = [
    i for i in range(10)
    if i % 2 == 0
]

print(even_numbers)

# Output:
# [0, 2, 4, 6, 8]


print("--------------------------------------")
print("List Comprehension with Expression")

squares = [
    num * num
    for num in range(1, 6)
]

print(squares)

# Output:
# [1, 4, 9, 16, 25]


print("--------------------------------------")
print("String Comprehension")

word = "Python"

letters = [
    ch.upper()
    for ch in word
]

print(letters)

# Output:
# ['P', 'Y', 'T', 'H', 'O', 'N']


print("--------------------------------------")
print("Nested List Comprehension")

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

flatten = [
    num
    for row in matrix
    for num in row
]

print(flatten)

# Output:
# [1, 2, 3, 4, 5, 6]


print("--------------------------------------")
print("Conditional Expression in Comprehension")

result = [
    "Even" if i % 2 == 0 else "Odd"
    for i in range(5)
]

print(result)

# Output:
# ['Even', 'Odd', 'Even', 'Odd', 'Even']


# ======================================
# Dictionary Comprehension
# ======================================

print("--------------------------------------")
print("Dictionary Comprehension Basics")

# Create dictionary
squares = {
    num: num * num
    for num in range(1, 6)
}

print(squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


print("--------------------------------------")
print("Dictionary Comprehension with Condition")

even_square = {
    num: num * num
    for num in range(1, 11)
    if num % 2 == 0
}

print(even_square)

print("--------------------------------------")
print("Swap Keys and Values")

student = {
    "name": "Mohan",
    "age": 22
}

swapped = {
    value: key
    for key, value in student.items()
}

print(swapped)

# ======================================
# Set Comprehension
# ======================================

print("--------------------------------------")
print("Set Comprehension Basics")

numbers = {
    num * num
    for num in range(1, 6)
}

print(numbers)

# Output:
# {1, 4, 9, 16, 25}


print("--------------------------------------")
print("Removing Duplicate Values")

numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = {
    num
    for num in numbers
}

print(unique_numbers)

# Output:
# {1, 2, 3, 4}


# ======================================
# Real-Life Examples
# ======================================

print("--------------------------------------")
print("Real-Life Example")

prices = [100, 200, 300]

gst_prices = [
    price + (price * 0.18)
    for price in prices
]

print(gst_prices)

print("--------------------------------------")
print("Real-Life Dictionary Example")

students = ["Mohan", "Rahul", "Aman"]

attendance = {
    student: "Present"
    for student in students
}

print(attendance)

# ======================================
# Generator Comprehension
# ======================================

print("--------------------------------------")
print("Generator Comprehension")

generator = (
    num * num
    for num in range(5)
)

print(generator)

# Generator object created


for value in generator:
    print(value)
