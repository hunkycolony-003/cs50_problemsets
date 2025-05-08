// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

void replace(char *word);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./no-vowel word\n");
        return 1;
    }

    char *word = argv[1];

    replace(word);
    printf("%s\n", word);

    return 0;
}

void replace(char *word)
{
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        switch (word[i])
        {
            case 'a':
                word[i] = '6';
                continue;
            case 'e':
                word[i] = '3';
                continue;
            case 'i':
                word[i] = '1';
                continue;
            case 'o':
                word[i] = '0';
            default:
                continue;
        }

    }
}
