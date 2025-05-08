def main():
    calories = make_dict()
    fruit = take_input()
    print_output(fruit, calories)

def make_dict():
    calories = {
        "apple" : "130",
        "avocado" : "50",
        "banana" : "110",
        "cantaloupe" : "50",
        "grapefruit" : "60",
        "grapes" : "90",
        "moneydew melon" : "50",
        "kiwifruit" : "90",
        "lemon" : "15",
        "lime" : "20",
        "nectarine" : "60",
        "orange" : "80",
        "peach" : "60",
        "pear" : "100",
        "pineapples" : "50",
        "plums" : "70",
        "strawberries" : "50",
        "sweet cherries" : "100",
        "tangerine" : "50",
        "watermelon" : "80",
    }
    return calories

def take_input():
    item = input("Item: ").lower()
    return item

def print_output(item, calories):
    if check_validity(item, calories):
        print("Calories =", calories[item])
    else :
        print()


def check_validity(name, dict):
    condition = False

    for i in dict:
        if i == name :
            condition = True
    return condition


main()
