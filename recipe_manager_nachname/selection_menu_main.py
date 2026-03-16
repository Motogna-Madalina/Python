# This is the main file for the recipe manager app. 
#It contains the menu options and calls the necessary 
#functions to display recipes or find recipes based on user ingredients.

from data_all_recipes import all_recipes
from find_ingredient import find_recipes
from user_write_ingredients import user_ingredients

def menu_options():

    print("Recipe Manager")
    print("A - Alle Rezepte anzeigen")
    print("B - Rezepte basierend auf verfügbaren Zutaten finden")

    choice = input("Ihre Auswahl: ").upper()

    if choice == "A":
 
        for recipe in all_recipes:

            print("\nRezept:", recipe)

            print("Zutaten:")
            for ingredient in all_recipes[recipe]["zutaten"]:
                print("-", ingredient)

            print("Anleitung:")
            print(all_recipes[recipe]["anleitung"])

    elif choice == "B":

        ingredients = user_ingredients()
        find_recipes(ingredients)

    else:
        print("Ungültige Auswahl.")


menu_options()