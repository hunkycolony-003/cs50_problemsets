def main():
    original = input()
    convert(original)

    
def convert(text):
    emoji = str(text.replace( ':)' , '🙂'))
    emoji = emoji.replace( ':(' , '🙁')
    print(emoji)


main()
