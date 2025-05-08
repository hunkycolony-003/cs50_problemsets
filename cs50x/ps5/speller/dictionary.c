// Implements a dictionary's functionality

#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

void insert(int index, node *word);

// TODO: Choose number of buckets in hash table
const unsigned int N = 45000;

// Hash table
node *table[N] = {NULL};

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    node *n = table[hash(word)];

    while (n != NULL)
    {
        if (strcasecmp(word, n->word) == 0)
        {
            return true;
        }

        n = n->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int sum = 0;
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        sum += toupper(word[i]) - 'A';
    }

    for (int i = 0; i < 2; i++)
    {
        int digits = log10(sum) + 1;
        unsigned int start = toupper(word[i]) - 'A';

        sum += start * pow(10, (digits + 1));
    }

    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        return false;
    }

    char c;
    char word[LENGTH + 1];

    while (fscanf(dict, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(dict);
            return false;
        }

        strcpy(n->word, word);
        insert((hash(word) % N), n);
    }

    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    unsigned int count = 0;

    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            node *n = table[i];
            while (n != NULL)
            {
                count++;
                n = n->next;
            }
        }
    }

    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *cursor = table[i];
            table[i] = cursor->next;

            free(cursor);
        }
    }

    return true;
}

void insert(int index, node *n)
{
    if (table[index] != NULL)
    {
        n->next = table[index];
        table[index] = n;

        return;
    }

    table[index] = n;
}
