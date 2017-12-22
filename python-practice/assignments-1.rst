Assignment 1 - The number cruncher
==================================

Create a program that takes a number from command line as a command line argument (using sys.argv) and then prints whether the number 
is odd or even. Additionally the program should also print if the number is prime.

Example runs::

    $ python3 num_info.py 4
    number 4 is even
    
    $ python3 num_info.py 7
    number 7 is odd
    number 7 is also a prime number

Note: $ means the command line prompt, you should not type $ too.


Assignment 2 - The birthday calendar
====================================

Create a program that has a predefined list of dates (datetime.date objects) stored with names of people that have birthdays on that
date. Then check to see if today (datetime.date.today()) matches the month and day with any of the dates in the above list (year has to be different as a person has to be at least an year old to have a brithday). If a matching item is found, display the names of people who
have birthdays today.

The birthdays could be stored as a dict like::

    from datetime import date
    
    birthdays = {
        date(year=1980, month=12, day=12): ['Picolo', 'Goku'],
        date(year=19950, month=10, day=1): ['Rob Stark', ]
    }

Example runs::

    $ python3 birthday_calendar.py
    Sorry no birthdays today

    $ python3 birthday_calendar.py
    !!! Happy Birthday Picolo !!!
    !!! Happy Birthday Goku !!!

**Tip:** Date objects have year, month and day properties allowing access to seperate parts of the date


Assignment 3 - Cooking Assistant
================================

Create a program that performs 2 actions.

1. It allows adding cooking recipies
2. It allows searching recipies by name or by ingredients

If searching by ingredients, multiple ingredients can be specified separating them using commas. Only recipes that match all 
ingredients should be returned

Example runs::

    $ python3 cooking_assistant.py
    
    ============ Cooking Assistant - Main Menu =================
    (a) add a new recipe
    (s) search recipe by name
    (i) search recipe by ingredients
    (q) quit

    Your choice: a
    
    ------------- Add Recipe -------------
    
    Recipe name: Boiled eggs
    ingredients are entered one per line, press enter without typing an ingredient name to finish entering ingredients list.
    ingredient: Eggs
    ingredient: Water
    ingredient:
    
    Recipe added!
    
    ============ Cooking Assistant - Main Menu =================
    (a) add a new recipe
    (s) search recipe by name
    (i) search recipe by ingredients
    (q) quit

    Your choice: a
    
    ------------- Add Recipe -------------
    
    Recipe name: Fried eggs
    ingredients are entered one per line, press enter without typing an ingredient name to finish entering ingredients list.
    ingredient: Eggs
    ingredient: Oil
    ingredient:
    
    Recipe added!
    
    ============ Cooking Assistant - Main Menu =================
    (a) add a new recipe
    (s) search recipe by name
    (i) search recipe by ingredients
    (q) quit
    
    Your choice: s
    Enter recipe name: Fried eggs
    
    ---------- Recipe: Fried eggs --------------------
    Ingredients: Eggs, Oil
    
    ============ Cooking Assistant - Main Menu =================
    (a) add a new recipe
    (s) search recipe by name
    (i) search recipe by ingredients
    (q) quit
    
    Your choice: s
    Enter recipe name: Daal Chawal
    Sorry the recipe was not found!
    
    ============ Cooking Assistant - Main Menu =================
    (a) add a new recipe
    (s) search recipe by name
    (i) search recipe by ingredients
    (q) quit
    
    Your choice: i
    Enter ingredient (multiple ingredients can be seperated by comma): Eggs
    
    ---------- Recipe: Fried eggs --------------------
    Ingredients: Eggs, Oil
    
    ---------- Recipe: Boiled eggs --------------------
    Ingredients: Eggs, Water
    
    ============ Cooking Assistant - Main Menu =================
    (a) add a new recipe
    (s) search recipe by name
    (i) search recipe by ingredients
    (q) quit
    
    Your choice: i
    Enter ingredient (multiple ingredients can be seperated by comma): Oil, Eggs
    
    ---------- Recipe: Fried eggs --------------------
    Ingredients: Eggs, Oil
    
    ============ Cooking Assistant - Main Menu =================
    (a) add a new recipe
    (s) search recipe by name
    (i) search recipe by ingredients
    (q) quit
    
    Your choice: q

    Good bye and happy cooking :-)

**Tip:** Python has a built-in function named input that allows asking user for input, example::

    # the user will be presented a prompt saying, Please enter your name, and user input will be saved in the name variable
    name = input("Please enter your name: ")
