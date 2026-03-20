from data_all_recipes import all_recipes
from b_user_ingredients import user_ingredients, find_recipes

def show_all_recipes(all_recipes):
    for recipe, details in all_recipes.items():
        
        print("\nRezept:", recipe)

        print("Zutaten:")
        for ingredient in details["zutaten"]:
            print("-", ingredient)

        print("Anleitung:")
        print(details["anleitung"])

