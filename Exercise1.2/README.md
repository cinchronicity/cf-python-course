# Exercise 1.2 — Working With Python Data Structures (Recipes Project)

This exercise introduced me to building and organizing Python data using dictionaries and lists. The goal was to create several recipe structures inside an IPython shell, store them in an outer structure, and practice accessing specific values like ingredients to prepare for creating a Recipe App. Below is an overview of my approach and why I chose the data structures I used.

---

## 🥣 1. Creating `recipe_1` (Tea Recipe)

I created the first recipe using a dictionary, because dictionaries allow me to store related pieces of information using meaningful keys. This made the structure easy to understand and work with later.

```python
recipe_1 = {
    "name": "Tea",
    "cooking_time": 5,
    "ingredients": ["Tea leaves", "Sugar", "Water"]
}
```


## 💡 Why I Chose a Dictionary for Each Recipe

I chose dictionaries to represent each recipe because they allow me to store structured, named pieces of data together in a clear and intuitive way. Each recipe naturally contains labeled attributes—like a name, cooking time, and a list of ingredients—and dictionaries map perfectly to that idea. They make it easy to access specific information later, such as retrieving only the ingredients or sorting recipes by cooking time.


## 🧺 2. Creating the Outer Structure: all_recipes

I stored all recipe dictionaries inside a list. A list is ideal because this project requires a sequential structure that can grow as new recipes are added. Lists preserve order, allow iteration, and make it easy to loop through all recipes—especially useful when printing all ingredient lists.

```python 
  all_recipes = []
```

## 🌮 3. Creating Additional Recipes (recipe_2 to recipe_5)

I created four additional mock recipes using the same structure as recipe_1:
```
recipe_2 = {
    "name": "Scrambled Eggs",
    "cooking_time": 7,
    "ingredients": ["Eggs", "Butter", "Salt", "Pepper"]
}
```
then added them to the outer list I created earlier 

```
  all_recipes.append(recipe_1)...
  all_recipes.append(recipe_5)
```

## 🧾 4. Printing Ingredients for Each Recipe

I used a simple loop to print the ingredients of each recipe:
```
for recipe in all_recipes:
    print(recipe["ingredients"])
```

## 🧠 Reflection

This exercise helped reinforce how Python’s core data structures work together. Dictionaries make it easy to group related data, while lists make it simple to scale and organize collections of objects. By building and printing recipe structures, I practiced accessing nested values and have a better understanding of how Python stores and manipulates structured data.