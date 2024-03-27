# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    .tester.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/26 07:35:55 by pwolff            #+#    #+#             #
#    Updated: 2024/03/26 07:35:55 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

from load_csv import load
import os

os.system('clear')

RED = "\033[1;31m"
WHITE = "\033[1;37m"
GREEN = "\033[1;32m"
BLUE = "\033[1;34m"


def tester():
    """
    Each program must have its main and not be a simple script
    """

    print(BLUE, load.__doc__, WHITE)
    print(load("life_expectancy_years.csv"))
    # load("life_expectancy_years.csv")

    print(load("life_expectancy_yearsvis.csv"))

    print(load("ImageNB.jpeg"))


if __name__ == "__main__":
    tester()
