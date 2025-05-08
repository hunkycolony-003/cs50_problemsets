import requests
import sys


def main():
    n = take_input()
    price = get_price()
    dollar = n * price
    print(f"${dollar:,}")


def take_input():
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing Command-line arguement")


def get_price():
    try:
        details = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        bitcoin = details.get("bpi").get("USD").get("rate_float")
        return float(bitcoin)
    except requests.RequestException:
        sys.exit


main()
