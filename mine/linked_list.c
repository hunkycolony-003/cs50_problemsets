#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
} node;

int add_node(node **list, int a);
void free_node(node *list);

int main()
{
    node *list = NULL;

    // Append to list
    for (int i = 0; i < 3; i++)
    {
        add_node(&list, get_int("Enter number %d: ", i));
    }

    // Print list
    node *ptr = list;

    while (ptr != NULL)
    {
        printf("%d\n", ptr->number);
        ptr = ptr->next;
    }

    free_node(list);
}

int add_node(node **list, int a)
{
    node *ptr = malloc(sizeof(node));
    if (ptr == NULL)
    {
        free_node(*list);
        return 1;
    }

    ptr->number = a;
    ptr->next = *list;
    *list = ptr;

    return 0;
}

void free_node(node *list)
{
    if (list == NULL)
    {
        return;
    }

    free_node(list->next);
    free(list);
}
