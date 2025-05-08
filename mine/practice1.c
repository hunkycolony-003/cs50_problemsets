#include <math.h>
#include <stdio.h>
int main()
{
    long n;
    scanf("%ld", &n);
    if (n * (n + 1) % 4 != 0)
    {
        printf("No\n");
    }
    else
    {
        printf("Yes\n");
        double k = (1 + sqrt(1 + 2 * (n) * (n + 1))) / 2;
        long x = (long) k;
        long y = (x * (x + 1)) / 2 - (n * (n + 1)) / 4;
        if (x != k)
        {
            printf("%ld\n", n + 1 - x);
            printf("%ld ", y);
            for (long i = x + 1; i <= n; i++)
            {
                printf("%ld ", i);
            }
            printf("\n");
            printf("%ld\n", x - 1);
            for (long j = 1; j <= x; j++)
            {
                if (j == y)
                {
                    continue;
                }
                else
                {
                    printf("%ld ", j);
                }
            }
        }
        else
        {
            printf("%ld\n", n + 1 - x);
            for (long i = x; i <= n; i++)
            {
                printf("%ld ", i);
            }
            printf("\n");
            printf("%ld\n", x - 1);
            for (long j = 1; j < x; j++)
            {
                if (j == y)
                {
                    continue;
                }
                else
                {
                    printf("%ld ", j);
                }
            }
        }
    }
}
