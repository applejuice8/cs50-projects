#include <stdio.h>
#include <cs50.h>

// This is in cs50.h, allowing us to use string as synonym for char *
typedef char *string;

int main(void)
{
    // int n = get_int("n: ")
    int n;
    printf("n: ");
    scanf("%i", &n);

    //
    printf("%i\n", n);
}