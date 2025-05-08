import random


def main():
    level = get_level()
    questions_left = 10
    score = 0
    while questions_left > 0:
        x, y = generate_integer(level)
        score = score + get_response(x, y)
        questions_left -= 1
    check_score(score)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 0 < n <= 3:
                return n
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    else:
        x = random.randrange(10 ** (level - 1), 10 ** (level))
        y = random.randrange(10 ** (level - 1), 10 ** (level))
    return x, y


def get_response(x, y):
    attempts = 3
    while attempts > 0:
        attempts -= 1
        try:
            z = int(input(f"{x} + {y} = "))
            if z == (x + y):
                return 1
            else:
                print("EEE")
        except ValueError:
            print("EEE")
    print(f"{x} + {y} =", (x + y))
    return 0


def check_score(n):
    print("Score:", n)


if __name__ == "__main__":
    main()
