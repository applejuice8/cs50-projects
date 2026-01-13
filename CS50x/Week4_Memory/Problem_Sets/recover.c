#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // Exactly 1 command line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Create a buffer for a block of data
    uint8_t buffer[512];

    // 000.jpg\0 has 8 chars
    char filename[8];

    int i = 0;
    FILE *img;

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) != 0)
    {
        // Check for header of JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (i > 0)
            {
                fclose(img); // Close previous img if new one found
            }
            sprintf(filename, "%03i.jpg", i); // 3 digits integer
            img = fopen(filename, "w");
            fwrite(buffer, 1, 512, img);
            i++;
        }
        else if (i > 0) // If previous file not finished yet
        {
            fwrite(buffer, 1, 512, img); // Keep writing
        }
    }

    // Close files
    fclose(img);
    fclose(card);
}