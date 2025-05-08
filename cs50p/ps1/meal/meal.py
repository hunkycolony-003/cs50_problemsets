def main():
    input_time = input("What time is it? ")

    if  check_format(input_time):
        input_time = input_time.rstrip("a.m.")
        time = convert(input_time)
        check_meal(time)
    else:
        input_time = input_time.rstrip("p.m.")
        time = convert(input_time)
        time = time + 12
        check_meal(time)



def check_format(time):

    temp = time.split(sep = " ", maxsplit = -1)
    if len(temp) == 1:
        return True
    else:
        first, last = temp
        if last == "a.m.":
            return True
        else :
            return False



def check_meal(time):
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")
    else :
        print(" ")




def convert(time):
    time = time.split(sep = ":", maxsplit = 1)
    hour, minute = time
    hour = int(hour)
    minute = float(minute)/100
    time = hour + round(minute*100/60, 2)
    return time

if __name__ == "__main__":
    main()
