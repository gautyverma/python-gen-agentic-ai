# String
customer_name = "Mohan"
item_name = "idli"
item_quantity = 2
item_price = 40

total_price = item_price * item_quantity

print(f"Item name: {item_name}"
      f"\nItem quantity: {item_quantity}"
      f"\norder for {customer_name} "
      f"\nTotal price: {total_price}")

# String Slicing
temp = "IKIGAI_KAIZEN"

print(temp[0])  # Output: I -> First character
print(temp[1])  # Output: K -> Second character
print(temp[-1])  # Output: N -> Last character

print(temp[0:6])  # Output: IKIGAI -> Characters from index 0 to 5
print(temp[7:13])  # Output: KAIZEN -> Characters from index 7 to 12

print(temp[:6])  # Output: IKIGAI -> From start to index 5
print(temp[7:])  # Output: KAIZEN -> From index 7 to end

print(temp[::2])  # Output: IIAKIE -> Every 2nd character
print(temp[::-1])  # Output: NEZIAK_IAGIKI -> Reverse string

print(temp[-6:])  # Output: KAIZEN -> Last 6 characters
print(temp[3:10])  # Output: GAI_KAI -> Characters from index 3 to 9

print(f"Skipping every 2nd char: {temp[0::2]}")

# Encoding
# String Encoding Example

temp = "IKIGAI_KAI\ZEN"

# Encode string into bytes using UTF-8
encoded_text = temp.encode("utf-8")

print(encoded_text)
# Output: b'IKIGAI_KAIZEN'
# String converted into bytes format

# Decode bytes back to string
decoded_text = encoded_text.decode("utf-8")

print(decoded_text)
# Output: IKIGAI_KAIZEN
# Bytes converted back to normal string

# Type checking
print(type(temp))
# Output: <class 'str'>

print(type(encoded_text))
# Output: <class 'bytes'>

print(type(decoded_text))
# Output: <class 'str'>
