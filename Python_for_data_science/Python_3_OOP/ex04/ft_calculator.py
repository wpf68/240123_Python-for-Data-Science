# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_calculator.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/12/18 10:56:00 by pwolff            #+#    #+#             #
#    Updated: 2024/12/18 10:56:00 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#


class calculator:
    """Class calculator for Vector"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """ft_dotproduct"""
        resultDot = 0
        i = 0
        while i < len(V1):
            resultDot += int(V1[i]*V2[i])
            i += 1
        print("Dot product is:", resultDot)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """ft_add_vec"""
        resultAdd = []
        i = 0
        while i < len(V1):
            resultAdd.append(float(V1[i]+V2[i]))
            i += 1
        print("Add Vector is :", resultAdd[:])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """ft_sous_vec"""
        resultSous = []
        i = 0
        while i < len(V1):
            resultSous.append(float(V1[i]-V2[i]))
            i += 1
        print("Sous Vector is:", resultSous[:])
