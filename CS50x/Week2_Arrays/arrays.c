#include <stdio.h>
#include <cs50.h>

const int N = 3;

// Prototype
float average(int length, int array[]);

int main(void)
{
    int scores[N];

    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Enter score %i: ", i + 1);
    }

    // Average
    float avg = average(N, scores);
    printf("Average: %f\n", avg);
}

float average(int length, int array[])
{
    int sum = 0;

    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return sum / (float) length;
}