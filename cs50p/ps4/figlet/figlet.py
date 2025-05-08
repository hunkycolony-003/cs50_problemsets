from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    if len(sys.argv) == 3 or len(sys.argv) == 1:
        fnt = take_font()
    else :
        print("Invalid usage")
        sys.exit

    figlet.setFont(font=fnt)
    text = input("Input: ")
    print(figlet.renderText(text))




def take_font():
    figlet = Figlet()

    if len(sys.argv) == 3:

        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            print("Invalid usage")
            sys.exit
        else :
            return sys.argv[2]

    else :
         try :
            font_list = figlet.getFonts()
         except ValueError :
            print("Invalid Font")
            sys.exit
         return random.choice(font_list)


main()
