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

"""


import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    https://www.livi.fr/sante/imc/
    
    """
    a = np.array(height)
    b = np.array(weight)


    return list(b / (a * a))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
     It returns a list of booleans (True if above the limit)
    
    """
    a = np.array(bmi)
    return list (a > limit)

def main():
    """
    
    
    
    """
    print("test")




if __name__ == "__main__":
    main()




