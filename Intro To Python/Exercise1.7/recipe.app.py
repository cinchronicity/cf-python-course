from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import and_ #import and_ for future use in queries

#used venv cf-python-base for this exercise, make sure to be in correct folder when running

# -----------------------------
# Part 1: SQLAlchemy Setup
# -----------------------------

# 1) Update these if needed
USERNAME = "cf-python"
PASSWORD = "password"
HOST = "localhost"
DBNAME = "task_database"

#global scope variables for DB connection
# 2) Engine: connects SQLAlchemy to your MySQL database
engine = create_engine(
    f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DBNAME}",
    echo=False
)

# 3) Session: lets you talk to the DB (add, update, delete, query)
Session = sessionmaker(bind=engine)
session = Session()

# -----------------------------
# Part 2: Model + Table
# -----------------------------

#store declarative base class
Base = declarative_base()

class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        # quick dev-friendly representation
        return f"<Recipe id={self.id} name='{self.name}' difficulty='{self.difficulty}'>"

    def __str__(self):
        # nicer user-friendly representation
        ingredients_list = self.return_ingredients_as_list()
        ingredients_pretty = ", ".join(ingredients_list) if ingredients_list else "None"
        #/n= new line, \t= tab space
        return (
            "\n" + "=" * 30 +
            f"\nRecipe ID:\t{self.id}"
            f"\nName:\t\t{self.name}"
            f"\nCooking Time:\t{self.cooking_time} min"
            f"\nDifficulty:\t{self.difficulty}"
            f"\nIngredients:\t{ingredients_pretty}"
            "\n" + "=" * 30
        )

    def calculate_difficulty(self):
        # assigns difficulty to self.difficulty (doesn't return it)
        num_ingredients = len(self.return_ingredients_as_list())

        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        # split by ", " and return as list
        return self.ingredients.split(", ")

# Create table in DB if it doesn't exist
Base.metadata.create_all(engine)

print("✅ SQLAlchemy connected. Table 'final_recipes' is ready.")


# ------------------------------------
# Part 3: Main Operations as functions
# ------------------------------------

def create_recipe(session):
    print("\n--- Create Recipe ---")

    # name validation: non-empty, <= 50 chars
    while True:
        name = input("Recipe name (max 50 chars): ").strip()
        if not name:
            print("Name can't be empty.")
            continue
        if len(name) > 50:
            print("Name is too long. Keep it 50 characters or less.")
            continue
        break

    # cooking_time validation: numeric only, int, >= 0
    while True:
        ct_raw = input("Cooking time in minutes (number): ").strip()
        if not ct_raw.isnumeric():
            print("Please enter numbers only (example: 5, 10, 25).")
            continue
        cooking_time = int(ct_raw)
        break

    # ingredients: user chooses how many, loop to collect
    ingredients = []
    while True:
        n_raw = input("How many ingredients would you like to enter? ").strip()
        if not n_raw.isnumeric():
            print("Please enter a whole number.")
            continue
        n = int(n_raw)
        if n <= 0:
            print("Enter a number greater than 0.")
            continue
        break

    for i in range(n):
        while True:
            ing = input(f"Ingredient #{i+1}: ").strip()
            if not ing:
                print("Ingredient can't be empty.")
                continue
            # normalize (helps searching + duplicates)
            ing_norm = ing.lower()
            if ing_norm in ingredients:
                print("You already added that ingredient. Try a different one.")
                continue
            ingredients.append(ing_norm)
            break

    ingredients_str = ", ".join(ingredients)

    recipe_entry = Recipe(
        name=name,
        ingredients=ingredients_str,
        cooking_time=cooking_time,
        difficulty="",
    )
    recipe_entry.calculate_difficulty()

    session.add(recipe_entry)
    session.commit()

    print("\n✅ Saved:")
    print(recipe_entry)


def view_all_recipes(session):
    print("\n--- View All Recipes ---")

    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes in the database yet.")
        return None

    for recipe in recipes:
        print(recipe)


def search_by_ingredients(session):
    print("\n--- Search Recipes by Ingredients ---")

    if session.query(Recipe).count() == 0:
        print("No recipes in the database yet.")
        return None

    # get only the ingredients column
    results = session.query(Recipe.ingredients).all()  # list of tuples: [('milk, sugar',), ...]

    all_ingredients = []
    seen = set()

    for (ingredients_str,) in results:
        if not ingredients_str:
            continue
        parts = [p.strip().lower() for p in ingredients_str.split(",") if p.strip()]
        for ing in parts:
            if ing not in seen:
                seen.add(ing)
                all_ingredients.append(ing)

    if not all_ingredients:
        print("No ingredients found in the database.")
        return None

    # display numbered ingredient list
    all_ingredients_sorted = sorted(all_ingredients)
    print("\nAvailable ingredients:")
    for idx, ing in enumerate(all_ingredients_sorted, start=1):
        print(f"{idx}. {ing}")

    print("\nType numbers separated by spaces (example: 1 4 7)")
    choices_raw = input("Which ingredients do you want to search by? ").strip()
    if not choices_raw:
        print("No selection made. Returning to menu.")
        return None

    # validate choices: must be numbers in range
    tokens = choices_raw.split()
    if not all(t.isnumeric() for t in tokens):
        print("Invalid input. Use numbers only.")
        return None

    choices = [int(t) for t in tokens]
    if any(c < 1 or c > len(all_ingredients_sorted) for c in choices):
        print("One or more numbers are out of range.")
        return None

    # map numbers -> ingredient strings
    # use set to avoid duplicates
    search_ingredients = list({all_ingredients_sorted[c - 1] for c in choices})

    # build LIKE conditions list
    conditions = []
    for ing in search_ingredients:
        like_term = f"%{ing}%"
        conditions.append(Recipe.ingredients.like(like_term))

    # filter with AND across all selected ingredients
    matches = session.query(Recipe).filter(and_(*conditions)).all()

    print("\nResults:")
    if not matches:
        print("No recipes matched those ingredients.")
        return None

    for recipe in matches:
        print(recipe)


def edit_recipe(session):
    print("\n--- Edit Recipe ---")

    if session.query(Recipe).count() == 0:
        print("No recipes in the database yet.")
        return None

    # show id + name
    results = session.query(Recipe.id, Recipe.name).all()
    print("\nRecipes:")
    for rid, name in results:
        print(f"{rid}: {name}")

    # pick id
    rid_raw = input("\nEnter the recipe ID to edit: ").strip()
    if not rid_raw.isnumeric():
        print("Invalid ID.")
        return None
    rid = int(rid_raw)

    recipe_to_edit = session.query(Recipe).filter(Recipe.id == rid).first()
    if not recipe_to_edit:
        print("That ID doesn't exist.")
        return None

    # show editable fields
    print("\nSelected recipe:")
    print(f"1. Name: {recipe_to_edit.name}")
    print(f"2. Ingredients: {recipe_to_edit.ingredients}")
    print(f"3. Cooking time: {recipe_to_edit.cooking_time}")

    choice = input("Which field do you want to edit? (1/2/3): ").strip()
    if choice not in ("1", "2", "3"):
        print("Invalid choice.")
        return None

    if choice == "1":
        new_name = input("Enter new name (max 50 chars): ").strip()
        if not new_name or len(new_name) > 50:
            print("Invalid name.")
            return None
        recipe_to_edit.name = new_name

    elif choice == "2":
        print("Enter ingredients as comma-separated (example: milk, sugar, eggs)")
        raw = input("New ingredients: ").strip()
        new_ings = [i.strip().lower() for i in raw.split(",") if i.strip()]
        if not new_ings:
            print("Invalid ingredients.")
            return None
        # remove duplicates while preserving order
        deduped = []
        seen = set()
        for ing in new_ings:
            if ing not in seen:
                seen.add(ing)
                deduped.append(ing)
        recipe_to_edit.ingredients = ", ".join(deduped)

    else:  # choice == "3"
        ct_raw = input("Enter new cooking time (number): ").strip()
        if not ct_raw.isnumeric():
            print("Invalid cooking time.")
            return None
        recipe_to_edit.cooking_time = int(ct_raw)

    # difficulty recalculated after any edit
    recipe_to_edit.calculate_difficulty()
    session.commit()

    print("\n✅ Updated:")
    print(recipe_to_edit)


def delete_recipe(session):
    print("\n--- Delete Recipe ---")

    if session.query(Recipe).count() == 0:
        print("No recipes in the database yet.")
        return None

    results = session.query(Recipe.id, Recipe.name).all()
    print("\nRecipes:")
    for rid, name in results:
        print(f"{rid}: {name}")

    rid_raw = input("\nEnter the recipe ID to delete: ").strip()
    if not rid_raw.isnumeric():
        print("Invalid ID.")
        return None
    rid = int(rid_raw)

    recipe_to_delete = session.query(Recipe).filter(Recipe.id == rid).first()
    if not recipe_to_delete:
        print("That ID doesn't exist.")
        return None

    confirm = input(f"Are you sure you want to delete '{recipe_to_delete.name}'? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Deletion cancelled.")
        return None

    session.delete(recipe_to_delete)
    session.commit()
    print("✅ Recipe deleted.")

# ------------------------------------
# Part 4: Main Menu
# ------------------------------------

def main_menu(session):
    choice = ""

    while choice != "quit":
        print("\nMain Menu")
        print("=" * 30)
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to quit the application.")

        choice = input("Your choice: ").strip().lower()

        if choice == "1":
            create_recipe(session)
        elif choice == "2":
            view_all_recipes(session)
        elif choice == "3":
            search_by_ingredients(session)
        elif choice == "4":
            edit_recipe(session)
        elif choice == "5":
            delete_recipe(session)
        elif choice == "quit":
            print("Goodbye! Closing connections...")
        else:
            print("Invalid option. Please choose 1–5 or type 'quit'.")


if __name__ == "__main__":
    try:
        main_menu(session)
    finally:
        session.close()
        engine.dispose()
        print("Session and engine closed.")

