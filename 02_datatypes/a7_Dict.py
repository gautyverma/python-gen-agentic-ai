object_vehicle = dict(vehicle="car", type="hatchBack", color="red", year=2020)
print(f"Object vehicle: {object_vehicle}")

# =============================
# Dictionary Operations in Python
# =============================

# Creating a Dictionary
student = {
    "name": "Mohan",
    "age": 22,
    "course": "Python"
}

print("Original Dictionary:", student)


# -----------------------------
# Accessing Values
# -----------------------------
print("\nAccessing Values")

# Using key
print("Name:", student["name"])

# Using get() method
print("Course:", student.get("course"))

# get() avoids error if key does not exist
print("City:", student.get("city", "Not Found"))


# -----------------------------
# Adding New Key-Value Pair
# -----------------------------
print("\nAdding New Data")

student["city"] = "Delhi"

print("Updated Dictionary:", student)


# -----------------------------
# Updating Existing Value
# -----------------------------
print("\nUpdating Existing Value")

student["age"] = 23

print("Updated Age:", student)


# -----------------------------
# Removing Elements
# -----------------------------
print("\nRemoving Elements")

# pop() removes specific key
removed_course = student.pop("course")

print("Removed Course:", removed_course)
print("After pop():", student)

# del removes key permanently
del student["city"]

print("After del:", student)


# -----------------------------
# Dictionary Length
# -----------------------------
print("\nDictionary Length")

print("Total Keys:", len(student))


# -----------------------------
# Checking Key Existence
# -----------------------------
print("\nChecking Key")

if "name" in student:
    print("Key 'name' exists")


# -----------------------------
# Looping Through Dictionary
# -----------------------------
print("\nLooping Through Dictionary")

# Print keys
for key in student:
    print("Key:", key)

# Print values
for value in student.values():
    print("Value:", value)

# Print key-value pairs
for key, value in student.items():
    print(f"{key} --> {value}")


# -----------------------------
# Copying Dictionary
# -----------------------------
print("\nCopying Dictionary")

student_copy = student.copy()

print("Copied Dictionary:", student_copy)


# -----------------------------
# Clearing Dictionary
# -----------------------------
print("\nClearing Dictionary")

student_copy.clear()

print("After clear():", student_copy)