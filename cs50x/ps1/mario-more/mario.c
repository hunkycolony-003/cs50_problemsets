#include <cs50.h>
#include <stdio.h>

void make_pyramid(int n);

int main()
{
    int n;
    do
    {
        n = get_int("Enter the height if pyramid: ");
    }
    while (n < 1 || n > 8);

    make_pyramid(n);
}

void make_pyramid(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            printf(" ");
        }
        for (int k = 0; k < i + 1; k++)
        {
            printf("#");
        }
        printf("  ");
        for (int j = 0; j < i + 1; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}
