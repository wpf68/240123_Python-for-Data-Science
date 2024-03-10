# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    give_bmi.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/09 10:27:57 by pwolff            #+#    #+#             #
#    Updated: 2024/03/09 10:27:57 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#


"""
https://fr.wikipedia.org/wiki/NumPy
https://numpy.org/doc/stable/user/absolute_beginners.html



python3 -m venv env
source env/bin/activate
pip install numpy

Chemin pour flack8 :
export PATH=$PATH:/home/pwolff/.local/bin
"""


import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
     -> list[int | float]:
    """
    https://www.livi.fr/sante/imc/
    give_bmi, take 2 lists of integers or floats in input and returns a list
    of BMI values.
    """
    a = np.array(height)
    b = np.array(weight)

    try:
        if len(height) != len(weight):
            raise AssertionError("the lists are not the same size")
        if len(a[a <= 0]) != 0 or len(b[b <= 0]) != 0:
            raise AssertionError("Value not valid !!!")
    except AssertionError as error:
        print("\033[1;31m" + AssertionError.__name__ +
              " : " + str(error) + "\033[1;37m")
        return list()
    except Exception:
        print("\033[1;31mthe lists are not int or float\033[1;37m")
        return list()

    return list(b / (a * a))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    apply_limit, accepts a list of integers or floats and an integer
    representing a limit as parameters. It returns a list of booleans
    (True if above the limit).
    """
    a = np.array(bmi)
    return list(a > limit)


def main():
    """
    """
    print("\033[1;34mYou want to go the .tester :)\033[1;37m")


if __name__ == "__main__":
    main()
