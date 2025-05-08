#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

void printSubsets(int arr[], int size);
int *tobinary(int n, int size);
int power(int a, int b);

int main()
{
    int n;
    printf("Enter the size of the set: ");
    scanf("%d", &n);

    int arr[n];
    printf("Prinf the elements in the array:\n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", arr + i);
    }

    printf("\n\nThe subsets are:\n");
    printSubsets(arr, n);
}

void printSubsets(int arr[], int size)
{
    for (int i = 0; i < power(2, size); i++)
    {
        printf("{");
        int *binary = tobinary(i, size);
        int status = 0;

        for (int j = 0; j < size; j++)
        {
            if (binary[j] == 1)
            {
                if (status == 1)
                    printf(", ");

                printf("%d", arr[j]);

                if (status == 0)
                    status = 1;
            }
        }

        printf("}");
        free(binary);
        printf("\n");
    }
}

int power(int a, int b)
{
    int result = 1;

    for (int i = 0; i < b; i++)
    {
        result *= a;
    }

    return result;
}
