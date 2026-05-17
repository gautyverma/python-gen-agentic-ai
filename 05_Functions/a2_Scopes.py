# ======================================
# Variable Scope in Python
# ======================================

# Scope means:
# "Where a variable can be accessed"

# Python mainly has:
# 1. Local Scope
# 2. Global Scope
# 3. Global Keyword
# 4. Nested Scope

print("--------------------------------------")
print("Local Scope")


# Variable created inside function
# can only be used inside that function

def my_function():
    message = "Hello from Local Scope"
    print(message)


my_function()

# print(message)
# ERROR -> message cannot be accessed outside function


print("--------------------------------------")
print("Global Scope")

# Variable created outside function
# can be accessed everywhere

name = "Mohan"


def display_name():
    print("Name:", name)


display_name()

print("Outside Function:", name)

print("--------------------------------------")
print("Local Variable vs Global Variable")

x = 100


def test_scope():
    x = 50  # Local variable
    print("Inside Function:", x)


test_scope()

print("Outside Function:", x)

# Output:
# Inside Function: 50
# Outside Function: 100


print("--------------------------------------")
print("Nested Scope")


# Inner function can access outer function variables

def outer():
    message = "Hello from Outer Function"

    def inner():
        print(message)

    inner()


outer()

print("--------------------------------------")
print("LEGB Rule")

# Python searches variables in this order:
#
# L -> Local
# E -> Enclosing
# G -> Global
# B -> Built-in


x = "Global"


def outer_function():
    x = "Enclosing"

    def inner_function():
        x = "Local"
        print("Inside Inner:", x)

    inner_function()

    print("Inside Outer:", x)


outer_function()

print("Outside:", x)

# Output:
# Inside Inner: Local
# Inside Outer: Enclosing
# Outside: Global

print("--------------------------------------")
print("Built-in Scope Example")

# print(), len(), sum() are built-in functions

numbers = [10, 20, 30]

print("Length:", len(numbers))
print("Total:", sum(numbers))

# ======================================
# Difference Between global and nonlocal
# ======================================

# global  -> modifies global variable
# nonlocal -> modifies enclosing variable


print("--------------------------------------")
print("global Example")

count = 100


def update_global():
    global count
    count += 10
    print("Global Count:", count)


update_global()

print("--------------------------------------")
print("nonlocal Example == ")


def outer_function():
    score = 50

    def update_score():
        nonlocal score
        score += 20
        print("Updated Score:", score)

    update_score()
    print("Final Score:", score)


outer_function()
