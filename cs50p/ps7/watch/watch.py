import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'src="https?://(?:www.)?youtube.com/embed/(\w+)"'
    if match := re.search(pattern, s):
        match = match.group(1)
        return f"https://youtu.be/{match}"
    else:
        return None


if __name__=="__main__":
    main()
