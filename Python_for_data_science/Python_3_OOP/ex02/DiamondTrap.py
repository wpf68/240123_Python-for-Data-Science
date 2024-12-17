# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    DiamondTrap.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/12/17 17:44:24 by pwolff            #+#    #+#             #
#    Updated: 2024/12/17 17:44:24 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Your docstring for Class"""

    def __init__(self, name, live=True):
        """Your docstring for Constructor"""
        super().__init__(name, live)

    def set_eyes(self, eyes):
        """Set Eyes"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set Hairs"""
        self.hairs = hairs

    def get_eyes(self):
        """Get Eyes"""
        return self.eyes

    def get_hairs(self):
        """Get Hairs"""
        return self.hairs
