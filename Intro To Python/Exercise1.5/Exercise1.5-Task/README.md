# ✅ Exercise 1.5 — Object-Oriented Programming (Recipes)

## Overview

In this exercise, I refactored the recipe project using Object-Oriented Programming (OOP). Instead of working with standalone dictionaries and lists, I designed a `Recipe` class to model recipes as objects with attributes and behaviors. This exercise helped me understand how OOP improves structure, reusability, and scalability in Python programs.

---

## Key Concepts Practiced

- Object-oriented programming (classes and objects)
- Instance vs class variables
- Getter and setter methods
- Methods with variable-length arguments
- Encapsulation and data validation
- Lazy evaluation (recalculating values only when needed)
- Searching through objects using methods

---

## What I Built / Did

- Created a `Recipe` class with attributes for:
  - name
  - ingredients
  - cooking_time
  - difficulty (auto-calculated)
- Implemented methods to:
  - add and manage ingredients
  - calculate and retrieve difficulty
  - search for ingredients within a recipe
  - update a shared list of all ingredients across recipes
- Used normalization (lowercasing) to prevent duplicate ingredients
- Created multiple recipe objects (Tea, Coffee, Cake, Banana Smoothie)
- Printed formatted recipe details using `__str__`
- Searched for recipes by ingredient using a reusable search function

---

## Data Structures & Design Choices

- **Class (`Recipe`)**:  
  Used to group related data and behavior into a single, reusable structure that models real-world recipes.

- **Instance variables**:  
  Store data unique to each recipe (ingredients, cooking time, difficulty).

- **Class variable (`all_ingredients`)**:  
  Tracks all ingredients across every recipe object.

- **Lazy difficulty calculation**:  
  Difficulty is recalculated only when needed, improving efficiency and keeping data accurate.

---

## Files Included

- `recipe_oop.py`
- screenshots of script execution
- Learning journal update

---

## Reflection

This exercise helped solidify my understanding of OOP by showing how classes and objects can model real-world problems more cleanly than procedural code. I feel more confident using methods, managing shared vs instance data, and designing code that is easier to extend and maintain as projects grow.
