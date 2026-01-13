#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h> // For malloc

int main(void)
{
    char *s = get_string("s: ");

    // a = s only copies the address, not the content (2 pointers pointing same location)
    char *a = s;

    // Correct copy
    char *t = malloc(strlen(s) + 1); // Allocate memory
    if (t == NULL) // If malloc fails
    {
        return 1;
    }
    for (int i = 0, len = strlen(s); i <= len; i++) // Copy \0 too
    {
        t[i] = s[i];
    }

    // Alternative (Copy s to t)
    strcpy(t, s);

    // Free memory after done
    free(t);

    // valgrind ./copy (Check memory-related errors)
}