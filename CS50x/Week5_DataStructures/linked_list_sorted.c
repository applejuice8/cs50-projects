#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

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
        // Allocate node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;
        }

        n->number = get_int("Number: ");
        n->next = NULL;

        if (list == NULL) // If first node, let list points to node
        {
            list = n;
        }

        else if (n->number < list->number) // Insert at start of list
        {
            n->next = list;
            list = n;
        }

        else // If middle of list
        {
            for (node *ptr = list; ptr != NULL; ptr = ptr->next)
            {
                if (ptr->next == NULL) // If at end of list, append
                {
                    ptr->next = n;
                    break;
                }

                if (n->number < ptr->next->number) // If middle of list (If new node's number < next node's number)
                {
                    n->next = ptr->next;
                    ptr->next = n;
                    break;
                }
            }
        }
    }
    // Final result in order (list -> 1 -> 2 -> 3)

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