#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int calculate_points(string s);
void print_winner(int points1, int points2);

int main(void)
{
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    int points1 = calculate_points(word1);
    int points2 = calculate_points(word2);

    print_winner(points1, points2);
}

int calculate_points(string s)
{
    const int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
    int letter;
    int sum = 0;

    for (int i = 0, len = strlen(s); i < len; i++)
    {
        letter = toupper(s[i]);
        if (letter >= 'A' && letter <= 'Z')
        {
            letter -= 'A';
            sum += POINTS[letter];
        }
    }
    return sum;
}

void print_winner(int points1, int points2)
{
    if (points1 > points2)
    {
        printf("Player 1 wins!\n");
    }
    else if (points1 < points2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}