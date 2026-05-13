print("Immutable and mutable")
num = 2
print(f"Number: {num}")
print(f"memory id of {num}: {id(num)}")

num = 12
print(f"Number:{num}")
print(f"memory id of {num}: {id(num)}")

# Both num are created at different memory location.
# Hence, we can say that numbers are immutable objects.
# where num variable is reference object which refers to above memory location

spice_mix = set()
print(f"Initial state of spice_mix: {spice_mix}")
spice_mix.add("Ginger")
spice_mix.add("Garlic")
spice_mix.add("Turmeric")
print(f"state after addition of spice_mix: {spice_mix}")
