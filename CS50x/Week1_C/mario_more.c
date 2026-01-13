#include <stdio.h>
#include <cs50.h>

int get_positive_int();
void print_pyramid(int height);

int main(void)
{
    int n = get_positive_int();
    print_pyramid(n);
}

int get_positive_int()
{
    int n;
    do
    {
        n = get_int("Enter height: ");
    }
    while (n <= 0);
    return n;
}

void print_pyramid(int height) // height = 4
{
    for (int i = 1; i <= height; i++) // 1 2 3 4
    {
        for (int j = height - i; j > 0; j--) // 3 2 1 0
        {
            printf(" ");
        }
        for (int k = 0; k < i; k++) // 1 2 3 4
        {
            printf("#");
        }
        printf("  ");
        for (int l = 0; l < i; l++) // 1 2 3 4
        {
            printf("#");
        }
        printf("\n");
    }
}