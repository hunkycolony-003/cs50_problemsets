// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    bool criteria[4] = {false};

    for (int i = 0, len = strlen(password); i < len; i++)
    {
        if (isupper(password[i]) && !criteria[0])
        {
            criteria[0] = true;
        }
        else if (islower(password[i]) && !criteria[1])
        {
            criteria[1] = true;
        }
        else if (isdigit(password[i]) && !criteria[2])
        {
            criteria[2] = true;
        }
        else if (!isalnum(password[i]) && !criteria[3])
        {
            criteria[3] = true;
        }

        if (criteria[0] && criteria[1] && criteria[2] && criteria[3])
        {
            return true;
        }
    }
    return false;
}
