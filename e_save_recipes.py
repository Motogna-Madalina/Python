def save_recipes(all_recipes):
    import json
    with open('recipes.json', 'w', encoding='utf-8') as file:
        json.dump(all_recipes, file, ensure_ascii=False, indent=4)