## ✅ Exercise 1.3 — Operators and Functions in Python

## Overview

In this exercise, I built a complete Python script that allows users to enter recipes, calculates difficulty levels, and tracks ingredients across all recipes.

## Key Concepts Practiced

- User input validation  
- Loops and control flow  
- Functions  
- Dictionaries and lists  

## What I Built / Did

- Prompted the user to enter any number of recipes (`n`)
- Collects each recipe’s:
  - name (string)
  - cooking_time (integer)
  - ingredients (list of strings)
- Stored each recipe as a dictionary inside `recipes_list`  
- Collected all unique ingredients in `ingredients_list`  
- Calculated recipe difficulty based on cooking time and ingredient count (without storing it)
- Printed recipes in a structured format  
- Displayed all ingredients in alphabetical order  

## Logic Used

Difficulty was calculated using conditional logic:

- **Easy:** cooking_time < 10 and ingredients < 4  
- **Medium:** cooking_time < 10 and ingredients ≥ 4  
- **Intermediate:** cooking_time ≥ 10 and ingredients < 4  
- **Hard:** cooking_time ≥ 10 and ingredients ≥ 4  

The script calculates difficulty at print-time (no need to store it).


## Files Included

- `Exercise_1.3.py`  
- Step screenshots  
- Learning journal update  

## Reflection

This exercise made Python feel more practical by tying multiple concepts together into a single program. I gained confidence writing functions, validating input, and managing structured data through loops and conditionals.
