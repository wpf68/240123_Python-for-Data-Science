# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    start.py                                           :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/19 07:07:59 by pwolff            #+#    #+#             #
#    Updated: 2024/03/19 07:13:23 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#


import os


def installLibs():
    os.system("pip install numpy")
    os.system("pip install Pillow")
    os.system("pip install matplotlib")
    print()


def pipList():
    os.system("pip list")
    print()


def test():
    os.system("python3 rotate.py")


if __name__ == "__main__":
    installLibs()
    pipList()
    test()
