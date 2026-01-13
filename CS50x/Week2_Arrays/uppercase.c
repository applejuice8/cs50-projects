#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    string s = get_string("Before: ");

    // Manually
    printf("After: ");
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            printf("%c", s[i] - ('a' - 'A'));
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");

    // Alternative
    printf("After: ");
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        printf("%c", toupper(s[i]));
    }
    printf("\n");
}