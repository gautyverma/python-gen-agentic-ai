# ======================================
# Decorators in Python
# ======================================

# Decorator:
#
# A decorator is a function that
# modifies another function
# without changing its original code.
#
# Decorators are used to:
#
# 1. Add extra behavior
# 2. Logging
# 3. Authentication
# 4. Timing
# 5. Validation
# 6. Caching
#
# Decorators follow:
#
# Functions are first-class objects in Python
#
# Meaning:
# Functions can be:
# - stored in variables
# - passed as arguments
# - returned from functions


print("--------------------------------------")
print("Functions as Variables")


def greet():

    print("Hello User")


say_hello = greet

say_hello()


print("--------------------------------------")
print("Function Inside Another Function")


def outer():

    print("Outer Function")

    def inner():

        print("Inner Function")

    inner()


outer()


print("--------------------------------------")
print("Returning Function from Function")


def parent():

    def child():

        print("Child Function")

    return child


returned_function = parent()

returned_function()


# ======================================
# Basic Decorator
# ======================================

print("--------------------------------------")
print("Basic Decorator Example")


def decorator_function(original_function):

    def wrapper():

        print("Before Function Call")

        original_function()

        print("After Function Call")

    return wrapper


def display():

    print("Hello from display function")


decorated_function = decorator_function(display)

decorated_function()


# ======================================
# Using @ Decorator Syntax
# ======================================

print("--------------------------------------")
print("@ Decorator Syntax")


def simple_decorator(func):

    def wrapper():

        print("Function Started")

        func()

        print("Function Ended")

    return wrapper


@simple_decorator
def greet_user():

    print("Welcome User")


greet_user()

# Equivalent to:
#
# greet_user = simple_decorator(greet_user)


# ======================================
# Decorator with Parameters
# ======================================

print("--------------------------------------")
print("Decorator with Parameters")


def smart_decorator(func):

    def wrapper(name):

        print("Before Greeting")

        func(name)

        print("After Greeting")

    return wrapper


@smart_decorator
def say_hello(name):

    print(f"Hello {name}")


say_hello("Mohan")


# ======================================
# Decorator Returning Value
# ======================================

print("--------------------------------------")
print("Decorator Returning Value")


def calculate_decorator(func):

    def wrapper(a, b):

        print("Calculation Started")

        result = func(a, b)

        print("Calculation Completed")

        return result

    return wrapper


@calculate_decorator
def add(a, b):

    return a + b


print(add(10, 20))


# ======================================
# Using *args and **kwargs
# ======================================

print("--------------------------------------")
print("Flexible Decorator")


def universal_decorator(func):

    def wrapper(*args, **kwargs):

        print("Before Function")

        result = func(*args, **kwargs)

        print("After Function")

        return result

    return wrapper


@universal_decorator
def multiply(a, b):

    return a * b


print(multiply(4, 5))


@universal_decorator
def student(name, age):

    print(f"Name: {name}, Age: {age}")


student("Rahul", 22)


# ======================================
# Real-Life Decorator Examples
# ======================================

print("--------------------------------------")
print("Logging Decorator")


def logger(func):

    def wrapper(*args, **kwargs):

        print(f"Calling Function: {func.__name__}")

        result = func(*args, **kwargs)

        print("Function Execution Completed")

        return result

    return wrapper


@logger
def login():

    print("User Logged In")


login()


print("--------------------------------------")
print("Authentication Decorator")


is_logged_in = False


def authentication(func):

    def wrapper():

        if is_logged_in:

            return func()

        else:

            print("Access Denied")

    return wrapper


@authentication
def dashboard():

    print("Welcome to Dashboard")


dashboard()


print("--------------------------------------")
print("Timing Decorator")


import time


def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end - start)

        return result

    return wrapper


@timer
def slow_function():

    time.sleep(2)

    print("Function Completed")


slow_function()


print("--------------------------------------")
print("Input Validation Decorator")


def validate_positive(func):

    def wrapper(number):

        if number < 0:

            print("Negative numbers not allowed")

            return

        return func(number)

    return wrapper


@validate_positive
def square(number):

    print(number * number)


square(5)
square(-2)


# ======================================
# Multiple Decorators
# ======================================

print("--------------------------------------")
print("Multiple Decorators")


def decorator_one(func):

    def wrapper():

        print("Decorator One")

        func()

    return wrapper


def decorator_two(func):

    def wrapper():

        print("Decorator Two")

        func()

    return wrapper


@decorator_one
@decorator_two
def display_message():

    print("Hello World")


display_message()

# Execution Order:
#
# decorator_one(
#     decorator_two(display_message)
# )


# ======================================
# Class Decorator Example
# ======================================

print("--------------------------------------")
print("Class Decorator Example")


def class_decorator(cls):

    cls.company = "Google"

    return cls


@class_decorator
class Employee:

    pass


emp = Employee()

print(emp.company)


# ======================================
# Real-Life Analogy
# ======================================

print("--------------------------------------")
print("Decorator Analogy")

# Think of decorator like:
#
# Gift Wrapping
#
# Original Function -> Gift
# Decorator -> Wrapper
#
# Gift stays same
# Extra layer added outside