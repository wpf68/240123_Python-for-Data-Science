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
        image = (ft_load("ImageNB.jpeg"))
        if isinstance(image, str) and image == "":
            raise AssertionError("Error ft load_image !!!")
        else:
            print(image)
    except AssertionError as error:
        print(f"\033[1;31m{AssertionError.__name__} : {error}\033[1;37m")
        exit()

    y, x = image.shape
    
    imageTemp = np.empty((y,x))

    #******************** REVERSE *****************************
    i = 0
    while i < y:
        temp = image[i:i+1,0:(x + 1)]
        # print(f"{i} : {temp}")
        # imageTemp[i] = np.append(imageTemp[i], temp)
        imageTemp[(y - 1) - i] = np.array(temp)
        i += 1

    print(f"\033[1;32mThe shape of image is: {imageTemp.shape}\033[1;37m")
    print(imageTemp)
    imageReverse = Image.fromarray(imageTemp)

    #**********************************************************

    #******************** Rotate *****************************
    i = 0
    while i < y:
        temp = image[i:i+1,0:(x+1)]
        # print(f"{i} : {temp}")
        # imageTemp[i] = np.append(imageTemp[i], temp)
        
        j = 0
        while j < x:
            # imageTemp[i, ((y-1) - j)] = np.array(temp[j])
            imageTemp[3,3] = 3
            j += 1
        i += 1

    print(f"\033[1;32mThe shape of image is: {imageTemp.shape}\033[1;37m")
    print(imageTemp)
    imageRotate = Image.fromarray(imageTemp)

    #**********************************************************

    
    imageNB = Image.fromarray(image)

    plt.imshow(imageNB, cmap="gray")
    plt.title("Zoomed Image")
    plt.axis('on')
    plt.show()

    plt.imshow(imageReverse, cmap="gray")
    plt.title("Zoomed Image")
    plt.axis('on')
    plt.show()
    
    plt.imshow(imageRotate , cmap="gray")
    plt.title("Zoomed Image")
    plt.axis('on')
    plt.show()

if __name__ == "__main__":
    rotate()