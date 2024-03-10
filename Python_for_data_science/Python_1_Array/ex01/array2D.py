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

# import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """
    
    """
    # source = np.array(family)
    # print(source)
    # print(type(source))
    # result = source[start:end]
    result = family[start:end]

    # print(source[start:end])
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    print(f"My new shape is : ({len(result)}, {len(result[0])})")

    return result



def main():
    """
    """
    print("\033[1;34mYou want to go the .tester :)\033[1;37m")


if __name__ == "__main__":
    main()

