import json
import os


def load_json_file():
    with open('recipes.json', 'r', encoding='utf-8') as file:
        all_recipes = json.load(file)
        return all_recipes
    

    