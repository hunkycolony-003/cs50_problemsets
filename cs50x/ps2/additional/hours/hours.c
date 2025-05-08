#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

int cal_hours(int weeks, int *hours);

int main()
{
    int weeks = get_int("Number of Weeks taking CS50: ");
    int hours[weeks];

    for (int i = 0; i < weeks; i++)
    {
        hours[i] = get_int("Week %i HW hours: ", i);
    }

    char output;

    do
    {
        output = toupper(get_char("Enter T for total hours, A for avarage hours per week: "));
    }
    while (output != 'A' && output != 'T');

    if (output == 'A')
    {
        printf("%.02f Hours\n", (float) cal_hours(weeks, hours) / weeks);
    }
    else
    {
        printf("%d Hours\n", cal_hours(weeks, hours));
    }
}

int cal_hours(int weeks, int *hours)
{
    int sum = 0;

    for (int i = 0; i < weeks; i++)
    {
        sum += hours[i];
    }

    return sum;
}
