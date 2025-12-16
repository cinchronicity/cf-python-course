# Exercise 1.3 — Recipes, Loops, and Difficulty Levels

In this exercise, I built a Python script (`Exercise_1.3.py`) that lets a user enter any number of recipes, stores them for later use, tracks all unique ingredients across recipes, and prints each recipe with a calculated difficulty level. This helped me practice user input, lists, dictionaries, loops, and control flow in a complete program.

---

## ✅ What This Script Does

- Asks the user how many recipes they want to enter (`n`)
- Collects each recipe’s:
  - name (string)
  - cooking_time (integer)
  - ingredients (list of strings)
- Stores each recipe as a dictionary and appends it to `recipes_list`
- Builds a master list of unique ingredients in `ingredients_list`
- Calculates a difficulty level for each recipe (without storing it)
- Prints:
  - each recipe in a clean format
  - the full ingredient list in alphabetical order

---

## 🧱 Data Structures Used (and why)

- **Dictionary (for each recipe):**  
  I used a dictionary because each recipe has labeled attributes (`name`, `cooking_time`, `ingredients`). This makes the data easy to access later using keys like `recipe["ingredients"]`.

- **List (for all recipes):**  
  I used a list for `recipes_list` because it’s sequential and easy to loop through. It also makes it simple to add as many recipes as the user enters.

- **List (for unique ingredients):**  
  I used `ingredients_list` to keep track of every ingredient found across all recipes. I check for duplicates before adding, so each ingredient appears only once.

---

## 🧠 Difficulty Logic

Difficulty is calculated using cooking time and ingredient count:

- **Easy:** cooking_time < 10 AND ingredients < 4  
- **Medium:** cooking_time < 10 AND ingredients ≥ 4  
- **Intermediate:** cooking_time ≥ 10 AND ingredients < 4  
- **Hard:** cooking_time ≥ 10 AND ingredients ≥ 4  

The script calculates difficulty at print-time (no need to store it).

---

## 📄 Files Included

- `Exercise_1.3.py`
- `Step-1...png` (Step screenshots)
- Learning journal update 

---

## 🧠 Reflection

This exercise made Python feel more “real” because I wasn’t just practicing isolated concepts—I built a full script with a clear flow. I feel more confident using nested loops, validating user input, and storing structured data in dictionaries and lists.
