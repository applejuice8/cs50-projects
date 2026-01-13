#include <stdio.h>
#include <stdlib.h>

// typedef struct
// {
//     int number;
//     node *next;      Cannot this, because node not defined yet
// } node;

typedef struct node
{
    int number;
    struct node *next;
} node;

int main(void)
{
    node *list = NULL;

    for (int i = 0; i < 3; i++)
    {
        // n points to node (n is not a node, is a pointer)
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;
        }

        // Change properties of node
        n->number = i + 1; // Follow arrow, change at dest
        n->next = list; // Same as (*n).next = list

        list = n;
    }
    // Final result reversed (list -> 3 -> 2 -> 1)

    // Print number of each node
    for (node *ptr = list; ptr != NULL; ptr = ptr->next)
    {
        printf("%i\n", ptr->number);
    }

    // Free memory
    node *ptr = list;
    while (ptr != NULL)
    {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }
}