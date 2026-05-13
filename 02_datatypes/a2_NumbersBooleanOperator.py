# Numbers
# Mathematical operations on numbers
import sys

print("-----------------------")
print("Numbers")
print("-----------------------")

num1 = 13
num2 = 5

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulo:", num1 % num2)
print("Exponentiation:", num1 ** num2)

# Boolean
print("-----------------------")
print("Boolean")
print("-----------------------")

is_condition = True
count_condition = 5
print("Condition:", is_condition)
print("upcasting:", count_condition + is_condition) # upcasting

is_false = False
print("False:", is_false)
#  1,or any value -> True and 0,None -> False
is_false = 0
print("False:", is_false)
print("False:", bool(is_false))

print("-----------------------")
is_true = "Random value"
print("True:", is_true)
print("True:", bool(is_true))
print("-----------------------")

# Logical Operators
print("-----------------------")
print("Logical Operators")
print("-----------------------")

condition_1 = True
condition_2 = False
condition_3 = "dummy value"
print("condition_1:", condition_1)
print("condition_2:", condition_2)
print("condition_3:", condition_3)
print("---------------------------------")
print("condition_1 and condition_2:", condition_1 and condition_2)
print("condition_1 or condition_2:", condition_1 or condition_2)
print("not condition_1:", not condition_1)
print("condition_1 and condition_3:", condition_1 and condition_3)
print("condition_1 and bool(condition_3):", condition_1 and bool(condition_3))


# Floating Numbers
print("-----------------------")
print("Floating Numbers")
print("-----------------------")


ideal_temp = 95.5
current_temp = 95.49
print(f"Ideal temp: {ideal_temp}")
print(f"Current temp: {current_temp}")
print(f"Difference b/w ideal temp and current temp: {ideal_temp - current_temp}")
print(sys.float_info)