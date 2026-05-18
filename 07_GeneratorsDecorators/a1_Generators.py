# ======================================
# Generators in Python
# ======================================

# Generator:
#
# A special function that produces
# values one at a time using yield.
#
# Generators are memory efficient because
# they do not store all values together.


print("--------------------------------------")
print("Basic Generator Example")


def numbers():
    yield 1
    yield 2
    yield 3


gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))

print("--------------------------------------")
print("Generator with Loop")


def even_numbers(limit):
    for i in range(limit):

        if i % 2 == 0:
            yield i


for num in even_numbers(10):
    print(num)

print("--------------------------------------")
print("Generator Expression")

squares = (
    num * num
    for num in range(5)
)

for value in squares:
    print(value)

print("--------------------------------------")
print("Real-Life Generator Example")


def read_data():
    data = [
        "Row 1",
        "Row 2",
        "Row 3"
    ]

    for row in data:
        yield row


for row in read_data():
    print(row)

# ======================================
# Infinite Generator
# ======================================

# Infinite Generator:
#
# A generator that keeps producing
# values forever until manually stopped.


print("--------------------------------------")
print("Infinite Generator Example")


def infinite_counter():
    num = 1

    while True:
        yield num

        num += 1


counter = infinite_counter()

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# Output:
# 1
# 2
# 3
# 4
# 5


print("--------------------------------------")
print("Infinite Even Number Generator")


def infinite_even_numbers():
    num = 0

    while True:
        yield num

        num += 2


even_gen = infinite_even_numbers()

for _ in range(10):
    print(next(even_gen))

# Output:
# 0
# 2
# 4
# 6
# 8
# ...


print("--------------------------------------")
print("Infinite Fibonacci Generator")


def fibonacci_generator():
    a = 0
    b = 1

    while True:
        yield a

        a, b = b, a + b


fib = fibonacci_generator()

for _ in range(10):
    print(next(fib))

# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# ...


print("--------------------------------------")
print("Stopping Infinite Generator Safely")


def infinite_numbers():
    n = 1

    while True:
        yield n

        n += 1


gen = infinite_numbers()

for value in gen:

    if value > 5:
        break

    print(value)

# Output:
# 1
# 2
# 3
# 4
# 5


print("--------------------------------------")
print("Why Infinite Generators are Useful")

# Infinite generators are useful for:
#
# 1. Live Data Streams
# 2. Sensor Data
# 3. Real-Time Events
# 4. Game Loops
# 5. Pagination
# 6. Large Data Processing


print("--------------------------------------")
print("Real-Life Infinite Generator Example")


def live_temperature_sensor():
    temperature = 25

    while True:
        yield f"Current Temperature: {temperature}°C"

        temperature += 1


sensor = live_temperature_sensor()

for _ in range(5):
    print(next(sensor))

print("--------------------------------------")
print("Send values to generator")


def order():
    print("Welcome! What would you like to order?")
    order = yield
    while True:
        print(f"Your order for {order} is being prepared.")
        order = yield


hub = order()
next(hub)  # Advance to the first yield
hub.send("Pizza")  # Send a value to the generator
hub.send("Burger")  # Send another value to the generator
