import pickle


def display_recipe(recipe):
    """Print one recipe's details."""
    print("\n--------------------")
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} min")
    print("Ingredients:")
    for ing in recipe["ingredients"]:
        print(f"- {ing}")
    print(f"Difficulty: {recipe['difficulty']}")
    print("--------------------")


def search_ingredient(data):
    """Show ingredients, let user pick one by number, then print matching recipes."""
    all_ingredients = data.get("all_ingredients", [])
    recipes_list = data.get("recipes_list", [])

    if not all_ingredients:
        print("No ingredients found in the file.")
        return

    print("\nAvailable Ingredients:")
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index}: {ingredient}")

    try:
        choice = int(input("\nEnter the number of the ingredient you want to search for: ").strip())
        ingredient_searched = all_ingredients[choice]
    except (ValueError, IndexError):
        print("Invalid selection. Please enter a valid number from the list.")
    else:
        print(f"\nRecipes containing '{ingredient_searched}':")

        found_any = False
        for recipe in recipes_list:
            if ingredient_searched in recipe["ingredients"]:
                display_recipe(recipe)
                found_any = True

        if not found_any:
            print("No recipes found with that ingredient.")


# ---------------- Main Program ----------------

filename = input("Enter the filename containing recipe data (example: recipes.bin): ").strip()

try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("File not found. Please run recipe_input.py first to create it.")
else:
    search_ingredient(data)
