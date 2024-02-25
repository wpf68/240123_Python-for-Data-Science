# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/08 06:53:11 by pwolff            #+#    #+#              #
#    Updated: 2024/02/08 08:10:38 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

tab = sys.argv

try:
    if len(tab) == 1:
        sys.exit()
    try:
        if len(tab) != 2:
            raise AssertionError("more than one argument is provided")
        val = int(tab[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
except AssertionError as error:
    print(f"{AssertionError.__name__}: {error}")
    sys.exit()

if val % 2:
    print("I'm Odd.")
else:
    print("I'm Even.")




    