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
https://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.Image.getbands
https://www.youtube.com/watch?v=pKFnUNY1TZ8

"""
import numpy as np
from PIL import Image

def ft_invert(array) -> np.ndarray:
    """
    Info ft_invert
    """
#your code here
    pass
    
def ft_red(array: np.ndarray) -> np.ndarray:
    y, x, color = array.shape
    # result = np.empty((y, x, color))

    print(f"x : {x}  y : {y}  Color : {color}")

    imageArray = Image.fromarray(array)
    result = Image.new('RGB', (x, y))


    R, G, B = imageArray.getpixel((3, 4))

    print(R, G, B)

    result.putpixel((3, 4), (R, G, B))






    return array

def ft_green(array) -> np.ndarray:
#your code here
    pass

def ft_blue(array) -> np.ndarray:
#your code here
    pass

def ft_grey(array) -> np.ndarray:
#your code here
    pass