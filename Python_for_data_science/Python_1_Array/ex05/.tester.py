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

array = ft_load("landscape.jpg")

imageOriginal = Image.fromarray(array)

ft_invert(array)


imageRed = ft_red(array)
print(imageRed)




ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)

plt.imshow(imageOriginal)
plt.title("Figure VIII.1: Original")
plt.axis('off')
plt.show()


plt.imshow(imageRed)
plt.title("Figure VIII.3: Red")
plt.axis('off')
plt.show()