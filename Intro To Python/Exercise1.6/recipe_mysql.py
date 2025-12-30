import mysql.connector

#-------- Part 1: Connect to MySQL and set up database/table --------#
def connect_and_setup():
    # 1) Connect to MySQL server (not to a specific database yet)
    conn = mysql.connector.connect(
        host="localhost",
        user="cf-python",
        passwd="password"
    )
    cursor = conn.cursor()

    # 2) Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

    # 3) Use the database
    cursor.execute("USE task_database")

    # 4) Create Recipes table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Recipes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            ingredients VARCHAR(255),
            cooking_time INT,
            difficulty VARCHAR(20)
        )
    """)

    # 5) Save changes (CREATE/ALTER statements should be committed)
    conn.commit()

    return conn, cursor

# pass conn, cursor to each function to use the same connection

#------ Part 3: Creating a recipe ------#
def calculate_difficulty(cooking_time, ingredients):
    num_ingredients = len(ingredients)

    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"
    
def create_recipe(conn, cursor):
    print("\n--- Create a New Recipe ---")

    name = ""
    while not name:
        name = input("Recipe name: ").strip()
        if not name:
            print("Recipe name cannot be empty. Please try again.")

    while True:
        try:
            cooking_time = int(input("Cooking time (minutes): ").strip())
            if cooking_time < 0:
                print("Cooking time cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a whole number (e.g., 5, 10, 25).")

    raw_ingredients = input("Ingredients (comma-separated): ").strip()
    ingredients = [i.strip().lower() for i in raw_ingredients.split(",") if i.strip()]

    if not ingredients:
        print("No ingredients entered. Saving recipe with an empty ingredient list.")

    difficulty = calculate_difficulty(cooking_time, ingredients)

    # convert list -> comma-separated string for MySQL
    ingredients_str = ", ".join(ingredients)

    # 6) INSERT into Recipes table (parameterized query)
    query = """
        INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
        VALUES (%s, %s, %s, %s)
    """
    values = (name, ingredients_str, cooking_time, difficulty)

    cursor.execute(query, values)
    conn.commit()

    print("\n✅ Recipe saved to database!")

    # Optional: quick verification by fetching the last inserted row
    cursor.execute("""
        SELECT id, name, ingredients, cooking_time, difficulty
        FROM Recipes
        ORDER BY id DESC
        LIMIT 1
    """)
    print("Saved row:", cursor.fetchone())


#------ Part 4: Searching recipes by ingredient ------#
def search_recipe(conn, cursor):
    print("\n--- Search Recipes by Ingredient ---")

    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()  

    if not results:
        print("No recipes found yet. Add a recipe first.")
        return

    #  Build a unique ingredient list (no duplicates)
    all_ingredients = []
    seen = set()

    for (ingredients_str,) in results:
        if not ingredients_str:
            continue

        parts = [p.strip() for p in ingredients_str.split(",") if p.strip()]
        for ing in parts:
            ing_norm = ing.lower()
            if ing_norm not in seen:
                seen.add(ing_norm)
                all_ingredients.append(ing_norm)

    if not all_ingredients:
        print("No ingredients found in recipes yet.")
        return

    # Display numbered ingredients for user to choose
    print("\nAvailable ingredients:")
    for idx, ing in enumerate(sorted(all_ingredients), start=1):
        print(f"{idx}. {ing}")

    while True:
        try:
            choice = int(input("\nPick an ingredient number to search: ").strip())
            sorted_ings = sorted(all_ingredients)
            if choice < 1 or choice > len(sorted_ings):
                print("Please choose a valid number from the list.")
                continue
            search_ingredient = sorted_ings[choice - 1]
            break
        except ValueError:
            print("Please enter a whole number.")

    # Search recipes using LIKE with wildcards
    query = """
        SELECT id, name, ingredients, cooking_time, difficulty
        FROM Recipes
        WHERE LOWER(ingredients) LIKE %s
    """
    pattern = f"%{search_ingredient}%"
    cursor.execute(query, (pattern,))
    matches = cursor.fetchall()

    print(f"\nResults for ingredient: {search_ingredient}")
    if not matches:
        print("No matching recipes found.")
        return

    for row in matches:
        rid, name, ing_str, cook_time, diff = row
        print(f"\nID: {rid}")
        print(f"Name: {name}")
        print(f"Cooking time: {cook_time} min")
        print(f"Ingredients: {ing_str}")
        print(f"Difficulty: {diff}")

#----- Part 5: Updating an existing recipe -----#
def update_recipe(conn, cursor):
    print("\n--- Update a Recipe ---")

    cursor.execute("SELECT id, name, ingredients, cooking_time, difficulty FROM Recipes")
    recipes = cursor.fetchall()

    if not recipes:
        print("No recipes found. Add a recipe first.")
        return

    print("\nCurrent recipes:")
    for r in recipes:
        rid, name, ing, ct, diff = r
        print(f"{rid}: {name} | {ct} min | {diff} | {ing}")

    while True:
        try:
            recipe_id = int(input("\nEnter the ID of the recipe to update: ").strip())
            if not any(r[0] == recipe_id for r in recipes):
                print("That ID doesn't exist. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")

    print("\nWhat would you like to update?")
    print("1. name")
    print("2. cooking_time")
    print("3. ingredients")

    while True:
        choice = input("Choose 1, 2, or 3: ").strip()
        if choice in ("1", "2", "3"):
            break
        print("Invalid choice. Enter 1, 2, or 3.")

    if choice == "1":
        # Update name only
        new_name = ""
        while not new_name:
            new_name = input("Enter new name: ").strip()
            if not new_name:
                print("Name cannot be empty.")
        cursor.execute("UPDATE Recipes SET name=%s WHERE id=%s", (new_name, recipe_id))
        conn.commit()
        print("✅ Name updated.")
        return

    # For cooking_time or ingredients, we may need to recalc difficulty
    # Fetch current recipe values first
    cursor.execute("SELECT ingredients, cooking_time FROM Recipes WHERE id=%s", (recipe_id,))
    current_ing_str, current_ct = cursor.fetchone()

    if choice == "2":
        while True:
            try:
                new_ct = int(input("Enter new cooking time (minutes): ").strip())
                if new_ct < 0:
                    print("Cooking time cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a whole number.")

        # Recalculate difficulty using current ingredients
        ingredients_list = [i.strip() for i in (current_ing_str or "").split(",") if i.strip()]
        new_diff = calculate_difficulty(new_ct, ingredients_list)

        cursor.execute("UPDATE Recipes SET cooking_time=%s WHERE id=%s", (new_ct, recipe_id))
        cursor.execute("UPDATE Recipes SET difficulty=%s WHERE id=%s", (new_diff, recipe_id))
        conn.commit()
        print("✅ Cooking time (and difficulty) updated.")
        return

    if choice == "3":
        raw = input("Enter new ingredients (comma-separated): ").strip()
        new_ingredients = [i.strip().lower() for i in raw.split(",") if i.strip()]
        new_ing_str = ", ".join(new_ingredients)

        new_diff = calculate_difficulty(current_ct, new_ingredients)

        cursor.execute("UPDATE Recipes SET ingredients=%s WHERE id=%s", (new_ing_str, recipe_id))
        cursor.execute("UPDATE Recipes SET difficulty=%s WHERE id=%s", (new_diff, recipe_id))
        conn.commit()
        print("✅ Ingredients (and difficulty) updated.")
        return

#----- Part 6: Deleting a recipe -----#
def delete_recipe(conn, cursor):
    print("\n--- Delete a Recipe ---")

    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()

    if not recipes:
        print("No recipes found.")
        return

    print("\nRecipes:")
    for rid, name in recipes:
        print(f"{rid}: {name}")

    while True:
        try:
            recipe_id = int(input("\nEnter the ID of the recipe to delete: ").strip())
            if not any(r[0] == recipe_id for r in recipes):
                print("That ID doesn't exist. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")

    confirm = input("Type 'yes' to confirm deletion: ").strip().lower()
    if confirm != "yes":
        print("Deletion cancelled.")
        return

    cursor.execute("DELETE FROM Recipes WHERE id=%s", (recipe_id,))
    conn.commit()
    print("✅ Recipe deleted.")



#------- Part 2: Main Menu loop -------#
def main_menu(conn, cursor):
    choice = ""

    while choice != "quit":
        print("\nMain Menu")
        print("=" * 30)
        print("Pick a choice:")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("Type 'quit' to exit the program.")

        choice = input("Your choice: ").strip().lower()

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "quit":
            print("\nExiting program...")
        else:
            print("\nInvalid option. Please choose 1–4 or type 'quit'.")


#-------- Main Program Execution-------#


if __name__ == "__main__":
    conn, cursor = connect_and_setup()
    try:
        main_menu(conn, cursor)
    finally:
        # If user exits, commit changes and close connection
        conn.commit()
        cursor.close()
        conn.close()
        print("Database connection closed.")
