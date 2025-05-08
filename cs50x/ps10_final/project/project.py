import get_input as gt
from tabulate import tabulate
from datetime import datetime
import re
import csv
import json
import os
import sys


def main():
    # prints the welcome message
    print(messages("welcome1"))

    # gets the filename from user
    csv_file = gt.get("Which recipe book do you want to open? ") + ".csv"

    # calls the required functions, according to the input of user, repeats until closed
    while True:
        print(messages("welcome2"))
        match gt.get("Enter your input: "):

            # adds recipe to a new/existing file
            case "Add":
                recipe = Recipe.get(csv_file)
                if recipe:
                    recipe.save_recipe(csv_file, "a")

            # Views recipe(s) from an existing file
            case "View":
                recipes = view(csv_file)

                # shows the result in a table
                if recipes:
                    print(tabulate(recipes,
                                   headers="keys",
                                   tablefmt="fancy_grid",
                                   maxcolwidths=[None, 15]))

            # Edits an existing file
            case "Edit":
                edit_recipe(csv_file)

            # Breaks the loop when requested
            case "Close":
                print(messages("close"))
                sys.exit()

            # Default case
            case _:
                print("Enter the correct Input from the above options")
                pass


# Gets the input from the user and adds the recipe to the file
class Recipe:

    # Initialises the values as attributes in a recipe
    def __init__(self, name: str, servings: int, ingredients: list):
        self.name = name
        self.servings = servings
        self.ingredients = ingredients

    # Gets the values to add to the recipe
    @classmethod
    def get(cls, csv_file, write=False) -> object:

        # Gets name of the recipe, only if name already not present
        name = gt.get("\n\nWhat is the name of your recipe? ")
        if not write:
            try:
                if os.path.isfile(csv_file):
                    name = name_exist(name, csv_file)
            except ValueError:
                return None

        # Gets the no. of servings
        servings = gt.get_int("How many servings does the recipe yield? ")

        # Adds ingridients to a list to add as attribute
        ingredients = list()
        while True:
            try:
                ingredients.append(get_ingredient())
            except ValueError:
                print("!! Not expected input !!")
                pass
            except EOFError:
                break
        return cls(name, servings, ingredients)

    # Returns the recipe as a dict to add to the file
    def get_recipe(self) -> dict:
        return {"name": self.name,
                "servings": self.servings,
                "ingredients": self.ingredients,
                }

    # Writes/appends the recipe to a new/existing file
    def save_recipe(self, csv_file, task) -> None:
        with open(csv_file, task) as file:
            writer = csv.DictWriter(file, fieldnames=["name", "servings", "ingredients"])
            if os.stat(csv_file).st_size == 0:
                writer.writeheader()
            writer.writerow(self.get_recipe())


# Returns the recipe(s) requested in the required format to view
def view(csv_file) -> list | None:

    # Fromats the ingridients
    def format(iter, ratio):
        formated_item = (
            lambda item: f"{item['name']} : {float(item['quantity']['value']) * ratio} {item['quantity']['unit']}"
        )
        return "\n".join(formated_item(item) for item in iter)

    # Reads the csv file as a list of dictionary
    try:
        reader = read_csv(csv_file)
    except FileNotFoundError:
        print(f"!! No file named {csv_file.removesuffix(".csv")} found to view !!\n")
        return None
    if sum(1 for _ in reader) < 1:
        print("!! Your file is empty !!")
        return None

    # Shows the recipes present in the book
    print(get_recipes_list(csv_file))

    # Gets the recipe names and servings
    asked_recipes = gt.get_list("Enter the item(s) you want to view: ",)
    servings = gt.get_int("How many servings is this for? ", "\n")

    # Gets only the list of recipes that were requested
    recipes = []

    # Gets all recipes if asked
    if "All" in asked_recipes:
        recipes = reader

    # Else, gets only the redipe(s) requested
    else:
        for recipe in asked_recipes:
            status = False
            for row in reader:
                if row["name"] == recipe:
                    status = True
                    recipes.append(row)
                    break

            # Prints message if recipe not found
            if not status:
                print(f"!! {recipe} not found in the book !!\n")

    # Returns recipe as a dict if any recipe found
    if len(recipes) != 0:
        for recipe in recipes:
            ratio = round(servings / float(recipe["servings"]), 2)
            recipe["servings"] = servings
            recipe["ingredients"] = json.loads(replace_quotes(recipe["ingredients"]))
            recipe["ingredients"] = format(recipe["ingredients"], ratio)
        return recipes
    else:
        return None


# Edits and existing recipe
def edit_recipe(csv_file: str) -> None:

    # Reads the recipe book as a list of dictionary, if existent and non-empty
    try:
        book = read_csv(csv_file)
    except FileNotFoundError:
        print(f"!! No Book named {csv_file.removesuffix(".csv")} found !!")
        return None
    if len(book) == 0:
        print("!! Your Book is empty !!")
        return None

    # prints the list of recipes present
    print(get_recipes_list(csv_file))

    # Gets the recipe to edit
    asked_recipe = gt.get(
        "Which recipe do you want to edit/remove?\n(enter 'whole' to re-write the whole book): ")

    # Re-writes the whole recipe book, if requested
    if asked_recipe == "Whole":
        recipe = Recipe.get(csv_file, write=True)
        recipe.save_recipe(csv_file, "w")

    # Else, finds the asked recipe in the list
    else:
        for i, row in enumerate(book):
            status = False
            if row["name"] == asked_recipe:
                status = True

                # Asks the user whether they want to edit or remove the recipe
                print("\n\nEnter 'edit' or 'remove':")
                task = gt.get("What do you want to do in the recipe? ")

                # Removes the recipe if chosen
                if task == "Remove":
                    print(f"{row["name"]} removed succesfully.")
                    book.pop(i)
                    break

                # Else, edits the recipe
                elif task == "Edit":

                    print(f"\nUpdate {asked_recipe}:")

                    # Edits only the part of the recipe which is asked for
                    match gt.get("what do want to change in the recipe? ",
                                 message="\nChoose 'name' or 'servings' or 'ingredients' or 'whole' "):
                        case "Name":
                            row["name"] = gt.get("Enter the new name: ")
                        case "Servings":
                            row["servings"] = gt.get_int("Enter new servings: ")
                        case "Ingredients":
                            row["ingredients"] = json.loads(replace_quotes(str(row["ingredients"])))
                            print(get_ingredients_list(row))
                            new_ingredients = modify_ingredients(row["ingredients"])
                            if new_ingredients:
                                row["ingredients"] = new_ingredients
                            else:
                                return None
                        case "Whole":
                            recipe = Recipe.get(csv_file)
                            if recipe:
                                row = recipe.get_recipe()
                        case _:
                            print("!! Invalid Input !!")
                            return None

                    print(f"\nUpdated {row["name"]} !!")
                    book[i] = row
                    break

                # Returns None if invalid inpur given
                else:
                    print("!! Invalid input !!")
                    return None

        # Prints message if recipe not found
        if not status:
            print(f"!! No recipe named {asked_recipe} found !!")
            return None

        # Re-writes the whole file with the updated list
        with open(csv_file, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "servings", "ingredients"])
            writer.writeheader()
            for row in book:
                writer.writerow(row)


# Reads the csv file as a dict
def read_csv(file) -> list:
    with open(file) as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


# Replaces the quotes in a string
def replace_quotes(d: str) -> str:
    d = d.replace("'", "_")
    d = d.replace('"', "'")
    d = d.replace("_", '"')
    return d


# Returns the recipes present as a list or as a str, as requested
def get_recipes_list(csv_file: str, list: bool = False) -> str | list | None:

    # Reads the file, if existent
    try:
        reader = read_csv(csv_file)
    except FileNotFoundError:
        print("!! No such file found to edit !!")
        return None

    # Returns list, if requested
    if list:
        return [row["name"] for row in reader]

    # Creates a name-list otherwise
    name_list = "\n".join(f"- {row["name"]}: {row["servings"]} servings" for row in reader)

    # Returns message, if not recipe present
    if len(name_list) == 0:
        return "!! Your Book is empty !!"

    # returns name-list with a message
    list_message = "Your Book has the following recipes: "
    return f"\n{list_message}\n\n{name_list}\n\n"


# Returns the ingridiens list in a recipe
def get_ingredients_list(recipe: dict) -> str:
    statement = f"The ingredients in {recipe["name"]} are:"
    list = "\n".join(
        f"- {ing["name"]} - {ing["quantity"]["value"]} {ing["quantity"]["unit"]}" for ing in recipe["ingredients"])
    return f"\n{statement}\n\n{list}\n"


# Gets and returns the components a single ingridiens
def get_ingredient() -> dict:

    # Parses the string
    def parse(s):
        pattern = r"(\d+(?:\.\d+)?) ?([A-Za-z]+)?"

        # Returns the parsed string, name and value separated
        if match := re.match(pattern, s):
            if match.group(2):
                return match.group(1), match.group(2).lower()
            else:
                return match.group(1), ""
        else:
            raise ValueError

    # Gets the name of ingridient
    name = gt.get("\nEnter the name of the ingredient: ")
    if name == "Done":
        raise EOFError

    # Gets the quantity of the ingridient
    quantity = gt.get("Enter the quantity (unit is optional): ")
    value, unit = parse(quantity)
    quantity = {"value": value, "unit": unit}

    # Returns the ingridient as a dict
    return {"name": name, "quantity": quantity}


# Checks if a recipe with same name already exists
def name_exist(name, csv_file):
    if get_recipes_list(csv_file):
        if name in get_recipes_list(csv_file, list=True):
            print(f"!! {name} already in the Book !!")
            raise ValueError
    return name


# Modifies ingridient(s) in a recipe during editing
def modify_ingredients(ingredients: list[dict]) -> list:
    print("Enter 'Add' or 'modify': ")
    task = gt.get("What do want to do in the ingredients? ")

    if task == "Add":
        ingredients.append(get_ingredient())

    elif task == "Modify":

        # Gets the ingridients to edit
        asked_ingredients = gt.get_list("Which of the ingredient(s) do you want to edit")

        # Finds the ingridients in the recipe
        for ingredient in asked_ingredients:
            status = False
            for i, item in enumerate(ingredients):

                # Re-takes the ingridient if found
                if item["name"] == ingredient:
                    status = True
                    print(f"\n\nUpdate {item["name"]}:\n")

                    print("Enter 're write' or 'remove': ")
                    task = gt.get(f"What do you want to do with the ingredient? ")

                    if task == "Remove":
                        ingredients.pop(i)
                        print(f"Removed {item["name"]} succesfully. ")

                    elif task == "Re Write":
                        ingredients[i] = get_ingredient()
                    else:
                        print("!! INVALID INPUT !!")
                        return None

            # Prints message if ingridient not found
            if not status:
                print(f"!! No ingredient named {ingredient} found !!")

    else:
        print("!! INVALID INPUT !!")
        return None

    # Returns the updated ingridient list
    return ingredients


# Returns the messsages to be printed at the command line
def messages(type):
    def get_time():
        time = datetime.now().hour + 6

        if 5 <= time < 12:
            return "Morning"
        elif 12 <= time < 16:
            return "Afternoon"
        elif 16 <= time < 21:
            return "Evening"
        else:
            return "Night"

    welcome_message1 = """
                            ************************************************
                            *** Welcome to a treasure chest of flavours! ***
                            ************************************************

    """
    welcome_message2 = """
         Enter your command (case insensitively) in correspondense with
         your objective from the following options:

         "Add" : To add recipe to a new or existing recipe book
         "View" : To View one or more recipe(s) from an existing recipe book
         "Edit" : To edit recipes in an existing recipe book
         "Close" : To exit

    """
    view_message = """
        * Enter the name of any specific recipe(s) you want to view that belong to this book
          OR enter "all" to view every recipe (default is "all")
        * Enter "Done" or use KeyboardInterruptKey when you are done
        * Enter the number of servings that you want to make the dish for default is 4

    """
    actual_close_message = f"Have a Flavourful {get_time()} !!"
    length = len(actual_close_message) + 10
    closing_message = f"""
                                {"*" * length}
                                **** {actual_close_message} ****
                                {"*" * length}
    """
    match type:
        case "view":
            return view_message
        case "welcome1":
            return welcome_message1
        case "welcome2":
            return welcome_message2
        case "close":
            return closing_message


if __name__ == "__main__":
    main()
