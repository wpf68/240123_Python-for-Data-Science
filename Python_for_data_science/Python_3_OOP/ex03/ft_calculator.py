# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_calculator.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/12/18 10:22:26 by pwolff            #+#    #+#             #
#    Updated: 2024/12/18 10:22:26 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#


class calculator:
    """#your code here"""

    def __init__(self, liste: list):
        """ft_init"""
        self.liste = liste

    def __add__(self, object) -> None:
        """ft_add"""
        temp = []
        for x in self.liste:
            temp.append(x + object)
        self.liste = temp
        print(self.liste[:])
        # print(object, type(object))

    def __mul__(self, object) -> None:
        """ft_mul"""
        temp = []
        for x in self.liste:
            temp.append(x * object)
        self.liste = temp
        print(self.liste[:])

    def __sub__(self, object) -> None:
        """ft_sub"""
        temp = []
        for x in self.liste:
            temp.append(x - object)
        self.liste = temp
        print(self.liste[:])

    def __truediv__(self, object) -> None:
        """ft_truediv"""
        temp = []
        for x in self.liste:
            if object == 0:
                temp.append(float("inf"))
            else:
                temp.append(x / object)
        self.liste = temp
        print(self.liste[:])
