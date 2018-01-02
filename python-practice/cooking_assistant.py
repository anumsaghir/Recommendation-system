import pprint
#a = ["a: add a new receipe"]
#s = ["s: search recipe by name"]
#i = ["i: search recipe by ingredients"]
#q = ["q: quit"]

main_menu = ["a: add a new receipe",
             "s: search recipe by name" ,
             "i: search recipe by ingredients" ,
             "q: quit"]
print(main_menu)
choice = input("please Enter you choice from Main Menu: ")
found_main_menu_choice == False
for choice in main_menu:
    if choice == "a":
        found_main_menu_choice == True
        Add_Recipe()
        print("Recipe Added")
    elif choice == "s":
        found_main_menu_choice == True
        #print("Search_Recipe_Name")
        search_name_recipe()
    elif choice == "i":
        found_main_menu_choice == True
        #print("Search Ingredient")
        search_ingredient_recipe()
    elif choice == "q":
        found_main_menu_choice == True
        print("Good bye and happy cooking :-)")
else:
        found_main_menu_choice == False    
             
    
def Add_Recipe():
    for Recipe in Add_Recipe:
        recipe = input("Enter Recipe")
        Add_Recipe.append()
        Add_Recipe ['Boiled egg']= {'Recipe Name': 'Boiled eggs',
                            'Ingredient': 'Eggs',
                            'Ingredient': 'Water'}
                            #'Ingredient' : ''}
        Add_Recipe ['Fried egg']= {'Recipe Name': 'Fried eggs',
                           'Ingredient': 'oil',
                           'Ingredient': 'eggs'}
                           #'Ingredient' : 'saults'}

    pprint.pprint(Add_Recipe)
    

def search_ingredient_recipe():
    for ingredients in Add_Recipe.items():
        Recipe_ingredients = input( " enter ingredients:  ")
        if Recipe_ingredients == Add_Recipe.items:
            print(Add_Recipe.items)
    else:
        print("Sorry the recipe was not found!")

def Search_Recipe_Name():
    for name in Add_Recipe.items():
        Recipe_name = input( " Recipe Name:  ")
        if Recipe_name == Add_Recipe.items:
            print(Add_Recipe.items)
    else:
        print("Sorry the recipe was not found!")



