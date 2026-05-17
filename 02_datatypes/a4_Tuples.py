crew_members = ("Moneky D Luffy", "Roronaro Zoro", "Vinsmoke Sanji")
(luffy, zoro, sanji) = crew_members  # unpacking the tuple into individual variables

print(f"Top members of straw hats are : {luffy}, {zoro}, {sanji}")

pos_zoro, pos_sanji, pos_luffy = 2, 3, 1
print(f"Crew Member positions are :"
      f"\n{luffy} : {pos_luffy}"
      f"\n{zoro} : {pos_zoro}"
      f"\n{sanji} : {pos_sanji}")

print(f"------------------------")
pos_zoro, pos_sanji, pos_luffy = pos_sanji, pos_zoro, pos_luffy  # Swapping without 3rd variable
print(f"Updated Crew Member positions are :"
      f"\n{luffy} : {pos_luffy}"
      f"\n{zoro} : {pos_zoro}"
      f"\n{sanji} : {pos_sanji}")

# Membership
robin = "Robin"
print(f"Is {robin} a member of straw hats? : {robin in crew_members}")
print(f"Is {luffy} a member of straw hats? : {luffy in crew_members}")
