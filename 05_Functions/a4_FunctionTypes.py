# ======================================
# Pure Functions vs Impure Functions
# ======================================

# Pure Function:
#
# 1. Same input -> Same output
# 2. No side effects
# 3. Does not modify external state

# Impure Function:
#
# 1. Depends on external state OR
# 2. Modifies external state
# 3. Can produce different outputs


print("--------------------------------------")
print("Pure Function Example")


def add(a, b):

    return a + b


print(add(10, 20))
print(add(10, 20))

# Output always same:
# 30
# 30


print("--------------------------------------")
print("Impure Function Example")


count = 0


def increment():

    global count

    count += 1

    return count


print(increment())
print(increment())
print(increment())

# Output changes:
# 1
# 2
# 3


print("--------------------------------------")
print("Impure Function Using External Variable")


name = "Mohan"


def greet():

    return f"Hello {name}"


print(greet())

# Depends on external variable


print("--------------------------------------")
print("Pure vs Impure Comparison")


# Pure Function
def pure_multiply(a, b):

    return a * b


# Impure Function
value = 10


def impure_multiply():

    global value

    value += 5

    return value * 2


print("Pure:", pure_multiply(2, 5))
print("Pure:", pure_multiply(2, 5))

print("Impure:", impure_multiply())
print("Impure:", impure_multiply())


# ======================================
# Recursive Functions
# ======================================

# Recursion:
#
# A function calling itself.
#
# Important:
# Every recursive function must have:
#
# 1. Base Case
# 2. Recursive Call


print("--------------------------------------")
print("Basic Recursion Example")


def countdown(n):

    if n == 0:
        print("Finished")
        return

    print(n)

    countdown(n - 1)


countdown(5)


print("--------------------------------------")
print("Factorial Using Recursion")


def factorial(n):

    # Base Case
    if n == 1:
        return 1

    # Recursive Call
    return n * factorial(n - 1)


print(factorial(5))

# 5 * 4 * 3 * 2 * 1
# Output: 120


# ======================================
# Lambda Functions
# ======================================

# Lambda:
#
# Small anonymous one-line function
#
# Syntax:
#
# lambda arguments : expression


print("--------------------------------------")
print("Basic Lambda Example")


# Normal Function
def square(num):

    return num * num


print(square(5))


# Lambda Function
square_lambda = lambda num: num * num

print(square_lambda(5))


print("--------------------------------------")
print("Lambda with Multiple Parameters")


add = lambda a, b: a + b

print(add(10, 20))


multiply = lambda x, y: x * y

print(multiply(4, 5))


print("--------------------------------------")
print("Lambda with map()")


numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))

print(doubled)

# Output:
# [2, 4, 6, 8, 10]


print("--------------------------------------")
print("Lambda with filter()")


numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)

# Output:
# [2, 4, 6]


print("--------------------------------------")
print("Lambda with sorted()")


students = [
    ("Mohan", 85),
    ("Rahul", 92),
    ("Aman", 78)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1]
)

print(sorted_students)

# Sorted by marks


print("--------------------------------------")
print("Lambda with Conditional Expression")


check_even = lambda num: (
    "Even" if num % 2 == 0 else "Odd"
)

print(check_even(10))
print(check_even(7))


print("--------------------------------------")
print("Immediate Lambda Execution")


result = (lambda a, b: a + b)(5, 3)

print(result)