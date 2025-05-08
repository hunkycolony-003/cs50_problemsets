def main():
    total = 50
    total = calculate_amount(total)
    final_print(total)

    
#calculates the total until its the final print
def calculate_amount(total):
    while(total > 0):
        coin = input_coin(total)
        total = total - coin
    return total

#called by calculate_amount() for user input
def input_coin(total):
    while True:
        print("Amount Due:", total)
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            break
    return coin

#prints the final owe
def final_print(total):
    if(total < 0):
        print("Change Owed:", -total)
    else :
        print("Change Owed: 0")


main()
