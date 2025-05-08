def main():
    menu = make_menu()
    total = take_order(menu)
    print_total(total)


def make_menu():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    return menu

def take_order(menu):
    total = 0
    while True :
        try :
            order = input("Item: ").title()
            total = float(total + menu[order])
            print_total(total)
        except (EOFError, KeyboardInterrupt) :
            print()
            return total
        except KeyError:
            pass


def print_total(total) :
    print("$", sep = "", end = "" )
    print(f"{total:.2f}")


main()
