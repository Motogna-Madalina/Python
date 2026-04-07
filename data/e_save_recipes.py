from models.data_all_recipes import all_recipes
import json

#this file contains the function to save the recipes in a json file,
#  so that we can load them again when we start the app.
#  We use the json module to do this, and we use the all_recipes dictionary 
# as a parameter, so that we can save it in the json file. 
# We also use the ensure_ascii=False parameter to make sure that the special characters are saved correctly, and we use the indent=4 parameter to make the json file more readable.

def save_recipes(all_recipes):
    
    with open('data/recipes.json', 'w', encoding='utf-8') as file:
        json.dump(all_recipes, file, ensure_ascii=False, indent=4)

#data/recipes.json is the file where we save the recipes, and we use the 'w' mode to write to the file.
#We also use the encoding='utf-8' parameter to make sure that the special characters are saved correctly.
#json.dump() is the function that saves the dictionary in the json file
#and we use the ensure_ascii=False parameter to make sure that the special characters are saved correctly
#and we use the indent=4 parameter to make the json file more readable.
