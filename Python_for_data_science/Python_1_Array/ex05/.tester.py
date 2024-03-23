# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    .tester.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/20 09:33:21 by pwolff            #+#    #+#             #
#    Updated: 2024/03/20 09:33:21 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

from pimp_image import ft_invert, ft_grey, ft_blue, ft_green, ft_red
from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def display(array: np.ndarray, name: str):
    """
        Display array with name
    """
    plt.imshow(array)
    plt.title(name)
    plt.axis('off')
    plt.show()



array = ft_load("landscape.jpg")

display(Image.fromarray(array), "Figure VIII.1: Original")
display(ft_invert(array), "Figure VIII.2: Invert")
display(ft_red(array), "Figure VIII.3: Red")
display(ft_green(array), "Figure VIII.4: Green")
display(ft_blue(array), "Figure VIII.5: Blue")
display(ft_grey(array), "Figure VIII.6: Grey")


print(ft_invert.__doc__)



