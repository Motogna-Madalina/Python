
from selection_menu_main import menu_options
from data_all_recipes import all_recipes


def user_ingredients():

    print("Geben Sie die Zutaten ein, die Sie zur Verfügung haben (durch Komma getrennt):")

    # save in a liste
    user_input = input("Ihre Zutaten: ").split(",")

    # make a new liste for save here later the cleaned ingredients
    cleaned_ingredients = []

    #we take the user input and clean it, we remove extra spaces and make it lowercase
    #strip() entfernt führende und nachfolgende Leerzeichen, lower() macht alles klein
    for ingredient in user_input:
        cleaned_ingredients.append(ingredient.strip().lower())

    return cleaned_ingredients

