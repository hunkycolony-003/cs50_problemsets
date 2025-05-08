import sys


def main():
    count = 0
    check_validity()
    with open(sys.argv[1]) as file:
        for line in file:
            if line.lstrip().startswith("#"):
                continue
            elif line.strip() == "":
                continue
            else:
                count += 1
    print(count)


def check_validity():
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a python directory of file")
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")


main()
