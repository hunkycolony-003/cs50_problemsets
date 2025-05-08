#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

const int POINTS[] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                      1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10
                      };

int get_score(string s);

int main(void)
{
    // Gets the input of words
    string w1 = get_string("Player 1: ");
    string w2 = get_string("Player 2: ");

    // Calls the functions to computes the score of each player
    int score1 = get_score(w1);
    int score2 = get_score(w2);

    // Identifies the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!");
    }
}

// Calculates the score of a player
int get_score(string word)
{
    int sum = 0;
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        char c = word[i];
        if (isalpha(c))
        {
            sum += POINTS[toupper(c) - 'A'];
        }
    }
    return sum;
}
