#include <stdio.h>
#include <cs50.h>

// "echo $?" command sees exit code of most recent program

int main(int args, string argv[])
{
    if (args != 2)
    {
        printf("Missing CLA\n");
        return 1;
    }

    printf("Hello, %s\n", argv[1]);
    return 0;
}