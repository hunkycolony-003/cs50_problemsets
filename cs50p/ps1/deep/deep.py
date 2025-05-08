def main():
    answer = input("What is the answer to the Great question of Life, the Universe and Everything ? ").lower().strip()
    if check(answer):
        print("Yes")
    else:
        print("No")


def check(text):
   return text == "42" or text == "forty two" or text == "forty-two"

main()
