#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// calls the prototypes
int calculate_index(int l, int w, int s);

int main(void)
{
    // Takes the text as input
    string text = get_string("Text: ");

    // initialises the counters
    int letters = 0;
    int words = 1;
    int sentences = 0;

    // Counts the occurences of letters, words and sntences
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        // increments letters in occurence of a alphabatic char
        if (isalpha(text[i]))
        {
            letters++;
        }
        // increments words in occurence of a space
        else if (text[i] == ' ')
        {
            words++;
        }
        /*
        increments sentences in occurence of a period, question mark or exclamation mark,
        which are followed by a space, except for the end of text
        */
        else if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            if (i + 1 < len)
            {
                if (text[i + 1] == ' ')
                {
                    sentences++;
                }
            }
            else
            {
                sentences++;
            }
        }
    }

    // computes the index using formula
    int index = calculate_index(letters, words, sentences);

    // prints the output using the value of index
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", index);
    }
}

// calculates the the value of index and returns this value rounded-off
int calculate_index(int l, int w, int s)
{
    float L = (float) l / (float) w * 100;
    float S = (float) s / (float) w * 100;

    // evaluates the index using formula
    float index = (0.0588 * L) - (0.296 * S) - 15.8;

    // returns the index as am integer
    return (int) round(index);
}

