#include <stdio.h>
#include <stdint.h>

typedef uint8_t BYTE; // Byte is only a thing in Windows, not C

int main(int args, char *argv[]) // ./copy_file source.c destination.c
{
    FILE *src = fopen(argv[1], "r");  // rb (Read as binary, dont interpret)
    FILE *dest = fopen(argv[2], "w"); // wb

    BYTE b;

    // Read in size of byte, copy into &b
    // Read 1 byte at a time
    // Read file "src"
    // Repeat until return 0
    while (fread(&b, sizeof(b), 1, src) != 0)
    {
        fwrite(&b, sizeof(b), 1, dest);
    }

    fclose(src);
    fclose(dest);
}