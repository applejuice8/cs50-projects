#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// Prototype
bool check_if_int(string s);
char encrypt(char c, int k);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        string key = argv[1];

        if (check_if_int(key))
        {
            int k = atoi(key);
            string s = get_string("plaintext:  ");

            printf("ciphertext: ");
            for (int i = 0, len = strlen(s); i < len; i++)
            {
                printf("%c", encrypt(s[i], k));
            }
            printf("\n");
            return 0;
        }
    }
    printf("Usage: ./caesar key\n");
    return 1;
}

bool check_if_int(string s)
{
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}

char encrypt(char c, int k)
{
    char base;

    if (isupper(c))
    {
        base = 'A';
    }
    else if (islower(c))
    {
        base = 'a';
    }
    else
    {
        return c; // Non alphabets
    }
    c = (c - base + k) % 26 + base;
    return c;
}