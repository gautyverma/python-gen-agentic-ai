# ================================
# Loops in Python
# ================================

# Loops are used to repeat a block of code multiple times.
# Python mainly provides:
# 1. for loop
# 2. while loop


# --------------------------------
# 1. for Loop
# --------------------------------

# for loop is used when we know
# how many times we want to repeat.

print("for Loop Example")

for i in range(5):
    print("Value of i:", i)


# range(5) -> Generates numbers from 0 to 4


# --------------------------------
# 2. range() Variations
# --------------------------------

print("\nrange(start, stop)")

for i in range(1, 6):
    print(i)


print("\nrange(start, stop, step)")

for i in range(1, 10, 2):
    print(i)


# --------------------------------
# 3. Loop Through String
# --------------------------------

print("\nLoop Through String")

name = "Python"

for ch in name:
    print(ch)


# --------------------------------
# 4. Loop Through List
# --------------------------------

print("\nLoop Through List")

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# --------------------------------
# 5. while Loop
# --------------------------------

# while loop runs until condition becomes False

print("\nwhile Loop Example")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# --------------------------------
# 6. Infinite Loop
# --------------------------------

# Be careful with infinite loops

# while True:
#     print("This runs forever")


# --------------------------------
# 7. break Statement
# --------------------------------

# break stops the loop immediately

print("\nbreak Example")

for i in range(1, 10):
    if i == 5:
        break

    print(i)


# --------------------------------
# 8. continue Statement
# --------------------------------

# continue skips current iteration

print("\ncontinue Example")

for i in range(1, 6):

    if i == 3:
        continue

    print(i)


# --------------------------------
# 9. pass Statement
# --------------------------------

# pass does nothing
# Used as placeholder

print("\npass Example")

for i in range(3):

    pass

print("Loop completed")


# --------------------------------
# 10. Nested Loop
# --------------------------------

# Loop inside another loop

print("\nNested Loop Example")

for i in range(1, 4):

    for j in range(1, 4):

        print(f"i = {i}, j = {j}")


# --------------------------------
# 11. Real-Life Example
# --------------------------------

print("\nTable of 5")

for i in range(1, 11):

    print(f"5 x {i} = {5 * i}")


# --------------------------------
# 12. else with Loop
# --------------------------------

# else executes when loop finishes normally

print("\nLoop with else")

for i in range(3):
    print(i)
else:
    print("Loop Finished Successfully")