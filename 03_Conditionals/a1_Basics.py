# ====================================
# Conditional Statements in Python
# ====================================

# Conditionals are used to make decisions in a program.
# Python uses:
# 1. if
# 2. if-else
# 3. if-elif-else
# 4. Nested if
# 5. Logical operators


print(" ------------------------------------")
print(" 1. Simple if Statement")

age = 20

# Checks if condition is True
if age >= 18:
    print("You are eligible to vote")

print(" ------------------------------------")
print(" 2. if-else Statement")

number = 7

# Executes one block if condition is True
# Otherwise executes else block
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print(" ------------------------------------")
print(" 3. if-elif-else Statement")

marks = 85

# Used when multiple conditions exist
if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

print(" ------------------------------------")
print(" 4. Nested if Statement")

username = "admin"
password = "1234"

# One if inside another if
if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

print(" ------------------------------------")
print(" 5. Logical Operators")

age = 25
has_id = True

# and -> both conditions must be True
if age >= 18 and has_id:
    print("Entry Allowed")

# or -> at least one condition must be True
temperature = 35

if temperature > 30 or temperature < 10:
    print("Extreme Weather")

# not -> reverses condition
is_logged_in = False

if not is_logged_in:
    print("Please Login")

print(" ------------------------------------")
print(" 6. Short-Hand if Statement")

salary = 50000

# Single line if
if salary > 40000:
    print("Good Salary")

print(" ------------------------------------")
print(" 7. Ternary Operator")

age = 16

# Short form of if-else
result = "Adult" if age >= 18 else "Minor"

print(result)

print(" ------------------------------------")
print(" 8. Multiple Conditions Example")

username = "Mohan"
password = "python123"

if username == "Mohan" and password == "python123":
    print("Login Success")
else:
    print("Login Failed")

print("------------------------------------")
print(" 9. Real-Life Example")

amount = 1500

if amount >= 2000:
    print("You got 20% discount")
elif amount >= 1000:
    print("You got 10% discount")
else:
    print("No discount available")
