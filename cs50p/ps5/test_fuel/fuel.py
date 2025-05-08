def main():
    frac = input("Fraction: ")
    p = convert(frac)
    print(gauge(p))


def convert(s):
    c, d = s.split("/")
    c, d = [int(c), int(d)]
    z = c / d * 100
    if z > 100:
        raise ValueError
    return int(round(z, 0))


def gauge(p):
    if p >= 99:
        return "F"
    elif p <= 1:
        return "E"
    else:
        return str(p) + "%"


if __name__ == "__main__":
    main()
