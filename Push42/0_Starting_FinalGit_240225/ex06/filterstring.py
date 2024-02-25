# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    filterstring.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/02/10 09:02:04 by pwolff            #+#    #+#             #
#    Updated: 2024/02/10 09:02:04 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#


"""
    pip install flak8
    alias norminette=flake8

    Chemin pour flack8 :
    export PATH=$PATH:/home/pwolff/.local/bin

    lire la doc :
    python3
    import building
    help(building)
"""

# TESTS :
# print(filter.__doc__, "\n")

# aquarium = [11, False, 18, 21, "", 12, 34, 0, [], {}]
# print(aquarium)
# filtre = filter(None, aquarium)
# print(list(filtre))
# aquarium = [11, 0, 18, 21, 90, 12, 34, 0]
# print(aquarium)

# print(list(filter(lambda value: value > 18, aquarium)))

import sys
from ft_filter import ft_filter


def main():
    fontion = ft_filter.__doc__
    origine = filter.__doc__

    print(fontion == origine)

    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        # for value in sys.argv:
        #     print(value, "Type :", type(value))
        try:
            if not isinstance(sys.argv[1], str):    # semble inutil car
                # les argv sont des string
                raise AssertionError("Invalid argument types")
            S = list(sys.argv[1].split())
            N = int(sys.argv[2])
        except ValueError as error:
            print(ValueError.__name__+": ", error)
            sys.exit()
    except AssertionError as error:
        print(AssertionError.__name__+": ", error)
        sys.exit()

    result = list(ft_filter(lambda string: len(string) > N, S))
    print(result)


if __name__ == "__main__":
    main()
