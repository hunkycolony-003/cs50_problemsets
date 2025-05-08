import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(?P<time_1>\d\d?(?::[0-5]\d)?) (?P<mer_1>[A,P]M) to (?P<time_2>\d\d?(?::[0-6]\d)?) (?P<mer_2>[A,P]M)"
    if match := re.search(pattern, s.strip()):
        time_1 = get_time(match.group("time_1"), match.group("mer_1"))
        time_2 = get_time(match.group("time_2"), match.group("mer_2"))
    else:
        raise ValueError
    return f"{time_1} to {time_2}"


def get_time(time, mer):
    pattern = r"(?P<hour>..?)(?P<min>:..)?"
    match = re.fullmatch(pattern, time)
    hour = int(match.group("hour"))
    if hour > 12:
        raise ValueError
    elif hour == 12:
        hour = 0
    if mer == "PM":
        hour = hour + 12
    if match.group("min"):
        time = f"{hour:02}{match.group("min")}"
    else:
        time = f"{hour:02}:00"
    return time


if __name__ == "__main__":
    main()
