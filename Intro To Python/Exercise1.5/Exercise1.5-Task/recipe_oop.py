class Recipe:
    # class variable that tracks all ingredients across recipes
    all_ingredients = []

    def __init__(self, name):

        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    # getters/setters for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # getters/setters for cooking_time
    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        if cooking_time < 0:
            print("Cooking time cannot be negative.")
        else:
            self.cooking_time = cooking_time
            self.difficulty = None  # difficulty depends on cooking_time, so mark it stale

    # getter for ingredients
    def get_ingredients(self):
        return self.ingredients

    # method to add ingredients
    def add_ingredients(self, *ingredients):
        for ingredient in ingredients:
            normalized = ingredient.strip().lower()
            if normalized and normalized not in self.ingredients:
                self.ingredients.append(normalized)
        self.difficulty = None # invalidate cached difficulty to recalculate when needed
        self.update_all_ingredients()

    def update_all_ingredients(self):
        for (ingredient ) in self.ingredients:  # <-- this recipe’s data (instance variable)
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)  #  <-- shared data (class variable)

    def search_ingredient(self, ingredient):
        return ingredient.lower() in self.ingredients

    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    def calculate_difficulty(self):
        num_ingredients = len(self.ingredients)

        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and num_ingredients >= 4:
            self.difficulty = "Hard"
        # or else self.difficulty = "Hard" meaning if its not any of the above cases, then it must be "Hard"

    def __str__(self):
        # format ingredients in title case for display
        ingredients_str = ", ".join(ingredient.title() for ingredient in self.ingredients)
        return (
            f"Recipe: {self.name}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Ingredients: {ingredients_str}\n"
            f"Difficulty: {self.get_difficulty()}"
        )


# method OUTSIDE the class to search ANY recipe by ingredient
# Using 'data' parameter makes this function reusable with any recipe list
def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)
            print()  


# ---------------- Main Program ----------------

if __name__ == "__main__":
    tea = Recipe("Tea")
    tea.add_ingredients("Tea Leaves", "Sugar", "Water")
    tea.set_cooking_time(5)
    print(tea)
    print()

    coffee = Recipe("Coffee")
    coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
    coffee.set_cooking_time(5)
    print(coffee)
    print()

    cake = Recipe("Cake")
    cake.add_ingredients(
        "Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"
    )
    cake.set_cooking_time(50)
    print(cake)
    print()

    banana_smoothie = Recipe("Banana Smoothie")
    banana_smoothie.add_ingredients(
        "Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"
    )
    banana_smoothie.set_cooking_time(5)
    print(banana_smoothie)
    print()

    recipes_list = [tea, coffee, cake, banana_smoothie]

    print("=== Recipes that contain Water ===")
    print()
    recipe_search(recipes_list, "Water")

    print("=== Recipes that contain Sugar ===")
    print()
    recipe_search(recipes_list, "Sugar")
    print()

    print("=== Recipes that contain Bananas ===")
    print()
    recipe_search(recipes_list, "Bananas")
