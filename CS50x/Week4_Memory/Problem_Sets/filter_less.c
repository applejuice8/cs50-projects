// helpers.c in Filter-less

#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    float average;

    // Loop over each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Average of rgb
            average = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);

            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int originalRed, originalGreen, originalBlue, sepiaRed, sepiaGreen, sepiaBlue;

    // Loop over each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            originalRed = image[i][j].rgbtRed;
            originalGreen = image[i][j].rgbtGreen;
            originalBlue = image[i][j].rgbtBlue;

            // Calculates sepia
            sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

            // Assigns 255 if exceed
            image[i][j].rgbtRed = sepiaRed > 255 ? 255 : sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen > 255 ? 255 : sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue > 255 ? 255 : sepiaBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp;
    int w, wHalf = width / 2;

    // Loop over each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < wHalf; j++)
        {
            w = width - j - 1;

            // Swap
            tmp = image[i][j];
            image[i][j] = image[i][w];
            image[i][w] = tmp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a copy of image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    int totalRed, totalGreen, totalBlue, h, w;
    float cells;

    // Loop over each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            totalRed = 0, totalGreen = 0, totalBlue = 0;
            cells = 0.0;

            // Average of 3x3 cube
            for (int a = -1; a < 2; a++)
            {
                for (int b = -1; b < 2; b++)
                {
                    h = i + a;
                    w = j + b;

                    if (h >= 0 && h < height && w >= 0 && w < width)
                    {
                        totalRed += copy[h][w].rgbtRed;
                        totalGreen += copy[h][w].rgbtGreen;
                        totalBlue += copy[h][w].rgbtBlue;
                        cells++;
                    }
                }
            }
            // Apply results
            image[i][j].rgbtRed = round(totalRed / cells);
            image[i][j].rgbtGreen = round(totalGreen / cells);
            image[i][j].rgbtBlue = round(totalBlue / cells);
        }
    }
}
