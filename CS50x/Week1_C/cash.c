#include <stdio.h>
#include <cs50.h>

int get_positive_int();

int main(void)
{
    int change = get_positive_int();

    int coins = 0;

    coins += change / 25; // Quarters
    change %= 25;
    coins += change / 10; // Dimes
    change %= 10;
    coins += change / 5; // Nickels
    change %= 5;
    coins += change / 1; // Pennies
    change %= 1;

    printf("%i\n", coins);
}

int get_positive_int()
{
    int n;
    do
    {
        n = get_int("Change owed: ");
    }
    while (n < 0);
    return n;
}