# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    S01E7.py                                           :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42mulhouse.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/12/17 14:43:42 by pwolff            #+#    #+#             #
#    Updated: 2024/12/17 14:43:42 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#


from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, name, live=True):
        """Your docstring for Constructor Baratheon"""
        # self.first_name = name
        # self.is_alive = live
        super().__init__(name, live)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        '''String preprisentation'''
        return super().__str__()

    def __repr__(self) -> str:
        '''Preprisentation'''
        repr = tuple([y for x, y in self.__dict__.items() if
                      x not in ["is_alive", "first_name"]])
        return "Vector: " + str(repr)

    def die(self):
        """Your docstring for Method Baratheon Die"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, name, live=True):
        """Your docstring for Constructor Lannister"""
        super().__init__(name, live)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        '''String preprisentation'''
        return super().__str__()

    def __repr__(self):
        '''Preprisentation'''
        repr = tuple([y for x, y in self.__dict__.items() if
                      x not in ["is_alive", "first_name"]])
        return "Vector: " + str(repr)

    def die(self):
        """Your docstring for Method Lannister Die"""
        self.is_alive = False

    @classmethod
    def create_lannister(self, name, live=True):
        return Lannister(name, live)
