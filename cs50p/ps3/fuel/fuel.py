def main():
    frac = input("Fraction: ")
    x , y = take_frac(frac)
    z = calculate(x, y)
    p = make_perc(z)
    print_fuel(p)
    exit()

def take_frac(s):
    try :
        c, d = s.split("/")
        return c, d
    except ValueError:
        main()

def calculate(c, d):
    try:
        return int(c)/int(d)
    except (ValueError, ZeroDivisionError) :
        main()


def make_perc(z):
    z = z * 100
    if z > 100 :
        main()
    else :
        return int(round(z, 0))

def print_fuel(p):
    if p >= 99 :
        print("F")
    elif p <= 1 :
        print("E")
    else :
        print( p , sep = "", end = "")
        print("%")

main()
