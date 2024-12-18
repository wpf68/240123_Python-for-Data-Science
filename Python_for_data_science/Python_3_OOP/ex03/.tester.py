# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    .tester.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/12/18 10:26:22 by pwolff            #+#    #+#             #
#    Updated: 2024/12/18 10:26:22 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

# https://github.com/znichola/piscine-python/blob/main/
# python_for_data_science/03-OOP/ex04/ft_calculator.py

from ft_calculator import calculator


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    print("-- Test div by zero -")
    v4 = calculator([10.0, 15.0, 20.0])
    v4 / 0


if __name__ == "__main__":
    main()
