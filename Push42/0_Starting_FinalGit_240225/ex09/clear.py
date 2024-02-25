# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    clear.py                                           :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/02/19 08:14:13 by pwolff            #+#    #+#             #
#    Updated: 2024/02/19 08:14:13 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

import os


def uninstall():
    os.system("rm -rf build")
    os.system("rm -rf dist")
    os.system("rm -rf ft_package.egg-info")
    os.system("rm -rf ft_package/__pycache__")
    os.system("pip3 uninstall ft_package")
    os.system("rm -rf env")


if __name__ == "__main__":
    uninstall()
