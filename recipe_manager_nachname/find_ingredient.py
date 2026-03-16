from data_all_recipes import all_recipes

def find_recipes(user_ingredients):

    print("\nPassende Rezepte:")

    for recipe in all_recipes:

        recipe_ingredients = all_recipes[recipe]["zutaten"]

        recipe_clean = []

        for ingredient in recipe_ingredients:
            recipe_clean.append(ingredient.lower())

        if all(item in user_ingredients for item in recipe_clean):
            print("-", recipe)