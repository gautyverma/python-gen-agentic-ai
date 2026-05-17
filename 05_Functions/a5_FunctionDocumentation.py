# ======================================
# Documenting Functions in Python
# ======================================

# Function documentation means:
# Explaining what a function does.
#
# Python uses:
# Docstrings
#
# Docstring:
# A string written inside triple quotes
# just below function definition.


print("--------------------------------------")
print("Basic Function Documentation")


def greet():
    """
    This function prints a welcome message.
    """

    print("Hello, Welcome to Python!")


greet()

# Accessing documentation
print(greet.__doc__)

print("--------------------------------------")
print("Function with Parameters Documentation")


def add(a, b):
    """
    Adds two numbers.

    Parameters:
    a (int) : First number
    b (int) : Second number

    Returns:
    int : Sum of a and b
    """

    return a + b


print(add(10, 20))

print(add.__doc__)
print("Function Name: " + add.__name__)

print("--------------------------------------")
print("Single-Line Docstring")


def square(num):
    """Returns square of a number."""

    return num * num


print(square(5))

print(square.__doc__)

print("--------------------------------------")
print("Multi-Line Docstring")


def student_details(name, age):
    """
    Displays student information.

    Args:
        name (str): Student name
        age (int): Student age

    Returns:
        None
    """

    print(f"Name: {name}")
    print(f"Age: {age}")


student_details("Mohan", 22)

print(student_details.__doc__)

print("--------------------------------------")
print("Using help() Function")


def multiply(a, b):
    """
    Multiplies two numbers.

    Example:
        multiply(2, 3) -> 6
    """

    return a * b


print(multiply(4, 5))

# Displays formatted documentation
help(multiply)

print("--------------------------------------")
print("Documenting Recursive Function")


def factorial(n):
    """
    Calculates factorial using recursion.

    Formula:
        n! = n * (n - 1)!

    Example:
        factorial(5) -> 120
    """

    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))

print(factorial.__doc__)

print("--------------------------------------")
print("Documenting Lambda Function")

# Lambda functions cannot directly
# have docstrings because they are anonymous.

square_lambda = lambda x: x * x

print(square_lambda(5))

print("--------------------------------------")
print("Real-Life Example")


def calculate_bill(price, quantity):
    """
    Calculates total bill amount.

    Parameters:
        price (float): Price of one item
        quantity (int): Number of items

    Returns:
        float: Total bill amount
    """

    return price * quantity


bill = calculate_bill(40, 3)

print("Total Bill:", bill)

print(calculate_bill.__doc__)
