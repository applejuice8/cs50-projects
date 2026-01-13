// Tree
typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
} node;

bool search(node *tree, int number)
{
    if (tree == NULL)
    {
        return false;
    }
    else if (number < tree->number) // If left of tree
    {
        return search(tree->left, number);
    }
    else if (number > tree->number) // If right of tree
    {
        return search(tree->right, number);
    }
    else
    {
        return true;
    }
}

// Hash table
typedef struct node
{
    char *name;
    char *number;
    struct node *next;
} node;

unsigned int hash(const char *word)
{
    return toupper(word[0]) - 'A';
}

node *table[26];

// Tries
typedef struct node
{
    struct node *children[26];
    char *number;
} node;