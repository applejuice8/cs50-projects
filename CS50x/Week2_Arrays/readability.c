#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int calculate_letters(string text);
int calculate_words(string text);
int calculate_sentences(string text);
int calculate_index(int letters, int words, int sentences);
void print_grade(int index);

int main(void)
{
    // Prompt string
    string text = get_string("Text: ");

    // Count
    int letters = calculate_letters(text);
    int words = calculate_words(text);
    int sentences = calculate_sentences(text);

    // Calculate index
    int index = calculate_index(letters, words, sentences);
    print_grade(index);
}

int calculate_letters(string text)
{
    int letters = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        text[i] = toupper(text[i]);
        if (text[i] >= 'A' && text[i] <= 'Z')
        {
            letters++;
        }
    }
    return letters;
}

int calculate_words(string text)
{
    int words = 1;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == ' ')
        {
            words++;
        }
    }
    return words;
}

int calculate_sentences(string text)
{
    int sentences = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }
    return sentences;
}

int calculate_index(int letters, int words, int sentences)
{
    // L = Average number of letters per 100 words
    // S = Average number of sentences per 100 words
    float L = (float) letters / words * 100;
    float S = (float) sentences / words * 100;

    int index = round(0.0588 * L - 0.296 * S - 15.8);
    return index;
}

void print_grade(int index)
{
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}