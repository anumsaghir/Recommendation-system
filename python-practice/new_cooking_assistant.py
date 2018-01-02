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
    recipes = d.append()  # Beta return k baad wala code to chalta hn nahi hay, function ki execution return pay khatam ho jati hay
    # so ye jo oper wali line hay ye to chalni hi nah hay. pluse recipes to global variable hay ap usay function k andar modify nahi
    # kar sakteen aisay. Additionally, d to dict hay aur append ka method to lists ka hota hay dicts ka nahi.
    # Aik line aur 3 mistakes :-/
    
    
for menu in main_menu():  # ye main_menu ka function to sirf aik single value return karta hay, loop to lists par lagaya jata hay
    for choice in menu:   # ye loop is liye chal raha hay k oper menu main bhi sirf aik hi character aya ho ga, is ki zaroorat nahi thi
        if choice == "a":
            add_recipe()  # add_recpie ka function kia koi value return nahi karta? dict return karta hay na? to woh ap nay kaheen store karai?
            print("Recipe Added")
    

# correct implementation
user_choice = main_menu()  # just main menu k function ko call kia aur return value store karwa li user_choice main

if user_choice == "a":    # compare kar lia k kia choice a hay
    new_recipe_dict = add_recipe()   # add_recipe ka function call kia aur jo dict us nay return ki woh new_recipe_dict k variable main store kara li
    recipes.append(new_recipe_dict)  # aur us dict ko jo humari recipes ki list hay us main append kara lia, aisay append karna tha, apko append ka syntax bhool gaya hay :-) jahan koi cheez clear na ho to dobara book ka woh section consult kar lia karain

print(recipes)


