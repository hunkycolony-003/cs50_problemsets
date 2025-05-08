import sys
import csv
from tabulate import tabulate


def main():
    check_arg()
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers="keys", tablefmt="grid"))


def check_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a python directory of file")
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")


main()
