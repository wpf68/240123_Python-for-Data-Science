# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    zoom.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/16 07:01:22 by pwolff            #+#    #+#             #
#    Updated: 2024/03/16 07:01:22 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#


from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

"""
https://infoforall.fr/python/python-act040.html
https://courspython.com/tableaux-numpy.html

https://www.delftstack.com/fr/howto/matplotlib/
convert-a-numpy-array-to-pil-image-python/

https://codatik.com/convertir-une-image-au-niveau-de-gris/
http://www.python-simple.com/python-matplotlib/matplotlib-intro.php
https://www.delftstack.com/fr/howto/matplotlib/
matplotlib-display-image-in-grayscale/
"""


def zoom():
    try:
        image = (ft_load("animal.jpeg"))
        if isinstance(image, str) and image == "":
            raise AssertionError("Error ft load_image !!!")
        else:
            print(image)
    except AssertionError as error:
        print(f"\033[1;31m{AssertionError.__name__} : {error}\033[1;37m")
        exit()

    # image2 = image[100:500,450:850,0:3]
    # imageColor = Image.fromarray(image2)
    # imageColor.show()
    # print(imageColor.format, imageColor.size, imageColor.mode)
    # print(np.array(imageColor).shape)

    imageColor = Image.fromarray(image)
    imageTemp = imageColor.crop((450, 100, 850, 500))
    imageNB = imageTemp.convert("L")
    print(f"\033[1;32mNew shape after slicing\
: {np.array(imageNB).shape}\033[1;37m")
    print(np.array(imageNB))

    # ************   Save image and Load  **************
    # imageColor2.save('imageNB.jpeg','jpeg')
    # imageNB = plt.imread('imageNB.jpeg')

    plt.imshow(imageNB, cmap="gray")
    plt.title("Zoomed Image")
    plt.axis('on')
    plt.show()


if __name__ == "__main__":
    zoom()
