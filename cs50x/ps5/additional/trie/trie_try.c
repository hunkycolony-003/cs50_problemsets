#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE_OF_ALPHABET 26
#define MAXCHAR 20

typedef struct node
{
    bool is_name;
    struct node *children[SIZE_OF_ALPHABET];
} node;

node *root;
char name[MAXCHAR];

int main(char *argv[], int argc)
{
    if (argc != 2)
    {
        printf("Usage: ./trie infile\n");
        return 1;
    }

    FILE *infile = fopen(argv[1], "r");
    if (!infile)
    {
        printf("Error opening file!\n");
        return 1;
    }

    // Allocate root of trie
    root = malloc(sizeof(node));
    if (root == NULL)
    {
        return 1;
    }

    root->is_word = false;
    for (int i = 0; i < SIZE_OF_ALPHABET; i++)
    {
        root->children[i] = NULL;
    }

    // Add words to the trie
    while (fscanf(infile, "%s", name) == 1)
    {

    }
}
