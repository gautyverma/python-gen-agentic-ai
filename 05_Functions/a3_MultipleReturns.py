# ======================================
# Multiple Return Values in Python
# ======================================

# Python functions can return
# multiple values at the same time.


print("--------------------------------------")
print("Basic Multiple Return Example")


def calculate(a, b):

    addition = a + b
    subtraction = a - b

    return addition, subtraction


result = calculate(10, 5)

print(result)

# Output:
# (15, 5)

# Python actually returns a tuple


print("--------------------------------------")
print("Unpacking Multiple Returns")


def math_operations(a, b):

    return a + b, a * b, a / b


add, multiply, divide = math_operations(20, 10)

print("Addition:", add)
print("Multiplication:", multiply)
print("Division:", divide)


print("--------------------------------------")
print("Returning Different Data Types")


def student_details():

    name = "Mohan"
    age = 22
    skills = ["Python", "Java"]

    return name, age, skills


name, age, skills = student_details()

print("Name:", name)
print("Age:", age)
print("Skills:", skills)


print("--------------------------------------")
print("Ignoring Unwanted Values")


def numbers():

    return 10, 20, 30, 40


a, _, c, _ = numbers()

print("a:", a)
print("c:", c)

# _ is commonly used to ignore values


print("--------------------------------------")
print("Returning List and Dictionary")


def get_data():

    numbers = [1, 2, 3]
    student = {
        "name": "Rahul",
        "age": 21
    }

    return numbers, student


num_list, student_data = get_data()

print("Numbers:", num_list)
print("Student:", student_data)


print("--------------------------------------")
print("Using * with Multiple Returns")


def marks():

    return 90, 85, 95, 88


first, *remaining = marks()

print("First:", first)
print("Remaining:", remaining)

# Output:
# First: 90
# Remaining: [85, 95, 88]


print("--------------------------------------")
print("Real-Life Example")


def login():

    username = "admin"
    is_logged_in = True
    token = "ABC123"

    return username, is_logged_in, token


user, status, auth_token = login()

print("Username:", user)
print("Login Status:", status)
print("Token:", auth_token)


print("--------------------------------------")
print("Returning Conditional Results")


def is_even_number(num):

    if num % 2 == 0:
        return "Even", True

    return "Odd", False


message, status = is_even_number(10)

print("Message:", message)
print("Status:", status)