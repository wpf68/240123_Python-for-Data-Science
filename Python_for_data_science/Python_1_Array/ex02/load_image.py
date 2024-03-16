# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    load_image.py                                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/15 06:50:09 by pwolff            #+#    #+#             #
#    Updated: 2024/03/15 06:50:09 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

import numpy as np
from PIL import Image


"""
python3 -m venv env
source env/bin/activate
pip install numpy
pip install Pillow

    lire la doc :
    python3
    import load_image
    help(load_image)

    from load_image import ft_load
    help(ft_load)

Chemin pour flack8 :
export PATH=$PATH:/home/pwolff/.local/bin
"""


"""
Pillow est une bibliothèque de traitement d'image, qui est un fork
et successeur du projet PIL (Python Imaging Library). Elle est conçue de
manière à offrir un accès rapide aux données contenues dans une image, et
offre un support pour différents formats de fichiers tels que PPM, PNG,
JPEG, GIF, TIFF et BMP.

https://codatik.com/lire-image-avec-python/

"""


def ft_load(path: str) -> np.ndarray:
    """
    You need to write a function that loads an image, prints its format,
    and its pixels content in RGB format.
    You have to handle, at least, JPG and JPEG format.
    You need to handle any error with a clear error message

    Parameters:
    path (str): The path to the image file to be loaded.

    Returns:
    np.ndarray: A NumPy array representing the loaded image.
    """

    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
    except AssertionError as error:
        print(f"\033[1;31m{AssertionError.__name__} : {error} \033[1;37m")
        return 0

    try:
        test = Image.open(path)
        test.show()
        test = np.array(test)
        print(f"\033[1;32mThe shape of image is: {test.shape}\033[1;37m")
        return test
    except Exception:
        print(f"\033[1;31m{Exception.__name__} : File no present\033[1;37m")
        return 0


def main():
    """
    """
    print("\033[1;34mYou want to go the .tester :)\033[1;37m")


if __name__ == "__main__":
    main()
