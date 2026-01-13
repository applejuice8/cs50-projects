#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // Original list
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }

    // Original list items
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // Expand list
    int *tmp = malloc(4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }

    // Copy list items
    for (int i = 0; i < 3; i++)
    {
        tmp[i] = list[i];
    }
    tmp[3] = 4;

    // Free old list, Pointer points to new list
    free(list);
    list = tmp;

    // Eventually free list
    free(list);
}