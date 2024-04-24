# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    load_csv.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/26 07:30:01 by pwolff            #+#    #+#             #
#    Updated: 2024/03/26 07:30:17 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

import pandas as pd
# import numpy as np

"""
https://datascientest.com/pandas-python-data-science
https://pandas.pydata.org/docs/
http://www.python-simple.com/python-pandas/panda-intro.php

https://ledatascientist.com/manipulez-vos-donnees-avec-pandas/

"""


"""
python3 -m venv env
source env/bin/activate
python3 start.py

or :
pip install numpy
pip install Pillow
pip install matplotlib
pip install pandas

    lire la doc :
    python3
    import load_image
    help(load_image)

    from load_image import ft_load
    help(ft_load)

Chemin pour flack8 :
export PATH=$PATH:/home/pwolff/.local/bin
"""


RED = "\033[1;31m"
WHITE = "\033[1;37m"
GREEN = "\033[1;32m"
BLUE = "\033[1;34m"


def load(path: str) -> pd.DataFrame:
    """
    Make a function that takes a path as argument, writes the dimensions of
    the data set and returns it. You have to handle the error cases and
    return None if the path is bad, bad format...
    """

    print(WHITE)
    try:
        df = pd.read_csv(path)
    except FileNotFoundError as error:
        print(f"{RED}Error : {FileNotFoundError} : {error} // \
File no found{WHITE}")
        return None
    except UnicodeDecodeError as error:
        print(f"{RED}Error : {UnicodeDecodeError} : {error} // \
Error format{WHITE}")
        return None
    # print(df.info())
    # print(df.describe())
    print(GREEN, "Loading dataset of dimensions", df.shape, WHITE)
    # print(df)
    # print(type(df))

    return df


def main():
    """
    Each program must have its main and not be a simple script
    """

    print("\033[1;34mYou want to go the aff_life.py :)\033[1;37m")


if __name__ == "__main__":
    main()
