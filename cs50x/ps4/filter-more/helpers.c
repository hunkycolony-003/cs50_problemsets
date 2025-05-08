#include "helpers.h"
#include <math.h>

RGBTRIPLE calculate_avg(int height, int width, RGBTRIPLE image[height][width], int i, int j);
RGBTRIPLE convolute(int height, int width, RGBTRIPLE image[height][width], int i, int j);
void weighted_sum(int *sum, int g[3][3], RGBTRIPLE surroundings[3][3]);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterates over all the pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Sets RGB vakue equal to the avarage of the RGB of the same pixel
            RGBTRIPLE pixel = image[i][j];
            BYTE avg = round((float) (pixel.rgbtBlue + pixel.rgbtGreen + pixel.rgbtRed) / 3);
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtRed = avg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Ceates a new image
    RGBTRIPLE new_image[height][width];

    // Copies pixels in image to vertically reflective pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            new_image[i][j] = image[i][width - j - 1];
        }
    }

    // Copies new_image to image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_image[i][j];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //  creates new_image
    RGBTRIPLE new_image[height][width];

    // Calculates the avarage of the surrounding pixels for each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            new_image[i][j] = calculate_avg(height, width, image, i, j);
        }
    }

    // Copies new_image to image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_image[i][j];
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Creates a new image
    RGBTRIPLE new_image[height][width];

    // Assigns the convlution for each pixel to new_image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            new_image[i][j] = convolute(height, width, image, i, j);
        }
    }

    // Copies new_image to image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_image[i][j];
        }
    }
    return;
}

// Calculates the avarage of the surrounding pixels for each of RGB
RGBTRIPLE calculate_avg(int height, int width, RGBTRIPLE image[height][width], int i, int j)
{
    int sum[3] = {0, 0, 0};
    int sum_count = 0;

    // Sums over the surrounding pixels
    for (int x = i - 1; x <= i + 1; x++)
    {
        for (int y = j - 1; y <= j + 1; y++)
        {
            if (x == -1 || y == -1 || x > height - 1 || y > width - 1)
            {
                continue;
            }
            else
            {
                sum[0] += image[x][y].rgbtBlue;
                sum[1] += image[x][y].rgbtGreen;
                sum[2] += image[x][y].rgbtRed;

                sum_count++;
            }
        }
    }

    // Calculates the avarage
    RGBTRIPLE blur_avg = {round((float) sum[0] / sum_count), round((float) sum[1] / sum_count),
                          round((float) sum[2] / sum_count)};

    return blur_avg;
}

// Calculates the convotution for each pixel
RGBTRIPLE convolute(int height, int width, RGBTRIPLE image[height][width], int i, int j)
{
    // Defines the kernels
    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    // Creates 2d array to store the surroundings
    RGBTRIPLE surroundings[3][3];

    // Populates the surrounding array appropriately
    for (int m = 0; m < 3; m++)
    {
        int k = i - 1 + m;

        for (int n = 0; n < 3; n++)
        {
            int l = j - 1 + n;

            if (k >= 0 && k < height && l >= 0 && l < width)
            {
                surroundings[m][n] = image[k][l];
            }

            else
            {
                surroundings[m][n].rgbtBlue = 0;
                surroundings[m][n].rgbtGreen = 0;
                surroundings[m][n].rgbtRed = 0;
            }
        }
    }

    // Creates array to store the weighted sum for each of the the kernels
    int gx_sum[3] = {0, 0, 0};
    int gy_sum[3] = {0, 0, 0};

    // Calculates the weighted sum for each of the kernels and updates the arrays
    weighted_sum(gx_sum, gx, surroundings);
    weighted_sum(gy_sum, gy, surroundings);

    // Combines the two sums
    int blue = round((float) sqrt(pow(gx_sum[0], 2) + pow(gy_sum[0], 2)));
    int green = round((float) sqrt(pow(gx_sum[1], 2) + pow(gy_sum[1], 2)));
    int red = round((float) sqrt(pow(gx_sum[2], 2) + pow(gy_sum[2], 2)));

    // Caps the values
    if (blue > 255)
    {
        blue = 255;
    }

    if (green > 255)
    {
        green = 255;
    }

    if (red > 255)
    {
        red = 255;
    }

    // Returns new pixel
    RGBTRIPLE new_pixel = {blue, green, red};
    return new_pixel;
}

// Calculates the weighted sum
void weighted_sum(int *sum, int g[3][3], RGBTRIPLE surroundings[3][3])
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            sum[0] += g[i][j] * (int) surroundings[i][j].rgbtBlue;
            sum[1] += g[i][j] * (int) surroundings[i][j].rgbtGreen;
            sum[2] += g[i][j] * (int) surroundings[i][j].rgbtRed;
        }
    }

    return;
}
