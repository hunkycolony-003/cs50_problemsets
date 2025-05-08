import sys
from PIL import Image, ImageOps


def main():
    check_arg_len()
    check_arg_name()
    check_arg_exist()
    shirt = Image.open("shirt.png")
    size = shirt.size
    img = Image.open(sys.argv[1])
    img = ImageOps.fit(img, size)
    img.paste(shirt, shirt)
    img.save(sys.argv[2])


def check_arg_len():
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")


def check_arg_name():
    ext = [".jpg", ".jpeg", ".png"]
    condition = False
    for i in ext:
        if sys.argv[1].endswith(i) and sys.argv[2].endswith(i):
            condition = True
    if condition == False:
        sys.exit("Enter correct argument")


def check_arg_exist():
    try:
        Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")


main()
