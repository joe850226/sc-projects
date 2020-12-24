"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage



def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    red = (red - pixel.red)
    green = (green - pixel.green)
    blue = (blue - pixel.blue)
    dist = ((red) ** 2 + (green) ** 2 + (blue) ** 2) ** (1/2)
    return dist

    pass


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    lst = []
    red = 0
    green = 0
    blue = 0
    for pixel in pixels:
        red += pixel.red
        green += pixel.green
        blue += pixel.blue
    red = int(red/len(pixels))
    green = int(green / len(pixels))
    blue = int(blue / len(pixels))
    lst.append(red)
    lst.append(green)
    lst.append(blue)
    return lst
    pass


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    lst = []
    red = 0
    green = 0
    blue = 0
    for pixel in pixels:
        red += pixel.red
        green += pixel.green
        blue += pixel.blue
    red = int(red / len(pixels))
    green = int(green / len(pixels))
    blue = int(blue / len(pixels))
    smallest_distance = 10000000000000000000000000000
    best_pix =0
    for pixel in pixels:
        red_distance = (red - pixel.red)
        green_distance = (green - pixel.green)
        blue_distance = (blue - pixel.blue)
        distance = (red_distance ** 2 + green_distance ** 2 + blue_distance ** 2) ** (1 / 2)
        if distance < smallest_distance:
            smallest_distance = distance
            best_pix = pixel

    # lst.append(smallest_distance)

    return best_pix
    pass


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect

    for x in range(width):
        for y in range(height):
            list = []
            for img in images:
                list.append(img.get_pixel(x, y))
            best = get_best_pixel(list)
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best.red
            result_pixel.green = best.green
            result_pixel.blue = best.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()


    # gree n_im = SimpleImage.blank(20, 20, 'green')
    # green_pixel = green_im.get_pixel(0,0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # # print(get_average([green_pixel, green_pixel, green_pixel,blue_pixel]))
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)