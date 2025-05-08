from random import randint


def main():
    n = prompt_input()
    m = randint(1, n)
    guess_num(m)


def prompt_input():
    while True:
        n = input("Level: ")
        try:
            if int(n) > 0:
                return int(n)
        except ValueError:
            continue


def guess_num(n):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0:
                continue
            elif guess > n:
                print("Too large!")
            elif guess < n:
                print("Too small!")
            elif guess == n:
                print("Just Right!")
                break
        except ValueError:
            continue


main()
