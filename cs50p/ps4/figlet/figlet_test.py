from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    if len(sys.argv) == 3 or len(sys.argv) == 1:
        fnt = take_font()
    else :
        sys.exit()

    f = Figlet(font=fnt)
    text = input("Input: ")
    print(f.renderText(text))




def take_font():
    figlet = Figlet()

    if len(sys.argv) == 3:

        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            print("Invalid usage")
            sys.exit()
        else :
            return sys.argv[2]

    else :
         font_list = figlet.getFonts()
         return random.choice(font_list)


main()
