# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    array2D.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/10 10:53:55 by pwolff            #+#    #+#             #
#    Updated: 2024/03/10 10:53:55 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#


"""



python3 -m venv env
source env/bin/activate
pip install numpy

Chemin pour flack8 :
export PATH=$PATH:/home/pwolff/.local/bin
"""

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Write a function that takes as parameters a 2D array, prints its shape,
    and returns a truncated version of the array based on the provided start
    and end arguments.
    You must use the slicing method.
    You have to handle error cases if the lists are not the same size,
    are not a list ...

    Args:
        family (list): 2D array to be truncated.
        start (int): Index to start truncation from.
        end (int): Index to end truncation at.

    Returns:
        list: Truncated version of the array.
    My shape:
        Calculates the shape of the original family array
        using NumPy's np.array() function and then retrieves its
        shape using the .shape attribute. The shape of a 2D array is
        a tuple representing the number of rows and columns.
        This line prints the shape of the original array.
    New shape:
        Calculates the shape of the truncated array.
        It first creates a NumPy array from the family list,
        then slices it from the start index to the end+1 index.
        The .shape attribute is used to retrieve the shape of the
        truncated array, which represents the number of rows and
        columns after the truncation.
    """

    # Method Python **********************************************
    # result = family[start:end]
    # print(f"My shape is : ({len(family)}, {len(family[0])})")
    # print(f"My new shape is : ({len(result)}, {len(result[0])})")
    # ************************************************************

    # Method numpy ***********************************************

    try:
        if not isinstance(family, list) or not isinstance(start, int) \
                or not isinstance(end, int):
            raise AssertionError("Value not valid !!!")
    except AssertionError as error:
        print("\033[1;31m" + AssertionError.__name__ +
              " : " + str(error) + "\033[1;37m")
        return list()

    try:
        source = np.array(family)
    except Exception:
        print("\033[1;31mError size list" + "\033[1;37m")
        return list()

    result = source[start: end]
    print(f"My shape is : {source.shape}")
    print(f"My new shape is : {result.shape}")

    # ************************************************************

    return result.tolist()


def main():
    """
    """
    print("\033[1;34mYou want to go the .tester :)\033[1;37m")


if __name__ == "__main__":
    main()
