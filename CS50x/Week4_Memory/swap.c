#include <stdio.h>

void swap_wrong(int a, int b);
void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("%i %i\n", x, y);
    swap_wrong(x, y);
    printf("%i %i\n", x, y);
    swap(&x, &y);
    printf("%i %i\n", x, y);
}

// Pass by value (Only swapped local variables, xy unchanged)
void swap_wrong(int a, int b)
{
    int tmp = a;
    a = b;
    b = tmp;
}

// Pass by reference
void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}