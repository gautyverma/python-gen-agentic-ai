# ======================================
# Functions in Python
# ======================================

# A function is a reusable block of code
# that performs a specific task.

# Syntax:
#
# def function_name():
#     code


# --------------------------------------
# 1. Basic Function
# --------------------------------------

def greet():
    print("Hello, Welcome to Python!")


# Function Call
greet()


# --------------------------------------
# 2. Function with Parameters
# --------------------------------------

# Parameters are inputs passed to function

def greet_user(name):
    print(f"Hello {name}")


greet_user("Mohan")
greet_user("Rahul")


# --------------------------------------
# 3. Function with Multiple Parameters
# --------------------------------------

def add(a, b):
    print("Addition:", a + b)


add(10, 20)
add(5, 7)


# --------------------------------------
# 4. Function with Return Value
# --------------------------------------

# return sends value back from function

def multiply(a, b):
    return a * b


result = multiply(4, 5)

print("Multiplication Result:", result)


# --------------------------------------
# 5. Difference Between print() and return
# --------------------------------------

# print() -> Displays output
# return -> Gives value back


def square(num):
    return num * num


value = square(6)

print("Square:", value)


# --------------------------------------
# 6. Default Parameters
# --------------------------------------

# Default value is used if argument not passed

def country(name="India"):
    print("Country:", name)


country()
country("Japan")


# --------------------------------------
# 7. Keyword Arguments
# --------------------------------------

def student(name, age):
    print(f"Name: {name}, Age: {age}")


student(age=22, name="Mohan")


# --------------------------------------
# 8. Arbitrary Arguments (*args)
# --------------------------------------

# *args accepts multiple values

def total_marks(*marks):
    print("Marks:", marks)

    print("Total:", sum(marks))


total_marks(80, 90, 70, 60)


# --------------------------------------
# 9. Arbitrary Keyword Arguments (**kwargs)
# --------------------------------------

# **kwargs accepts multiple key-value pairs

def student_info(**details):
    print(details)


student_info(name="Mohan", age=22, city="Delhi")


# --------------------------------------
# 10. Function with Loop
# --------------------------------------

def print_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


print_table(5)


# --------------------------------------
# 11. Function with Conditional
# --------------------------------------

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"

    return "Odd"


print(check_even_odd(10))
print(check_even_odd(7))


# --------------------------------------
# 12. Nested Function
# --------------------------------------

def outer_function():
    print("Outer Function")

    def inner_function():
        print("Inner Function")

    inner_function()


outer_function()


# --------------------------------------
# 13. Real-Life Example
# --------------------------------------

def calculate_bill(price, quantity):
    total = price * quantity

    return total


bill = calculate_bill(40, 3)

print("Total Bill:", bill)

print("--------------------------------")
print("Handling arguments in functions")
print("*args & **kargs")


def items(*essentials, **extras):
    print("Essential Items:", essentials)
    print("Extra Items:", extras)


items("Bread", "Milk", "Eggs", snacks="Chips", drinks="Juice")
