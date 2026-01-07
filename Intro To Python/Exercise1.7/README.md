# Exercise 1.7 — Object Relational Mapping in Python

## Overview

In this exercise, I rebuilt the recipe application using SQLAlchemy, Python’s Object Relational Mapper (ORM). Instead of interacting with MySQL using raw SQL queries, I defined database models as Python classes and used sessions to manage database operations.

This exercise helped me understand how ORMs abstract database logic while still allowing full control over persistent data.

---

## Key Concepts Practiced

- SQLAlchemy engine and session setup
- ORM models and declarative base
- Mapping Python classes to database tables
- CRUD operations using ORM queries
- Data validation and user input handling
- Transitioning from raw SQL to ORM-based workflows

---

## What I Built / Did

- Created a SQLAlchemy engine connected to a MySQL database
- Defined a `Recipe` model mapped to a database table
- Implemented methods for:
  - Creating recipes
  - Viewing all recipes
  - Searching recipes by ingredients
  - Editing existing recipes
  - Deleting recipes
- Designed a loop-based command-line menu to navigate all actions
- Ensured database sessions and connections close cleanly on exit
- Tested all features by creating, updating, searching, and deleting sample recipes

---

## Files Included

- `recipe_app.py`
- Terminal screenshots demonstrating:
  - Recipe creation
  - Searching by ingredient
  - Editing entries
  - Deleting entries
- Updated learning journal

---

## Reflection

This exercise tied together everything I learned in Achievement 1. Using SQLAlchemy made database interactions feel more natural and Pythonic compared to raw SQL. I now better understand how ORMs improve scalability, readability, and long-term maintainability in real-world applications.

Building a full CRUD application with an ORM gave me confidence that I can design data-driven applications that cleanly separate logic, data, and persistence.
