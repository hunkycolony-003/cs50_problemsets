def main():
    n = input("Number: ")
    while True:
        try:
            if int(n) < 0:
                raise ValueError
            break
        except ValueError:
            pass
    print(check_card(n))


def check_card(n):
    n = list(n)
    if checksum(n.copy()):
        if 13 <= len(n) <= 16:

            if len(n) == 15 and n[0] == "3" and n[1] in ["4", "7"]:
                return "AMEX"
            elif len(n) == 16 and n[0] == "5" and int(n[1]) in range(1, 6):
                return "MASTERCARD"
            elif n[0] == "4":
                return "VISA"

    return "INVALID"


def checksum(digits):
    digits.reverse()
    flag = 1
    sum1, sum2 = 0, 0
    for i in digits:
        if flag == 0:
            sum1 += (2 * int(i)) % 10 + (2 * int(i)) // 10
            flag = 1
        else:
            sum2 += int(i)
            flag = 0

    sum = sum1 + sum2

    if sum % 10 == 0:
        return True
    return False


main()
