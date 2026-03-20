from load_data import load_json_file
from c_add_recipe import add_recipe
from b_user_ingredients import user_ingredients, find_recipes
from d_erase_recipe import erase_recipe
from e_save_recipes import save_recipes
from a_show_recipes import * 
from edit_recipe import edit_recipe



#this is the main file that runs the recipe manager app.
# It imports the necessary functions and data from other files and provides 
# a menu for the user to interact with the app.
#def menu_options():
while True:
        print("\nRecipe Manager")
        print("A - Alle Rezepte anzeigen")
        print("B - Rezepte basierend auf verfügbaren Zutaten finden")
        print("C - Neues Rezept hinzufügen")
        print("D - Rezepte löschen")
        print("E - Rezepte speichern")
        print("F - Rezepte laden")
        print("G - Rezepte bearbeiten")
        print("H - Programm beenden")

        choice = input("Ihre Auswahl: ").upper()

        if choice == "A":
            show_all_recipes(all_recipes)

        elif choice == "B":
            find_recipes()
    
        elif choice == "C":
            add_recipe()

        elif choice == "D":
            erase_recipe()
            
        elif choice == "E":
             save_recipes()
             print("Rezepte gespeichert!")

    #    elif choice == "F":
    #        load_recipes()
    #        print("Rezepte geladen!")

    #    elif choice == "G":
    #        edit_recipe()

    #    elif choice == "H":
    #        print("Programm beendet. Auf Wiedersehen!")
    #        break

     #   else:
     #       print("Ungültige Auswahl.")


