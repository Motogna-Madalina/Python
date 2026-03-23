from data_all_recipes import all_recipes
import json

def save_recipes(all_recipes):
    
    with open('recipes.json', 'w', encoding='utf-8') as file:
        json.dump(all_recipes, file, ensure_ascii=False, indent=4)