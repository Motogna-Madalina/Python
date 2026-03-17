
from data_all_recipes import all_recipes
from user_ingredients import user_ingredients
from find_recipes import find_recipes

#this is the main file that runs the recipe manager app.
# It imports the necessary functions and data from other files and provides 
# a menu for the user to interact with the app.


def show_all_recipes():
    for recipe in all_recipes:
        
        print("\nRezept:", recipe)

        print("Zutaten:")
        for ingredient in all_recipes[recipe]["zutaten"]:
            print("-", ingredient)

        print("Anleitung:")
        print(all_recipes[recipe]["anleitung"])

def search_recipes():
    find_recipes(user_ingredients())

def menu_options():

    while True:
        print("\nRecipe Manager")
        print("A - Alle Rezepte anzeigen")
        print("B - Rezepte basierend auf verfügbaren Zutaten finden")
        print("C - Beenden")

        choice = input("Ihre Auswahl: ").upper()

        if choice == "A":
            show_all_recipes()
        elif choice == "B":
            search_recipes()
        elif choice == "C":
            print("Programm beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Auswahl.")
            break

menu_options()