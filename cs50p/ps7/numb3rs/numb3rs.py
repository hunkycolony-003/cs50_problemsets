import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    if match := re.search(pattern, ip.strip()):
        for i in match.groups():
            try:
                if int(i) > 255:
                    return False
            except ValueError:
                return False
    else:
        return False
    return True


if __name__ == "__main__":
    main()
