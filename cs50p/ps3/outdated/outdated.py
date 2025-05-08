import re


def main():
    list = month_list()
    while True :
        date = input("Date: ").strip().title()
        if check_format(date):
            m, d, y = check_format(date)
            break
    if m.isalpha():
        m = check_month(m, list)
    print_date(int(m), int(d), int(y))


def month_list():
    return {
        1 : "January",
        2 : "February",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December",
    }


def check_format(date):
    pattern_1 = r"^(\d\d?)/(\d\d?)/(\d{4})$"
    pattern_2 = r"^(\w+) (\d), (\d{4})$"
    if match_1 := re.search(pattern_1, date):
        if 1 < int(match_1.group(1)) < 12 and 1 < int(match_1.group(2)) < 31:
            return match_1.groups()
    elif match_2 := re.search(pattern_2, date):
        if 1 < int(match_2.group(2)) < 31:
            return match_2.groups()
    else:
        return False
    return False


def check_month(month, list):
    for i in list:
        if month == list[i]:
            return i


def print_date(m, d, y):
    print(f"{y}-{m:02}-{d:02}")


main()
