essential_device = {"Keyboard", "Mouse", "CPU", "Monitor", "Speaker"}
optional_device = {"Printer", "Scanner", "Speaker"}

# Union of two sets
all_devices = essential_device | optional_device
print(f"All devices: {all_devices}")

# Intersection of two sets
common_devices = essential_device & optional_device
print(f"Common devices: {common_devices}")

# Only in essential
only_devices_in_essential = essential_device - optional_device
print(f"Only in essential: {only_devices_in_essential}")

# Only in optional
only_devices_in_optional = optional_device - essential_device
print(f"Only in optional: {only_devices_in_optional}")
