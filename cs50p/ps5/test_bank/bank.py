def main():
    greet = input()
    print(value(greet))


def value(response):
    response = response.lower()
    if not response.startswith("h"):
        return 100
    else:
        if response.startswith("hello"):
            return 0
        else:
            return 20

if __name__ == "__main__":
    main()
