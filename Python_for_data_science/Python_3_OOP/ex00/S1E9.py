# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    S1E9.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/12/17 09:59:11 by pwolff            #+#    #+#             #
#    Updated: 2024/12/17 10:17:00 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""

    def __init__(self, name, live=True):
        """Your docstring for Constructor"""
        self.first_name = name
        self.is_alive = live

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """Your docstring for Class"""

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False


# class Character(ABC):
#     """Your docstring for Class"""
#     @abstractmethod
#     def die(self):
#         pass


# class Stark(Character):
#     """Your docstring for Class"""
#     def __init__(self, name, live=True):
#         """Your docstring for Constructor"""
#         self.first_name = name
#         self.is_alive = live

#     def die(self):
#         """Your docstring for Method"""
#         self.is_alive = False
