def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_len(s) and start_with(s) and number(s) and other(s):
        return True
    else :
        return False


#Checks first condition
def check_len(s):
    return 2 <= len(s) <= 6


#Checks second condition
def start_with(s):
    return s[0].isalpha() and s[1].isalpha()


#Checks condition 3
def number(s):
    n = -1
    for i in s:
        n += 1
        if i.isdigit():
            break
    #Checks if the whole string is alphabatic
    if n == len(s) - 1:
        return True
    #If not, only then checks the number condition
    else :
        return number_1(s, n) and number_2(s, n)


#checks condition 3_A
def number_1(s, n):
    condition = True
    for i in range(n, len(s)):
        if s[i].isalpha():
            condition = False
    return condition


#checks condition 3_B
def number_2(s, n):
    return s[n] != "0"


#checks condition 4
def other(s):
    condition = True
    for i in s:
        if not i.isalnum():
            condition = False
    return condition


main()
