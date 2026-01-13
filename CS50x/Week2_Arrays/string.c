#include <stdio.h>
#include <cs50.h>
#include <string.h>

void print_str(void);
void calculate_len(string s);

int main(void)
{
    print_str();
    calculate_len("Adam");
}

void print_str(void)
{
    // Prints out ASCII of 'H', 'I', '!'
    // String always ends with \0
    string s = "HI!";
    printf("%i %i %i %i\n", s[0], s[1], s[2], s[3]);
}

void calculate_len(string s)
{
    int i = 0;
    while (s[i] != '\0')
    {
        i++;
    }
    printf("Len: %i\n", i);

    // Alternative
    i = strlen(s);
    printf("%i\n", i);
}