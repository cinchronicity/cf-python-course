## ✅ Exercise 1.4 — File Handling in Python

## Overview

In this exercise, I expanded the recipe project by adding file storage and search functionality. I created two Python scripts: one to collect and store recipes in a binary file, and another to load that data and allow users to search for recipes by ingredient. This exercise introduced persistent data storage and working across multiple scripts.

## Key Concepts Practiced

- Reading from and writing to binary files
- Using the `pickle` module for data serialization
- Separating functionality across multiple Python scripts
- Error handling with try–except–else–finally blocks
- Searching data structures using user input

## What I Built / Did

- Created `recipe_input.py` to:
  - Collect recipes from user input
  - Calculate and store recipe difficulty
  - Track all unique ingredients across recipes
  - Save recipes and ingredients to a binary file using `pickle`
- Implemented logic to load existing data so new recipes can be appended instead of overwritten
- Created `recipe_search.py` to:
  - Load stored recipe data from the binary file
  - Display all available ingredients
  - Allow the user to select an ingredient by number
  - Display all recipes that contain the selected ingredient
- Ran both scripts multiple times to verify data persistence and search functionality

## Data Structures Used (and Why)

- **Dictionary (for each recipe):**  
  Each recipe is stored as a dictionary containing its name, cooking time, ingredients, and difficulty. This keeps related data grouped together and easy to access.

- **List (for recipes_list):**  
  A list allows recipes to be stored sequentially and iterated over when displaying or searching.

- **List (for all_ingredients):**  
  A separate list tracks all unique ingredients across recipes, making it easy to present searchable options to the user.

- **Dictionary (for stored data):**  
  Both lists are stored together in a single dictionary before being written to the binary file, allowing them to be loaded and reused later.

## Files Included

- `recipe_input.py`
- `recipe_search.py`
- `recipes.bin` (binary data file)
- Step screenshots
- Updated learning journal

## Reflection

This exercise helped me understand how Python programs can persist data beyond a single run. Working with binary files and separating functionality across scripts made the project feel more like a real application. I also gained confidence using error handling and designing programs that can be extended over time.
