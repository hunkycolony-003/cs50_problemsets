#include<stdio.h>
#include<cs50.h>

int main(void)
{
    int sum;
    int total = get_int( "What is yout total bill?\n" );
    int n = total;
    if (n>0)
    {
        int r1 = n/25;
        n = n % 25;

        int r2 = n/10;
        n = n% 10;

        int r3 = n/5;
        n = n % 5;

        int r4 = n;

        sum = r1 + r2 + r3 + r4;
        printf("The number of coins needed is %d\n", sum);
    }
    else
    {
        printf("Enter a positive integer\n");
    }
}
