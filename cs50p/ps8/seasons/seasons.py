from datetime import date
import inflect
import sys


def main():
    print(get_minutes(input("What's your Date of Birth: ")))


def get_minutes(day_str):
    try:
        days = date.today() - date.fromisoformat(day_str)
    except Exception:
        sys.exit(1)
    days = days.days
    convert = inflect.engine()
    return f"{convert.number_to_words(days * 24 * 60, andword="").capitalize()} minutes"


if __name__ == "__main__":
    main()
