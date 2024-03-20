# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    rotate.py                                          :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/19 07:36:37 by pwolff            #+#    #+#             #
#    Updated: 2024/03/19 07:36:37 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def rotate():
    try:
        typeImage = int((input("Image square(1) or rectangle(2) ?")) or '1')
        print(typeImage)
    except ValueError as error:
        print(f"\033[1;31m{ValueError.__name__} : {error}\033[1;37m")
        exit()
    try:
        if typeImage == 1:
            image = (ft_load("ImageNB.jpeg"))
        else:
            image = (ft_load("landscape.jpg"))
            image = Image.fromarray(image)
            image = image.convert("L")
            image = np.array(image)

        if isinstance(image, str) and image == "":
            raise AssertionError("Error ft load_image !!!")
        else:
            print(image)
    except AssertionError as error:
        print(f"\033[1;31m{AssertionError.__name__} : {error}\033[1;37m")
        exit()

    print(image.shape)
    y, x = image.shape
    print(f"y : {y}  --  x : {x}")

    imageTemp = np.empty((y, x))
    print(imageTemp.shape)

# ******************** REVERSE *****************************
    i = 0
    while i < y:
        temp = image[i]
        # print(f"{i} : {temp}")
        imageTemp[(y - 1) - i] = np.array(temp)
        i += 1

    print(f"\033[1;32mNew shape after Transpose (Reverse): \
{imageTemp.shape}\033[1;37m")
    print(imageTemp)
    imageReverse = Image.fromarray(imageTemp)
# **********************************************************

# ******************** Rotate *****************************
    imageTemp = np.empty((x, y))
    i = 0
    while i < y:
        temp = image[i]
        j = 0
        while j < x:
            imageTemp[j, i] = temp[j]
            j += 1
        i += 1

    print(f"\033[1;32mNew shape after Transpose (Rotate): \
{imageTemp.shape}\033[1;37m")
    print(imageTemp)
    imageRotate = Image.fromarray(imageTemp)
# **********************************************************


# ******************** Rotate *****************************
    imageArray = Image.fromarray(image)
    transposed_image = Image.new("L", (y, x))
    for Y in range(y):
        for X in range(x):
            pixel = imageArray.getpixel((X, Y))
            transposed_image.putpixel((Y, X), pixel)
    print(f"\033[1;32mNew shape after Transpose (Rotate_2): \
{transposed_image.size}\033[1;37m")
    print(np.array(transposed_image))
# **********************************************************

    imageNB = Image.fromarray(image)

    plt.imshow(imageNB, cmap="gray")
    plt.title("Zoomed Image")
    plt.axis('on')
    plt.show()

    plt.imshow(imageReverse, cmap="gray")
    plt.title("Zoomed Image Reverse")
    plt.axis('on')
    plt.show()

    plt.imshow(imageRotate, cmap="gray")
    plt.title("Zoomed Image Rotate")
    plt.axis('on')
    plt.show()

    plt.imshow(transposed_image, cmap="gray")
    plt.title("Zoomed Image transposed_image")
    plt.axis('on')
    plt.show()


if __name__ == "__main__":
    rotate()
