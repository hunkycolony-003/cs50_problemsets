import sys
from inflect import engine


def main():
    name_list = []
    take_input(name_list)
    if len(name_list) > 0:
        print("Adieu, adieu, to", end=" ")
        print_list(name_list)
    else:
        sys.exit


def take_input(list):
    while True:
        try:
            list.append(input("Name: "))
        except EOFError:
            print()
            break


def print_list(list):
    p = engine()
    print(p.join(list))

main()
