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


def search_recipe_name():
    search_by_name = input ("Enter Recipe name: ")
    for rd in recipes:
        if rd['recipe name'] == search_by_name:
            print("Name: " + rd["recipe name"])
            print("Ingredients: " + rd["recipe ingredients"])
        else:
            print("Recipe not Found")
                  
            
def search_by_ingredients():
    search_by_ingredients = input ("Enter Recipe ingredients: ")
    for rd in recipes:
        if rd['recipe ingredients'] == search_by_ingredients:
            print("Name: " + rd["recipe name"])
            print("Ingredients: " + rd["recipe ingredients"])
        else:
            print("Recipe not Found")
        
    
user_choice = main_menu()  
while user_choice != 'q':
    if user_choice == "a":    
        new_recipe_dict = add_recipe()   
        recipes.append(new_recipe_dict)   
        print("recipe added")
    
    elif user_choice == "s":
        search_recipe_name()
    
    elif user_choice == "i":
        search_by_ingredients()
        
    elif user_choice == "q":
        print("Good bye and happy cooking :-) ")
    
    else:
        print("wrong choice")
        
    user_choice = main_menu()


