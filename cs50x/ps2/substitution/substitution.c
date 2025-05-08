#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#define ALPHA_SIZE 26

int main(int argc, string argv[])
{
    // creates a key to store the original key in uppercase
    char key[ALPHA_SIZE];

    // validates the no. of arguments
    if (argc == 2)
    {
        // gets the original key
        string original_key = argv[1];

        // validates the key and store it in another variable
        for (int i = 0; i < ALPHA_SIZE; i++)
        {
            if (isalpha(original_key[i]))
            {
                for (int j = 0; j < i; j++)
                {
                    // exits if duplicate lcharacter exists
                    if (toupper(original_key[i]) == key[j])
                    {
                        printf("Invalid key.");
                        return 1;
                    }
                }
                key[i] = toupper(original_key[i]);
            }
            else
            {
                // exits if non-alphabatic character exists in key
                printf("Not correct key!\n");
                return 1;
            }
        }
    }
    else
    {
        // exits if argument no. is not 2
        printf("Enter correct no. of arguments.\n");
        return 1;
    }

    // gets the plaintext
    string plain = get_string("plaintext: ");

    // converts to ciphertext
    printf("ciphertext: ");
    for (int i = 0, len = strlen(plain); i < len; i++)
    {
        // maps to key if character is alphabatic
        if (isalpha(plain[i]))
        {
            char c;
            if (isupper(plain[i]))
            {
                c = key[plain[i] - 65];
            }
            else
            {
                c = key[toupper(plain[i]) - 65];
                c = tolower(c);
            }
            printf("%c", c);
        }

        // prints as it is if character is not alphabatic
        else
        {
            printf("%c", plain[i]);
        }
    }

    // prints a newline and returns succesful message
    printf("\n");
    return 0;
}
