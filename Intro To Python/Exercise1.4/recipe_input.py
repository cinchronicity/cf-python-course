import pickle


def calc_difficulty(cooking_time, ingredients):
    """Return difficulty based on cooking_time and number of ingredients."""
    num_ingredients = len(ingredients)

    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"


def take_recipe():
    """Take recipe input from user and return a recipe dictionary."""
    # Get recipe name and validate non-empty
    while True: 
        name = input("Enter recipe name: ").strip()
        if name:
            break
        else:
            print("Recipe name cannot be empty. Please enter a valid name.")
    # Get cooking time and validate as non-negative integer
    while True:
        try:
            cooking_time = int(input("Enter cooking time (minutes): ").strip())
            if cooking_time < 0:
                print("Cooking time can't be negative. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a whole number (e.g., 5, 10, 25).")
    #collect ingredients as comma-separated values in lowercase
    raw_ingredients = input("Enter ingredients (comma-separated): ").strip()
    ingredients = [ing.strip().lower() for ing in raw_ingredients.split(",") if ing.strip()]
    # Calculate difficulty
    difficulty = calc_difficulty(cooking_time, ingredients)

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty,
    }
    return recipe


# ---------------- Main Program ----------------

filename = input("Enter the filename to store your recipes (example: recipes.bin): ").strip()

# Try to load existing data
try:
    file = open(filename, "rb")
    data = pickle.load(file)
except FileNotFoundError:
    print("File not found. Creating a new recipe file.")
    data = {"recipes_list": [], "all_ingredients": []}
except Exception:
    print("Something went wrong while loading the file. Creating a new recipe file.")
    data = {"recipes_list": [], "all_ingredients": []}
else:
    file.close()
finally:
    recipes_list = data.get("recipes_list", [])
    all_ingredients = data.get("all_ingredients", [])

# Ask user how many recipes to enter
while True:
    try:
        n = int(input("How many recipes would you like to enter? ").strip())
        if n <= 0:
            print("Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a whole number (e.g., 1, 2, 5).")

# Collect recipes
for i in range(n):
    print(f"\n--- Recipe {i + 1} ---")
    recipe = take_recipe()
    recipes_list.append(recipe)

    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

# Update data dictionary
data["recipes_list"] = recipes_list
data["all_ingredients"] = all_ingredients

# Save to binary file
with open(filename, "wb") as file:
    pickle.dump(data, file)

print(f"\nSaved {n} recipe(s) to '{filename}'.")
