import sys


def main():
    text = input("Input: ")
    print("Output :", shorten(text))


def shorten(text):
    n = 0
    short = ""
    for i in text:
        i = i.lower()
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            short = short + text[n]
        n += 1
    return short


if __name__ == "__main__":
    main()
