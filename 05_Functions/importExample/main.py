from recipes import Dishes

# Create an instance of the Dishes class
dishes = Dishes()

print("=== Recipes Menu Example ===\n")

# Display the menu
print("Available Dish Categories:")
menu = dishes.get_menu()
for i, dish in enumerate(menu, 1):
    print(f"{i}. {dish}")

print("\n=== Getting Recipes ===\n")

# Get recipes for each dish
for dish in menu:
    recipes = dishes.get_recipes(dish)
    print(f"{dish} recipes:")
    for recipe in recipes:
        print(f"  - {recipe}")
    print()

# Test with an invalid dish
print("Testing with invalid dish:")
result = dishes.get_recipes("Burger")
print(f"Result: {result}")
