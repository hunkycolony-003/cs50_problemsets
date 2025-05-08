#include <stdio.h>

int main()
{
    int test_cases;
    scanf("%d", &test_cases);

    for (int t = 0; t < test_cases; t++)
    {
        // Get the values
        int n, f, a, b;
        scanf("%d %d %d %d", &n, &f, &a, &b);

        int m[n];

        // Populates the array from user
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &m[i]);
        }

        int i = 0;

        while(f > 0 && i != n - 1)
        {
            f -= b;
            if (f <= 0)
            {
                break;
            }

            for (int j = i + 1; j < n; j++)
            {
                int messages = j - i + 1;
                int time = m[j] - m[i] + 1;

                if ((time * a) + b > messages * (b + a))
                {
                    // The time between m[j - 1] and m[i]
                    f -= (m[j - 1] - m[i] + 1) * a;

                    i = j;
                    break;
                }

                if (j == n - 1)
                {
                    // The rest of the time
                    f -= (m[n - 1] - m[i] + 1) * a;

                    i = j;
                    break;
                }
            }

            if (f <= 0)
            {
                break;
            }
        }

        printf("%d\n", f);

        if (f <= 0)
        {
            printf("No\n");
        }
        else
        {
            printf("Yes\n");
        }

    }

}
