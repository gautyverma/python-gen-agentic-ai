crew_members = ["Luffy", "Zoro", "Sanji"]
crew_members.append("Nami")  # Adding a new member to the list
print(f"Members of straw hats are : {crew_members}")
crew_members.remove("Sanji")
print(f"Members of straw hats are : {crew_members}")

new_members = ['Jimbie', 'Robin', 'Chopper', 'Franky', 'Usopp']

crew_members.extend(new_members)  # Adding multiple members to the list
print(f"Members of straw hats are : {crew_members}")
crew_members.append("Sanji")
print(f"Members of straw hats are : {crew_members}")

# remove last item from list
print(f"{crew_members.pop()}")
crew_members.reverse()
print(f"Reversed: Members of straw hats are : {crew_members}")

# Sorting
crew_members.sort()
print(f"Sorted:Members of straw hats are : {crew_members}")

# Operator overloading
base_liquid = ["Water", "Milk", "Juice"]
mix_flavor = ["Soda", "Mango"]
print(f"All Drinks : {base_liquid + mix_flavor}")

print(f"Two Times base_liquid : {base_liquid * 2}")

# Byte Array
raw_data = bytearray(b"Mango")
print(f"Byte Raw data: {raw_data}")

raw_data = raw_data.replace(b"M", b"T")
print(f"Byte Raw data: {raw_data}")
