#include <stdio.h>
#include <cs50.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
} person;

int main(void)
{
    person people[2];

    people[0].name = "John";
    people[0].number = "012";
    people[1].name = "Adam";
    people[1].number = "345";

    string name = get_string("Search for: ");

    for (int i = 0; i < 2; i++)
    {
        if (strcmp(people[i].name, name) == 0)
        {
            printf("Found. %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
}