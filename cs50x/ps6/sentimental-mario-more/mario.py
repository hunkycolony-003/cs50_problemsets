from cs50 import get_int

while True:
    h = get_int("Height: ")
    if 1 <= h <= 8:
        break

for i in range(1, h + 1):
    print(" " * (h - i), "#" * i, end="  ", sep="")
    print("#" * i)
