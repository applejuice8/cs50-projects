#include <stdio.h>
#include <cs50.h>

void draw_pyramid(int height);

int main(void)
{
    int height = get_int("Height: ");
    draw_pyramid(height);
}

void draw_pyramid(int height)
{
    if (height <= 0)
    {
        return;
    }

    draw_pyramid(height - 1);

    for (int i = 0; i < height; i++)
    {
        printf("#");
    }
    printf("\n");
}