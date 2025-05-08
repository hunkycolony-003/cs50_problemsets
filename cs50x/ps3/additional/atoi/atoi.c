#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int originalLength;

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    originalLength = strlen(input);

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    if (input[1] == '\0')
    {
        return (input[0] - '0');
    }

    int len = strlen(input);

    int number = (input[0] - '0') * pow(10, len - 1) + convert(input + 1);
    return number;
}
