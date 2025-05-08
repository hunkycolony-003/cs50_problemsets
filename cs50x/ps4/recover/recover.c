#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

const int BLOCKSIZE = 512;

int main(int argc, char *argv[])
{
    // Check command-line argument
    if (argc != 2)
    {
        printf("Usage: ./volume filename\n");
        return 1;
    }

    // Opens the rawa file
    FILE *card = fopen(argv[1], "rb");
    if (card == NULL)
    {
        printf("Could not open file\n");
        return 1;
    }

    // Creates a buffer to store each 'block'
    BYTE buffer[BLOCKSIZE];

    // Creates vriables
    char *jpeg_filename = malloc(sizeof(char) * 20);
    if (jpeg_filename == NULL)
    {
        return 1;
    }
    FILE *jpeg = NULL;
    int file_count = 0;

    // Reads data as long as there are consecutive 'blocks' left
    while (fread(buffer, sizeof(BYTE), BLOCKSIZE, card) == BLOCKSIZE)
    {
        // OPens ne jpeg file when there is a begining of a jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            if (jpeg != NULL)
            {
                fclose(jpeg);
            }

            sprintf(jpeg_filename, "%03i.jpg", file_count);
            jpeg = fopen(jpeg_filename, "w");
            if (jpeg == NULL)
            {
                return 1;
            }

            file_count++;
        }

        // Writes blocks to the jpeg file
        if (jpeg != NULL)
        {
            fwrite(buffer, sizeof(BYTE), BLOCKSIZE, jpeg);
        }
    }

    // frees the heap
    free(jpeg_filename);

    // Closes the files
    fclose(card);

    if (jpeg != NULL)
    {
        fclose(jpeg);
    }
}

/*
 * Create a BYTE
 * Open the input file
 * read in a chunk of 512 bytes
 * check the first 4 bytes
 * if begining, open a new JPEG file and write
 * else, write
 */
