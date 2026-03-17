from data_all_recipes import all_recipes

def find_recipes(user_ingredients):

    print("\nPassende Rezepte:")

    found = False

    for recipe in all_recipes:

        for ingredient in all_recipes[recipe]["zutaten"]:

            last_word = ingredient.split()[-1].lower()

            if last_word in user_ingredients:
                print("-", recipe)
                found = True
                break

    if found == False:
        print("Keine passenden Rezepte gefunden.")