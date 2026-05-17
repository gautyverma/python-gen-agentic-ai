class Dishes:
    """A class to manage recipes for different dishes"""

    def __init__(self):
        self.menu = ["Pasta", "Pizza", "Salad"]

    def get_menu(self):
        """Returns the available dish categories"""
        return self.menu

    def get_recipes(self, dish_name):
        """Returns recipes for a given dish name"""
        match dish_name:
            case "Pasta":
                return ["Spaghetti Carbonara", "Penne Arrabiata", "Fettuccine Alfredo"]
            case "Pizza":
                return ["Margherita", "Pepperoni", "Veggie"]
            case "Salad":
                return ["Caesar Salad", "Greek Salad", "Garden Salad"]
            case _:
                return "Invalid Dish Name"
