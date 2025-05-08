import sys
import csv


def main():
    check_arg()
    with open(sys.argv[1]) as file, open(sys.argv[2], "w") as new:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(new, fieldnames=["first","last","house"])
        writer.writeheader()

        for row in reader:
            name = row["name"]
            last, first = name.split(", ")
            writer.writerow(
                {
                    "first" : first,
                    "last" : last,
                    "house" : row["house"]
                }
            )


def check_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a python directory of file")
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")


main()
