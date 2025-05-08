from validator_collection import validators


def main():
    try:
        validators.email(input("what's your email id? "))
        print("Valid")
    except ValueError:
        print("Invalid")

main()
