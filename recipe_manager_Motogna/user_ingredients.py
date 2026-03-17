

# This file contains the function to get user input for ingredients
# and clean it for recipe searching.

def user_ingredients():

    print("\nGeben Sie die Zutate ein für die Rezeptsuche ein")
    print("(Trennen Sie die Zutaten mit einem Komma):")
    
    user_input = input("Ihre Zutaten: ").split(",")

    cleaned_ingredients = []


    for ingredient in user_input:

        keyword = ingredient.strip().split()[-1].lower()
        
        cleaned_ingredients.append(keyword)

    return cleaned_ingredients


        #-1 take the last word of the ingredient, which is often the main ingredient (e.g., "500g Mehl" -> "Mehl")
        #strip() removes leading and trailing whitespace from the ingredient, ensuring that the keyword is clean and standardized for searching recipes.
        #lower() converts the keyword to lowercase, making the search case-insensitive and more flexible when matching user ingredients with recipe ingredients.
        #keyword wird zur Liste der bereinigten Zutaten hinzugefügt, die für die Rezeptsuche
        #verwendet wird