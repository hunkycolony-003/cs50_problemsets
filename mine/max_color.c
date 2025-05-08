#include <stdbool.h>
#include <stdio.h>

// Defines a node
typedef struct
{
    bool color;
    int value;
} node;

// Calls the prototype of the function
int max(int n, node arr[n], bool status);

int main()
{
    // Gets the number of inputs from user
    int n;
    printf("Enter the number of inputs: ");
    scanf("%d", &n);

    // Creates a array of type node
    node arr[n];

    // Keeps count of the number of colored, uncolored elements
    int colored_count = 0;
    int uncolored_count = 0;

    // Initialises the nodes with values and color status
    printf("Enter the values:\n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i].value);
        if (i % 2 == 0)
        {
            arr[i].color = true;
            colored_count++;
        }
        else
        {
            arr[i].color = false;
            uncolored_count++;
        }
    }

    // Gets the max values of colored and uncolored nodes
    int colored_max = max(n, arr, true);
    int uncolored_max = max(n, arr, false);

    // Calculates the scores of coloed and uncolored elements
    int score1 = colored_max + colored_count;
    int score2 = uncolored_max + uncolored_count;

    // Prints the larger score
    printf("Output: ");
    if (score1 > score2)
    {
        printf("%d\n", score1);
    }
    else
    {
        printf("%d\n", score2);
    }

    return 0;
}

// Calculates the maximum of the colored or uncolored elements
int max(int n, node arr[n], bool status)
{
    int max = 0;

    for (int i = 0; i < n; i++)
    {
        if (arr[i].color == status)
        {
            if (arr[i].value > max)
            {
                max = arr[i].value;
            }
        }
    }

    return max;
}
