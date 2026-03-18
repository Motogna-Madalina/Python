from data_all_recipes import all_recipes

def add_recipe():
    while True:
        
        print("\nNeues Rezept hinzufügen")

        #name of the recipe
        recipe_name = input("Name des Rezepts: ")
        #validate the recipe name 
        if recipe_name.strip() == "":
            print("Der Name darf nicht leer sein.")
            continue
        elif len(recipe_name) > 200:
            print("Der Name des Rezepts darf nicht länger als 200 Zeichen sein.")
            continue
        elif not recipe_name.replace(" ", "").isalpha():
            #replace (temporal) the spaces to check if the remaining characters are all letters
            print("Der Name des Rezepts darf nur Buchstaben enthalten (keine Zahlen oder Symbole).")
            continue
      
        #ingredients of the recipe
        ingredients = input("Zutaten (durch Komma getrennt): ").split(",")

        if len(ingredients) == 0:
            print("Bitte geben Sie mindestens eine Zutat ein.")
            continue
        for each in ingredients:
         if len(each.strip()) > 100:
            print("Die Zutaten dürfen nicht länger als 100 Zeichen sein.")
            continue
         elif not each.strip().isalnum():
            print("Die Zutaten dürfen nur Buchstaben und Zahlen enthalten.")
            continue
        
        #instructions of the recipe
        instructions = input("Anleitung: ")

        all_recipes[recipe_name] = {
            "zutaten": [ingredient.strip() for ingredient in ingredients],
            "anleitung": instructions
        }

        print(f"Rezept '{recipe_name}' wurde hinzugefügt!")