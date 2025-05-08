import sys


def main():
    name_list = []
    take_input(name_list)
    if len(name_list) > 0:
        print()
        print("Adieu, adieu, to", end=" ")
        print_list(name_list)
    else:
        sys.exit


def take_input(list):
    while True:
        try:
            list.append(input("Name: "))
        except EOFError:
            break


def print_list(list):

    if len(list) == 1:
        print(list[0])
    elif len(list) == 2:
        print(list[0], list[1], sep=" and ")
    else:
        for name in list[: len(list) - 1]:
            print(name, end=", ")

        print("and", end=" ")
        print(list[len(list) - 1])


main()
