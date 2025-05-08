#include "bmp.h"
#include <math.h>

RGBTRIPLE calculate_avg(RGBTRIPLE image[100][100], int i, int j, int height, int width);

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE new_image[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            new_image[i][j] = calculate_avg(image, i, j, height, width);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_image[i][j];
        }
    }
    return;
}

RGBTRIPLE calculate_avg(RGBTRIPLE image[100][100], int i, int j, int height, int width)
{
    int sum[3] = {0, 0, 0};
    int sum_count = 0;

    for (int x = i - 1; x <= i + 1; x++)
    {
        for (int y = j - 1; y <= j + 1; y ++)
        {
            if (x == -1 || y == -1 || x > height - 1 || y > width - 1)
            {
                continue;
            }
            else
            {
                sum[0] +=  image[x][y].rgbtBlue;
                sum[1] +=  image[x][y].rgbtGreen;
                sum[2] +=  image[x][y].rgbtRed;

                sum_count++;
            }
        }
    }

    RGBTRIPLE blur_avg = {round((float) sum[0] / sum_count),
                          round((float) sum[1] / sum_count),
                          round((float) sum[2] / sum_count)};

    return blur_avg;
}

