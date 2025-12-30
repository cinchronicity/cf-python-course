# Exercise 1.6 — Using MySQL with Python

## Overview
In this exercise, I extended my command-line recipe app by integrating it with a MySQL database. Instead of storing data in memory or files, recipes are now persisted in a relational database and managed using SQL queries executed through Python.

---

## Key Concepts Practiced
- Connecting Python to MySQL using `mysql-connector-python`
- Creating databases and tables programmatically
- Writing SQL queries (CREATE, INSERT, SELECT, UPDATE, DELETE)
- Using parameterized queries for safety
- Managing database connections and commits
- Normalizing data for reliable searching

---

## What I Built / Did
- Connected a Python script to a local MySQL server
- Created a `Recipes` table with appropriate columns and constraints
- Built a menu-driven CLI with four core actions:
  - Create recipes
  - Search recipes by ingredient
  - Update existing recipes
  - Delete recipes
- Stored ingredients as comma-separated strings and converted them as needed
- Calculated recipe difficulty based on cooking time and ingredient count
- Ensured database changes were committed and connections closed safely

---

## Database Design
**Table: Recipes**
- `id` — auto-incrementing primary key
- `name` — recipe name
- `ingredients` — comma-separated string
- `cooking_time` — integer (minutes)
- `difficulty` — Easy / Medium / Intermediate / Hard

---

## Files Included
- `recipe_mysql.py`
- Step-by-step execution screenshots
- Updated learning journal

---

## Reflection
This exercise helped me understand how Python applications interact with relational databases in real-world projects. I gained confidence writing SQL queries, handling user input safely, and building a complete CRUD workflow. Seeing how data persists beyond a single program run made the application feel much closer to production-ready software.
