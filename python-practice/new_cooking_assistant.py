recipes = []
def main_menu():
    menu = """a: add a new receipe
              s: search recipe by name 
              i: search recipe by ingredients 
              q: quit"""
    print(menu)
    choice = input(" please Enter your choice from Main Menu: ")
    return choice
    

def add_recipe():
    d = dict()
    recipe_name = input (" Enter Recipe Name: ")
    d['recipe name'] = recipe_name
    recipe_ingredients = input (" Enter Recipe Ingredients: ")
    d['recipe ingredients'] = recipe_ingredients
    return d
    recipes = d.append()
    
    
for menu in main_menu():
    for choice in menu:
        if choice == "a":
            add_recipe()
            print("Recipe Added")
    

    