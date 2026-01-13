// dictionary.c in speller


// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include <stdio.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
// const unsigned int N = 26;   Default
const unsigned int N = ('Z' * 2) - ('A' * 2) + 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // Iterate all items of linked list
    for (node *ptr = table[hash(word)]; ptr != NULL; ptr = ptr->next)
    {
        if (strcasecmp(word, ptr->word) == 0) // If found word
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // return toupper(word[0]) - 'A';   Default

    if (word[1]) // If >=2 letters
    {
        return toupper(word[0]) + toupper(word[1]) - ('A' + 'A') + 26; // 26 alphabets
    }
    else // If only 1 letter
    {
        return toupper(word[0]) - 'A';
    }
}

int count = 0;

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open dict
    FILE *src = fopen(dictionary, "r");
    if (src == NULL)
    {
        return false;
    }

    // Declare variables
    int index;
    char word[LENGTH + 1];
    node *cursor;
    node *n;

    // Read str by str
    while (fscanf(src, "%s", word) != EOF)
    {
        // Create node for word
        n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(src);
            return false;
        }

        // Get hash value
        index = hash(word);

        strcpy(n->word, word); // Set word
        n->next = table[index]; // New first item points to former first item (Pointed by sidebar)
        table[index] = n; // Sidebar points to new first item
        count++;
    }

    fclose(src);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count; // Counted when loading into hash table
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    node *ptr;
    node *next;

    for (int i = 0; i < N; i++)
    {
        ptr = table[i];

        // If not last node
        while (ptr != NULL)
        {
            // Continue next node
            next = ptr->next;
            free(ptr);
            ptr = next;
        }
    }
    return true;
}
