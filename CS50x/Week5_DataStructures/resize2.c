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
    int *tmp = realloc(list, 4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }

    // Dont need to copy list items
    tmp[3] = 4;

    // Pointer points to new list
    // Dont need to free old list (Gone)
    list = tmp;

    // Eventually free list
    free(list);
}