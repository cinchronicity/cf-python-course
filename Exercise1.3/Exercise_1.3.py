# Exercise 1.3 - Recipe Input + Difficulty
# step 1 - Open a Python script in an editor of your choice and name it “Exercise_1.3.py”.

# step 3 - Function to take recipe details from user
def take_recipe():
    # name should be a non-empty string
    while True:
        name = input("Enter recipe name: ").strip()
        if name:
            break
        else:
            print("Recipe name cannot be empty. Please enter a valid name.")

    # cooking_time should be an int
    while True:
        try:
            cooking_time = int(input("Enter cooking time in minutes: ").strip())
            if cooking_time < 0:
                print("Cooking time can't be negative. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a whole number (example: 5, 10, 25).")

    # ingredients: user enters comma-separated values in lowercase
    raw_ingredients = input("Enter ingredients (comma-separated): ").strip()
    ingredients = [ing.strip().lower() for ing in raw_ingredients.split(",") if ing.strip()]

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }
    return recipe


def get_difficulty(recipe):
    """Return the difficulty level for a recipe (no need to store it)."""
    cooking_time = recipe["cooking_time"]
    num_ingredients = len(recipe["ingredients"])

    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"


# ----- Main Program -----

# step 2 - Initialize two empty lists: recipes_list and ingredients_list.
recipes_list = []
ingredients_list = []

# step 4 - Get number of recipes user would like to enter
      #Loop until user enters valid whole number > 0 
while True:
    try:
        n = int(input("How many recipes would you like to enter? ").strip())
        if n <= 0:
            print("Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a whole number (example: 1, 2, 5).")

#step 5 - Run for loop n times to get recipes
for i in range(n):
    print(f"\n--- Recipe {i + 1} ---")
    recipe = take_recipe()

    # Add unique ingredients to ingredients_list only if not already present
    for ingredient in recipe["ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

    # Add recipe to recipes_list
    recipes_list.append(recipe)

# Display all recipes with difficulty
print("\n====================")
print("RECIPES ENTERED")
print("====================")
#Step 6 - Display all recipes with difficulty
for recipe in recipes_list:
    difficulty = get_difficulty(recipe)
    print(f"\nRecipe: {recipe['name']}")
    print(f"Cooking Time (min): {recipe['cooking_time']}")
    print(f"Ingredients: {recipe['ingredients']}")
    print(f"Difficulty: {difficulty}")

# Display all ingredients in alphabetical order
print("\n====================")
print("ALL INGREDIENTS (A–Z)")
print("====================")

for ingredient in sorted(ingredients_list):
    print(ingredient)
