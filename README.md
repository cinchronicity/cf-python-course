# cf-python-course

📘 CareerFoundry Python Course — Exercise Repository

This repository contains my solutions and notes for the CareerFoundry Python curriculum.
The course is organized into sections, with each exercise having its own folder and summary documenting what I completed and practiced.

## 📂 Course Structure

### 🐍 [Intro To Python](Intro%20To%20Python/) (Exercises 1.1–1.7)

### 🌐 [Web Development and Django](Web%20Development%20and%20Django/) (Coming Soon)

## 📋 Table of Contents — Introduction to Python

- [Exercise 1.1 — Python Environment Setup](Intro%20To%20Python/Exercise1.1/) — Environment setup with virtualenvwrapper
- [Exercise 1.2 — Data Types in Python](Intro%20To%20Python/Exercise1.2/) — Dictionaries and lists with recipes
- [Exercise 1.3 — Operators & Functions in Python](Intro%20To%20Python/Exercise1.3/) — User input, loops, and difficulty calculation
- [Exercise 1.4 — File Handling in Python](Intro%20To%20Python/Exercise1.4/) — Reading/writing files and recipe search
- [Exercise 1.5 — Object-Oriented Programming in Python](#Intro%20To%20Python/Exercise1.5/)
- [Exercise 1.6 — Databases in Python](#Intro%20To%20Python/Exercise1.6/)
- [Exercise 1.7 — Object Relational Mapping in Python](#Intro%20To%20Python/Exercise1.7/) -->

## Exercise 1.1 — Python Environment Setup

In this exercise, I installed Python using Homebrew, set up virtual environments with `virtualenvwrapper`, and practiced managing packages inside isolated environments. I installed useful tools like IPython, created a simple script (`add.py`), and learned how to export and reuse a requirements file. These steps established the workflow I will use throughout the course. Full details and screenshots are in the [Exercise 1.1](Intro%20To%20Python/Exercise1.1/) folder.

## Exercise 1.2 — Data Types in Python (Recipes)

In this exercise, I practiced building structured data using Python dictionaries and lists. I created five recipe objects, stored them inside an outer list, and printed the ingredients for each recipe inside an IPython shell. I also explained why dictionaries are a good fit for recipe data and why a list works well for managing multiple recipes. Screenshots and full notes are included in the [Exercise 1.2](Intro%20To%20Python/Exercise1.2/) folder.

## Exercise 1.3 — Operators and Functions in Python

In this exercise, I created a Python script (`Exercise_1.3.py`) that prompts the user to enter any number of recipes, stores them in a list of dictionaries, and collects a master list of unique ingredients. The program calculates each recipe’s difficulty level using conditional logic and prints the recipe details in an organized format. It also prints all ingredients alphabetically at the end. Full details and screenshots are in the [Exercise 1.3](Intro%20To%20Python/Exercise1.3/) folder.

## Exercise 1.4 — File Handling in Python

In this exercise, I expanded the recipe project by adding persistent file storage and search functionality. I created two Python scripts: one to collect and store recipes in a binary file using the `pickle` module, and another to load that data and allow users to search for recipes by ingredient. This exercise helped me understand how Python programs can save data across runs, handle file-related errors, and work with structured data across multiple scripts. Full details and screenshots are in the [Exercise 1.4](Intro%20To%20Python/Exercise1.4/) folder.

## Exercise 1.5 — Object-Oriented Programming in Python (Recipes)

In this exercise, I rebuilt the recipe application using object-oriented programming. I designed a `Recipe` class with attributes and methods to manage ingredients, calculate difficulty levels, and search recipes by ingredient. This exercise strengthened my understanding of classes, objects, instance vs class variables, and how OOP helps organize and scale Python programs more effectively. Full implementation details and screenshots are included in the [Exercise 1.5](Intro%20To%20Python/Exercise1.5/Exercise1.5-Task/) folder.

## Exercise 1.6 — Databases in Python 

In this exercise, I extended the recipe application by integrating a MySQL database to persist and manage recipe data. I built a menu-driven command-line program that connects Python to MySQL, creates the necessary database and table, and allows users to create, search, update, and delete recipes using SQL queries. Ingredients are stored in a normalized format to support reliable searching, and recipe difficulty is calculated dynamically based on cooking time and ingredient count. This exercise helped me understand how Python applications interact with relational databases, manage persistent data, and implement full CRUD functionality. Full details and screenshots are in the [Exercise 1.6](Intro%20To%20Python/Exercise1.6/) folder.

### Exercise 1.7 — Object Relational Mapping in Python
In this final exercise for Achievement 1, I rebuilt the recipe application using SQLAlchemy. Instead of writing raw SQL queries, I defined models, sessions, and ORM-based operations to interact with a MySQL database in a more scalable and maintainable way. Full details and screenshots are in the [Exercise 1.7](Intro%20To%20Python/Exercise1.7/) folder.
