import get_input as gt
import re
import csv
import json
import os


class Recipe:
    def __init__(self, name: str, servings: int, ingredients: list):
        self.name = name
        self.servings = servings
        self.ingredients = ingredients

    @classmethod
    def get(cls, csv_file) -> object:
        try:
            name = gt.get("\n\nWhat is the name of your recipe? ")
            if os.path.isfile(csv_file):
                name = name_exist(name, csv_file)
        except ValueError:
            return None
        servings = gt.get_int("How many servings does the recipe yield? ")
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

    def get_recipe(self) -> dict:
        return {"name": self.name,
                "servings": self.servings,
                "ingredients": self.ingredients,
                }

    def save_recipe(self, csv_file, task) -> None:
        with open(csv_file, task) as file:
            writer = csv.DictWriter(file, fieldnames=["name", "servings", "ingredients"])
            if os.stat(csv_file).st_size == 0:
                writer.writeheader()
            writer.writerow(self.get_recipe())


def view(csv_file) -> dict | None:
    def format(iter, ratio):
        formated_item = (
            lambda item: f"{item['name']} : {int(item['quantity']['value']) * ratio} {item['quantity']['unit']}"
        )
        return "\n".join(formated_item(item) for item in iter)

    try:
        reader = read_csv(csv_file)
    except FileNotFoundError:
        print(f"!! No file named {csv_file.removesuffix(".csv")} found to view !!\n")
        return None
    if sum(1 for _ in reader) > 1:
        print("!! Your file is empty !!")
        return None

    print(get_list_recipes(csv_file))
    asked_recipes = gt.get_list("Enter the item(s) you want to view: ",)
    servings = gt.get_int("How many servings is this for? ", "\n")

    recipes = []

    if "All" in asked_recipes:
        recipes = reader
    else:
        for recipe in asked_recipes:
            status = False
            for row in reader:
                if row["name"] == recipe:
                    status = True
                    recipes.append(row)
                    break
            if not status:
                print(f"!! {recipe} not found in the book !!")

    print()
    if len(recipes) != 0:
        for recipe in recipes:
            ratio = round(servings / int(recipe["servings"]), 2)
            recipe["servings"] = servings
            recipe["ingredients"] = json.loads(replace_quotes(recipe["ingredients"]))
            recipe["ingredients"] = format(recipe["ingredients"], ratio)
        return recipes
    else:
        return None


def edit_recipe(csv_file: str) -> None:
    try:
        book = read_csv(csv_file)
    except FileNotFoundError:
        print(f"!! No Book named {csv_file.removesuffix(".csv")} found !!")
        return None
    if len(book) == 0:
        print("!! Your Book is empty !!")
        return None

    print(get_list_recipes(csv_file))
    asked_recipe = gt.get("Which recipe do you want to edit?\n(enter 'whole' to re-write the whole book): ")

    if asked_recipe == "Whole":
        recipe = Recipe.get(csv_file)
        recipe.save_recipe(csv_file, "w")
    else:
        for row in book:
            status = False
            if row["name"] == asked_recipe:

                status = True
                print(f"\nUpdate {asked_recipe}:")

                match gt.get("what do want to change in the recipe? ",
                             message="\nChoose 'name' or 'servings' or 'ingredients'"):
                    case "Name":
                        row["name"] = gt.get("Enter the new name: ")
                    case "Servings":
                        row["servings"] = gt.get_int("Enter new servings: ")
                    case "Ingredients":
                        row["ingredients"] = json.loads(replace_quotes(str(row["ingredients"])))
                        print(get_ingredients_list(row["ingredients"]))
                        row["ingredients"] = modify_ingredients(row["ingredients"])
                    case _:
                        print("!! Invalid Input !!")
                        return None

        if not status :
            print(f"!! No recipe named {asked_recipe} found !!")
            return None

        with open(csv_file, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "servings", "ingredients"])
            writer.writeheader()
            for row in book:
                writer.writerow(row)


def read_csv(file) -> list:
    with open(file) as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def replace_quotes(d: str) -> str:
    d = d.replace("'", "_")
    d = d.replace('"', "'")
    d = d.replace("_", '"')
    return d


def get_list_recipes(csv_file: str, list=False) -> str | list | None:
    try:
        reader = read_csv(csv_file)
    except FileNotFoundError:
        print("!! No such file found to edit !!")
        return None

    if list:
        return [row["name"] for row in reader]

    name_list = "\n".join(f"-{row["name"]}" for row in reader)

    if len(name_list) == 0:
        return "!! Your Book is empty !!"

    list_message = "Your Book has the following recipes: "
    return f"\n{list_message}\n{name_list}\n\n"


def get_ingredients_list(recipe: list) -> str:
    statement = f"The ingredients in {recipe} are:"
    list = "\n".join(f"-{ing["name"]}" for ing in recipe)
    return f"\n{statement}\n\n{list}\n"


def get_ingredient() -> dict:
    def parse(s):
        pattern = r"(\d+) ?([A-Za-z]+)?"

        if match := re.match(pattern, s):
            if match.group(2):
                return match.group(1), match.group(2).lower()
            else:
                return match.group(1), ""
        else:
            raise ValueError

    name = gt.get("\nEnter the name of the ingredient: ")
    if name == "Done":
        raise EOFError

    quantity = gt.get("Enter the quantity (unit is optional): ")
    value, unit = parse(quantity)
    quantity = {"value": value, "unit": unit}

    return {"name": name, "quantity": quantity}


def name_exist(name, csv_file):
    if get_list_recipes(csv_file):
        if name in get_list_recipes(csv_file, list=True):
            print(f"!! {name} already in the Book !!")
            raise ValueError
    return name


def modify_ingredients(ing: list[dict]) -> list:
    asked_ingredients = gt.get_list("Which of the ingredient(s) do you want to edit")

    for ingredient in asked_ingredients:
        status = False

        for item in ing:
            if item["name"] == ingredient:
                status = True
                item = get_ingredient()

        if not status:
            print(f"!! No ingredient named {ingredient} found !!")

    return ing
