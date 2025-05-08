import sys


def get_int(statement="", end=""):
    while True:
        try:
            value = int(input(statement).strip())
            break
        except ValueError:
            print("Enter an Integer")
        except KeyboardInterrupt:
            sys.exit("\n")
        print(end, sep="", end="")
    return value


def get(statement="", end="", message=""):
    if message != "":
        print(message)
    while True:
        try:
            value = input(statement)
        except KeyboardInterrupt:
            sys.exit("\n")
        if value != "":
            print(end, sep="", end="")
            return value.strip().title()


'''def get_match(statement, list, message=None):
    while True:
        try:
            value = input(statement).strip().title()
        except KeyboardInterrupt:
            sys.exit("\n")
        if value in list:
            return True, value
        else:
            if message:
                print(message)
            return False'''


def get_list(statement="", end=""):
    list = []
    print(statement)
    while True:
        try:
            list.append(input().strip().title())
            print(end, end="")
            if list[-1] == "Done":
                list.pop()
                return list
            elif list[-1] == "All":
                return list
        except EOFError:
            print()
            return list
        except KeyboardInterrupt:
            sys.exit("\n")
