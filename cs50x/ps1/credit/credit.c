#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int checksum(long n);
int length(long n);
string check_card(long n);

// Calls the functions to validate and prints the output
int main(void)
{
    long card_number = get_long("Enter the card number: ");
    if (checksum(card_number) == 1)
    {
        string card_type = check_card(card_number);
        if (strcmp(card_type, "none") != 0)
        {
            printf("%s\n", card_type);
            return 0;
        }
    }
    printf("INVALID\n");
    return 0;
}

// Validates the checksum of the number
int checksum(long n)
{
    // Calculates the first sum (Which are multiplied by 2)
    int sum1 = 0;
    long copy = n;
    while (copy > 0)
    {
        int temp = (copy % 100) / 10;
        temp = temp * 2;
        while (temp > 0)
        {
            sum1 += temp % 10;
            temp = temp / 10;
        }
        copy = copy / 100;
    }

    // Calculates the second sum (Rest of the digits)
    int sum2 = n % 10;
    n = n / 10;
    while (n > 0)
    {
        int temp = (n % 100) / 10;
        sum2 += temp;
        n = n / 100;
    }

    int sum = sum1 + sum2;

    if (sum % 10 == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

// Calculates the number of digits in a number
int length(long n)
{
    int count = 0;
    while (n > 0)
    {
        count++;
        n = n / 10;
    }
    return count;
}

// Validates and returns the type of the card ("none" if invalid)
string check_card(long n)
{
    if (length(n) == 15)
    {
        if ((int)(n / pow(10, 13)) == 34 || (int)(n / pow(10, 13)) == 37)
        {
            return "AMEX";
        }
    }
    else if (length(n) == 13)
    {
        if ((int)(n / pow(10, 12)) == 4)
        {
            return "VISA";
        }
    }
    else if (length(n) == 16)
    {
        if ((int)(n / pow(10, 15)) == 4)
        {
            return "VISA";
        }
        else if ((int)(n / pow(10, 15)) == 5)
        {
            n = (int)(n / pow(10, 14));
            n = n % 10;
            if (n >= 1 && n <= 5)
            {
                return "MASTERCARD";
            }
        }
    }
    return "none";
}
