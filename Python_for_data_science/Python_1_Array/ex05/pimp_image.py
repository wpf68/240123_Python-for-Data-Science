# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    pimp_image.py                                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/20 09:22:11 by pwolff            #+#    #+#             #
#    Updated: 2024/03/20 09:22:11 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#


"""
https://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.\
Image.getbands
https://www.youtube.com/watch?v=pKFnUNY1TZ8

"""
import numpy as np
from PIL import Image


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
        Inverts the color of the image received.
    """
    y, x, color = array.shape
    # print(f"x : {x}  y : {y}  Color : {color}")

    imageArray = Image.fromarray(array)

    for Y in range(y):
        for X in range(x):
            R, G, B = imageArray.getpixel((X, Y))
            R = 255 - R
            G = 255 - G
            B = 255 - B
            imageArray.putpixel((X, Y), (R, G, B))
    return np.array(imageArray)


def ft_red(array: np.ndarray) -> np.ndarray:
    """
        Keeps only the red channel of the image.
    """
    y, x, color = array.shape
    # print(f"x : {x}  y : {y}  Color : {color}")

    imageArray = Image.fromarray(array)
    # result = Image.new('RGB', (x, y))

    # R, G, B = imageArray.getpixel((3, 4))
    # print(R, G, B)
    # result.putpixel((3, 4), (R, G, B))

    for Y in range(y):
        for X in range(x):
            R, G, B = imageArray.getpixel((X, Y))
            imageArray.putpixel((X, Y), (R, 0, 0))

    return np.array(imageArray)


def ft_green(array: np.ndarray) -> np.ndarray:
    """
        Keeps only the green channel of the image.
    """

    green = array[:, :, 1]
    imageArray = array.copy()
    imageArray[:, :, 0] = 0
    imageArray[:, :, 1] = green
    imageArray[:, :, 2] = 0

    return imageArray

    # *************  First method ********************
    # y, x, color = array.shape
    # print(f"x : {x}  y : {y}  Color : {color}")

    # imageArray = Image.fromarray(array)

    # for Y in range(y):
    #     for X in range(x):
    #         R, G, B = imageArray.getpixel((X, Y))
    #         imageArray.putpixel((X, Y), (0, G, 0))

    # return np.array(imageArray)


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
        Keeps only the blue channel of the image.'
    """
    y, x, color = array.shape
    # print(f"x : {x}  y : {y}  Color : {color}")

    imageArray = Image.fromarray(array)

    for Y in range(y):
        for X in range(x):
            R, G, B = imageArray.getpixel((X, Y))
            imageArray.putpixel((X, Y), (0, 0, B))

    return np.array(imageArray)


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
        Converts the image to greyscale.
    """


# ************  First solution with + and / or // ***********
    # y, x, color = array.shape
    # # print(f"x : {x}  y : {y}  Color : {color}")

    # imageArray = Image.fromarray(array)

    # for Y in range(y):
    #     for X in range(x):
    #         R, G, B = imageArray.getpixel((X, Y))
    #         gray = int((R + G + B)/3)
    #         # gray = (R + G + B)//3
    #         imageArray.putpixel((X, Y), (gray, gray, gray))

    # return np.array(imageArray)

# ************  Secound solution // perte de la troisieme dimension !!! *
    # imageGrey = Image.fromarray(array).convert("L")
    # imageGrey.show()
    # imageGrey = np.array(imageGrey).astype(np.uint8)
    # print(imageGrey.shape)
    # return imageGrey

# ************  Troisieme solution moyenne : mean ***********

    # array (Y, X, 1)
    grey_ar = np.mean(array, axis=2, keepdims=True)
    # print(grey_array.shape)
    # array (Y, X, 3)
    grey_image = np.concatenate([grey_ar, grey_ar, grey_ar], axis=2)
    # print(grey_image.shape)
    return grey_image.astype(np.uint8)
