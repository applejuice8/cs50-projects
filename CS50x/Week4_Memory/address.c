#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n; // Assign address of n to pointer p
    printf("%p\n", p);

    // Both prints 50
    printf("%i\n", n);
    printf("%i\n", *p); // Go to location and read (Dereference operator)

    // s storing address of first char of s
    char *s = "Hi";
    printf("%p\n", &s); // Address of pointer s
    printf("%p\n", s);  // s pointing where (s = &s[0])
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);

    // Print strings with 2 methods
    char *r = "Hi!";
    printf("%c", r[0]);
    printf("%c", r[1]);
    printf("%c\n", r[2]);

    printf("%c", *r);
    printf("%c", *(r + 1));
    printf("%c\n", *(r + 2));

    // Start from second char
    printf("%s", r + 1);
}